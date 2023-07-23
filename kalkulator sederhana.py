def tambah(angka1, angka2):
    return angka1 + angka2

def kurang(angka1, angka2):
    return angka1 - angka2

def kali(angka1, angka2):
    return angka1 * angka2

def bagi(angka1, angka2):
    return angka1 / angka2

print("Pilih operasi:")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

pilihan = input("Masukkan pilihan (1/2/3/4): ")

angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

if pilihan == '1':
    print(angka1, "+", angka2, "=", tambah(angka1, angka2))
elif pilihan == '2':
    print(angka1, "-", angka2, "=", kurang(angka1, angka2))
elif pilihan == '3':
    print(angka1, "*", angka2, "=", kali(angka1, angka2))
elif pilihan == '4':
    if angka2 != 0:
        print(angka1, "/", angka2, "=", bagi(angka1, angka2))
    else:
        print("Tidak dapat melakukan pembagian dengan angka nol!")
else:
    print("Pilihan yang Anda masukkan tidak valid.")
