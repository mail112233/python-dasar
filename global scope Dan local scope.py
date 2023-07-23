# global and local scope

nama = "mail" # <- ini variabel global 

# akses variabel global 
def fungsi():
    print(f"menampilkan {nama}")

fungsi()

# percabangan 
for i in range(0,5):
    print(f" {i} - {nama}")

# variabel local scope
def fungsi1():
    nama_local = "mail" # <- ini adalah variabel local scope

fungsi1()
# print(nama_local) tidak bisa dijalankan 

# contoh penggunaan akses variabel

def say_mail():
    print(f"hello {nama1}")

nama1 = "mail"
say_mail()
