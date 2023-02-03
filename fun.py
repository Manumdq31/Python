def mi_funcion ():
    print ("Hola Función.!!!")

def valida_contenido (valor):    
    if valor >= 0 and valor <= 7:
        return True
    else:
        return False

def valida_set(dato1,dato2,numero_juego):

    print("Numero de juego :",numero_juego)

    if dato1 <= 5 and dato2 <= 5 :
        print("Juego incompleto")        
    if dato1 == 6 and dato2 <= 4 :
        print("Ganado por la pareja 1")
    if dato1 == 7 and dato2 <= 6 :
        print("Ganado por la pareja 1 en Tie-Break")
    if dato2 == 6 and dato1 <= 4 :
        print("Ganado por la pareja 2")
    if dato2 == 7 and dato1 <= 6 :
        print("Ganado por la pareja 2 en Tie-Break")
    


