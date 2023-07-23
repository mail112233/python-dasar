teman_teman = {
    'tong':'otong',
    'mal':'mail',
    'il':'ilham',
    'us':'ulis',
    'ri':'riza'
}

friend = teman_teman.copy()

print(teman_teman)
print(friend)


teman_teman['il']="ilham gandudt" 

print(teman_teman)
print(friend)

# operator ini akan mengambil data dengan di pilih
# pop dictionary 
dataMal = friend.pop('mal')
print(dataMal)
print(friend)

# pop item ini mengambil data terkhir 
dataAkhir = friend.popitem()
print(f" data akhir = {dataAkhir}")
print(friend)