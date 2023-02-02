###valida resultados de la partida###

# Variables Globales
import fun

pareja1 = []
pareja2 = []
set1, set2, set3 = 0, 0, 0
i=1

while i <= 3:
    while True:
        try:
            print("Set Nro :",i)
            set1 = int(input("Por favor ingresa el resultado la pareja 1 :"))
            set2 = int(input("Por favor ingresa el resultado la pareja 2 :"))        
            break
        except ValueError:
            print("Lo siento, eso no es un número. Por favor inténtalo de nuevo.")

    if fun.valida_contenido(set1):
        print("El resultado es correcto")
        pareja1.append(set1)
        pareja2.append(set2)
        i += 1
    else:
            print("El resultado es INcorrecto")
else:
    print ("Carga finalizada Correctamene.!!!")

print("Resultados pareja 1: ",pareja1)
print("Resultados pareja 2: ",pareja2)