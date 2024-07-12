import csv
import random

trabajadores = ["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]
sueldo_trabajadores = []

def asignar_sueldo(trabajadores):
    sueldo = round(random.uniform(300000,2500000))
    print(f"El empleado {trabajadores} tiene un sueldo de: {sueldo}")

def clasificar_sueldo(trabajadores):
    if sueldo < 800000:
        print("sueldos menores a $800000 TOTAL")

