from PyQt5.QtWidgets import QApplication
import sys
from Window import MyApp


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    myWindow = MyApp()
    myWindow.show()
    
    sys.exit(app.exec_())
