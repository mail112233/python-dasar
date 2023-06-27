# a = 10, a adalah variabel dengan nilai 10 

# tipe data: angka satuan yang gaada komanya (integer)
data_integer = 110
print (" data :" , data_integer )
print (" - bertype : ", type(data_integer) )

# tipe data: angka dengan koma (float)
data_float = 1.4
print (" data :" , data_float )
print (" - bertype : ", type (data_float))

# tipe data: kumpulan karakter (string)
data_string = "ujar"
print (" data :" , data_string )
print (" - bertype : ", type (data_string))

# tipe data: biner true/false (boolean)
data_bool = True
print (" data :" , data_bool)
print (" - bertype : ", type (data_bool))

## tipe data khusus

# tipe data: komplek
data_complex = complex(4,5)
print (" data :" , data_complex )
print (" - bertype : ", type (data_complex))

# tipe data dari bahasa C

from ctypes import c_double

data_c_double = c_double(20.29)
print (" data :" , data_c_double )
print (" - bertype : ", type (data_c_double))