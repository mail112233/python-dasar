import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def run_password_generator():
    length = int(input("Masukkan panjang password yang diinginkan: "))
    password = generate_password(length)
    print("Password yang dihasilkan:", password)

run_password_generator()
