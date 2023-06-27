# 1 ------0++++++5-----8+++++++11-------

inputUser = float(input('masukin angka lebih dari 0\n dan kurang dari 5 ='))

lebihdari = inputUser > 0
print('lebih dari 0  = ',lebihdari)
kurangdari = inputUser < 5
print('kurang dari 5 = ',kurangdari)

iscorrect = lebihdari and kurangdari
print('jawaban = ', iscorrect)
#end

inputUser = float(input('masukin angka lebih dari 8\n dan kurang dari 11 ='))

lebihdari = inputUser > 8
print('lebih dari 8 = ',lebihdari)
kurangdari = inputUser < 11
print('kurang dari 11 = ',kurangdari) 

iscorrect = lebihdari and kurangdari
print('jawaban = ', iscorrect)


# 2 ++++++0-----5++++++8------11+++++++
inputUser = float(input('masukin angka kurang dari 0\n atau lebih dari 5 = '))

kurangdari = inputUser < 0
print('kurang dari = ', kurangdari)
lebihdari = inputUser > 5
print('lebih dari = ',lebihdari)
iscorrect = lebihdari or kurangdari
print('jawaban = ', iscorrect)
#end

inputUser = float(input('masukin angka kurang dari 8\n atau lebih dari 11 = '))

kurangdari = inputUser < 8
print('kurang dari 8 = ', kurangdari)
lebihdari  = inputUser > 11
print('lebih dari 11 =', lebihdari)
iscorrect = lebihdari or kurangdari
print('jawaban = ', iscorrect)

