import estudiantes as est

estudiantes_copy = est.estudiantes

def listar_los_alumnos(lista:list):
    bandera_swap = True
    while bandera_swap:
        bandera_swap = False
        for i in range(len(lista)-1):
            if lista[i]["apellido"] > lista[i+1]["apellido"]:
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
                bandera_swap = True
            if lista[i]["apellido"] == lista[i+1]["apellido"] and lista[i]["nombre"] > lista[i+1]["nombre"]:
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
                bandera_swap = True
    
        for estudiante in lista:
            print(f"Legajo: {estudiante["legajo"]}, Nombre: {estudiante["nombre"]}, "
                f"Apellido: {estudiante["apellido"]}, Edad: {estudiante["edad"]}")

    



def promedio_de_notas_de_estudiante(lista:list):
    
    for e_estudiante in lista:
        if e_estudiante["notas"]:
            # promedio = sum(e_estudiante["notas"]) / len(e_estudiante["notas"])
            # print(f"Nombre: {e_estudiante["nombre"]}, su promedio es {promedio}")
            acumulador = 0
            for nota in e_estudiante["notas"]:
                acumulador += nota
                promedio = acumulador / len(e_estudiante["notas"])
            print(f"Nombre: {e_estudiante["nombre"]}, su promedio es {promedio}") ## Preguntar
                
            




def estudiantes_ingenieria_informatica(lista:list):
    for e_estudiante in lista:
        if e_estudiante["programa"]["nombre"] == "Ingenieria en Informatica":
            print(f"Nombre:{e_estudiante["nombre"]} ,Edad:{e_estudiante["edad"]}, Apellido:{e_estudiante["apellido"]}, legajo:{e_estudiante["legajo"]}")





def promedio_edad_estudiantes(lista:list):
    acumulador_edad = 0
    for e_estudiante in lista:
        acumulador_edad += e_estudiante["edad"]
    promedio_edad = acumulador_edad / len(lista)
    print(f"El promedio de edad de los estudiantes es {promedio_edad}")



def mayor_promedio_notas(lista:list):
    mayor_nota = 0
    nombre_mayor_promedio = ""
    apellido_mayor_promedio = ""

    for e_estudiante in lista:
        acumulador_notas = 0
        for nota in e_estudiante["notas"]:
            acumulador_notas += nota
        nota_estudiante_final = acumulador_notas / len(e_estudiante["notas"])

        if nota_estudiante_final > mayor_nota:
            mayor_nota = nota_estudiante_final
            nombre_mayor_promedio = e_estudiante["nombre"]
            apellido_mayor_promedio = e_estudiante["apellido"]

    return print(f"El estudiante con el mayor promedio es: {nombre_mayor_promedio} {apellido_mayor_promedio}")




def club_de_informatica(lista:list):
    for e_estudiante in lista:
        if e_estudiante["grupos"]:

            if e_estudiante ["nombre"] == "Club de Informatica":
                acomulador_notas = 0
                for nota in e_estudiante["notas"]:
                    acomulador_notas += nota
                nota_estudiante = acomulador_notas / len(e_estudiante["notas"])
                print(f"El nombre del estudiante es {e_estudiante["nombre"]}, su apellido:{e_estudiante["apellido"]}, y el promedio de notas es: {nota_estudiante}")

#club_de_informatica(estudiantes)

""" def club_de_informatica(lista: list):
    for e_estudiante in lista:
        if "grupos" in e_estudiante:
            for grupo in e_estudiante["grupos"]:
                if grupo.get("nombre") == "Club de Informatica":
                    acumulador_notas = 0
                    if e_estudiante["notas"]:  # Asegura que haya notas para evitar división por cero
                        for nota in e_estudiante["notas"]:
                            acumulador_notas += nota
                        nota_estudiante = acumulador_notas / len(e_estudiante["notas"])
                        print(f"El nombre del estudiante es {e_estudiante['nombre']}, su apellido: {e_estudiante['apellido']}, y el promedio de notas es: {nota_estudiante}")
                    
                    break  # Salir del bucle si se encuentra el grupo
club_de_informatica(estudiantes) """

""" def club_de_informatica(lista: list):
    for e_estudiante in lista:
        if "grupos" in e_estudiante and e_estudiante["grupos"].get("nombre") == "Club de Informatica":
            acumulador_notas = 0
            if e_estudiante["notas"]:  # Asegura que haya notas para evitar división por cero
                for nota in e_estudiante["notas"]:
                    acumulador_notas += nota
                nota_estudiante = acumulador_notas / len(e_estudiante["notas"])
                print(f"El nombre del estudiante es {e_estudiante['nombre']}, su apellido: {e_estudiante['apellido']}, y el promedio de notas es: {nota_estudiante}")
            else:
                print(f"El nombre del estudiante es {e_estudiante['nombre']}, su apellido: {e_estudiante['apellido']}, y no tiene notas registradas.")

 """
#club_de_informatica(estudiantes)
def alumnos_mas_jovenes():
    pass



def menu()->int:
    seguir = True
    while seguir == True:
        opcion = int(input("""

                1-Listar los alumnos por orden ascendente de apellido, si se repite, 
                ordenar por nombre. # Mostrar legajo, nombre, apellido y edad 
                2-Obtener el promedio de notas para cada estudiante 
                3-Listar legajo, nombre, apellido y edad de los estudiantes que cursan el programa de “Ingenieria en Informatica” 
                4-Obtener un promedio de edad de los estudiantes.
                5-Informar el alumno con mayor pomedio de notas. Mostrar nombre y 
                apellido 
                6-Listar nombre y apellido de los alumnos que forman el grupo “Club de 
                Informática” con sus respectivos promedios 
                7-Listar legajo, nombre, apellido y programas que cursan los alumnos 
                más jóvenes. 
                8- Salir del programa


            """))
        if opcion == 1:
            listar_los_alumnos(estudiantes_copy)
        elif opcion == 2:
            promedio_de_notas_de_estudiante(estudiantes_copy)
        elif opcion == 3:
            estudiantes_ingenieria_informatica(estudiantes_copy)
        elif opcion == 4:
            promedio_edad_estudiantes(estudiantes_copy)
        elif opcion == 5:
            mayor_promedio_notas(estudiantes_copy)
        elif opcion == 6:
            club_de_informatica(estudiantes_copy)
        elif opcion == 7:
            alumnos_mas_jovenes()
        elif opcion == 8:
            seguir = False
        else:
            opcion= int(input("Error Ingrese un valor valido (1-8)"))

