# memasukan banyak data pada argumen

def fungsi(nama,umur,berat):
    print(f"{nama} punya umur {umur} dan berat {berat}")

fungsi("mail",17,140)

def fungsi(data_list):
    data = data_list.copy()
    nama = data[0]
    umur = data[1]
    berat = data[2]
    print(f"{nama} punya umur {umur} dan berat {berat}")

fungsi(["ilham",18,140]) 

# *args atau argumen

def fungsi(*args):
    nama = args[0]
    umur = args[1]
    berat = args[2]
    print(f"{nama} punya umur {umur} dan berat {berat}")

fungsi("dadung",18,150)

# studi kasus
def fungsi(*data):
    # data adalah type tuple dan bisa di itirasi
    output = 0
    for angka in data:
        output += angka

    return output


hasil = fungsi(1,2,3,4,5,6,7,8,9)
print(f"hasil = {hasil}")

hasil = fungsi(20,30,40)
print(f"hasil dari = {hasil}")

# waktu tepat menggunakan args adalah ketik
# membuat fungsi dan jumlah parameternya tidak jelas alias not fixed