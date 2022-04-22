from subprocess import Popen
from PyQt5 import QtWidgets
from PyQt5.QtGui import QMovie
from guessTheWord import recognize_speech_from_mic
import speech_recognition as sr
from PyQt5.QtCore import QThread, pyqtSignal

from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from scipy.linalg import norm

class MyApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.workThread = MyThread()
        #MAC OS PLATFORM ONLY
        self.cmds = [
            ['open','./hw2/resources/AGA - Better Me.mp3'],
            ['open','./hw2/resources/takeNotes.txt'],
            ['open','/System/Applications/Calculator.app']
        ]
        
        self.setWindowTitle("Voice Assistant")
        
        self.movie = QMovie("./hw2/icon/play.gif")
        label = QtWidgets.QLabel()
        self.movie.start()
        label.setMovie(self.movie)
        self.movie.stop()
        
        label1 = QtWidgets.QLabel("Hi! How can I help you?")
        label1.setWordWrap(True)
        label2 = QtWidgets.QLabel("You can:")
        label2.setWordWrap(True)
        label3 = QtWidgets.QLabel("Enjoy music by saying 'Play Music'")
        label3.setWordWrap(True)
        label4 = QtWidgets.QLabel("Task some notes by saying 'Take Notes'")
        label4.setWordWrap(True)
        self.label5 = QtWidgets.QLabel()
        self.label5.setWordWrap(True)
        label6 = QtWidgets.QLabel("Calculate by saying 'Open Calculator'")
        label6.setWordWrap(True)
        hbox1 = QtWidgets.QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(self.label5)
        hbox1.addStretch(1)
        self.button = QtWidgets.QPushButton("Speak")
        self.button.clicked.connect(self.onButtonClick)
        
        hbox = QtWidgets.QHBoxLayout(self)
        vbox = QtWidgets.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(label)
        vbox.addStretch(3)
        vbox.addLayout(hbox1)
        vbox.addStretch(1)
        vbox.addWidget(label1)
        vbox.addStretch(3)
        vbox.addWidget(label2)
        vbox.addStretch(1)
        vbox.addWidget(label3)
        vbox.addStretch(1)
        vbox.addWidget(label4)
        vbox.addStretch(1)
        vbox.addWidget(label6)
        vbox.addStretch(1)
        vbox.addWidget(self.button)
        vbox.addStretch(3)
        
        hbox.addStretch(1)
        hbox.addLayout(vbox)
        hbox.addStretch(1)
        
        self.resize(self.sizeHint())
        
    def onButtonClick(self):
        self.button.setDisabled(True)
        self.movie.start()
        self.label5.setText("<div style='color:blue;'>I'm Hearing you</div>")
        
        self.workThread.start()
        self.workThread.signal.connect(self.onVoiceRecognize)
    
    def onVoiceRecognize(self, guess:dict):
        if not guess["success"]:
            self.label5.setText("<div style='color:red;'>API unavailable</div>")
            self.button.setEnabled(True)
            self.movie.stop()
            return
        
        if guess["error"]:
            self.label5.setText("<div style='color:blue;'>Unable to recognize speech, Try Again</div>")
            self.button.setEnabled(True)
            self.movie.stop()
            return

        sims = np.array([self.tf_similarity(guess['transcription'],'play music'),
                  self.tf_similarity(guess['transcription'],'take notes'),
                  self.tf_similarity(guess['transcription'],'open calculator')],dtype=np.float32)
        
        print(sims)
        if np.max(sims)>=0.5:
            Popen(self.cmds[np.argmax(sims)],shell=False)
        
        self.label5.setText(f"<div style='color:green;'>{guess['transcription']}</div>")
        self.button.setEnabled(True)
        self.movie.stop()
    
    def tf_similarity(self,s1, s2):
        cv = CountVectorizer(tokenizer=lambda s: s.split())
        corpus = [s1, s2]
        vectors = cv.fit_transform(corpus).toarray()
        sim = np.dot(vectors[0], vectors[1]) / (norm(vectors[0]) * norm(vectors[1]))
        return sim


class MyThread(QThread):
    signal = pyqtSignal(dict)
    
    def __init__(self):
        super().__init__()
        # create recognizer and mic instances
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
    
    def run(self):
        guess = recognize_speech_from_mic(self.recognizer, self.microphone)
        self.signal.emit(guess)