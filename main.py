lis = ['mail','ilham','udin','anang','abdi']

for i, lis in enumerate(lis):
    print(i,lis)

print("\n")
for i in range(0,10):
    print(i)

print("\n")


data = int(input("masukan angka : "))

while data > 1:
    print(data)
    data += 1

    if data > 4000:
        angka = int(input("masukin angka lagi "))

        if angka > 3:
            print(angka)