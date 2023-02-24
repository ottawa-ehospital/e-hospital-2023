import warnings
from PIL import Image, ImageEnhance
warnings.filterwarnings('ignore')
import tensorflow as tf
from keras.models import load_model
from keras.applications.vgg16 import preprocess_input
import numpy as np
#from keras.preprocessing import image
import keras.utils as image

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QMessageBox

from win32com.client import Dispatch


def speak(str1):
    speak=Dispatch(("SAPI.SpVoice"))
    speak.Speak(str1)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        #setting main window size for app
        MainWindow.resize(700, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        #setting background color of app
        self.frame.setGeometry(QtCore.QRect(0, 0, 710, 700))
        self.frame.setStyleSheet("background-color: #888dd9;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        #setting the image geometry and location on the app
        self.label.setGeometry(QtCore.QRect(200, -100, 700, 620))
        self.label.setText("")
        #can set as gif or a jpg
        self.jpg=QMovie("picture.jpg")
        self.label.setMovie(self.jpg)
        #starting jpg file
        self.jpg.start()
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        #setting main title geometry and location
        self.label_2.setGeometry(QtCore.QRect(60, 330, 591, 101))
        font = QtGui.QFont()
        #setting font size of text
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        #setting  left button geometry and location (moves text side , moves text up and down, makes box wider horizontally, makes box wider vertically )
        self.pushButton.setGeometry(QtCore.QRect(120, 470, 201, 31))
        font = QtGui.QFont()
        #setting font size of text one button
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("patient.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"border-radius: 10px;\n"
" background-color:#DF582C;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
" background-color: #7D93E0;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        #setting right button geometry and location (moves text side , moves text up and down, makes box wider horizontally, makes box wider vertically )
        self.pushButton_2.setGeometry(QtCore.QRect(380, 470, 201, 31))
        font = QtGui.QFont()
        #setting font size of text
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"border-radius: 10px;\n"
" background-color:#DF582C;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
" background-color: #7D93E0;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.upload_image)
        self.pushButton_2.clicked.connect(self.predict_result)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "App for Pneumonia Prediction"))
        self.label.setToolTip(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/picture.jpg\"/></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "PNEUMONIA Detection"))
        self.pushButton.setText(_translate("MainWindow", "Upload Image"))
        self.pushButton_2.setText(_translate("MainWindow", "Prediction"))
    def upload_image(self):
        filename=QFileDialog.getOpenFileName()
        path=filename[0]
        path=str(path)
        print(path)
        model=load_model('patient_xrays.h5') 
        img_file=image.load_img(path,target_size=(224,224))
        x=image.img_to_array(img_file)
        x=np.expand_dims(x, axis=0)
        img_data=preprocess_input(x)
        classes=model.predict(img_data)
        global result
        result=classes

    def predict_result(self):
        print(result)
        if result[0][0]>0.5:
            print("Patient is Healthy")
            speak("Patient is Healthy")
        else:
            print("Patient has PNEUMONIA")
            speak("Patient has PNEUMONIA")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
