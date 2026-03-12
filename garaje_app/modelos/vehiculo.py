"""
Modelo Vehiculo

Este archivo define la clase Vehiculo, la cual representa
un objeto del mundo real dentro del sistema.

Un vehículo tiene tres atributos principales:
- Placa
- Marca
- Propietario
"""


class Vehiculo:
    """
    Clase que representa un vehículo dentro del sistema.
    """

    def __init__(self, placa, marca, propietario):
        """
        Constructor de la clase Vehiculo.

        Parámetros:
        placa : identificador único del vehículo
        marca : marca del vehículo
        propietario : persona dueña del vehículo
        """

        # Guardamos cada dato en atributos del objeto
        self.placa = placa
        self.marca = marca
        self.propietario = propietario

    def a_diccionario(self):
        """
        Convierte el objeto Vehiculo en un diccionario.

        Esto es necesario porque el formato JSON solo
        puede guardar estructuras como diccionarios o listas.
        """

        return {
            "placa": self.placa,
            "marca": self.marca,
            "propietario": self.propietario
        }