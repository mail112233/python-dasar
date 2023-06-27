# operasi manipulasi string

# 1. menyambung string (concatenate)
nama_pertama = "otong"
nama_tengah = "bridge"
nama_akhir = "samto"

nama_lengkap = nama_pertama + " " + nama_tengah + "'" + nama_akhir
print(nama_lengkap)

# 2. Menghitung panjang string
panjang = len("ini barapa hayu")
print(panjang)

# 3. operator untuk string 

# mengecek apakah ada komponen char atau string di string
d = "d"
status = d in nama_lengkap
print(d + " = " + str(status))
D = "D"
status = D in nama_lengkap
print(D + " = " + str(status))
D = "D"
status = D not in nama_lengkap
print(D + " = " + str(status))

# mengulang string
print("wk"*10)
print(10*"wk")

# indexing
print("index ke 0 = " + nama_lengkap[0])
print("index ke 12 = " + nama_lengkap[12])
print("index ke -2 = " + nama_lengkap[-2])
print("index ke [0:5] = " + nama_lengkap[0:5])
print("index ke [4:13] = " + nama_lengkap[4:13])
print("index ke [0,2,4,6,8,10] = " + nama_lengkap[0:10:2])

# item paling kecil
print('paling kecil : ' + min(nama_lengkap))
# item paling besar
print('paling kecil : ' + max(nama_lengkap))
 
ascii_code = ord(" ")
print("asci code spasi = " + str(ascii_code))
ascii_code = ord("t")
print('asci code untuk "t" = ' + str(ascii_code))
data = 177
print('char untuk "177" = ' + chr(data))

# operator dalam bentuk menthod
data = "mail bin ismail kamis tuk dalang"
jumlah = data.count("i")
print("jumlah i pada ismail bin kamis adalah = " + str(jumlah))
