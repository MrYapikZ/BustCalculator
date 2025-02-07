from PyQt5.QtWidgets import QMainWindow, QApplication, QCheckBox, QDialogButtonBox, QVBoxLayout, QWidget, QComboBox, QLabel, QFileDialog, QPushButton, QToolButton, QMessageBox, QAbstractItemView
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
from PyQt5 import QtGui, QtWidgets, QtCore
from typing import List, Optional, Tuple
from PyQt5.QtGui import QPixmap
import textwrap
import subprocess
import json
import sys
import csv
import os
import re
import cv2
import numpy as np
import matplotlib.pyplot as plt

from main_ui import Ui_MainWindow

class MainUI(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        self.setupUi(self)

        self.setWindowTitle("Bust Calculator")

        self.resize(500, 500)
        self.max_size = 800
        self.label_Preview.setScaledContents(True)

        self.image_path = ''

        self.toolButton_locateImage.clicked.connect(self.locate_image)
        self.pushButton_generate.clicked.connect(self.generate)

# PyQt Program =========================================================================================================
    def locate_image(self):
        imagePath, _ = QFileDialog.getOpenFileName(
            None,  # Parent window (None if standalone)
            "Open Image File",  # Dialog title
            "",  # Default directory
            "Images (*.png *.jpg *.jpeg *.bmp *.gif)"  # Filter for image files
        )

        if imagePath:
            self.image_path = imagePath
            self.label_imagePath.setText(str(imagePath))
            pixmap = QPixmap(str(imagePath))
            if not pixmap.isNull():
                pixmap = pixmap.scaled(self.max_size, self.max_size, Qt.AspectRatioMode.KeepAspectRatio)
                self.label_Preview.setPixmap(pixmap)
            print(f"Blender executable path selected: {self.image_path}")

# Main Program =========================================================================================================
    def keliling_oval(self, a, b):
        return np.pi * (3 * (a + b) - np.sqrt((3 * a + b) * (a + 3 * b)))

    # Menghitung ukuran cup
    def hitung_cup(self, keliling_dada, keliling_bawah_dada):
        selisih = keliling_dada - keliling_bawah_dada
        if selisih < 12.5:
            return "A"
        elif selisih < 15:
            return "B"
        elif selisih < 17.5:
            return "C"
        elif selisih < 20:
            return "D"
        else:
            return "E+"

    # Fungsi untuk memilih titik pada gambar
    def pilih_titik(self, gambar, title):
        plt.imshow(cv2.cvtColor(gambar, cv2.COLOR_BGR2RGB))
        plt.title(title)
        titik = plt.ginput(2)  # Pilih dua titik
        plt.close()
        return titik

    # Program utama
    def generate(self):
        if not self.image_path or not os.path.exists(self.image_path):
            QMessageBox.warning(self, "Error", f"Image path is not set or invalid: {self.image_path}")
            return

        if not self.lineEdit_height.text():
            QMessageBox.warning(self, "Error", f"Please input character height!")
            return

        # path_gambar = input("Masukkan path gambar: ")
        # tinggi_karakter = float(input("Masukkan tinggi karakter (cm): "))

        gambar = cv2.imread(self.image_path)
        tinggi_gambar = gambar.shape[0]

        # Skala piksel ke cm
        skala = int(self.lineEdit_height.text()) / tinggi_gambar

        # Pilih titik pengukuran
        print("Pilih dua titik untuk masing-masing pengukuran.")
        lebar_dada_depan = self.pilih_titik(gambar, "Lebar Dada (Depan)")
        lebar_dada_samping = self.pilih_titik(gambar, "Lebar Dada (Samping)")
        lebar_bawah_dada_depan = self.pilih_titik(gambar, "Lebar Bawah Dada (Depan)")
        lebar_bawah_dada_samping = self.pilih_titik(gambar, "Lebar Bawah Dada (Samping)")

        # Menghitung jarak dalam cm
        def hitung_jarak(p1, p2):
            return np.linalg.norm(np.array(p1) - np.array(p2)) * skala

        ld_depan = hitung_jarak(lebar_dada_depan[0], lebar_dada_depan[1])
        ld_samping = hitung_jarak(lebar_dada_samping[0], lebar_dada_samping[1])
        lbd_depan = hitung_jarak(lebar_bawah_dada_depan[0], lebar_bawah_dada_depan[1])
        lbd_samping = hitung_jarak(lebar_bawah_dada_samping[0], lebar_bawah_dada_samping[1])

        # Menghitung keliling
        keliling_dada = self.keliling_oval(ld_depan / 2, ld_samping / 2)
        keliling_bawah_dada = self.keliling_oval(lbd_depan / 2, lbd_samping / 2)

        # Menghitung ukuran cup
        ukuran_cup = self.hitung_cup(keliling_dada, keliling_bawah_dada)

        # Menampilkan hasil
        print(f"Keliling Dada: {keliling_dada:.2f} cm")
        print(f"Keliling Bawah Dada: {keliling_bawah_dada:.2f} cm")
        print(f"Ukuran Cup: {ukuran_cup}")
        QMessageBox.warning(self, "Result", f"Keliling Dada: {keliling_dada:.2f} cm\n"
                                            f"Keliling Bawah Dada: {keliling_bawah_dada:.2f} cm \n"
                                            f"Ukuran Cup: {ukuran_cup}")

if __name__== "__main__":
    app = QApplication(sys.argv)
    ui = MainUI()
    ui.show()
    app.exec_()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
