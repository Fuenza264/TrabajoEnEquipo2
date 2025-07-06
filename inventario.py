# Tienda de regalos Gifty - Inventario y registro de ventas

#Inventario y conteo ventas

'''
inventario = {
    "001": {"nombre": "peluche", "precio": 100, "cantidad": 50},
    "002": {"nombre": "taza", "precio": 50, "cantidad": 100},
}
'''

inventario = {

}

ventas = {sku: 0 for sku in inventario.keys()}
