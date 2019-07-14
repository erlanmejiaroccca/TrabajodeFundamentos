import math


def Ejercicio5():
    print("Calcular la medie geometrica y la media aritmetica:")
    n = int(input("Ingrese n"))
    medG = 1
    medA = 0
    for i in range(n):
        numero = int(input("Ingrese el %s numero:" % str(i + 1)))
        medG = medG * numero
        medA = medA + numero

    medG = math.sqrt(medG)
    medA = medA / n
    print("medA:", medA)
    print("medG:", medG)
    if medA < medG:
        print("Menor:medA")
    else:
        print("Menor:medG")

if __name__=="__main__":
    Ejercicio5()