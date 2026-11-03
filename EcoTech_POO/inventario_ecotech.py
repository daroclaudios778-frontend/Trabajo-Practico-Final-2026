
import json

class StockInvalidoError(Exception):
    pass


class DispositivoEcologico:

    def __init__(self, nombre, precio, stock):

        self.nombre = nombre
        self.precio = precio

        self._stock = 0
        self.stock = stock

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, nuevo_stock):

        if nuevo_stock < 0:
            raise StockInvalidoError(
                "El stock no puede ser negativo."
            )

        self._stock = nuevo_stock

    def ficha_tecnica(self):

        return (
            f"Producto: {self.nombre}\n"
            f"Precio: ${self.precio}\n"
            f"Stock: {self.stock}"
        )


# ==========================================
# 3. CLASE HIJA: PANEL SOLAR
# ==========================================

class PanelSolar(DispositivoEcologico):

    def __init__(self, nombre, precio, stock, potencia, eficiencia):

        super().__init__(nombre, precio, stock)

        self.potencia = potencia
        self.eficiencia = eficiencia

    def ficha_tecnica(self):

        return (
            f"=== FICHA TECNICA PANEL SOLAR ===\n"
            f"Producto: {self.nombre}\n"
            f"Precio: ${self.precio}\n"
            f"Stock: {self.stock}\n"
            f"Potencia: {self.potencia} W\n"
            f"Eficiencia: {self.eficiencia}%"
        )




class GestorInventario:

    def guardar_catalogo_json(self, lista_dispositivos, ruta_archivo):

        catalogo = []

        for dispositivo in lista_dispositivos:

            producto = {
                "tipo": dispositivo.__class__.__name__,
                "nombre": dispositivo.nombre,
                "precio": dispositivo.precio,
                "stock": dispositivo.stock
            }

            if isinstance(dispositivo, PanelSolar):

                producto["potencia"] = dispositivo.potencia
                producto["eficiencia"] = dispositivo.eficiencia

            catalogo.append(producto)

        with open(ruta_archivo, "w", encoding="utf-8") as archivo:

            json.dump(
                catalogo,
                archivo,
                indent=4,
                ensure_ascii=False
            )

        print(
            f"\nCatalogo guardado correctamente: {ruta_archivo}"
        )



# 5. BLOQUE PRINCIPAL DE EJECUCION


if __name__ == "__main__":

    # Crear productos
    panel1 = PanelSolar(
        "Panel Solar Eco 450",
        250000,
        15,
        450,
        22.5
    )

    panel2 = PanelSolar(
        "Panel Solar Eco 550",
        320000,
        10,
        550,
        23.8
    )

    # Comprobar error de stock
    try:

        panel1.stock = -5

    except StockInvalidoError as error:

        print("ERROR CONTROLADO:", error)

    # Mostrar fichas tecnicas
    print("\n", panel1.ficha_tecnica())
    print("\n", panel2.ficha_tecnica())

    # Crear lista de productos
    lista_dispositivos = [panel1, panel2]

    # Crear gestor
    gestor = GestorInventario()

    # Guardar catalogo
    gestor.guardar_catalogo_json(
        lista_dispositivos,
        "catalogo_ecotech.json"
    )
