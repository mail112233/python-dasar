# Date dan Time

import datetime as dt

print(+8*"="+"PROGRAM"+8*"=")
print("masukan tanggal lahir\nbulan lahir dan tahun")
tanggal= int(input("tanggal \t:"))
bulan = int(input("bulan \t\t:"))
tahun = int(input("tahun \t\t:"))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"tanggal lahir anda = {tanggal_lahir}")
print(f"Harinya adalah : {tanggal_lahir:%A}")

hari_ini = dt.date.today()
print(f"hari ini adalah hari : {hari_ini:}")
umur = hari_ini - tanggal_lahir
umur_tahun = umur.days // 365
umur_bulan_sisa = (umur_tahun.days % 365) // 30
print(f"umur anda adalah = {umur_tahun} tahun dan\nharinya {tanggal_lahir:%A} bulan {umur_bulan_sisa} ")
print(f"jumlah hari : {umur.days} hari") 
