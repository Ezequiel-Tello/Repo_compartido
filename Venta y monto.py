#1 saludamos con un msj de presentacion
print("montos y ventas")
#2 solicitamos la cantidad de ventas
cantidad = int(input("¿cuantas ventas queres ingresar?: "))
#3 iniciamos la lista (vector)
ventas = []
#4 cargamos el vector con los montos
for i in range(cantidad):
    monto = float(input(f"ingrese el monto de la venta {i+1}: "))
    ventas.append(monto)
#5 calculamos el total de los montos de cada venta
total_ventas = 0
for venta in ventas:
    total_ventas += venta
#6  mostramos el resultado
print(f"El total de ventas realizadas es:${total_ventas:.2f}")


