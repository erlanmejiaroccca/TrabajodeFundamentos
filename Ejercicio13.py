def Ejercicio13():
    print("Club contra la obesidad:")
    for i in range(1, 6):
        pesoBascula = 0
        pesoInit = float(input(f"Ingrese el Peso Inicial de Persona {i} :"))
        for j in range(1, 11):
            pesoReal = float(input(f"Ingrese el peso calculado de la Bascula {j} :"))
            pesoBascula = pesoBascula + pesoReal
        if (pesoBascula / j > pesoInit):
            estadoPeso = "SUBIDO"
            diferenciaPeso = (pesoBascula / j) - pesoInit
        else:
            estadoPeso = "BAJADO"
            diferenciaPeso = pesoInit - (pesoBascula / j)
        print("Su peso es:", pesoBascula / j, " Ud. a:", estadoPeso, " en ", diferenciaPeso, " Kilos")

if __name__=="__main__":
    Ejercicio13()