def hitung_luas_segitiga():
    alas = float(input("Masukkan alas segitiga: "))
    tinggi = float(input("Masukkan tinggi segitiga: "))
    luas = 0.5 * alas * tinggi
    print(f"Luas segitiga adalah: {luas}\n")

def hitung_luas_persegi_panjang():
    panjang = float(input("Masukkan panjang persegi panjang: "))
    lebar = float(input("Masukkan lebar persegi panjang: "))
    luas = panjang * lebar
    print(f"Luas persegi panjang adalah: {luas}\n")

def tentukan_ganjil_genap():
    angka = int(input("Masukkan sebuah angka: "))
    if angka % 2 == 0:
        print(f"{angka} adalah angka genap\n")
    else:
        print(f"{angka} adalah angka ganjil\n")

def main():
    while True:
        print("===== Program Kalkulator Sederhana =====")
        print("Menu")
        print("1. Hitung Luas Segitiga")
        print("2. Hitung Luas Persegi Panjang")
        print("3. Tentukan number gan
