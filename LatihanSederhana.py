import datetime as td 

print("masukin tanggal, bulan dan tahun lahir anda")
tanggal = int(input("tanggal lahir : "))
bulan = int(input("bulan lahir : "))
tahun = int(input("tahun lahir : "))

tanggal_lahir = td.date(tahun,bulan,tanggal)
print(f"tanggal lahir anda : {tanggal_lahir}")

hari_lahir = td.date.today()
print(f"hari lahir anda {hari_lahir:%A}")

jumlah_umur = hari_lahir - tanggal_lahir
jumlah_tahun = jumlah_umur.days // 365
jumlah_bulan = (jumlah_umur.days % 365) // 30
print(f"umur anda adalah {jumlah_tahun} tahun, bulan {jumlah_bulan} bulan")