# Tienda de regalos Gifty - Inventario y registro de ventas

# Operaciones de modificacion

from inventario import inventario, ventas

def agregar_producto():
    while True:
        if inventario:
            nuevo_sku = str(max([int(sku) for sku in inventario.keys()]) + 1).zfill(3)
        else:
            nuevo_sku = "001"

        print(f"\nEl SKU asignado automáticamente es: {nuevo_sku}")
        nombre = input("Ingrese el nombre del producto: ")

        while True:
            try:
                precio = int(input("Ingrese el precio del producto: "))
                if precio <= 0:
                    print("El precio debe ser mayor a cero.")
                    continue
                break
            except ValueError:
                print("Ingrese un valor numérico válido.")

        while True:
            try:
                cantidad = int(input("Ingrese la cantidad del producto: "))
                if cantidad <= 0:
                    print("La cantidad debe ser mayor a cero.")
                    continue
                break
            except ValueError:
                print("Ingrese un número entero válido.")

        inventario[nuevo_sku] = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
        ventas[nuevo_sku] = 0
        print(f"Producto {nombre} agregado al inventario con SKU {nuevo_sku}.")

        while True:
            otro = input("\n¿Desea agregar otro producto? (s = sí / n = no): ").lower()
            if otro == 's':
                break
            elif otro == 'n':
                return
            else:
                print("Opción no válida. Ingrese 's' o 'n'.")
    
def actualizar_producto():
    if not inventario:
        print("\nNo hay productos en el inventario para actualizar.")
        return

    while True:
        sku = input("\nIngrese el SKU del producto a actualizar: \n(Si quiere volver al menú, ingrese 0)\n")
        if sku == '0':
            return

        if not sku.isdigit() or len(sku) != 3:
            print("El SKU debe ser un número de tres dígitos. Ejemplo: 001, 002.")
            continue

        if sku not in inventario:
            print("Producto no encontrado. Ingrese un SKU válido.")
            continue

        producto = inventario[sku]
        print(f"\nProducto actual: SKU: {sku}, Nombre: {producto['nombre']}, Precio: ${int(producto['precio'])}, Cantidad: {producto['cantidad']}")

        nombre = input("Ingrese el nuevo nombre del producto: \n(Si quiere dejar el nombre actual presione ENTER)\n")
        if nombre.strip() == "":
            nombre = producto['nombre']

        while True:
            try:
                precio_input = input("Ingrese el nuevo precio del producto: \n(Si quiere dejar el precio actual presione ENTER)\n")
                if precio_input.strip() == "":
                    precio = producto['precio']
                    break
                precio = float(precio_input)
                if precio <= 0:
                    print("El precio debe ser mayor a cero.")
                    continue
                break
            except ValueError:
                print("Ingrese un valor numérico válido.")

        while True:
            try:
                cantidad_input = input("Ingrese la nueva cantidad del producto: \n(Si quiere dejar la cantidad actual presione ENTER)\n")
                if cantidad_input.strip() == "":
                    cantidad = producto['cantidad']
                    break
                cantidad = int(cantidad_input)
                if cantidad < 0:
                    print("La cantidad no puede ser negativa.")
                    continue
                break
            except ValueError:
                print("Ingrese un número entero válido.")

        inventario[sku] = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
        print(f"\nProducto {sku} actualizado correctamente.")

        while True:
            otro = input("\n¿Desea actualizar otro producto? (s = sí / n = no): ").lower()
            if otro == 's':
                break
            elif otro == 'n':
                return
            else:
                print("Opción no válida. Ingrese 's' o 'n'.")

def eliminar_producto():
    if not inventario:
        print("\nNo hay productos en el inventario para eliminar.")
        return
    
    while True:
        sku = input("\nIngrese el SKU del producto a eliminar: \n(Si quiere volver al menú, ingrese 0)\n")
        if sku == '0':
            return
        
        if not sku.isdigit() or len(sku) != 3:
            print("El SKU debe ser un número de tres dígitos. Ejemplo: 001, 002.")
            continue
        
        if sku not in inventario:
            print("Producto no encontrado. Ingrese un SKU válido.")
            continue
        
        producto = inventario[sku]
        print(f"\nDatos del producto a eliminar: SKU: {sku}, Nombre: {producto['nombre']}, Precio: ${int(producto['precio'])}, Cantidad: {producto['cantidad']}")

        while True:
            confirmar = input(f"\n¿Está seguro que desea eliminar este producto? (s = sí / n = no): ").lower()
            if confirmar == 's':
                del inventario[sku]
                del ventas[sku]
                print(f"Producto {sku} eliminado del inventario.")
                break
            elif confirmar == 'n':
                print("Operación cancelada. No se eliminó ningún producto.")
                break
            else:
                print("Opción no válida. Por favor ingrese 's' o 'n'.")

        while True:
            otro = input("\n¿Desea eliminar otro producto? (s = sí / n = no): ").lower()
            if otro == 's':
                break
            elif otro == 'n':
                return
            else:
                print("Opción no válida. Por favor ingrese 's' o 'n'.")

def actualizar_existencias():
    if not inventario:
        print("\nNo hay productos en el inventario para actualizar.")
        return

    while True:
        print("\n¿Qué desea realizar?")
        print("1. Agregar existencias de un producto")
        print("2. Eliminar existencias de un producto")
        print("0. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == '0':
            return

        elif opcion == '1':
            while True: 
                sku = input("\nIngrese el SKU del producto a agregar existencia: \n(Si quiere volver al menú de existencias, ingrese 0)\n")
                if sku == '0':
                    break

                if not sku.isdigit() or len(sku) != 3:
                    print("El SKU debe ser un número de tres dígitos. Ejemplo: 001, 002.")
                    continue

                if sku not in inventario:
                    print("Producto no encontrado. Ingrese un SKU válido.")
                    continue

                producto = inventario[sku]
                print(f"\nDatos del producto: SKU: {sku}, Nombre: {producto['nombre']}, Precio: ${int(producto['precio'])}, Cantidad: {producto['cantidad']}")

                while True:
                    try:
                        cantidad = int(input("Ingrese la cantidad a aumentar: "))
                        if cantidad < 0:
                            print("La cantidad debe ser mayor a cero.")
                            continue
                        if cantidad == 0:
                            print("No se ha modificado la cantidad.")
                            break 

                        inventario[sku]['cantidad'] += cantidad
                        print(f"Existencias actualizadas. Nueva cantidad: {inventario[sku]['cantidad']}")
                        break

                    except ValueError:
                        print("Ingrese un número entero válido para la cantidad.")

                while True:
                    otra = input("\n¿Desea aumentar existencias de otro producto? (s = sí / n = no): ").lower()
                    if otra == 's':
                        break
                    elif otra == 'n':
                        break
                    else:
                        print("Opción no válida. Por favor ingrese 's' o 'n'.")

                if otra == 'n':
                    break

        elif opcion == '2':
            while True:
                sku = input("\nIngrese el SKU del producto a disminuir existencia: \n(Si quiere volver al menú de existencias, ingrese 0)\n")
                if sku == '0':
                    break

                if not sku.isdigit() or len(sku) != 3:
                    print("El SKU debe ser un número de tres dígitos. Ejemplo: 001, 002.")
                    continue

                if sku not in inventario:
                    print("Producto no encontrado. Ingrese un SKU válido.")
                    continue

                producto = inventario[sku]
                print(f"\nDatos del producto: SKU: {sku}, Nombre: {producto['nombre']}, Precio: ${int(producto['precio'])}, Cantidad: {producto['cantidad']}")

                while True:
                    try:
                        cantidad = int(input("Ingrese la cantidad a disminuir: "))
                        if cantidad < 0:
                            print("La cantidad debe ser mayor a cero.")
                            continue
                        if cantidad == 0:
                            print("No se ha modificado la cantidad.")
                            break
                        if cantidad > inventario[sku]['cantidad']:
                            print("No se puede disminuir más de lo que hay en existencias.")
                            continue

                        inventario[sku]['cantidad'] -= cantidad
                        print(f"Existencias actualizadas. Nueva cantidad: {inventario[sku]['cantidad']}")
                        break

                    except ValueError:
                        print("Ingrese un número entero válido para la cantidad.")

                while True:
                    otra = input("\n¿Desea disminuir existencias de otro producto? (s = sí / n = no): ").lower()
                    if otra == 's':
                        break
                    elif otra == 'n':
                        break
                    else:
                        print("Opción no válida. Por favor ingrese 's' o 'n'.")

                if otra == 'n':
                    break

        else:
            print("Opción no válida. Por favor, seleccione 1, 2 o 0.")
            
