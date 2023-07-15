# program list buku
list_buku = []
while True:
    print("masukan data buku")
    judul_buku = input("judul buku\t:")
    nama_penulis = input("nama penulis\t:")

    data_buku = [judul_buku,nama_penulis]
    list_buku.append(data_buku)

    print("\n\n",10*"=","DATA BUKU","="*10)
    for index,buku in enumerate(list_buku):
        print(f"{index+1} | {buku[0]} | {buku[1]}")
    
    print("\n\n",20*"=")
    islanjut = input("apakah anda mau lanjut? (y/n) ")
    
    if islanjut == "n":
        break

print(20*"=","PROGRAMM SELESAI","="*20)