data_dict = {
    'ml':'mail',
    'old':17,
    'hb':'coding'
}

print(data_dict['ml'])
print(data_dict['old'])
print(data_dict['hb'])

# operasi di dictionary
data_dict = {
    'mal':'mail',
    'apl':'apel',
    'ding':'riza'
}

# panjang dictionary
LENDICT = len(data_dict)
print(f"panjang dari dictionary: {LENDICT}")

# mengecek key exist(ada) atau tidak
KEY = "ucup"
CHECKKEY = KEY in data_dict
print(CHECKKEY)

# mengakses value (read) dengan get

print(data_dict['mal'])
print(data_dict.get('mal'))
print(data_dict.get('mil', "tidak ditemukan")) # key dengan pesan

# mengaupdate data

data_dict.update({'mal':'mail'})
data_dict.update({"jam":"time"})

print(data_dict)

data_dict.clear()
print(data_dict)

