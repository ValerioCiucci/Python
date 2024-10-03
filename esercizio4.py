temp=float(input("Inserisci una temperatura in celsius"))
if temp<-273.15:
    print("Il numero inserito non e' valido ")

tempf= 9/5 * temp + 32
tempk = temp + 273.15
print("temperatura in fahrenheit : " + str(tempf))

print("temperatura in kelvin : " + str(tempk))
