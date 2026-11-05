from django.shortcuts import render
from .emisiones import obtener_metricas_consumo


def vista_panel_sustentabilidad(request):

    registros = [
        {"planta": "Planta Norte", "consumo_kwh": 100},
        {"planta": "Planta Sur", "consumo_kwh": 200},
        {"planta": "Planta Este", "consumo_kwh": 500},
    ]

    metricas = obtener_metricas_consumo(registros)
    consumos_por_planta = metricas["consumos_por_planta"]
    consumo_maximo = max(consumos_por_planta.values(), default=0)
    plantas = [
        {
            "nombre": planta,
            "consumo": consumo,
            "porcentaje": consumo / consumo_maximo * 100 if consumo_maximo else 0,
        }
        for planta, consumo in consumos_por_planta.items()
    ]

    contexto = {
        "total_emisiones": metricas["total_emisiones"],
        "planta_mayor_consumo": metricas["planta_mayor_consumo"],
        "total_consumo": sum(consumos_por_planta.values()),
        "plantas": plantas,
    }

    return render(
        request,
        "sustentabilidad/panel.html",
        contexto
    )