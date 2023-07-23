import datetime
import os

mahasiswa1 = {
    'nama':'mail',
    'nim':'287927489',
    'sks_lulus':130,
    'beasiswa':True,
    'lahir':datetime.datetime(2005,10,31)
}
mahasiswa2 = {
    'nama':'abdi',
    'nim':'2879274437',
    'sks_lulus':136,
    'beasiswa':False,
    'lahir':datetime.datetime(2007,10,31)
}
mahasiswa3 = {
    'nama':'rixa',
    'nim':'587927489',
    'sks_lulus':130,
    'beasiswa':True,
    'lahir':datetime.datetime(2001,10,31)
}

data_mahasiswa = {
    'MAH1':mahasiswa1,
    'MAH2':mahasiswa2,
    'MAH3':mahasiswa3
}
os.system("cls")
print(f"{'KEY':<6} {'NAMA':<17}{'SKS':<7} {'BEASISWA':<10} {'LAHIR':<10}")
print(60*"-")
 
for mahasiswa in data_mahasiswa:
    KEY = mahasiswa

    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nim']
    SKS = data_mahasiswa[KEY]['sks_lulus']
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime('%x')

    print(f"{KEY:<6} {NAMA:<17} {SKS:<8} {BEASISWA:^9} {LAHIR:<10}")


