import csv

inventario = []  


def agregar():
    nombre = input("Nombre: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))

    inventario.append({
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    })
    print("Producto agregado.\n")


def mostrar():
    if not inventario:
        print("Inventario vacío.\n")
        return

    for p in inventario:
        print(f"{p['nombre']} - ${p['precio']} - Cant: {p['cantidad']}")
    print()


def buscar():
    nombre = input("Nombre del producto: ")

    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            print("Encontrado:", p, "\n")
            return
    print("No encontrado.\n")


def actualizar():
    nombre = input("Producto a actualizar: ")

    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            p["precio"] = float(input("Nuevo precio: "))
            p["cantidad"] = int(input("Nueva cantidad: "))
            print("Actualizado.\n")
            return
    print("No encontrado.\n")


def eliminar():
    nombre = input("Producto a eliminar: ")

    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            inventario.remove(p)
            print("Eliminado.\n")
            return
    print("No encontrado.\n")


def estadisticas():
    if not inventario:
        print("Inventario vacío.\n")
        return

    total_unidades = sum(p["cantidad"] for p in inventario)
    total_valor = sum(p["cantidad"] * p["precio"] for p in inventario)

    print("Unidades totales:", total_unidades)
    print("Valor total:", total_valor, "\n")


def guardar_csv():
    ruta = input("Nombre del archivo (*.csv): ")

    with open(ruta, "w", newline="") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["nombre", "precio", "cantidad"])
        for p in inventario:
            writer.writerow([p["nombre"], p["precio"], p["cantidad"]])

    print("Inventario guardado.\n")


def cargar_csv():
    ruta = input("Archivo CSV a cargar: ")

    try:
        with open(ruta, "r") as archivo:
            reader = csv.reader(archivo)
            next(reader)  

            inventario.clear() 
            for row in reader:
                nombre, precio, cantidad = row
                inventario.append({
                    "nombre": nombre,
                    "precio": float(precio),
                    "cantidad": int(cantidad)
                })

        print("Inventario cargado.\n")
    except FileNotFoundError:
        print("Archivo no encontrado.\n")


def menu():
    while True:
        print("1. Agregar")
        print("2. Mostrar")
        print("3. Buscar")
        print("4. Actualizar")
        print("5. Eliminar")
        print("6. Estadísticas")
        print("7. Guardar CSV")
        print("8. Cargar CSV")
        print("9. Salir")

        op = input("Opción: ")

        if op == "1": agregar()
        elif op == "2": mostrar()
        elif op == "3": buscar()
        elif op == "4": actualizar()
        elif op == "5": eliminar()
        elif op == "6": estadisticas()
        elif op == "7": guardar_csv()
        elif op == "8": cargar_csv()
        elif op == "9":
            print("Adiós")
            break
        else:
            print("Opción inválida.\n")


menu()
