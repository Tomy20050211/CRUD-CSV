from servicios import (
    agregar_producto, mostrar_inventario, buscar_producto,
    actualizar_producto, eliminar_producto, calcular_estadisticas
)
from archivos import guardar_csv, cargar_csv

# Inventario en memoria
inventario = []

def mostrar_menu():
    print("\n" + "="*30)
    print("     SISTEMA DE INVENTARIO")
    print("="*30)
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Estadísticas")
    print("7. Guardar en CSV")
    print("8. Cargar desde CSV")
    print("9. Salir")

def main():
    while True:
        mostrar_menu()
        try:
            opcion = input("\nElige una opción (1-9): ").strip()
            
            if opcion == "1":
                agregar_producto(inventario)
            elif opcion == "2":
                mostrar_inventario(inventario)
            elif opcion == "3":
                nombre = input("Nombre del producto a buscar: ")
                buscar_producto(inventario, nombre)
            elif opcion == "4":
                actualizar_producto(inventario)
            elif opcion == "5":
                nombre = input("Nombre del producto a eliminar: ")
                eliminar_producto(inventario, nombre)
            elif opcion == "6":
                calcular_estadisticas(inventario)
            elif opcion == "7":
                ruta = input("Nombre del archivo CSV (ej: datos.csv): ")
                guardar_csv(inventario, ruta)
            elif opcion == "8":
                ruta = input("Ruta del archivo CSV a cargar: ")
                cargar_csv(inventario, ruta)
            elif opcion == "9":
                print("¡Hasta pronto!")
                break
            else:
                print("Opción no válida. Intenta de nuevo.")
                
        except KeyboardInterrupt:
            print("\n\nSaliendo...")
            break
        except Exception as e:
            print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()