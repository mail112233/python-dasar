# width dan multiline

# data
nama = "mail"
umur = 17
tinggi = 169.9
ukuran_kaki = 45

# string menggunakan multilane dengan menggunakan newline
data_string = f"nama = {nama} \numur = {umur} \ntinggi = {tinggi} \nukuran kaki = {ukuran_kaki}"

print(5*"="+"DATA STRING"+5*"=")
print(data_string)

# string multilinr (kutip triplets)

data_string = f"""
nama = {nama}
nama = {nama:>5}
umur = {umur:>5}
tinggi = {tinggi}
ukuran kaki = {ukuran_kaki}
"""

print(5*"="+"DATA STRING"+5*"=")
print(data_string)