# operasi komperasi 

# setiap hasil dari komperasi adalah boolean
# <,<,>=,<=,==,is,is not

a = 11
b = 3

# lebih besar dari >
print("=========LEBIH DARI=======")
hasil = a > 1
print(a,'>',1,hasil)
hasil = a > 9
print(a,'>',1,hasil)
hasil = b > 1
print(b,'>',1,hasil)
hasil = b > 9
print(b,'>',1,hasil)

# kurang dari <
print("=========KURANG DARI=======")
hasil = a < 1
print(a,'<',1,hasil)
hasil = a < 9
print(a,'<',1,hasil)
hasil = b < 1
print(b,'<',1,hasil)
hasil = b < 9
print(b,'<',1,hasil)
# kurang dari >
print("=========KURANG DARI=======")
hasil = a < 1
print(a,'<',1,hasil)
hasil = a < 9
print(a,'<',1,hasil)
hasil = b < 1
print(b,'<',1,hasil)
hasil = b < 9
print(b,'<',1,hasil)

# is sebgai kompresi objek identity
print('\nINI ADALAH IS\n')
x = 5 # ini adalah assigment membuat objek
y = 5
hasil = x is y
print ('x is y',hasil)

# is sebgai kompresi objek identity
print('\nINI ADALAH IS\n')
x = 5 # ini adalah assigment membuat objek
y = 7
hasil = x is y
print ('x is y',hasil)

