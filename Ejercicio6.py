def Ejercicio6():
    print("Suma de los primeros N numeros naturales:")
    n = int(input("Ingrese n"))
    sumar = 0
    for i in range(1, n + 1):
        sumar = sumar + i
        print(i)
    print("sumar:", sumar)

if __name__=="__main__":
    Ejercicio6()
