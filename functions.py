def create_json_products():
    nombre_Producto = input("Nombre producto: ")
    descripcion = input("Descripcion: ")
    precio = input("Precio: ")
    marca = input("Marca: ")
    vencimiento = input("Fecha vencimiento: ")

    producto = {
        "nombre_Producto": nombre_Producto,
        "descripcion": descripcion,
        "precio": precio,
        "marca": marca,
        "vencimiento": vencimiento
    }
    return producto


def create_json_update():
    print("Menu de opciones")
    print("1. Modificar todos los datos del producto: ")
    print("2. Modificar un dato del producto: ")
    opcion = input("Ingrese una opcion: ")
    if opcion == "1":
        nombre_Producto = input("Nombre producto: ")
        descripcion = input("Descripcion: ")
        precio = input("Precio: ")
        marca = input("Marca: ")
        vencimiento = input("Fecha vencimiento: ")

        producto = {
            "nombre_Producto": nombre_Producto,
            "descripcion": descripcion,
            "precio": precio,
            "marca": marca,
            "vencimiento": vencimiento
        }
        return producto
    elif opcion == "2":
        indice = input("Ingrese el indice: ")
        valor = input("Ingrese el valor a modificar: ")
        producto = {indice: valor}
        return producto
    else:
        print("Dato ingresado no valido")