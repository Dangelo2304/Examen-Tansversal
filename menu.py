from ectructura import *

estadistica = []

while True:
    print("\n      Menu")
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadisticas ")
    print("4. Reporte de sueldo")
    print("5. Salir del programa")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        asignar_sueldo(estadistica) 
    elif opcion == "2":
        clasificar_sueldo(estadistica) 
    elif opcion == "3":
        ver_estadisticas(estadistica) 
    elif opcion == "4":
        reporte_sueldo(estadistica) 
    elif opcion == "5":
        guardar_estadisticas_csv(estadistica) 
        break
    else:
        print("La opción ingresada no es valida. Por favor, ingrese una opción")
