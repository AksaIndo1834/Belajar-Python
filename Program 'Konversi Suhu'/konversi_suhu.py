print()

print('========== KONVERSI SUHU ==========')

print()

#Celcius ke satuan suhu lainnya
Data_suhu_celcius = float(input("Masukan nilai suhu dalam celcius = "))
print("Suhu celcius =",Data_suhu_celcius,"°C")

print()

print("Hasil konversi:")
print("Suhu dalam Fahrenheit =", ((9/5)*Data_suhu_celcius)+32, "°F")
print("Suhu dalam Kelvin =", Data_suhu_celcius+273, "K")
print("Suhu dalam Reamur =", (4/5)*Data_suhu_celcius, "°Re")

print()
print("-"*40)
print()

#Fahrenheit ke satuan suhu lainnya
Data_suhu_fahrenheit = float(input("Masukan nilai suhu dalam fahrenheit = "))
print("Suhu fahrenheit =",Data_suhu_fahrenheit,"°F")

print()

print("Hasil konversi:")
print("Suhu dalam Celcius =", 5/9*(Data_suhu_fahrenheit-32), "°C")
print("Suhu dalam Kelvin =", 5/9*(Data_suhu_fahrenheit-32)+273, "K")
print("Suhu dalam Reamur =", 4/9*(Data_suhu_fahrenheit-32), "°Re")

print()
print("-"*40)
print()

#Kelvin ke satuan suhu lainnya
Data_suhu_kelvin = float(input("Masukan nilai suhu dalam kelvin = "))
print("Suhu kelvin =",Data_suhu_kelvin,"K")

print()

print("Hasil konversi:")
print("Suhu dalam Celcius =", Data_suhu_kelvin-273, "°C")
print("Suhu dalam Fahrenheit =", 9/5*(Data_suhu_kelvin-273)+32, "°F")
print("Suhu dalam Reamur =", 4/5*(Data_suhu_kelvin-273), "°Re")

print()
print("-"*40)
print()

#Reamur ke satuan suhu lainnya
Data_suhu_reamur = float(input("Masukan nilai suhu dalam reamur = "))
print("Suhu reamur =",Data_suhu_reamur,"°Re")

print()

print("Hasil konversi:")
print("Suhu dalam Celcius =", (4/5)*Data_suhu_reamur, "°C")
print("Suhu dalam Fahrenheit =", ((9/4)*Data_suhu_reamur)+32, "°F")
print("Suhu dalam Kelvin =", ((5/4)*Data_suhu_reamur)+273, "K")

print()
print()

print("**Konversi Selesai**")

print()