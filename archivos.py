import csv

# Lista donde se guardan todos los productos del inventario
inventario = []  


def agregar():
    # Pide datos del producto
    nombre = input("Nombre: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))

    # Guarda el producto como un diccionario dentro de la lista
    inventario.append({
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    })
    print("Producto agregado.\n")


def mostrar():
    # Si la lista está vacía, no hay nada que mostrar
    if not inventario:
        print("Inventario vacío.\n")
        return

    # Muestra cada producto en una línea
    for p in inventario:
        print(f"{p['nombre']} - ${p['precio']} - Cant: {p['cantidad']}")
    print()


def buscar():
    # Pide el nombre a buscar
    nombre = input("Nombre del producto: ")

    # Recorre el inventario buscando coincidencias
    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            print("Encontrado:", p, "\n")
            return
    print("No encontrado.\n")


def actualizar():
    # Producto que se desea modificar
    nombre = input("Producto a actualizar: ")

    for p in inventario:
        # Busca por nombre sin importar mayúsculas o minúsculas
        if p["nombre"].lower() == nombre.lower():
            # Actualiza datos
            p["precio"] = float(input("Nuevo precio: "))
            p["cantidad"] = int(input("Nueva cantidad: "))
            print("Actualizado.\n")
            return
    print("No encontrado.\n")


def eliminar():
    # Producto a eliminar
    nombre = input("Producto a eliminar: ")

    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            # Elimina el producto de la lista
            inventario.remove(p)
            print("Eliminado.\n")
            return
    print("No encontrado.\n")


def estadisticas():
    # No se pueden calcular estadísticas si no hay productos
    if not inventario:
        print("Inventario vacío.\n")
        return

    # Suma todas las cantidades
    total_unidades = sum(p["cantidad"] for p in inventario)
    # Suma el valor total (precio * cantidad)
    total_valor = sum(p["cantidad"] * p["precio"] for p in inventario)

    print("Unidades totales:", total_unidades)
    print("Valor total:", total_valor, "\n")


def guardar_csv():
    # Nombre del archivo donde guardar
    ruta = input("Nombre del archivo (*.csv): ")

    # Abre el archivo en modo escritura
    with open(ruta, "w", newline="") as archivo:
        writer = csv.writer(archivo)

        # Escribe la fila de encabezados
        writer.writerow(["nombre", "precio", "cantidad"])

        # Escribe cada producto del inventario
        for p in inventario:
            writer.writerow([p["nombre"], p["precio"], p["cantidad"]])

    print("Inventario guardado.\n")


def cargar_csv():
    # Archivo a leer
    ruta = input("Archivo CSV a cargar: ")

    try:
        with open(ruta, "r") as archivo:
            reader = csv.reader(archivo)
            next(reader)  # Saltar la fila de encabezados

            inventario.clear()  # Limpia el inventario actual

            # Convierte cada fila en un diccionario y lo agrega
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
    # Bucle que mantiene activo el menú
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

        # Llama a la función según la opción
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


# Iniciar el programa
menu()
