# Tienda de regalos Gifty - Inventario y registro de ventas

# Main

from operaciones_modificacion import agregar_producto, actualizar_producto, eliminar_producto
from operaciones_administracion import mostrar_inventario, vender_producto, buscar_producto
from reportes import generar_reporte

def gestion_tienda():
    while True:
        print("\n-------------------------------------------------")
        print("Bienvenido a la aplicación de inventario de Gifty")
        print("-------------------------------------------------")
        print("1. Mostrar inventario")
        print("2. Vender producto")
        print("3. Agregar producto")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("6. Buscar producto")
        print("7. Reporte de ventas")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            mostrar_inventario()
        elif opcion == '2':
            vender_producto()
        elif opcion == '3':
            agregar_producto()
        elif opcion == '4':
            actualizar_producto()
        elif opcion == '5':
            eliminar_producto()
        elif opcion == '6':
            buscar_producto()
        elif opcion == '7':
            generar_reporte()
        elif opcion == '8':
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    gestion_tienda()
