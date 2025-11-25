from datetime import date
import Inventario   # importar el módulo inventario.py
import Pedidos      # importar el módulo pedidos.py

def mostrar_menu():
    print("\n=== Sistema de Inventario y Pedidos ===")
    print("1. Registrar producto")
    print("2. Registrar entrada (compra)")
    print("3. Registrar salida (venta)")
    print("4. Ver stock de producto")
    print("5. Productos bajo stock")
    print("6. Productos por caducar")
    print("7. Generar pedido")
    print("8. Listar pedidos")
    print("9. Confirmar pedido")
    print("0. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":

            
            nombre = input("Nombre del producto: ")
            stock_minimo = int(input("Stock mínimo: "))
            proveedor = input("Proveedor: ")
            Inventario.agregar_producto(nombre, stock_minimo, proveedor)

        elif opcion == "2":
            producto = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            caducidad_str = input("Fecha de caducidad (YYYY-MM-DD): ")
            caducidad = date.fromisoformat(caducidad_str)
            Inventario.registrar_entrada(producto, cantidad, caducidad)

        elif opcion == "3":
            producto = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            Inventario.registrar_salida(producto, cantidad)

        elif opcion == "4":
            producto = input("Nombre del producto: ")
            Inventario.ver_stock(producto)

        elif opcion == "5":
            bajos = Inventario.productos_bajo_stock()
            print("Productos bajo stock:", bajos)

        elif opcion == "6":
            proximos = Inventario.productos_por_caducar()
            print("Productos por caducar:", proximos)

        elif opcion == "7":
            proveedor = input("Proveedor: ")
            productos = []
            while True:
                nombre = input("Producto (o ENTER para terminar): ")
                if not nombre:
                    break
                cantidad = int(input("Cantidad: "))
                productos.append({"nombre": nombre, "cantidad": cantidad})
            Pedidos.generar_pedido(proveedor, productos)

        elif opcion == "8":
            Pedidos.listar_pedidos()

        elif opcion == "9":
            pedido_id = int(input("ID del pedido a confirmar: "))
            Pedidos.confirmar_pedido(pedido_id)

        elif opcion == "0":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
    main()