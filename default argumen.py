def fungsi(nama = "ilham"): # nah yang pake sama dengan ini adalah defaulf argumwn
    print(f"halo {nama}")

fungsi("mail")
fungsi()


def kiau(pesan,nama = "mail"):
    '''ini contoh 2'''
    print(f"halo {nama} kamu sangat {pesan}")

kiau(f"bodoh")


def hitung(angka, pangkat):
    hasil = angka**pangkat
    return hasil

print(hitung(2,4))
hasil = hitung(pangkat=2, angka=6)
print(hasil)


# contoh 4
def fungsi(input1=10,input2=31,input3=32):
    hasil = input1 + input2 + input3
    return hasil

print(fungsi())
print(fungsi(input3=40))


