def Ejercicio14():
    print("Censo Nacional de Vivienda")
    isVivienda = 1
    primaria, secundaria, carrTecnica, carrProfesional, postgrado = 0, 0, 0, 0, 0
    while (isVivienda):
        nombrePersona = input("Ingrese el Nombre de la Persona:")
        print("1=Primaria\n2=Secundaria\n3=Carrera Tecnica\n4=Carrera Profesional\n5=Postgrado")
        nivelEstudio = int(input("Ingrese el Nivel de Estudio:"))
        if (nivelEstudio == 1):
            primaria = primaria + 1
        elif (nivelEstudio == 2):
            secundaria = secundaria + 1
        elif (nivelEstudio == 3):
            carrTecnica = carrTecnica + 1
        elif (nivelEstudio == 4):
            carrProfesional = carrProfesional + 1
        else:
            postgrado = postgrado + 1
        isVivienda = int(input("Hay Mas viviendas ? 1=True, 0=False"))
    print("Los resultados de la encuesta en cuanto a nivel de estudio es la siguiente:")
    totalPersonasEncuestadas = primaria + secundaria + carrTecnica + carrProfesional + postgrado
    print("Personas con nivel de estudio Primario representan un: ", (primaria * 100) / totalPersonasEncuestadas, "%")
    print("Personas con nivel de estudio Secundario representan un: ", (secundaria * 100) / totalPersonasEncuestadas,
          "%")
    print("Personas con nivel de estudio de Carrera tecnica representan un: ",
          (carrTecnica * 100) / totalPersonasEncuestadas, "%")
    print("Personas con nivel de estudio de Carrera Profesional representan un: ",
          (carrProfesional * 100) / totalPersonasEncuestadas, "%")
    print("Personas con nivel de estudio de Postgrado representan un: ", (postgrado * 100) / totalPersonasEncuestadas,
          "%")
if __name__=="__main__":
    Ejercicio14()