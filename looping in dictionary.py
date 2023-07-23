teman_teman = {
    'tong':'otong',
    'mal':'mail',
    'il':'ilham',
    'uls':'ulis',
}

for teman in teman_teman: # ini ngeprint keys nya aja
    print(teman)
print("\n")
for teman in teman_teman.keys(): # dan ini juga sama keysnya saja namun ini menggunakan operator
    print(teman)
print("\n")
# nah kalau ini mengambil nilai dalam keysnya atau value
for teman in teman_teman.values():
    print(teman)

item = teman_teman.items()
print(item)
# bisa juga begini dengan menggunakan operator item lebih mudah mengetahui tupple
for item in teman_teman.items():
    print(item)

# bisa juga begini mengambil keduanya
for key,value in teman_teman.items():
    print(f"{key}, value = {value}")


