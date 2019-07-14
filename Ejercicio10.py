def Ejercicio10(n):
    print("El Departamento de Seguridad Publica y transito de la Cd. De Merida:")
    amarillo=0
    rosa=0
    roja=0
    verde=0
    azul=0
    for i in range(n):
        digito=int(input("Ingrese el ultimo digito de la placa:"))
        if digito==1 or digito==2:
            amarillo=amarillo+1
        elif digito==3 or digito==4:
            rosa=rosa+1
        elif digito==5 or digito==6:
            roja=roja+1
        elif digito==7 or digito==8:
            verde=verde+1
        elif digito==9 or digito==0:
            azul=azul+1
    print("amarillo:", amarillo)
    print("rosa:", rosa)
    print("roja:", roja)
    print("verde:", verde)
    print("azul:", azul)
if __name__=="__main__":
    Ejercicio10(2)