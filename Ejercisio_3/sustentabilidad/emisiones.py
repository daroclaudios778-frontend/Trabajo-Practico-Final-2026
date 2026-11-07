def calcular_emisiones_carbono(consumo_kwh, factor_emision=0.4):

    if consumo_kwh < 0:
        raise ValueError("El consumo no puede ser negativo.")

    emisiones = consumo_kwh * factor_emision

    return emisiones


def obtener_metricas_consumo(registros):

    total_emisiones = 0
    consumos_por_planta = {}

    for registro in registros:

        nombre_planta = registro["planta"]
        consumo = registro["consumo_kwh"]

        emisiones = calcular_emisiones_carbono(consumo)

        total_emisiones += emisiones

        consumos_por_planta[nombre_planta] = (
            consumos_por_planta.get(nombre_planta, 0) + consumo
        )

    if consumos_por_planta:
        planta_mayor_consumo = max(
            consumos_por_planta,
            key=consumos_por_planta.get
        )
    else:
        planta_mayor_consumo = None

    return {
        "total_emisiones": total_emisiones,
        "planta_mayor_consumo": planta_mayor_consumo,
        "consumos_por_planta": consumos_por_planta
    }