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
            try:
                stock_minimo = int(input("Stock mínimo: "))
            except ValueError:
                print("Stock mínimo inválido. Introduce un número entero.")
                continue
            proveedor = input("Proveedor: ")
            Inventario.agregar_producto(nombre, stock_minimo, proveedor)

        elif opcion == "2":
            producto = input("Nombre del producto: ")
            try:
                cantidad = int(input("Cantidad: "))
            except ValueError:
                print("Cantidad inválida. Introduce un número entero.")
                continue
            caducidad_str = input("Fecha de caducidad (YYYY-MM-DD) (ENTER si no aplica): ")
            if caducidad_str.strip() == "":
                caducidad = None
            else:
                try:
                    caducidad = date.fromisoformat(caducidad_str)
                except Exception:
                    print("Formato de fecha inválido. Use YYYY-MM-DD o deje vacío.")
                    continue
            Inventario.registrar_entrada(producto, cantidad, caducidad)

        elif opcion == "3":
            producto = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            Inventario.registrar_salida(producto, cantidad)

        elif opcion == "4":
            producto = input("Nombre del producto: ")
            stock = Inventario.ver_stock(producto)
            # ver_stock imprime por sí misma, pero devolvemos y mostramos el valor también
            if stock is not None:
                print(f"Stock de {producto}: {stock}")

        elif opcion == "5":
            bajos = Inventario.productos_bajo_stock()
            if not bajos:
                print("No hay productos bajo stock.")
            else:
                print("Productos bajo stock:")
                for b in bajos:
                    print(f" - {b['producto']}: {b['stock']} (min {b['stock_minimo']})")

        elif opcion == "6":
            proximos = Inventario.productos_por_caducar()
            if not proximos:
                print("No hay lotes próximos a caducar.")
            else:
                print("Lotes por caducar:")
                for lote in proximos:
                    cad = lote.get("caducidad")
                    print(f" - {lote['producto']} x{lote['cantidad']} caduca {cad}")

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