# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)
from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import cv2

### Face_recognition ###
# first 'pip install cmake'
# second 'pip install face_recognition'
import face_recognition
from face_recognition.api import face_encodings

import semimagem
import lebron1
import anthony
import lebron2

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(868, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.lb_imagemTreino = QLabel(self.centralwidget)
        self.lb_imagemTreino.setObjectName(u"lb_imagemTreino")
        self.lb_imagemTreino.setGeometry(QRect(110, 180, 301, 291))
        self.lb_imagemTreino.setMinimumSize(QSize(280, 280))
        self.lb_imagemTeste = QLabel(self.centralwidget)
        self.lb_imagemTeste.setObjectName(u"lb_imagemTeste")
        self.lb_imagemTeste.setGeometry(QRect(430, 180, 301, 291))
        self.lb_imagemTeste.setMinimumSize(QSize(280, 280))
        self.lb_titulo = QLabel(self.centralwidget)
        self.lb_titulo.setObjectName(u"lb_titulo")
        self.lb_titulo.setGeometry(QRect(130, 50, 581, 61))
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(120, 100, 601, 41))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(403, 190, 41, 281))
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.bt_imagemTreino = QPushButton(self.centralwidget)
        self.bt_imagemTreino.setObjectName(u"bt_imagemTreino")
        self.bt_imagemTreino.setGeometry(QRect(130, 140, 120, 30))
        self.bt_imagemTreino.setMinimumSize(QSize(120, 30))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.bt_imagemTreino.setFont(font)
        self.bt_imagemTreino.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.bt_imagemTreino.setStyleSheet(u"")
        self.lb_tituloTreino = QLabel(self.centralwidget)
        self.lb_tituloTreino.setObjectName(u"lb_tituloTreino")
        self.lb_tituloTreino.setGeometry(QRect(260, 140, 141, 30))
        self.lb_tituloTreino.setMinimumSize(QSize(120, 30))
        self.lb_tituloTreino.setFont(font)
        self.bt_imagemTeste = QPushButton(self.centralwidget)
        self.bt_imagemTeste.setObjectName(u"bt_imagemTeste")
        self.bt_imagemTeste.setGeometry(QRect(440, 140, 120, 30))
        self.bt_imagemTeste.setMinimumSize(QSize(120, 30))
        self.bt_imagemTeste.setSizeIncrement(QSize(0, 10))
        self.bt_imagemTeste.setFont(font)
        self.bt_imagemTeste.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.bt_imagemTeste.setStyleSheet(u"")
        self.lb_tituloTeste = QLabel(self.centralwidget)
        self.lb_tituloTeste.setObjectName(u"lb_tituloTeste")
        self.lb_tituloTeste.setGeometry(QRect(570, 140, 131, 30))
        self.lb_tituloTeste.setMinimumSize(QSize(120, 30))
        self.lb_tituloTeste.setFont(font)
        self.bt_imagemPredizer = QPushButton(self.centralwidget)
        self.bt_imagemPredizer.setObjectName(u"bt_imagemPredizer")
        self.bt_imagemPredizer.setGeometry(QRect(600, 480, 120, 30))
        self.bt_imagemPredizer.setMinimumSize(QSize(120, 30))
        self.bt_imagemPredizer.setFont(font)
        self.bt_imagemPredizer.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.bt_imagemPredizer.setStyleSheet(u"")
        self.txt_predicao = QLineEdit(self.centralwidget)
        self.txt_predicao.setObjectName(u"txt_predicao")
        self.txt_predicao.setGeometry(QRect(310, 480, 281, 30))
        self.txt_predicao.setMinimumSize(QSize(0, 30))
        self.txt_predicao.setStyleSheet(u"")
        self.lb_resultadoPredicao = QLabel(self.centralwidget)
        self.lb_resultadoPredicao.setObjectName(u"lb_resultadoPredicao")
        self.lb_resultadoPredicao.setGeometry(QRect(130, 480, 181, 30))
        self.lb_resultadoPredicao.setMinimumSize(QSize(120, 30))
        self.lb_resultadoPredicao.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(whatsthis)
        self.lb_imagemTreino.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.lb_imagemTreino.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/semimagem/imagens/semImagem.png\"/></p></body></html>", None))
#if QT_CONFIG(whatsthis)
        self.lb_imagemTeste.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.lb_imagemTeste.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/semimagem/imagens/semImagem.png\"/></p></body></html>", None))
        self.lb_titulo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">Sistema de Reconhecimento Facial</span></p></body></html>", None))
        self.bt_imagemTreino.setText(QCoreApplication.translate("MainWindow", u"Carregar", None))
        self.lb_tituloTreino.setText(QCoreApplication.translate("MainWindow", u"Imagem Treino", None))
        self.bt_imagemTeste.setText(QCoreApplication.translate("MainWindow", u"Carregar", None))
        self.lb_tituloTeste.setText(QCoreApplication.translate("MainWindow", u"Imagem Teste", None))
        self.bt_imagemPredizer.setText(QCoreApplication.translate("MainWindow", u"Predizer", None))
        self.lb_resultadoPredicao.setText(QCoreApplication.translate("MainWindow", u"Resultado predi\u00e7\u00e3o:", None))
    # retranslateUi

### Botões sistema ###
        self.bt_imagemTreino.clicked.connect(self.imagemTreino)
        self.bt_imagemTeste.clicked.connect(self.imagemTeste)
        self.bt_predizer.clicked.connect(self.predizer)


    ### Funções do sistema
    ## Carrega imagem Treino ##
    def imagemTreino(self):
        Tk().withdraw()
        path = askopenfilename()
        arquivo = path.split('Imagens/')
        listaTreino = arquivo[1].split('.')
        global imgTreino
        imgTreino = listaTreino[0]
        urlTreino = 'image: url(:/' + imgTreino + '/Imagens/' + imgTreino + '.png)'
        self.lb_imagemTreino.setStyleSheet(urlTreino)
        imgTreino = face_recognition.load_image_file(path)

    ## Carrega imagem Teste ##
    def imagemTeste(self):
        Tk().withdraw()
        path = askopenfilename()
        arquivo = path.split('Imagens/')
        listaTeste = arquivo[1].split('.')
        global imgTeste
        imgTeste = listaTeste[0]
        urlTeste = 'image: url(:/' + imgTeste + '/Imagens/' + imgTeste + '.png)'
        self.lb_imagemTeste.setStyleSheet(urlTeste)
        imgTeste = face_recognition.load_image_file(path)

    ## Predição de Imagens ##
    def predizer(self):
        # Cortar imagem #
        treino_rgb = cv2.cvtColor(imgTreino, cv2.COLOR_BGR2RGB)
        teste_rgb = cv2.cvtColor(imgTeste, cv2.COLOR_BGR2RGB)
        locations_treino = face_recognition.face_locations(treino_rgb)
        locations_teste = face_recognition.face_locations(teste_rgb)
        for top, right, bottom, left in locations_treino:
            crop_treino = treino_rgb[top:bottom, left:right]
            cv2.imwrite('crop_treino.png', crop_treino)
        for top, right, bottom, left in locations_teste:
            crop_teste = teste_rgb[top:bottom, left:right]
            cv2.imwrite('crop_teste.png', crop_teste)
        cv2.imshow('crop_treino', crop_treino)
        cv2.imshow('crop_teste', crop_teste)
        # Carrega imagens para predição #
        my_face_encoding = face_recognition.face_encodings(imgTreino)[0]
        unknown_face_encoding = face_recognition.face_encodings(imgTeste)[0]
        # Predição #
        results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)
        # Resultados #
        if results[0] == True:
            resultado = 'As imagens são da mesma pessoa'
            self.txt_predicao.setText(resultado)
        else:
            resultado = 'As imagens não são da mesma pessoa'
            self.txt_predicao.setText(resultado)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())