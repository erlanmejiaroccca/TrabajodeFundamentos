class AlgoritmoRep(object):
    def calcularAreaCuadro(self):
        lado = float(input("Ingrese el Lado del Cuadrado:"))
        resulArea = lado * lado
        print("El area del cuadrado es:", resulArea)

    def calacularAreaTriangulo(self):
        base = float(input("Ingrese la Base del triangulo:"))
        altura = float(input("Ingrese la altura del triangulo:"))
        resulArea = (base * altura) / 2
        print("El area del Triangulo es:", resulArea)

    def calcularAreaTrapecio(self):
        baseMayor = float(input("Ingrese la Base Mayor del Trapecio:"))
        baseMenor = float(input("Ingrese la Base Menor del Trapecio:"))
        altura = float(input("Ingrese la Altura del Trapecio:"))
        resulArea = ((baseMayor + baseMenor) * altura) / 2


def main():
    obj = AlgoritmoRep()
    opcion = "continuar"
    while (opcion != "exit"):
        figura = input("Ingrese la Figura para calcular el area:")
        if (figura.lower() == "cuadrado"):
            obj.calcularAreaCuadro()
        elif (figura.lower() == "triangulo"):
            obj.calacularAreaTriangulo()
        elif (figura.lower() == "trapecio"):
            obj.calcularAreaTrapecio()
        else:
            print("Figura no encontrada!!")
        opcion = input("Desea continuar? si desea salir coloque exit:")


if __name__ == '__main__':
    main()
