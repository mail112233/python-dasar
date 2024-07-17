# # fahrenhiet

# print("\nPROGRAM KONVERSI FAHRENHIET KE KELVIN\n")

# fahrenhiet = float(input('masukin fahrenhiet disini :'))
# print("suhu adalah",fahrenhiet,"fahrenhiet")

# kelvin = fahrenhiet + 273
# print("suhu dalam kelvin adalah",kelvin,"kelvin")


# # kelvin ke fahrenhiet
# print("\nPROGRAM KONVERSI KELVIN KE FAHRENHIET\n")

# kelvin = float(input('masukin kelvin disini :'))
# print("suhu adalah",kelvin,"kelvin")

# fahrenhiet = ((9/5) * kelvin) + 32
# print("suhu dalam fahrenheit adalah ",fahrenhiet,"fahrenhiet")

new version
import time

def delay_print(text, delay=0.01):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # untuk pindah ke baris baru setelah teks selesai dicetak


import time

def delay_printk(text, delay=0.01):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

    
delay_print("=====konversi fahrenheit -> kelvin=====")
delay_print("program konversi fahrenheit ke kelvin")

fahrenheit = float(input("masukkan fahrenheit : "))
delay_print(f"fahrenheit adalah = {fahrenheit} fahrenheit")
kelvin = (fahrenheit - 32) / 1.8 + 273.15
delay_print(f"kelvin adalah = {kelvin} kelvin")
delay_print("=====konversi fahrenheit -> kelvin=====")


delay_printk("=====program kelvin -> fahrenheit=====")
kelvin = float(input("masukkan kelvin = "))
delay_printk(f"kelvin adalah = {kelvin} kelvin")
fahrenheit  = (kelvin - 273) * 1.8 + 32
delay_printk(f"fahrenheit adalah = {fahrenheit} fahrenheit")




