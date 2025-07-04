# Tienda de regalos Gifty - Inventario y registro de ventas

#Inventario y conteo ventas

'''
inventario = {
    "001": {"nombre": "peluche", "precio": 10.0, "cantidad": 50},
    "002": {"nombre": "taza", "precio": 5.0, "cantidad": 100},
    "003": {"nombre": "camiseta", "precio": 15.0, "cantidad": 75},
    "004": {"nombre": "llavero", "precio": 3.0, "cantidad": 200},
    "005": {"nombre": "bufanda", "precio": 20.0, "cantidad": 30},
    "006": {"nombre": "gorro", "precio": 12.0, "cantidad": 40},
    "007": {"nombre": "agenda", "precio": 8.0, "cantidad": 60},
    "008": {"nombre": "correa_hombre", "precio": 25.0, "cantidad": 20},
    "009": {"nombre": "correa_mujer", "precio": 22.0, "cantidad": 25},
    "010": {"nombre": "cuadro_pared", "precio": 30.0, "cantidad": 15},
    "011": {"nombre": "juego_mesa", "precio": 18.0, "cantidad": 10},
    "012": {"nombre": "juego_cartas", "precio": 7.0, "cantidad": 80},
    "013": {"nombre": "rompecabezas", "precio": 14.0, "cantidad": 45},
    "014": {"nombre": "pelota_futbol", "precio": 11.0, "cantidad": 35},
    "015": {"nombre": "pelota_baloncesto", "precio": 13.0, "cantidad": 25},
    "016": {"nombre": "set_tenis", "precio": 16.0, "cantidad": 20},
    "017": {"nombre": "set_pintura", "precio": 9.0, "cantidad": 50},
    "018": {"nombre": "set_jardineria", "precio": 17.0, "cantidad": 30},
    "019": {"nombre": "reloj_hombre", "precio": 40.0, "cantidad": 10},
    "020": {"nombre": "reloj_mujer", "precio": 35.0, "cantidad": 15},
    "021": {"nombre": "mochila", "precio": 28.0, "cantidad": 20},
}
'''

inventario = {

}

ventas = {sku: 0 for sku in inventario.keys()}
