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
        nombre = input("Ingrese el nombre del producto a ver:").strip().title()
        if nombre in inventario:
            producto = inventario[nombre]
            print(f"\n -- Detalles de {nombre} --")
            print(f"Precio: $(producto.precio:,.2f)")
            print(f"Stock: {producto.cantidad} unidades")
            print(f" Precio con 10% de Descuento: ${producto.descuento():,.2f})")
        else:
            print(f"Producto {nombre} no encontrado en el inventario")
    def agregar_producto(inventario):
        nombre = input("Ingrese el nombre del producto").strip().title()
        if nombre in inventario:
            print("El producto {nombre} ya existe. Use 'Actualizar Stock' o 'Actualizar Precio'.")
            return
        while True:
            try:
                precio = float(input("Ingrese el precio del producto: $"))
                cantidad = int(input("Ingrese la cantidad (stock):"))
                if precio < 0 or cantidad < 0:
                    print("El precio y la cantidad debe ser validos positivos")
                    continue
                break
            except ValueError: 
                print("Error: Por Favor, ingrese un numero valido para precio y cantidad")
                nuevo_producto = Producto(nombre,precio,cantidad)
                inventario[nombre] = nuevo_producto
                print(f"Producto'{nombre}' agregado correctamente")
    def vender_producto(inventario):
        nombre_producto = input("Ingrese el nombre del producto a vender:").strip().title()
        if nombre_producto in inventario:
            producto = inventario[nombre_producto]
            while True:
                try:
                    cantidad = int(input(f"Stock actual: {producto.cantidad}. ¿Cuantas unidades de {nombre_producto} desea vender?:"))
                    if cantidad <= 0:
                        print("La cantidad a vender debe ser mayor a cero:")
                        continue
                    break
                except ValueError:
                    print(f"Error: Por Favor, ingrese un numero entero para la cantidad")
                    if producto.cantidad >= cantidad:
                        producto.cantidad -= cantidad
                        print(f" Se vendieron {cantidad} unidades de {nombre_producto}. Stock restante {producto.cantidad}")
                    else:
                        print("No hay suficiente stock de {nombre_producto}. Stock disponible: {producto.cantidad}")
                else: 
                        print(f"No se encontro el producto {nombre_producto} en el inventario")

    def listar_inventario(inventario,umbral):
        if not inventario:
            print("\n -- Inventario Vacio --")
            return
        print("\n -- Inventario Actual -- ")
        productos_con_alerta = 0
        for nombre, producto in inventario.items():
            alerta = ""
            if producto.cantidad < umbral:
                alerta = " (Stock Bajo)"
                productos_con_alerta += 1
                print(f"{nombre}: Stock: {producto.cantidad}, Precio: $ {producto.precio:,.2f}{alerta}")
                if productos_con_alerta > 0:
                    print(f"\n Hay {productos_con_alerta} productos con stock bajo el umbral de {umbral}.")
    def actualizar_stock(inventario):
        nombre = input("Ingrese el nombre del producto a actualizar:").strip().title()
        if nombre in inventario:
            producto = inventario[nombre]
            print(f"Stock actual de {nombre}: {producto.cantidad}")
            while True:
                try:
                    ajuste = int(input("Ingrese el ajuste de stock (+ para agregar, - para quitar):"))
                    nuevo_stock = producto.cantidad + ajuste
                    if nuevo_stock < 0:
                        print(f"Error: El stock ({nuevo_stock}) no puede ser negativo")
                        return
                    else:
                        producto.cantidad = nuevo_stock
                        print("Stock de {nombre} actualizado. Nuevo stock: {nuevo_stock}")
                        return
                except ValueError:
                    print("Ingrese un numero valido para el ajuste")
                else:
                    print("Producto {nombre} no encontrado")
    def main():
        try:
            df_productos = pd.read_csv("productos.csv")
        except:
            print("Error no se encontro el archivo 'productos.csv. inventario vacio")
            df_productos = pd.DataFrame(columns=['nombre','precio','cantidad'])
            inventario = {} #Almacenara los productos
            for index, row in df_productos.iterrows():
                try:
                    nombre = str(row['nombre']).strip().title
                    precio = float(row['precio'])
                    cantidad = int(row['cantidad'])
                    inventario[nombre] = Producto(nombre, precio, cantidad)
                except (KeyError, ValueError, TypeError) as e:
                    print("Error al procesar la fila {index} del CSV: {e}. Fila Incorrecta")
                    while True:
                        print("\n -- Menu Inventario --")
                        print("1.Ver Producto")
                        print("2.Agregar Producto")
                        print("3.Vender Producto")
                        print("4.Actualizar Precio")
                        print("5.Listar Inventario")
                        print("6.Actualizar Stock")
                        print("7.Salir")
                        
                        opcion = input("Seleccione una opcion").strip()
  
                    if opcion == "1":
                        ver_producto(inventario)
                    elif opcion == "2":
                            agregar_producto(inventario)
                    elif opcion == "3":
                            vender_producto(inventario)
                    elif opcion == "4":
                            actualizar_precio(inventario)
                    elif opcion == "5":
                            listar_inventario(inventario, umbral_bajo_stock)
                    elif opcion == "6": 
                            actualizar_stock(inventario)
                    elif opcion == "7":
                            print("Saliendo del sistema inventario")
                            break
                    else:
                            print("Opcion incorrecta. intente de nuevo")
                            if __name__ == "__main__":
                                main()








                                   






    