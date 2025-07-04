# Tienda de regalos Gifty - Inventario y registro de ventas

# Reportes

from inventario import inventario, ventas

def generar_reporte():
    print("\n--- Reporte Completo del Inventario ---")

    total_productos = sum(producto['cantidad'] for producto in inventario.values())
    print(f"Total de productos en inventario: {total_productos}")

    print("\nProductos más vendidos:")
    ventas_ordenadas = sorted(ventas.items(), key=lambda x: x[1], reverse=True)

    productos_con_ventas = False
    for sku, cantidad_vendida in ventas_ordenadas:
        if cantidad_vendida > 0:
            producto = inventario[sku]
            print(f"SKU: {sku}, Nombre: {producto['nombre']}, Vendidos: {cantidad_vendida}")
            productos_con_ventas = True

    if not productos_con_ventas:
        print("Aún no se han registrado ventas.")

    print("\nProductos con stock bajo (menos de 10 unidades):")
    stock_bajo = False
    for sku, producto in inventario.items():
        if producto['cantidad'] < 10:
            print(f"SKU: {sku}, Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}")
            stock_bajo = True

    if not stock_bajo:
        print("No hay productos con stock bajo actualmente.")
