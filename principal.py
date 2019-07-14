from Ejercicio1 import Ejercicio1
from Ejercicio2 import Ejercicio2
from Ejercicio3 import Ejercicio3
from Ejercicio4 import Ejercicio4
from Ejercicio5 import Ejercicio5
from Ejercicio6 import Ejercicio6
from Ejercicio7 import Ejercicio7
from Ejercicio8 import Ejercicio8
from Ejercicio9 import Ejercicio9
from Ejercicio10 import Ejercicio10
from Ejercicio11 import Ejercicio11
from Ejercicio12 import Ejercicio12
from Ejercicio13 import Ejercicio13
from Ejercicio14 import Ejercicio14
def main():
    opcion = "continuar"
    while (opcion != "exit"):
        numEjercicio = input("Ingrese el numero del ejercicio:")
        if numEjercicio=="1":
            Ejercicio1()
        elif numEjercicio=="2":
            Ejercicio2()
        elif numEjercicio=="3":
            Ejercicio3()
        elif numEjercicio=="4":
            Ejercicio4()
        elif numEjercicio=="5":
            Ejercicio5()
        elif numEjercicio=="6":
            Ejercicio6()
        elif numEjercicio=="7":
            Ejercicio7()
        elif numEjercicio=="8":
            Ejercicio8()
        elif numEjercicio=="9":
            Ejercicio9()
        elif numEjercicio=="10":
            Ejercicio10()
        elif numEjercicio=="11":
            Ejercicio11()
        elif numEjercicio=="12":
            Ejercicio12()
        elif numEjercicio=="13":
            Ejercicio13()
        elif numEjercicio=="14":
            Ejercicio14()
        else:
            print("Ejercicio no encontrada")
        opcion = input("Desea continuar? si desea salir coloque exit:")


if __name__ == '__main__':
    main()