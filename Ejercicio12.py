def Ejercicio12():
    print("Cajero de supermercado:")
    opcion=input("Para ingresar datos de un nuevo cliente ingrese N o T para terminar el dia:")
    totalCobrado=0
    while opcion=="N":
        opcion2 = "N"
        totalaPagar=0
        while opcion2=="N":
            precio=float(input("Ingrese el precio del articulo:"))
            unidades=int(input("Ingrese la cantidad de unidades:"))
            totalaPagar=totalaPagar+precio*unidades
            opcion2=input("Si desea ingresar un nuevo articulo ingrese N o T para terminar:")
        print("Total a pagar:", totalaPagar)
        totalCobrado=totalCobrado+totalaPagar
        opcion = input("Para ingresar datos de un nuevo cliente ingrese N o T para terminar el dia:")

    print("Total cobrado:", totalCobrado)

if __name__=="__main__":
    Ejercicio12()


