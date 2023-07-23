def fungsi(nama,tinggi,berat):
    print(f"{nama} punya tinggi {tinggi} punya berat {berat}")

fungsi("mail",180,40)


def fungsi(**kwargs):
    '''fungsi kwargs'''
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]
    print(f"{nama} punya tinggi {tinggi} punya berat {berat}")


fungsi(nama="mail",tinggi=180,berat=40)

# studi kasus
def math(*args, **kwargs):
    '''studi kasus'''
    output = 0
    if kwargs["option"] == "tambah":
        for angka in args:
            output += angka
    elif kwargs["option"] == "kali":
        output = 1
        for angka in args:
            output *= angka
    return output

hasil = math(1,2,3,4,5,option="tambah")
print(f"hasil tambahan {hasil}")

hasil = math(1,2,3,4,5,option="kali")
print(f"hasil pengkalian {hasil}")