# Tienda de regalos Gifty - Inventario y registro de ventas

#Inventario y conteo ventas

'''
inventario = {
    "001": {"nombre": "peluche", "precio": 100, "cantidad": 50},
    "002": {"nombre": "taza", "precio": 50, "cantidad": 100},
    "003": {"nombre": "camiseta", "precio": 150, "cantidad": 75},
    "004": {"nombre": "llavero", "precio": 30, "cantidad": 200},
    "005": {"nombre": "bufanda", "precio": 200, "cantidad": 30},
    "006": {"nombre": "gorro", "precio": 120, "cantidad": 40},
    "007": {"nombre": "agenda", "precio": 80, "cantidad": 60},
    "008": {"nombre": "correa_hombre", "precio": 250, "cantidad": 20},
    "009": {"nombre": "correa_mujer", "precio": 220, "cantidad": 25},
    "010": {"nombre": "cuadro_pared", "precio": 300, "cantidad": 15},
    "011": {"nombre": "juego_mesa", "precio": 180, "cantidad": 10},
    "012": {"nombre": "juego_cartas", "precio": 70, "cantidad": 80},
    "013": {"nombre": "rompecabezas", "precio": 140, "cantidad": 45},
    "014": {"nombre": "pelota_futbol", "precio": 110, "cantidad": 35},
    "015": {"nombre": "pelota_baloncesto", "precio": 130, "cantidad": 25},
    "016": {"nombre": "set_tenis", "precio": 160, "cantidad": 20},
    "017": {"nombre": "set_pintura", "precio": 90, "cantidad": 50},
    "018": {"nombre": "set_jardineria", "precio": 170, "cantidad": 30},
    "019": {"nombre": "reloj_hombre", "precio": 400, "cantidad": 10},
    "020": {"nombre": "reloj_mujer", "precio": 350, "cantidad": 15},
    "021": {"nombre": "mochila", "precio": 280, "cantidad": 20},
}
'''

inventario = {

}

ventas = {sku: 0 for sku in inventario.keys()}
