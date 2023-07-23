'''fungsi dengan return'''

# template fungsi
# def fungsi(argument):
#     badan fungsi
#     return output

# fungsi kuadrat

def kuadrat(input_angka):
    '''fungsi kuadrat'''
    output_kuadrat = input_angka**2
    return output_kuadrat

y = kuadrat(3)
print(y)

def devision(kurang):
    '''fungsi kurang'''
    output = kurang-5
    return output
 
x = devision(10)
print(x)

def kali(kali):
    '''fungsi kalian'''
    xali = kali*2
    return xali

z = kali(10)
print(z)


# fungsi return dengan dua argumen
def tambahan2(angka1,angka2):
    hasil = angka1 + angka2

    return hasil

x = tambahan2(2,8)
print(x)

# fungsi dengan banyak return
def matematika(angka1,angka2):
    tambah = angka1 + angka2
    kurang = angka1 - angka2
    kali = angka1 * angka2
    bagi = angka1 / angka2

    return tambah,kurang,kali,bagi

a,b,c,d = matematika(1,9)

print(f"hasil dari = {a}")
print(f"hasil dari = {b}")
print(f"hasil dari = {c}")
print(f"hasil dari = {d}")


'''end'''