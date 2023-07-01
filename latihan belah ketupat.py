sisi = 10
count = 1
center = int(sisi/2)
while True:
    if (count%2):
        print(" "*center,"x"*count)
        center -= 1
        count += 1
    else:
        count += 1
        continue

    if count > sisi:
        break
    
count = count - 2
center = 1
while True:
    if (count%2):
        print(" "*center, "x"*count)
        center += 1
        count -= 1
    else:
        count -= 1
        continue
    if count == 0:
        break    

print("\n")
count = 1
while True:
    if (count%2):
        print("x"*count)
        count += 1
    else:
        count += 1
        continue

    if count > sisi:
        break
    
count = count - 2
while True:
    if (count%2):
        print("x"*count)
        count -= 1
    else:
        count -= 1
        continue
    if count == 0:
        break    

# belah ketupat
center = 5
for i in range(sisi):
    print(" "*center, "*"*count)
    count +=1
for i in range(sisi-1):
    print(" "*center, "*"*count)
    count -=1
    