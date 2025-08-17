from producto import Producto
from inventario import Inventario

def leer_entero(mensaje):
    while True:
        dato = input(mensaje).strip()
        try:
            valor = int(dato)
            if valor < 0:
                print("Ingrese un número entero no negativo.")
                continue
            return valor
        except ValueError:
            print("Ingrese un número entero válido (ej: 10).")

def leer_flotante(mensaje):
    while True:
        dato = input(mensaje).strip().replace(",", ".")
        try:
            valor = float(dato)
            if valor < 0:
                print("Ingrese un número no negativo.")
                continue
            return valor
        except ValueError:
            print("Ingrese un número válido (use punto decimal, ej: 12.50).")

def menu():
    inventario = Inventario()

    while True:
        print("\n--- Sistema de Gestión de Inventarios ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            id = input("Ingrese el ID del producto: ").strip()
            nombre = input("Ingrese el nombre: ").strip()
            cantidad = leer_entero("Ingrese la cantidad: ")
            precio = leer_flotante("Ingrese el precio: ")
            nuevo = Producto(id, nombre, cantidad, precio)
            inventario.agregar_producto(nuevo)

        elif opcion == "2":
            id = input("Ingrese el ID del producto a eliminar: ").strip()
            inventario.eliminar_producto(id)

        elif opcion == "3":
            id = input("Ingrese el ID del producto a actualizar: ").strip()
            cantidad_txt = input("Nueva cantidad (deje en blanco para no cambiar): ").strip()
            precio_txt = input("Nuevo precio (deje en blanco para no cambiar): ").strip()

            cantidad = None
            precio = None

            if cantidad_txt != "":
                try:
                    cantidad = int(cantidad_txt)
                    if cantidad < 0:
                        print("La cantidad no puede ser negativa.")
                        cantidad = None
                except ValueError:
                    print("Cantidad inválida; no se actualizará.")

            if precio_txt != "":
                try:
                    precio = float(precio_txt.replace(",", "."))
                    if precio < 0:
                        print("El precio no puede ser negativo.")
                        precio = None
                except ValueError:
                    print("Precio inválido; no se actualizará.")

            inventario.actualizar_producto(id, cantidad, precio)

        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ").strip()
            inventario.buscar_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            print("👋 Saliendo del sistema...")
            break
        else:
            print("❌ Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
