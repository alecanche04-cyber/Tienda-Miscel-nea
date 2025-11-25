from datetime import date
pedidos = []   

def generar_pedido(proveedor, productos):
    
    pedido_id = len(pedidos) + 1
    pedido = {
        "id": pedido_id,
        "proveedor": proveedor,
        "productos": productos,
        "fecha": date.today(),
        "estado": "borrador"
    }
    pedidos.append(pedido)
    print(f"Pedido #{pedido_id} generado para proveedor '{proveedor}'.")
    return pedido

def listar_pedidos():

    if not pedidos:
        print("No hay pedidos registrados.")
    for p in pedidos:
        print(f"ID: {p['id']} | Proveedor: {p['proveedor']} | Fecha: {p['fecha']} | Estado: {p['estado']}")
        for item in p["productos"]:
            print(f"   - {item['nombre']} x {item['cantidad']}")
    return pedidos

def confirmar_pedido(pedido_id):
    
    for p in pedidos:
        if p["id"] == pedido_id:
            p["estado"] = "confirmado"
            print(f"Pedido #{pedido_id} confirmado.")
            return p
    print(f"Error: Pedido con ID {pedido_id} no encontrado.")
    return None


if __name__ == "__main__":

    generar_pedido("Proveedor A", [{"nombre": "Leche", "cantidad": 20}, {"nombre": "Arroz", "cantidad": 50}])
    generar_pedido("Proveedor B", [{"nombre": "Aceite", "cantidad": 10}])


    listar_pedidos()


    confirmar_pedido(1)

    listar_pedidos()