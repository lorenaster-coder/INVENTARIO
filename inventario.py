# Programa para administrar un inventario de productos con funciones

inventario = {}

def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input(f"Ingrese el precio de {nombre}: "))
    inventario[nombre] = precio
    print(f"Producto '{nombre}' agregado con precio ${precio}.")

def consultar_producto():
    nombre = input("Ingrese el nombre del producto a consultar: ")
    if nombre in inventario:
        print(f"El precio de {nombre} es: ${inventario[nombre]}")
    else:
        print(f"El producto '{nombre}' no está en el inventario.")

def modificar_producto():
    nombre = input("Ingrese el nombre del producto a modificar: ")
    if nombre in inventario:
        nuevo_precio = float(input(f"Ingrese el nuevo precio de {nombre}: "))
        inventario[nombre] = nuevo_precio
        print(f"Precio de '{nombre}' actualizado a ${nuevo_precio}.")
    else:
        print(f"El producto '{nombre}' no existe en el inventario.")

def eliminar_producto():
    nombre = input("Ingrese el nombre del producto a eliminar: ")
    if nombre in inventario:
        del inventario[nombre]
        print(f"Producto '{nombre}' eliminado del inventario.")
    else:
        print(f"El producto '{nombre}' no existe en el inventario.")

def mostrar_inventario():
    if inventario:
        print("\n--- Inventario Completo ---")
        for producto, precio in inventario.items():
            print(f"Producto: {producto} - Precio: ${precio}")
    else:
        print("El inventario está vacío.")

# Menú principal
def menu():
    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Agregar producto")
        print("2. Consultar producto")
        print("3. Modificar producto")
        print("4. Eliminar producto")
        print("5. Mostrar inventario")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            consultar_producto()
        elif opcion == "3":
            modificar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            mostrar_inventario()
        elif opcion == "6":
            print("\nInventario final:")
            mostrar_inventario()
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Ejecutar el programa
menu()

