# operasi yang dilakukan dengan penyingkatan
# operasi ditambah dengan assigment

a = 5 # a adalah assigemnt
print("nilai a : ", a)

a += 1 # ini artinya a = 5 + 1
print("nilai a = ", a)

a -= 2 # ini artinya a = 6 - 2
print("nilai a = ", a)

a *= 5 # ini artinya a = 4 * 5
print("nilai a = ", a)

a /= 2 # ini artinya a = 20 /(bagi) 2
print("nilai a = ", a)

b = 10
print("\nnilai b = ", b)
 
b %= 3 
print("nilai b = ", b)

b = 10
print("\nnilai b = ", b)
 
b //= 3 
print("nilai b = ", b)

a = 5
print("nilai a = ", a)

a **= 3
print('nilai a = ', a)

# operasi bitwise

# OR
c = True
print("\nnilai c = ", c)
c |= False
print('nilai c |= ', c)
c = False
print("\nnilai c = ", c)
c |= False
print('nilai c |= ', c)

# AND

c = True
print("\nnilai c = ", c)
c &= False
print('nilai c &= ', c)
c = True
print("\nnilai c = ", c)
c &= True
print('nilai c &= ', c)

# XOR

c = True
print("\nnilai c = ", c)
c ^= False
print('nilai c ^= ', c)
c = True
print("\nnilai c = ", c)
c ^= True
print('nilai c ^= ', c)

# geser geser
d = 0b0100
print("\nnilai d = ", format(d,'04b'))
d >>= 2
print('nilai d >>= 2 = ', format(d, '04b'))
d <<= 1
print('nilai d <<= 1 = ', format(d, '04b'))
