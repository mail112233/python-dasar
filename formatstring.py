# format string 

# contoh generic
nama = "mail"
format_str = f"hallo {nama}"
print(format_str)

# angka 
angka = 2005.5
format_str = f"angka = {angka}"
print(format_str)

#bolean
boolean = True
format_str = f"bolean = {boolean}"
print(format_str)

# bilangan bulat 
angka = 15 
format_str = f"bilangan bulat = {angka:d}"
print(format_str)

#bilangan ribuan
angka = 1000
format_str = f"ribuan = {angka:,}"
print(format_str)

# jutaan 
angka = 2000000
format_str = f"jutaan = {angka:,}"
print(format_str)

# bilangan decimal
angka = 2005.54321
format_str = f"decimal = {angka:.1f}"
print(format_str)

# menampilkan leading zero
angka = 2005.54321
format_str = f"decimal = {angka:0009.1f}"
print(format_str)

# menampilkan tanda + tanda -
angka_minus = -10
angka_plus = 10.8576
format_minus = f"angka minus = {angka_minus:-d}"
format_plus = f"angka plus = {angka_plus:+.4f}"
print(format_minus)
print(format_plus)

# memformat persen
persentase = 0.080
format_persen = f"format persen {persentase:.2%}"
print(format_persen)

# mengoperasikan aritmatika di dalam placeholder
harga = 100000
jumlah = 8
format_str = f"harga total = Rp.{harga*jumlah:,}"
print(format_str)

# format angka lain (binary, octal, hexadecimal)
angka = 538
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hexa = f"hexadecimal = {hex(angka)}"
print(format_binary)
print(format_octal)
print(format_hexa)w
