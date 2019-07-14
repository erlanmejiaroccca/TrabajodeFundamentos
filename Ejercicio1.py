def Ejercicio1():
    print("Calcular el factorial de N:")
    n = int(input("Ingrese N"))
    resultado=1
    for i in range(n):
        resultado=resultado*(i+1)
    print("Resultado:", resultado)
if __name__ == '__main__':
    Ejercicio1()