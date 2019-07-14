def Ejercicio7():
    print("Calcular la suma de N valores capturados:")
    n = int(input("Ingrese n"))
    sumar = 0
    for i in range(n):
        numero = int(input("Ingrese el %s numero:" % str(i + 1)))
        sumar = sumar + numero
    print("sumar:", sumar)

if __name__=="__main__":
    Ejercicio7()