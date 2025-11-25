import sqlite3
from datetime import date

# --- Conexión y creación de tablas ---
def init_db():
    conn = sqlite3.connect("tienda.db")
    cursor = conn.cursor()

    # Crear tabla productos
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        stock_minimo INTEGER NOT NULL,
        proveedor TEXT NOT NULL
    )
    """)

    # Crear tabla lotes
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS lotes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        producto_id INTEGER NOT NULL,
        cantidad INTEGER NOT NULL,
        fecha_caducidad DATE NOT NULL,
        FOREIGN KEY(producto_id) REFERENCES productos(id)
    )
    """)

    # Crear tabla pedidos
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pedidos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        proveedor TEXT NOT NULL,
        fecha DATE NOT NULL,
        estado TEXT NOT NULL
    )
    """)

    # Crear tabla pedido_items
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pedido_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pedido_id INTEGER NOT NULL,
        producto_id INTEGER NOT NULL,
        cantidad INTEGER NOT NULL,
        FOREIGN KEY(pedido_id) REFERENCES pedidos(id),
        FOREIGN KEY(producto_id) REFERENCES productos(id)
    )
    """)

    conn.commit()
    conn.close()

# --- Funciones básicas ---

def agregar_producto(nombre, stock_minimo, proveedor):
    conn = sqlite3.connect("tienda.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO productos (nombre, stock_minimo, proveedor) VALUES (?, ?, ?)",
                    (nombre, stock_minimo, proveedor))
    conn.commit()
    conn.close()

def registrar_entrada(producto_id, cantidad, fecha_caducidad):
    conn = sqlite3.connect("tienda.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO lotes (producto_id, cantidad, fecha_caducidad) VALUES (?, ?, ?)",
                    (producto_id, cantidad, fecha_caducidad))
    conn.commit()
    conn.close()

def registrar_pedido(proveedor, productos):
    """
    productos: lista de dicts [{"producto_id": int, "cantidad": int}]
    """
    conn = sqlite3.connect("tienda.db")
    cursor = conn.cursor()

    # Crear pedido
    cursor.execute("INSERT INTO pedidos (proveedor, fecha, estado) VALUES (?, ?, ?)",
                    (proveedor, date.today(), "borrador"))
    pedido_id = cursor.lastrowid

    # Insertar items
    for item in productos:
        cursor.execute("INSERT INTO pedido_items (pedido_id, producto_id, cantidad) VALUES (?, ?, ?)",
                        (pedido_id, item["producto_id"], item["cantidad"]))

    conn.commit()
    conn.close()
    return pedido_id

def confirmar_pedido(pedido_id):
    conn = sqlite3.connect("tienda.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE pedidos SET estado = ? WHERE id = ?", ("confirmado", pedido_id))
    conn.commit()
    conn.close()

def listar_pedidos():
    conn = sqlite3.connect("tienda.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pedidos")
    pedidos = cursor.fetchall()
    conn.close()
    return pedidos

# --- Ejemplo de uso ---
if __name__ == "__main__":
    init_db()

    # Agregar productos
    agregar_producto("Leche", 10, "Proveedor A")
    agregar_producto("Arroz", 20, "Proveedor B")

    # Registrar entrada de lotes
    registrar_entrada(1, 15, "2025-12-10")
    registrar_entrada(2, 30, "2026-01-05")

    # Crear pedido
    pedido_id = registrar_pedido("Proveedor A", [{"producto_id": 1, "cantidad": 20}])

    # Listar pedidos
    print("Pedidos:", listar_pedidos())

    # Confirmar pedido
    confirmar_pedido(pedido_id)
    print("Pedidos después de confirmar:", listar_pedidos())