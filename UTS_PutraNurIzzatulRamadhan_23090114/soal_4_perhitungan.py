def hitung_bmi(berat, tinggi):
    bmi = berat / tinggi
    return bmi

def kategori(bmi):
    if bmi < 18.5:
        print("Berat badan kurang")
    elif 18.5 <= bmi < 24.9:
        print("Berat badan normal")
    elif 25 <= bmi < 29.9:
        print("Kelebiahan berad badan")
    else:
        print("Anda termasuk obesitas.")