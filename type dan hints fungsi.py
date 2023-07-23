# type hint in python

# studi kasus
# # bentuk fungsi yang udah di pelajari 
# def fungsi(argumen):
#     # hasil = argumen**2 nah ini gabisa 
#     print(argumen)

# fungsi("ucup")

import string

def fungsi(argumen:int):
    hasil = 10**argumen
    return hasil

jawab = fungsi(2)
print(jawab)


def display(argumen:string):
    print(argumen)

display("ucup")

# type hints merupakan fitur dari python untuk kita mengenali syntak di dalam sebuah fungstion
# atau argumen 
# Kemudahan dalam memahami type data dari sebuah argument atau variabel.
# Menghasilkan kualitas code yang lebih baik dan terorganisir.