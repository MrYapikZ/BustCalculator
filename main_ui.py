# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_Preview = QtWidgets.QLabel(self.centralwidget)
        self.label_Preview.setObjectName("label_Preview")
        self.gridLayout.addWidget(self.label_Preview, 3, 0, 1, 2)
        self.label_imagePath = QtWidgets.QLabel(self.centralwidget)
        self.label_imagePath.setObjectName("label_imagePath")
        self.gridLayout.addWidget(self.label_imagePath, 1, 0, 1, 1)
        self.pushButton_generate = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_generate.setObjectName("pushButton_generate")
        self.gridLayout.addWidget(self.pushButton_generate, 4, 0, 1, 2)
        self.lineEdit_height = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_height.setObjectName("lineEdit_height")
        self.gridLayout.addWidget(self.lineEdit_height, 2, 0, 1, 2)
        self.toolButton_locateImage = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_locateImage.setObjectName("toolButton_locateImage")
        self.gridLayout.addWidget(self.toolButton_locateImage, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 33))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_Preview.setText(_translate("MainWindow", "Preview Image"))
        self.label_imagePath.setText(_translate("MainWindow", "ImagePath"))
        self.pushButton_generate.setText(_translate("MainWindow", "Generate"))
        self.lineEdit_height.setPlaceholderText(_translate("MainWindow", "Tinggi Character"))
        self.toolButton_locateImage.setText(_translate("MainWindow", "Locate Image"))
        self.label.setText(_translate("MainWindow", "© 2025 Expi Project. All rights reserved."))
import resource_qrc
