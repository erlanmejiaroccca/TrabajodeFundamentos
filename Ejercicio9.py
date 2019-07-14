def Ejercicio9():
    print("Verificacion de automoviles:")
    automoviles = 25
    sumar = 0
    for i in range(automoviles):
        contaminantes = int(input("Ingrese la cantidad de puntos contaminantes del automovil %s :" % str(i + 1)))
        sumar = sumar + contaminantes
    promedio = sumar / automoviles

    print("promedio de puntos contaminantes:", promedio)

if __name__=="__main__":
    Ejercicio9()