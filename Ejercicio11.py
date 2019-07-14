def Ejercicio11():
    print("Banco de inversiones:")
    inversion=100
    for i in range(12):
        print("Inversion, mes:", inversion, i+1)
        inversion=inversion+(2*inversion/100)
    print("La ganancia total del año es:", inversion)

if __name__=="__main__":
    Ejercicio11()
