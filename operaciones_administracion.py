# Tienda de regalos Gifty - Inventario y registro de ventas

# Operacion de administracion

from inventario import inventario, ventas

def mostrar_inventario():
    if not inventario:
        print("\nNo hay ningún producto en el inventario.")
        return

    print("\nInventario de Gifty:")
    for sku, producto in inventario.items():
        print(f"SKU: {sku}, Nombre: {producto['nombre']}, Precio: ${int(producto['precio'])}, Cantidad: {producto['cantidad']}")

def vender_producto():
    if not inventario:
        print("\nNo hay productos en el inventario para vender.")
        return
    
    while True:
        sku = input("\nIngrese el SKU del producto a vender: \n(Si quiere volver al menú, ingrese 0)\n")
        if sku == '0':
            return

        if not sku.isdigit() or len(sku) != 3:
            print("El SKU debe ser un número de tres dígitos. Ejemplo: 001, 002.")
            continue

        if sku in inventario:

            if inventario[sku]['cantidad'] == 0:
                print(f"El producto {inventario[sku]['nombre']} no tiene stock disponible.")
                continue
            
            while True:
                try:
                    cantidad_vendida = int(input(f"Ingrese la cantidad de {inventario[sku]['nombre']} a vender (hay {inventario[sku]['cantidad']}): "))
                    if cantidad_vendida <= 0:
                        print("La cantidad debe ser mayor a cero.")
                        continue
                    if cantidad_vendida <= inventario[sku]['cantidad']:
                        inventario[sku]['cantidad'] -= cantidad_vendida
                        ventas[sku] += cantidad_vendida
                        total_venta = cantidad_vendida * inventario[sku]['precio']
                        print(f"Venta exitosa. Total a pagar: ${total_venta:}")
                        break
                    else:
                        print("Cantidad insuficiente en inventario.")
                except ValueError:
                    print("Ingrese un número válido.")
        else:
            print("Producto no encontrado.")
            continue

        while True:
            otra_venta = input("\n¿Desea realizar otra venta? (s = sí / n = no): ").lower()
            if otra_venta == 's':
                break
            elif otra_venta == 'n':
                return
            else:
                print("Opción no válida. Ingrese 's' o 'n'.")

def buscar_producto():
    while True:
        print("\n¿Cómo desea buscar el producto?")
        print("1. Buscar por SKU")
        print("2. Buscar por nombre")
        print("0. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == '0':
            return

        elif opcion == '1':
            while True:
                sku = input("\nIngrese el SKU del producto a buscar: \n(Si quiere volver al menú de búsqueda, ingrese 0)\n")
                if sku == '0':
                    break

                if not sku.isdigit() or len(sku) != 3:
                    print("El SKU debe ser un número de tres dígitos. Ejemplo: 001, 002.")
                    continue

                if sku in inventario:
                    producto = inventario[sku]
                    print(f"\nProducto encontrado: SKU: {sku}, Nombre: {producto['nombre']}, Precio: ${int(producto['precio'])}, Cantidad: {producto['cantidad']}")
                else:
                    print("Producto no encontrado.")

                otra_busqueda = input("\n¿Desea buscar otro producto por SKU? (s = sí / n = no): ").lower()
                if otra_busqueda != 's':
                    break

        elif opcion == '2':
            while True:
                nombre_buscar = input("\nIngrese el nombre del producto a buscar: \n(Si quiere volver al menú de búsqueda, ingrese 0)\n").lower().strip()
                
                if nombre_buscar == '0':
                    break

                if nombre_buscar == "":
                    print("Debe ingresar un nombre válido.")
                    continue

                encontrados = []
                for sku, producto in inventario.items():
                    if nombre_buscar in producto['nombre'].lower():
                        encontrados.append((sku, producto))

                if encontrados:
                    print("\nProductos encontrados:")
                    for sku, producto in encontrados:
                        print(f"SKU: {sku}, Nombre: {producto['nombre']}, Precio: ${int(producto['precio'])}, Cantidad: {producto['cantidad']}")
                else:
                    print("No se encontraron productos con ese nombre.")

                otra_busqueda = input("\n¿Desea buscar otro producto por nombre? (s = sí / n = no): ").lower()
                if otra_busqueda != 's':
                    break

        else:
            print("Opción no válida. Por favor seleccione 1, 2 o 0.")
