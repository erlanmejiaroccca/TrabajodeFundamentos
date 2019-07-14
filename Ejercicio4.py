def Ejercicio4():
    print("Preguntar contraseña:")
    encontro = False

    for i in range(3):
        contrasena = input("Ingrese la contraseña:")
        if contrasena == "123":
            print("¡Enhorabuena!")
            encontro = True
            break
        else:
            print("Lo siento, contraseña equivocada")

    if encontro == False:
        print("Oportunidades Agotadas")

if __name__=="__main__":
    Ejercicio4()