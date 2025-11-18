
import csv
import os


def guardar_csv(inventario, ruta):
    """Guarda el inventario en un archivo CSV con encabezado."""
    if not inventario:
        print("No hay productos para guardar.\n")
        return

    try:
        with open(ruta, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["nombre", "precio", "cantidad"])  
            for p in inventario:
                writer.writerow([p["nombre"], p["precio"], p["cantidad"]])
        print(f"Inventario guardado correctamente en: {ruta}\n")
    except PermissionError:
        print("Error: permiso denegado para escribir el archivo.\n")
    except Exception as e:
        print(f"Error al guardar: {e}\n")


def cargar_csv(inventario, ruta):
    """Carga un CSV y permite sobrescribir o fusionar el inventario actual."""
    if not os.path.exists(ruta):
        print("Archivo no encontrado.\n")
        return

    productos_nuevos = []
    filas_invalidas = 0

    try:
        with open(ruta, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            header = next(reader, None)

            if header is None or header != ["nombre", "precio", "cantidad"]:
                print("Encabezado inválido. Debe ser: nombre,precio,cantidad\n")
                return

            for linea, row in enumerate(reader, start=2):
                if len(row) != 3:
                    filas_invalidas += 1
                    continue

                nombre, precio_str, cantidad_str = row

                try:
                    precio = float(precio_str)
                    cantidad = int(cantidad_str)

                    if precio < 0 or cantidad < 0:
                        raise ValueError

                    productos_nuevos.append({
                        "nombre": nombre.strip(),
                        "precio": precio,
                        "cantidad": cantidad
                    })
                except ValueError:
                    filas_invalidas += 1

        if not productos_nuevos:
            print("No se cargaron productos válidos.\n")
            return

        # Mostrar resumen antes de decidir
        print(f"Se encontraron {len(productos_nuevos)} productos válidos.")
        if filas_invalidas > 0:
            print(f"{filas_invalidas} filas inválidas fueron omitidas.\n")

        eleccion = input("¿Sobrescribir inventario actual? (S/N): ").strip().upper()

        if eleccion == "S":
            inventario.clear()
            inventario.extend(productos_nuevos)
            print("Inventario reemplazado correctamente.\n")
        else:
            # Fusión: si el producto existe → suma cantidad y actualiza precio
            for nuevo in productos_nuevos:
                existente = next(
                    (p for p in inventario if p["nombre"].lower() == nuevo["nombre"].lower()),
                    None
                )
                if existente:
                    existente["cantidad"] += nuevo["cantidad"]
                    existente["precio"] = nuevo["precio"]  # toma el precio del CSV
                else:
                    inventario.append(nuevo)
            print("Inventario fusionado correctamente.\n")

    except UnicodeDecodeError:
        print("Error de codificación. Asegúrate de que el archivo sea UTF-8.\n")
    except Exception as e:
        print(f"Error al cargar el archivo: {e}\n")