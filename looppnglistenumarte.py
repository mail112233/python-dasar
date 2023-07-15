kumpulan_angka = [1,2,3,4,5,2,5,2,5,6,2]

for angka in kumpulan_angka:
    print(f"angka = {angka}")

peserta = ['dadang','fifng','fange']

for nama in peserta:
    print(f"nama peserta = {nama}")

# for loop dan range 

kumpulan_angka = [1,2,3,4,5,2,5,2,5,6,2]

panjang = len(kumpulan_angka)

for i in range(panjang):
    print(f"angka = {kumpulan_angka[i]}")

# while
print("\n")
print(5*"="+"while"+"="*5)
kumpulan_angka = [1,2,3,4,5,2,5,2,5,6,2]

panjang = len(kumpulan_angka)
i = 0

while i < panjang:
    print(f"angka = {kumpulan_angka[i]}")
    i += 1


# list comprehension

print("\n")
data = ["ucup",1,2,3,4,5,"otong"]

[print(f"data={x}") for x in data]

# enumerate
print("\n")

data_list = ["ucup",1,2,3,4,5,"otong"]
for index,data in enumerate(data_list):
    print(f"data ={data}, index = {index}")

# angka kuadrat
print("\n")

angka = [20,30,30,49,29]

angka_kuadrat = [i**2 for i in angka]
print(f"angka kuadrat = {angka_kuadrat}")