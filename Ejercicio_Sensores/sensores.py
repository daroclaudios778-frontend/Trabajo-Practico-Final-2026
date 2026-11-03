def limpiar_registro_sensor(registro_raw):

    sensor_id = registro_raw.get("sensor_id", "").strip()

    temperatura = registro_raw.get("temperatura", "0")
    temperatura = float(temperatura.replace("C", "").strip())

    ubicacion = registro_raw.get(
        "ubicacion", "Ubicación desconocida"
    )

    ubicacion = ubicacion.strip() or "Ubicación desconocida"

    registro_limpio = {
        "sensor_id": sensor_id,
        "temperatura": temperatura,
        "ubicacion": ubicacion
    }

    return registro_limpio


def generar_resumen_sensores(lista_sensores_limpios, umbral_temperatura):

    lista_sensores_alerta = []
    suma_temperaturas = 0

    for sensor in lista_sensores_limpios:

        temperatura = sensor["temperatura"]

        suma_temperaturas += temperatura

        if temperatura > umbral_temperatura:
            lista_sensores_alerta.append(sensor["sensor_id"])

    promedio_temperatura = suma_temperaturas / len(lista_sensores_limpios)

    return lista_sensores_alerta, promedio_temperatura


if __name__ == "__main__":

    # Datos originales de los sensores
    registros_raw = [
        {
            "sensor_id": " SENSOR-001 ",
            "temperatura": "24.5C",
            "ubicacion": "Planta Norte"
        },
        {
            "sensor_id": " SENSOR-002 ",
            "temperatura": "35C",
            "ubicacion": "Planta Sur"
        },
        {
            "sensor_id": " SENSOR-003 ",
            "temperatura": "29C",
            "ubicacion": "Planta Este"
        },
        {
            "sensor_id": " SENSOR-004 ",
            "temperatura": "32.5C"
        }
    ]

    # Limpiar todos los registros
    sensores_limpios = []

    for registro in registros_raw:
        sensor = limpiar_registro_sensor(registro)
        sensores_limpios.append(sensor)

    # Establecer el límite de temperatura
    umbral = 30

    # Generar el resumen
    alertas, promedio = generar_resumen_sensores(
        sensores_limpios, umbral
    )

    # Imprimir el reporte
    print("\n===== REPORTE DE SENSORES ECOTECH =====")

    print("\nSensores registrados:")

    for sensor in sensores_limpios:
        print(
            f"{sensor['sensor_id']} | "
            f"{sensor['temperatura']} °C | "
            f"{sensor['ubicacion']}"
        )

    print("\nSensores que superan el umbral:")

    if alertas:
        for sensor_id in alertas:
            print(f"ALERTA: {sensor_id}")
    else:
        print("No se detectaron alertas.")

    print(f"\nUmbral establecido: {umbral} °C")
    print(f"Promedio general: {promedio:.2f} °C")

    print("\n== FIN DEL REPORTE     ===")