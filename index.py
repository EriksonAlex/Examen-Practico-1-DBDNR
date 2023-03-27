from Productos import *
from functions import *
while True:
    print("Menu de opciones")
    print("1. Ver todos los productos")
    print("2. Buscar un producto")
    print("3. Agregar un producto")
    print("4. Modificar un producto")
    print("5. Eliminar un producto")
    opcion = input("Ingrese un opcion: ")
    if opcion == "1":
        read_products()
    elif opcion == "2":
        id = input("Ingrese el ID a buscar: ")
        read_products(id)
    elif opcion == "3":
        employee = create_json_products()
        create_products(employee)
    elif opcion == "4":
        id = input("Ingrese el ID a modificar: ")
        employee = create_json_update()
        update_products(id, employee)
    elif opcion == "5":
        id = input("Ingrese el ID a eliminar: ")
        delete_products(id)