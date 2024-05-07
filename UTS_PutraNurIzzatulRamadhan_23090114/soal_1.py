bilangan_pertama = float(input("Masukkan Bilangan Pertama : "))
bilangan_kedua = float(input("Masukkan Bilangan Kedua : "))

print("Silahkan Pilih Operasi : ")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Modulus")

pilihan = int(input("Masukkan Pilihan : "))

if pilihan == 1:
    hasil = bilangan_pertama + bilangan_kedua
    print("Hasil Penjumlahan :  ",hasil)
elif pilihan == 2:
    hasil = bilangan_pertama - bilangan_kedua
    print("Hasil Pengurangan :  ",hasil)
elif pilihan == 3:
    hasil = bilangan_pertama % bilangan_kedua
    print("Hasil Modulus :  ",hasil)
else:
    print("Pilihan tidak valid")