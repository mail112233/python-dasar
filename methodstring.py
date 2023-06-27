# operator method dalam string

## merubah case dalam string 

# merubah semua ke UPPERCASE
salam = "halo?"
print("biasa = " + salam)
salam = salam.upper()
print("besar = " + salam)

# LOWER
salam = "AHAHAHAHAHHAHAHAHA"
print("BESAR = " + salam)
print("BESAR = " + salam)
salam = salam.lower()
print("kecil = " + salam)

## pengecekan dengan isX method

# contoh untuk pengecekan 

salam = "skjskah"
apakah_lower = salam.islower() # hasilnya bool
print(salam + "is lower = " + str(apakah_lower))
salam = "skjskah"
apakah_lower = salam.isupper() # hasilnya bool
print(salam + "is upper = " + str(apakah_lower))

# isalpha() <-- untuk mengecek semuanya huruf
print("=======alpha=======")
is_alpha = "ABCDEFGHJ"
cek_alpha = is_alpha.isalpha()
print(is_alpha + " cek alpha = " + str(cek_alpha))
print("=======alpha=======")
# isalnum() <-- huruf dan angka
print("=======huruf dan angka=======")
number = "12345ABCDEFG"
cek_number = number.isalnum()
print(number + " is number = " + str(cek_number))
print("=======huruf dan angka=======")
# isdecimal() <-- untuk angka saja
print("=======number=======")
decimal = "12343653724586"
cek_decimal = decimal.isdecimal()
print(decimal + " is decimal + = " + str(cek_decimal))
print("=======number=======")
# isspace() <-- tab, spasi, newline \n
space = "none"
cek_space = space.isspace()
print(space + " isspace = " + str(cek_space) )
# istitle() <-- semua kata dimulai dengan huruf besar
judul = "Its Okay Gets Rich Bro"
cek_judul = judul.istitle()
print(judul + " is\ntitle = " + str(cek_judul))

## mengecek kompenen startswith() endswith() <--- gatau lagi katanya keren
cek_start = "Mail im senin".startswith("Mail")
print("start = " + str(cek_start))

cek_end = "Mail im senin".endswith("senin")
print("end = " + str(cek_end))

## penggabungan komponen join() split()
pisah = ['mail', 'bin', 'senin', 'kamis']
gabung = ','.join(pisah)
print(pisah)
print(gabung)

gabung = ' '.join(pisah)
print(gabung)

gabung = '....'.join(pisah)
print(gabung)
#splitttt
gabung = "mail,bin,kamis,haaha,"
print(gabung.split(','))

# alokasi karakter rjust(), ljust(), center()

kanan = "kanan".rjust(20)
print("'"+kanan+"'")
kiri = "kiri".ljust(20)
print("'"+kiri+"'")
tengah = "tengah".center(20,"=")
print("'"+tengah+"'")

# kebalikannya .strip() <---
tengah = "tengah".strip("=") # menghilangkan tanda =
print("'"+tengah+"'")

