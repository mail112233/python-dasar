# Buatlah program kalkulator sederhana untuk dua masukan bilangan yang mengerjakan operasi,
# penjumlahan, pengurangan, perkalian dan pembagian.

print(10*"="+"kalkutaor sederhana"+"="*10)

print(5*"-"+"penambahan"+"-"*5)
angka = input("masukan angka : ")
angka2 = input("masukan angka yang mau ditambah : ")
penambahan = int(angka) + int(angka2)
print(f"jawaban : {penambahan}")


print(5*"-"+"pengurangan"+"-"*5)
angka = input("masukan angka : ")
angka2 = input("masukan angka yang mau dikurang : ")
penambahan = int(angka) - int(angka2)
print(f"jawaban : {penambahan}")


print(5*"-"+"pengakalian"+"-"*5)
angka = input("masukan angka : ")
angka2 = input("masukan angka yang mau dikali : ")
penambahan = int(angka) * int(angka2)
print(f"jawaban : {penambahan}")


print(5*"-"+"pembagian"+"-"*5)
angka = input("masukan angka : ")
angka2 = input("masukan angka yang mau dibagi : ")
penambahan = int(angka) / int(angka2)
print(f"jawaban : {penambahan}")
print(5*"-"+"end"+"-"*5)
