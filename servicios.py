# servicios.py

def agregar_producto(inventario):
    """Pide datos y agrega un producto al inventario."""
    try:
        nombre = input("Nombre del producto: ").strip()
        if not nombre:
            print("El nombre no puede estar vacío.\n")
            return

        precio = float(input("Precio: "))
        if precio < 0:
            print("El precio no puede ser negativo.\n")
            return

        cantidad = int(input("Cantidad: "))
        if cantidad < 0:
            print("La cantidad no puede ser negativa.\n")
            return

        inventario.append({
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        })
        print("Producto agregado correctamente.\n")

    except ValueError:
        print("Error: Precio y cantidad deben ser números válidos.\n")


def mostrar_inventario(inventario):
    """Muestra todos los productos del inventario."""
    if not inventario:
        print("El inventario está vacío.\n")
        return

    print("\n" + "="*50)
    print("               INVENTARIO ACTUAL")
    print("="*50)
    for i, p in enumerate(inventario, 1):
        print(f"{i:2}. {p['nombre']:<20} | ${p['precio']:>8.2f} | Cantidad: {p['cantidad']:>4}")
    print("="*50 + "\n")


def buscar_producto(inventario, nombre):
    """Busca un producto por nombre (insensible a mayúsculas)."""
    nombre = nombre.strip()
    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            print(f"Producto encontrado: {p['nombre']} | Precio: ${p['precio']:.2f} | Cantidad: {p['cantidad']}\n")
            return
    print("Producto no encontrado.\n")


def actualizar_producto(inventario):
    """Actualiza precio y/o cantidad de un producto existente."""
    nombre = input("Nombre del producto a actualizar: ").strip()
    if not nombre:
        print("El nombre no puede estar vacío.\n")
        return

    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            print(f"Producto encontrado: {p['nombre']} (Precio actual: ${p['precio']}, Cantidad: {p['cantidad']})")
            try:
                nuevo_precio_input = input("Nuevo precio (Enter para mantener actual): ").strip()
                nueva_cantidad_input = input("Nueva cantidad (Enter para mantener actual): ").strip()

                if nuevo_precio_input:
                    nuevo_precio = float(nuevo_precio_input)
                    if nuevo_precio < 0:
                        print("El precio no puede ser negativo.\n")
                        return
                    p["precio"] = nuevo_precio

                if nueva_cantidad_input:
                    nueva_cantidad = int(nueva_cantidad_input)
                    if nueva_cantidad < 0:
                        print("La cantidad no puede ser negativa.\n")
                        return
                    p["cantidad"] = nueva_cantidad

                print("Producto actualizado correctamente.\n")
                return

            except ValueError:
                print("Error: Ingresa valores numéricos válidos.\n")
                return

    print("Producto no encontrado.\n")


def eliminar_producto(inventario, nombre):
    """Elimina un producto del inventario."""
    nombre = nombre.strip()
    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            inventario.remove(p)
            print("Producto eliminado correctamente.\n")
            return
    print("Producto no encontrado.\n")


def calcular_estadisticas(inventario):
    """Muestra estadísticas completas del inventario."""
    if not inventario:
        print("Inventario vacío. No hay estadísticas para mostrar.\n")
        return

    total_unidades = sum(p["cantidad"] for p in inventario)
    total_valor = sum(p["precio"] * p["cantidad"] for p in inventario)

    producto_mas_caro = max(inventario, key=lambda p: p["precio"])
    producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"])

    print("\n" + "="*40)
    print("           ESTADÍSTICAS DEL INVENTARIO")
    print("="*40)
    print(f"Total de unidades        : {total_unidades}")
    print(f"Valor total del inventario: ${total_valor:,.2f}")
    print(f"Producto más caro        : {producto_mas_caro['nombre']} → ${producto_mas_caro['precio']:.2f}")
    print(f"Mayor stock              : {producto_mayor_stock['nombre']} → {producto_mayor_stock['cantidad']} unidades")
    print("="*40 + "\n")