from soal_4_perhitungan import hitung_bmi, kategori

def main():
    berat = float(input("Masukkan berat badan Anda (kg): "))
    tinggi = float(input("Masukkan tinggi badan Anda (meter): "))

    bmi = hitung_bmi(berat, tinggi)

    print("BMI Anda:", bmi)
    print("Kategori:", kategori(bmi))

main()