"""
Archivo principal del sistema.

Este archivo se encarga únicamente de iniciar la aplicación.
Aquí se crea la ventana principal de Tkinter y se ejecuta la
clase que contiene toda la interfaz gráfica.

Separar el main del resto del código es una buena práctica
porque permite mantener el proyecto organizado y modular.
"""

# Importamos la librería tkinter que permite crear interfaces gráficas
import tkinter as tk

# Importamos la clase que contiene toda la interfaz gráfica del sistema
from ui.app_tkinter import AppGaraje


def main():
    """
    Función principal del programa.
    Se encarga de crear la ventana principal y ejecutar la aplicación.
    """

    # Creamos la ventana principal del sistema
    root = tk.Tk()

    # Creamos una instancia de nuestra aplicación
    # y le pasamos la ventana principal como parámetro
    app = AppGaraje(root)

    # Ejecutamos el ciclo principal de la interfaz gráfica
    # Esto mantiene la ventana abierta esperando eventos del usuario
    root.mainloop()


# Punto de entrada del programa
# Este bloque asegura que la función main() se ejecute
# solo cuando este archivo se ejecuta directamente.
if __name__ == "__main__":
    main()