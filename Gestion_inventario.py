import pandas as pd
import os

UMBRAL_STOCK_BAJO = 20  

class Producto:
    def __init__(self, nombre,precio,cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = int(cantidad)
    def descuento(self):
        return self.precio * 0.9
    def ver_producto(inventario):
        nombre = input

    