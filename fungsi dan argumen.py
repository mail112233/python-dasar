
def nama_fungsi(nama):
    '''fungsi string'''
    print(f"selamat datang {nama}")

nama_fungsi("mail")
nama_fungsi("ilham")

# fungsi menggunakan tambah atau aritmatika
def tambahan(angka1,angka2):
    '''fungsi tambah'''
    hasil = angka1 + angka2
    print(f"{angka1} + {angka2} = {hasil}")

tambahan(4,8486)
tambahan(5,3)

def loop(list_peserta):
    '''fungsi looping'''
    daftar_peserta = list_peserta.copy()
    for peserta in daftar_peserta:
        print(f"halo anggota peserta {peserta}")

anggota = ["1. mail", "ilham", "maul"]

loop(anggota)

anggota2 = ['said','abdi','arul']

loop(anggota2)

def looping(list_operasi):
    for operasi in list_operasi:
        print(f"{operasi}")

header = ["tambahan","kurangan","kalian","bagian"]
looping(header)