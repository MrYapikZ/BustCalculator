import cv2
import numpy as np
import matplotlib.pyplot as plt

# Rumus keliling oval
def keliling_oval(a, b):
    return np.pi * (3*(a + b) - np.sqrt((3*a + b)*(a + 3*b)))

# Menghitung ukuran cup
def hitung_cup(keliling_dada, keliling_bawah_dada):
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
def pilih_titik(gambar, title):
    plt.imshow(cv2.cvtColor(gambar, cv2.COLOR_BGR2RGB))
    plt.title(title)
    titik = plt.ginput(2)  # Pilih dua titik
    plt.close()
    return titik

# Program utama
def main():
    path_gambar = input("Masukkan path gambar: ")
    tinggi_karakter = float(input("Masukkan tinggi karakter (cm): "))

    gambar = cv2.imread(path_gambar)
    tinggi_gambar = gambar.shape[0]

    # Skala piksel ke cm
    skala = tinggi_karakter / tinggi_gambar

    # Pilih titik pengukuran
    print("Pilih dua titik untuk masing-masing pengukuran.")
    lebar_dada_depan = pilih_titik(gambar, "Lebar Dada (Depan)")
    lebar_dada_samping = pilih_titik(gambar, "Lebar Dada (Samping)")
    lebar_bawah_dada_depan = pilih_titik(gambar, "Lebar Bawah Dada (Depan)")
    lebar_bawah_dada_samping = pilih_titik(gambar, "Lebar Bawah Dada (Samping)")

    # Menghitung jarak dalam cm
    def hitung_jarak(p1, p2):
        return np.linalg.norm(np.array(p1) - np.array(p2)) * skala

    ld_depan = hitung_jarak(lebar_dada_depan[0], lebar_dada_depan[1])
    ld_samping = hitung_jarak(lebar_dada_samping[0], lebar_dada_samping[1])
    lbd_depan = hitung_jarak(lebar_bawah_dada_depan[0], lebar_bawah_dada_depan[1])
    lbd_samping = hitung_jarak(lebar_bawah_dada_samping[0], lebar_bawah_dada_samping[1])

    # Menghitung keliling
    keliling_dada = keliling_oval(ld_depan/2, ld_samping/2)
    keliling_bawah_dada = keliling_oval(lbd_depan/2, lbd_samping/2)

    # Menghitung ukuran cup
    ukuran_cup = hitung_cup(keliling_dada, keliling_bawah_dada)

    # Menampilkan hasil
    print(f"Keliling Dada: {keliling_dada:.2f} cm")
    print(f"Keliling Bawah Dada: {keliling_bawah_dada:.2f} cm")
    print(f"Ukuran Cup: {ukuran_cup}")

if __name__ == "__main__":
    main()
