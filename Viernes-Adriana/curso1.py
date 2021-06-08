
#skdaskdnas


"""
#ejercicio1
print("CONVERTIDOR DE CM A KM, M Y CM")
centimetros = int(input("Escriba una distancia en centímetros: "))

if centimetros <= 0:
    print("Escriba una distancia mayor que cero.")
else:
    kilometros = centimetros // 100000 #km
    metros = centimetros % 100000 // 100 #m
    resto = centimetros % 100 #cm

    print(str(centimetros) + " centímetros son " + str(kilometros) + " km "+ str(metros)+ " m " + str(resto) +" cm.")
   # print(f"{centimetros} centímetros son {kilometros} km {metros} m {resto} cm.")


#ejercico 2 y agregamos while
respuesta= input("quieres convertir? ")
while(respuesta == "si"):
    print("CONVERTIDOR DE CM A KM, M Y CM")
    centimetros = int(input("Escriba una distancia en centímetros: "))
    if centimetros <= 0:
        print("Escriba una distancia mayor que cero.")
    else:
        kilometros = centimetros // 100000
        metros = centimetros % 100000 // 100
        resto = centimetros % 100

        print(f"{centimetros} cm son ", end = "")

        if kilometros:
            print(f"{kilometros} km ", end="")
        if metros:
            print(f"{metros} m ", end="")
        if resto:
            print(resto, "cm")

    respuesta= input("\n quieres seguir convirtiendo? ")

print("gracias")
        


#usando print(f)
name = "Fred"
edad = 23
print("Su nombre es: " + name + " y su edad es: "+ str(edad)  )
print(f"Su nombre es: {name} y su edad es: {edad} ")

"""

year = int(input("Escriba el año: "))

if year%4 !=0:
    print("No es bisiesto porque no es multiplo de 4")
elif year%4==0 and year%100!=0:
    print("Es un año bisiesto porque es multiplo de 4 sin ser multiplo de 100")
elif year%100==0 and year%400!=0:
    print("No es un año bisiesto porque es multiplo de 100, sin ser multiplo de 400")
else:
    print("El año es bisiesto porque es multiplo de 400")

