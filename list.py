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