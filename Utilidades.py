import csv
from datetime import date, timedelta

# --- Configuración global ---
CONFIG = {
    "dias_alerta_caducidad": 30,   # productos que caducan en <= 30 días
    "ciclo_revision": 7            # revisión semanal (7 días)
}

# --- Manejo de fechas (caducidad) ---
def esta_por_caducar(fecha_caducidad, dias_alerta=None):
    """
    Verifica si un producto está por caducar en los próximos N días.
    """
    if dias_alerta is None:
        dias_alerta = CONFIG["dias_alerta_caducidad"]
    limite = date.today() + timedelta(days=dias_alerta)
    return fecha_caducidad <= limite

# --- Exportar reporte simple ---
def exportar_reporte_csv(nombre_archivo, datos, encabezados):
    """
    Exporta un reporte a CSV.
    datos: lista de diccionarios
    encabezados: lista de nombres de columnas
    """
    with open(nombre_archivo, mode="w", newline="", encoding="utf-8") as archivo:
        writer = csv.DictWriter(archivo, fieldnames=encabezados)
        writer.writeheader()
        writer.writerows(datos)
    print(f"Reporte exportado a {nombre_archivo}")

def imprimir_reporte(datos, titulo="Reporte"):
    """
    Imprime un reporte en pantalla de forma tabular.
    """
    print(f"\n=== {titulo} ===")
    if not datos:
        print("No hay datos para mostrar.")
        return
    for fila in datos:
        linea = " | ".join(f"{k}: {v}" for k, v in fila.items())
        print(linea)
    print("=" * 40)

# --- Configuración ---
def cambiar_configuracion(clave, valor):
    """
    Cambia un parámetro de configuración global.
    """
    if clave in CONFIG:
        CONFIG[clave] = valor
        print(f"Configuración '{clave}' actualizada a {valor}.")
    else:
        print(f"Error: clave '{clave}' no existe en configuración.")

def mostrar_configuracion():
    """
    Muestra la configuración actual.
    """
    print("\n--- Configuración actual ---")
    for k, v in CONFIG.items():
        print(f"{k}: {v}")
    print("----------------------------")

# --- Ejemplo de uso ---
if __name__ == "__main__":
    # Ejemplo de fechas
    fecha_caducidad = date(2025, 12, 10)
    print("¿Está por caducar?", esta_por_caducar(fecha_caducidad))

    # Ejemplo de reporte
    datos = [
        {"producto": "Leche", "stock": 5, "caducidad": "2025-12-10"},
        {"producto": "Arroz", "stock": 20, "caducidad": "2026-01-05"}
    ]
    imprimir_reporte(datos, titulo="Inventario Actual")
    exportar_reporte_csv("reporte_inventario.csv", datos, encabezados=["producto", "stock", "caducidad"])

    # Configuración
    mostrar_configuracion()
    cambiar_configuracion("ciclo_revision", 14)
    mostrar_configuracion()