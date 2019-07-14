def Ejercicio2():
    print("Suma de numeros pares comprendidos entre A y B:")
    a = int(input("Ingrese A:"))
    b = int(input("Ingrese B:"))
    resultado=0
    for i in range(a, b+1):
        if  i%2==0:
            resultado=resultado+i
    print("Suma:", resultado)

if __name__ == '__main__':
    Ejercicio2()


