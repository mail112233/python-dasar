# latihan logika dan komperasi


#+++++++3---------10+++++++++


#+++++++++++3--------
print("=====BIASA=====")
inputUser = float(input("masukan angka kurang dari 3\natau lebih dari 10 : "))

isKurangdari = (inputUser < 3)
print('kurang dari 3 =',isKurangdari)


#-----------10+++++++
isBesardari = (inputUser > 10)
print('lebih dari 10 =',isBesardari)

#logika komperasi

isbenar = isKurangdari or isBesardari
print('angka yng dimasukin',isbenar)



#-------3+++++++10-------

# kasus irisan

print("=====IRISAN=====")
inputUser = float(input('masukan angka yang bernilai\n lebih dari 3 dan\n kurang dari 10 = '))

islebihdari = (inputUser > 3)
print('lebih dari 3     = ',islebihdari)

isKurangdari = (inputUser < 10)
print('kurang dari 10   = ',isKurangdari)


isbenar = islebihdari and islebihdari
print(isbenar)