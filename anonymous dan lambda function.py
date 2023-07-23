# lambda function

def kuadrat(angka):
    '''ini fungsi biasa'''
    return angka**2

print(kuadrat(3))

# fungsi lambda
kuadrat = lambda angka:angka**2
print(kuadrat(3))

pangkat = lambda num,pow : num**pow
print(f"hasil dari = {pangkat(2,4)}")

# kegunaannya 

# sorting
data_list = ["mail","ilham","zain"]
data_list.sort()
print(data_list)

# sorting sesuai panjang huruf panjang 
data_list.sort(key=len)
print(data_list)

# menggunakan costum def
def panjang_nama(nama):
    return len(nama)

data_list.sort(key=panjang_nama)
print(data_list)

# sort pakai lambda
data_list = ["mail","ilham","zain"]
data_list.sort(key=lambda nama:len(nama))
print(data_list)

# filter 
data_angka = [1,2,3,4,5,6,7,8,9,10,11]
data_angka_baru = list(filter(lambda y:y<7,data_angka))
print(data_angka_baru)

# kasus genap
data_angka_baru = list(filter(lambda y:(y%2==0),data_angka))
print(data_angka_baru)
# kasus ganjil
data_angka_baru = list(filter(lambda y:(y%2!=0),data_angka))
print(data_angka_baru)
# bilaangan 3
data_angka_baru = list(filter(lambda y:(y%3==0),data_angka))
print(data_angka_baru)
# bilaangan 5
data_angka_baru = list(filter(lambda y:(y%5==0),data_angka))
print(data_angka_baru)


# anonymous function
# currying <- Haskel Curry

def pankat(angka,n):
    hasil =angka**n
    return hasil

data_hasil = pangkat(2,4)
print(data_hasil)


# dengan currying
def pangkat(n):
    return lambda angka:angka**n

pangkat2 = pangkat(2)
print(pangkat2(3))
pangkat3 = pangkat(3)
print(pangkat3(3))
print(f"pangkat dari 5 pangkat 5 = {pangkat(5)(5)}")

