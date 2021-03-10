print("===== Program Menghitung Luas Persegi Panjang =====")

panjang = float(input("Masukkan panjang"))
lebar = float(input("Masukkan lebar"))
luas = panjang*lebar
print("Luas persegi panjang adalah", luas, "satuan")


print("===== Program Menghitung Luas Lingkaran =====")

jari_jari = float(input("masukkan jari-jari"))
phi = 3.14
luas = jari_jari*jari_jari*phi
print("Luas lingkaran adalah", luas, "satuan")


print("===== Program Menghitung Luas Permukaan Kubus =====")

sisi = float(input("Masukkan sisi"))
luas_permukaan = 6*sisi*sisi
print("Luas permukaan kubus adalah", luas_permukaan, "satuan")


print("===== Menghitung Konversi Suhu Celsius ke Farenheit =====")
celcius = float(input("Masukkah suhu celsius"))
konversi = ((9/5)*celcius)+32
print("Konversi suhu celcius ke farenheit nya adalah", konversi, "derajat")


print("===== Menghitung Konversi Suhu Reamur ke Kelvin =====")

reamur = float(input("Masukkan suhu reamur"))
konversi = ((5/4)*reamur)+273
print("Konversi suhu reamur ke kelvin adalah", konversi, "derajat")
