"""
Servicio del Garaje

Contiene la lógica principal del sistema.
Se encarga de:

- Cargar los vehículos desde el archivo JSON
- Guardar vehículos
- Validar placas repetidas
- Eliminar vehículos
"""

import json
import os


class GarajeServicio:

    def __init__(self):
        """
        Constructor del servicio.

        Aquí se define el archivo donde se guardarán
        los vehículos y se cargan los datos existentes.
        """

        # Archivo donde se guardarán los vehículos
        self.archivo = "vehiculos.json"

        # Cargamos los vehículos guardados previamente
        self.vehiculos = self.cargar_archivo()

    def cargar_archivo(self):
        """
        Carga los vehículos desde el archivo JSON.
        """

        # Verificamos si el archivo existe
        if os.path.exists(self.archivo):

            # Abrimos el archivo en modo lectura
            with open(self.archivo, "r") as f:

                # Convertimos el JSON a lista de Python
                return json.load(f)

        # Si no existe el archivo retornamos lista vacía
        return []

    def guardar_archivo(self):
        """
        Guarda la lista actual de vehículos en el archivo JSON.
        """

        with open(self.archivo, "w") as f:
            json.dump(self.vehiculos, f, indent=4)

    def agregar_vehiculo(self, placa, marca, propietario):
        """
        Agrega un vehículo nuevo al sistema.

        También valida que la placa no esté repetida.
        """

        # Validar placa repetida
        for v in self.vehiculos:

            if v["placa"] == placa:
                return False

        # Crear vehículo
        vehiculo = {
            "placa": placa,
            "marca": marca,
            "propietario": propietario
        }

        # Agregar a la lista
        self.vehiculos.append(vehiculo)

        # Guardar cambios
        self.guardar_archivo()

        return True

    def eliminar_vehiculo(self, placa):
        """
        Elimina un vehículo usando su placa.
        """

        # Recorremos la lista buscando la placa
        for v in self.vehiculos:

            if v["placa"] == placa:

                # Eliminamos el vehículo
                self.vehiculos.remove(v)

                # Guardamos cambios
                self.guardar_archivo()

                return True

        return False

    def listar_vehiculos(self):
        """
        Retorna la lista de vehículos registrados.
        """

        return self.vehiculos