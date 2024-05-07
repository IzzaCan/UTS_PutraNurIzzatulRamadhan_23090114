tahun_input = input("Masukkan tahun: ")

if tahun_input.isdigit():
    tahun = int(tahun_input)
    if (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0):
        print(f"Tahun {tahun} merupakan tahun kabisat.")
    else:
        print(f"Tahun {tahun} bukan merupakan tahun kabisat.")
else:
    print("Input tidak valid.")
