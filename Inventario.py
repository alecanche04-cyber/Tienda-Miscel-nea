from datetime import date, timedelta

productos = {}
lotes = [] 

def agregar_producto(nombre, stock_minimo, proveedor):
    productos[nombre] = {"stock_minimo": stock_minimo, "provevedor": proveedor}
    print(f"producto {nombre} registrado con stock minimo {stock_minimo} y proveedor {proveedor}")

def registrar_entrada(producto, cantidad, caducidad):
    if producto not in productos:
        print(f"El producto {producto} no está registrado.")
        return
    lotes.append({"producto": producto, "cantidad": cantidad, "caducidad": caducidad})
    print(f"Entrada registrada: {cantidad} unidades de {producto} con caducidad {caducidad}")


def registrar_salida(producto, cantidad):
    if producto not in productos:
        print(f"El producto {producto} no está registrado.")
        return
    lotes.sort(key=lambda x: x["caducidad"])
    restante = cantidad

    for lote in lotes:
        if lote["producto"] == producto and restante > 0:
            usar = min(lote["cantidad"], restante)
            lote["cantidad"] -= usar
            restante -= usar
    lotes[:] = [lote for lote in lotes if lote["cantidad"] > 0]
    if restante > 0:
        print(f"No hay suficiente stock de {producto}. Salida incompleta.")
    else:
        print(f"Salida registrada: {cantidad} unidades de {producto}")

def ver_stock(producto):
    if producto not in productos:
        print(f"El producto {producto} no está registrado.")
        return 0
    total = sum(lote["cantidad"] for lote in lotes if lote["producto"] == producto)
    print(f"Stock actual de {producto}: {total}")
    return total

def productos_bajo_stock():
    bajos = []
    for nombre, datos in productos.items():
        stock = ver_stock(nombre)
        if stock < datos["stock_minimo"]:
            bajos.append({"producto": nombre, "stock": stock, "stock_minimo": datos["stock_minimo"]})
    return bajos

def productos_por_caducar(dias=30):
    proximos = []
    limite = date.today() + timedelta(days=dias)
    for lote in lotes:
        if lote["caducidad"] <= limite:
            proximos.append(lote)
    return proximos

if __name__ == "__main__":
    agregar_producto("Leche", 10, "Proveedor A")
    agregar_producto("Arroz", 20, "Proveedor B")

    registrar_entrada("Leche", 15, date(2025, 12, 10))
    registrar_entrada("Arroz", 30, date(2026, 1, 5))

    ver_stock("Leche")
    registrar_salida("Leche", 5)
    ver_stock("Leche")

    print("Productos bajo stock:", productos_bajo_stock())
    print("Productos por caducar:", productos_por_caducar(40))
