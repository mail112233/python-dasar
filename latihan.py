# menggunakan range


# count = 1
# for i in range(sisi):
#     print("*"*count)
#     count += 1

# # menggunakan while
# count = 1
# while True:
#     print("*"*count)
#     count += 1

#     if count > sisi:
#         break

# menggunakan ganjil saja
sisi = 8
count = 1
spasi = int(sisi/2)
while count > 0:
    print(" "*spasi , "+"*count)
    count += 1
    spasi -= 1

    if count > sisi: # ini akan berhenti ketika count melebihi sisi
        break
    # while count > 0:
    #     print("+"*count)
    #     if count > sisi:
    #         break