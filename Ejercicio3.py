def Ejercicio3():
    print("Matricula Cursos Estudiante:")
    isCurso = 1
    nCursos = 10
    contador = 0
    sumCreditos = 0
    multCredCalif = 0
    multCredCalifX = 0
    matriz = [[0] * nCursos for i in range(nCursos)]
    while (isCurso):
        matriz[contador][0] = input("Ingrese el codigo del curso:")
        if (matriz[contador][0] != "9999"):
            matriz[contador][1] = input("Ingrese el Nombre del Curso:")
            matriz[contador][2] = float(input("Ingrese la calificacion del curso:"))
            matriz[contador][3] = int(input("Ingrese el numero de Creditos:"))
            multCredCalif = matriz[contador][2] * matriz[contador][3]
            multCredCalifX = multCredCalifX + multCredCalif
            sumCreditos = sumCreditos + matriz[contador][3]
            contador = contador + 1
        else:
            if (sumCreditos >= 25 and sumCreditos <= 50):
                isCurso = 0
                for i in range(0, contador):
                    print(matriz[i][0], "\t", matriz[i][1], "\t", matriz[i][2], "\t", matriz[i][3])
                print("Cantidad de Cursos Matriculados es:", contador)
                print("Promedio Ponderado es:", multCredCalifX / sumCreditos)
                print("La suma de los creditos es:", sumCreditos)
            else:
                print("La suma de creditos debe ser mayor o igual que 25 y menor o igual que 50")
                print("Ingrese Nuevamente los Cursos:")
                isCurso = 1
                contador = 0
                sumCreditos = 0
if __name__=="__main__":
    Ejercicio3()