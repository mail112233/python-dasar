# operasi logika atau boolean

# not, or, and, xor

# NOT
print('=====NOT====')
a = True
b = False
c = not b
print('not b:',c)
a = True
b = False
c = not a
print('not a:',c)

# or (jika 2 nilai false makan nilainya false)
print('=====OR====')
a = False
b = False
c = a or b
print( a,'OR',b,'=',c)
a = True
b = False
c = a or b
print( a,'OR',b,'=',c)
b = False
a = True
c = a or b
print( a,'OR',b,'=',c)
a = True
b = True
c = a or b
print( a,'OR',b,'=',c)
# AND (jika 2 nilai true maka hasilnya true)
print('=====and====')
a = False
b = False
c = a and b
print( a,'and',b,'=',c)
a = True
b = False
c = a and b
print( a,'and',b,'=',c)
b = False
a = True
c = a and b
print( a,'and',b,'=',c)
a = True
b = True
c = a and b
print( a,'and',b,'=',c)
# XOR (jika salah satu true maka nilainya true)
print('=====XOR====')
a = False
b = False
c = a ^ b
print( a,'XOR',b,'=',c)
a = True

b = False
c = a ^ b
print( a,'XOR',b,'=',c)
b = False
a = True
c = a ^ b
print( a,'XOR',b,'=',c)
a = True
b = True
c = a ^ b
print( a,'XOR',b,'=',c)
