import unittest
from .emisiones import calcular_emisiones_carbono
from django.test import TestCase


class TestCalculoEmisiones(unittest.TestCase):

    def test_calculo_normal(self):
        self.assertEqual(calcular_emisiones_carbono(100), 40.0)

    def test_factor_personalizado(self):
        self.assertEqual(calcular_emisiones_carbono(200, 0.5), 100.0)

    def test_consumo_cero(self):
        self.assertEqual(calcular_emisiones_carbono(0), 0.0)

    def test_consumo_negativo(self):
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-50)


class PanelSustentabilidadTests(TestCase):

    def test_panel_disponible_en_inicio_y_ruta_de_app(self):
        for ruta in ("/", "/sustentabilidad/"):
            with self.subTest(ruta=ruta):
                respuesta = self.client.get(ruta)

                self.assertEqual(respuesta.status_code, 200)
                self.assertContains(respuesta, "Panel de sustentabilidad")
                self.assertContains(respuesta, "320,0")
                self.assertContains(respuesta, "Consumo total")
                self.assertContains(respuesta, "static/sustentabilidad/panel.css")