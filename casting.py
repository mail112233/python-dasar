# merubah satu tipe ke tipe lain
# tipe data = int, float, str, bool

print("============INTEGER=========")
data_int = 9;
print("data = ", data_int, ",type =", type(data_int))

data_float = float(data_int)
data_str   = str(data_int)
data_bool  = bool(data_int) # akan false jika nilai INTEGER = 0
print("data = ", data_float, ",type =", type(data_float))
print("data = ", data_str, ",type =", type(data_str))
print("data = ", data_bool, ",type =", type(data_bool))


## ini data float
print("============FLOAT===========")
data_float = 9;
print("data = ", data_float, ",type =", type(data_float))

data_int   = int(data_float) # ini akan dibulatkan kebawah
data_str   = str(data_float)
data_bool  = bool(data_float) # akan false jika nilai FLOAT = 0 
print("data = ", data_int, ",type =", type(data_int))
print("data = ", data_str, ",type =", type(data_str))
print("data = ", data_bool, ",type =", type(data_bool))


## ini data boolean
print("============BOOLEAN===========")
data_bool = False;
print("data = ", data_bool, ",type =", type(data_bool))

data_int    = int(data_bool)
data_str    = str(data_bool)
data_float  = float(data_bool) # akan false jika nilai FLOAT = 0 
print("data = ", data_int, ",type =", type(data_int))
print("data = ", data_str, ",type =", type(data_str))
print("data = ", data_float, ",type =", type(data_float))

## ini data string
print("============STRING===========")
data_str = "10";
print("data = ", data_str, ",type =", type(data_str))

data_int    = int(data_str) # ini harus angka
data_float  = float(data_str) # akan false jika nilai FLOAT = 0 
data_bool   = bool(data_str) # ini harus angka
print("data = ", data_int, ",type =", type(data_int))
print("data = ", data_float, ",type =", type(data_float))
print("data = ", data_bool, ",type =", type(data_bool))