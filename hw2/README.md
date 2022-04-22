

## Assignment 1

## 1850668 李俊杰

![image-20220423013043373](https://tva1.sinaimg.cn/large/e6c9d24ely1h1j18i896zj20gy0skjsu.jpg)

### Modifications to GUI and the Codes

Note that the GUI in the example uses absolute positioning for layout, which is very inflexible. Therefore, according to the original UI design, I used HBox and VBox for layout and rewrote the previous code so that the interface can adapt to the size of the window. At the same time, buttons are added for user interaction. When the user clicks the button, the earpiece icon at the top of the interface will start to play an animation to indicate that the program is listening to the user, and the label below the icon will also display blue fonts for feedback. When the user finishes speaking, the earpiece icon stops playing the animation, and the label below it will display what the program heard the user said or display the reason for the error, such as "API Unavailable".

It is worth mentioning that since speech recognition is a CPU-intensive task, if it is executed in the UI thread, it will affect the user's interaction. Therefore, the task is moved to the worker thread for execution, of which the execution result will be passed to the UI thread through `pyqtSignal`.

```python
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
```

After that, the result of the program's processing will be matched (similarity calculation) with the target sentence (eg 'play music', 'Take Notes', 'Open Calculator', etc.) in order to execute the corresponding command. The similarity comparison uses the similarity of the two vectors in the [TF](https://cloud.tencent.com/developer/article/1145941) matrix. As for executing commands, Python library subprocess.Popen is used to execute shell commands when the similarity is greater than or equal to 0.5, so the code is OS-dependent (**MAC OS** here).

```python
#similarity
def tf_similarity(self,s1, s2):
  	cv = CountVectorizer(tokenizer=lambda s: s.split())
  	corpus = [s1, s2]
  	vectors = cv.fit_transform(corpus).toarray()
  	sim = np.dot(vectors[0], vectors[1]) / (norm(vectors[0]) * norm(vectors[1]))
  	return sim
  
#MAC OS PLATFORM ONLY
#Part of the code in another function
  self.cmds = [
      ['open','./hw2/resources/AGA - Better Me.mp3'],
      ['open','./hw2/resources/takeNotes.txt'],
      ['open','/System/Applications/Calculator.app']
  ]
	if np.max(sims)>=0.5:
    Popen(self.cmds[np.argmax(sims)],shell=False)
```

One thing to mention, the API called by the speech recognition in the original example is `recognizer.recognize_sphinx(audio)`. Since the accuracy rate is too low, another API, `recognizer.recognize_google(audio)`(**maybe you need global proxy**), is called after consulting the relevant information, and the accuracy has risen sharply.

### Accuracy of speech recognition

As mentioned above, after calling the API, `recognize_google()`, the accuracy of speech recognition is greatly improved. Below is the accuracy of speech recognition for three instructions, corresponding to the three in the next Feature section.

```python
sims = np.array([self.tf_similarity(guess['transcription'],'play music'),
                  self.tf_similarity(guess['transcription'],'take notes'),
                  self.tf_similarity(guess['transcription'],'open calculator')],dtype=np.float32)
print(sims)

#sims
#Feature 1
#[1. 0. 0.]
#Feature 2
#[0. 1. 0.]
#Feature 3
#[0. 0. 1.]
```

### Feature

####  Play Music

![image-20220423001306961](https://tva1.sinaimg.cn/large/e6c9d24ely1h1j18lcpjnj205c01gdfm.jpg)

![image-20220423001252035](https://tva1.sinaimg.cn/large/e6c9d24ely1h1j18n0ltaj219j0u0q96.jpg)



#### Take Notes

![image-20220423001401293](https://tva1.sinaimg.cn/large/e6c9d24ely1h1j18r07kcj206001ct8h.jpg)

![image-20220423001349944](https://tva1.sinaimg.cn/large/e6c9d24ely1h1j18op86kj216w0sodim.jpg)

#### Open Calculator

![image-20220423001445218](https://tva1.sinaimg.cn/large/e6c9d24ely1h1j18tsthtj205o01ajr5.jpg)

![image-20220423001436131](https://tva1.sinaimg.cn/large/e6c9d24ely1h1j18vqo0kj20ua0scmzt.jpg)



### Environment & Run

Note1: Since the code contains commands for the Mac platform (i.e, open a text editor), it may not execute correctly on other platforms.

Note2: Maybe you need global proxy to call API `recognize_google()`.

Note3: You need to install conda environment.

```shell
conda env create -f ./hw2/environment.yml
conda activate hci2
cd hw2
python main.py
```





