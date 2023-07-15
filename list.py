data_angka = [1,2,3]
print(data_angka)

data_string = ["mail", "tok dalang", "mei mei"]
print(data_string)

data_boolean = [True, False, True, False]
print(data_boolean)


data_campuran = [1,"ucup mau beli", True]
print(data_campuran)

data_range = range(0,9,2) # range (start, stop, step)
print(data_range)
data_list = list(data_range)
print(data_list)

list_pake_for = [i for i in range(0,10)]
print(list_pake_for)

# pakai pangkat
list_pake_for = [i**5 for i in range(0,10)]
print(list_pake_for)

list_pakai_for_if = [i for i in range(0,10) if i != 5]
print(list_pakai_for_if)

list_pakai_for_if = [i for i in range(0,10) if i%2 ==0]
print(list_pakai_for_if)

print("\n")
print(10*"="+"MANIPULASI LIST"+"="*10)
# manipulaition list 
# index  0[-3]  1[-2]    2 [-1]
data = ["ucup","mail","tok dalang"]

# mengambil data dari list 
data_0 = data[0]
print(f"index 0 = {data_0}")

# mengambil data terakhir 
data_1 = data[-1]
print(f"data terakhir = {data_1}")

# cara mengetahui panjang list
panjang = len(data)
print(f"panjang dataa adalah = {panjang}")

# cara menambah item di list 
data.insert(1,"anak kecil")
print(data)

# cara menambah data di akhhir list 
data.append("amar")
print(data)

# cara menambah list di dalam list
data_baru = ["apel", "pen","pulpen"]
data.extend(data_baru)
print(f"data gabungan = {data}")

# merubah data 
data[2] = "pacil"
print(data)

# cara menghapus data 
data.remove("pacil")
print(data)

# cara manghapus akhir data
data.pop()
print(data)

# cara membalik data 
data.reverse()
print(data)

# mensortir data list
data.sort()
print(data)

# mensortir data list
angka = [1,3489,3,3,4,5,3,26,5100,53,]
angka.sort()
print(angka)


print("\n")
print(5*"="+"MANIPULASI LIST ANGKA"+"="*5)

data_angka = [1,4,6,3,6,2,4,5,3,4,6,3,1,4,6,2,6,]

print(f"data angka adalah = {data_angka}")

# count data 

data_6 = data_angka.count(6)
data_3 = data_angka.count(3)

print(f"JUMLAH ANGKA  6 = {data_6}")
print(f"JUMLAH ANGKA  3 = {data_3}")

# ambil posisi data

print(f"data = {data}") 

index_ucup = data.index("ucup")
print(f"index data = {index_ucup}")

# cara mengurutkan data 

data_angka.sort()
print(f"data angka sort =\n{data_angka}")

# data string
data.sort()
print(f"data string sort =\n{data}")

# cara membalik data 
data_angka.reverse()
print(f"data angka reverse =\n{data_angka}")

# cara membalik data string
data.reverse()
print(f"data string reverse =\n{data}")


# copy data 
print("\n")
print(5*"="+"COPY LIST"+"="*5)

a = ["mail","amel","mael"]
print(f"a = {a}")

# ini data a dan b sama

b = a
print(f"b = {b}")

# dengan menggunakan copy bisa menduplikat 

c = a.copy()
print(f"c = {c}")

c[0] = "jarjit"
print(f"c = {c}")


print("\n")
print(5*"="+"NESTED LIST ATAU LIST BERSARANG "+"="*5)
print("\n")

data_0 = [1,2]
data_1 = [3,4]

list_2d = [data_0,data_1,4,5,"mail"]
print(f"list 2D = {list_2d}")

# contoh pengunaan 

peserta_0 = ["mail",18,"laki laki"]
peserta_1 = ["otong",19,"laki laki"]
peserta_2 = ["meimei",20,"betina"]

list_peserta = [peserta_0,peserta_1,peserta_2]

for peserta in list_peserta:
    print(f"nama :\t{peserta[0]}")
    print(f"umur :\t{peserta[1]}")
    print(f"gander : {peserta[2]}\n")


print("\n")
print(5*"="+"NESTED LIST ATAU LIST BERSARANG "+"="*5)
print("\n")

data_0 = [1,2]
data_1 = [3,4]

data_2d = [data_0,data_1]

print(f"data 2d = {data_2d}")