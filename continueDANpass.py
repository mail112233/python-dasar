# continue, pass, break

# pas -> dia berfungsi sebagai dummy, tidak akan berfungsi ketika di eksekusi

# pass
angka = 0

while angka < 5:
    angka += 1

    if angka == 3:
        pass # ini tidak di eksekusi
    print(angka)

# continue

x = 0
while x < 10:
    x += 1
    print(x)

    if x == 5:
        print("mantap")
        continue

    print("gaes")