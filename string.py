data = "ini adalah string"
print(data)
print(type(data))

# 1. cara membuat string 

'''
    1. bisa menggunakan single quote '....'
    2. bisa menggunakan double quote "...."
'''

data = 'menggunakan single quote'
print(data)

data = "menggunakan double quote"
print(data)

data = '"menggunakan double quote"'
print(data)

data = "'menggunakan double quote'"
print(data)

# 2. menggunakan tanda \

# membuat tanda \
    # membuat tanda ' menjadi string
print('saya mau sholat jum\'at')

# backlash
print('C:mail\\mail\\mail')

# backspace
print('print\b mail')

# tab
print('mail\t jauh')

# Newline
print('ini mail.\nini ilham.') # LF -> line feed
print('ini ilham.\rini mail.') # CR -> cariege return
print('ini mail.\r\nini ilham.') # CRLF -> line feed cariege return 

# 3. string literal atau raw

print(r'ini\b bisa\n apa\t aja')
# RAW string
print(r'ini\nnamanya\braw\\string')

# multine literal string 
print("""
nama ilham : ilham
kelas : otkp      
""")
# multine literal string dan raw 
print(r"""
nama ilham : ilham
kelas :3\notkp
website : www.ilham.com/newid     
""")