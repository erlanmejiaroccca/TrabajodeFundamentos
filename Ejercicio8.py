def Ejercicio8():
    print("Tienda de naranjas:")
    costoPorKilo = 2
    costoTotal = 0

    for i in range(15):
        pedido = int(input("Ingrese cuando pide el cliente %s:" % str(i + 1)))
        if pedido > 10:
            costo = pedido * costoPorKilo
            costoConDescuento = costo - (costo * 0.15)
            costoTotal = costoTotal + costoConDescuento

            print("el monto a pagar con descuento es:", costoConDescuento)
        else:
            costo = pedido * costoPorKilo
            costoTotal = costoTotal + costo
            print("el monto a pagar es:", costo)
    print("Costo Total:", costoTotal)

if __name__=="__main__":
    Ejercicio8()