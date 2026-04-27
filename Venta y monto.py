ventas = []
cantidad = int(input("¿cuantas ventas queres ingresar"))
for i in range(cantidad):
    monto = float(input(f"ingrese el monto de la venta{i+1}"))
    ventas.append(monto)
    #calculamos el total de los montos de cada venta
total_ventas = 0
for venta in ventas:
    total_ventas += venta
    print("el total de ventas es",total_ventas)
    