"""
Interfaz gráfica del sistema de garaje.

Este archivo utiliza Tkinter para crear la interfaz
que permite al usuario interactuar con el sistema.
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from servicios.garaje_servicio import GarajeServicio


class AppGaraje:

    def __init__(self, root):

        # Guardamos la ventana principal
        self.root = root

        # Título de la ventana
        self.root.title("Sistema de Gestión de Garaje")

        # Creamos el servicio que maneja los datos
        self.servicio = GarajeServicio()

        # ======================
        # TITULOS
        # ======================

        tk.Label(
            root,
            text="Universidad Estatal Amazónica",
            font=("Arial", 12, "bold")
        ).grid(row=0, column=0, columnspan=3)

        tk.Label(
            root,
            text="Carrera de Ingeniería en Sistemas",
            font=("Arial", 11)
        ).grid(row=1, column=0, columnspan=3)

        tk.Label(
            root,
            text="Realizado por: Daniel Luzuriaga",
            font=("Arial", 8)
        ).grid(row=2, column=0, columnspan=3, pady=10)

        # ======================
        # CAMPOS
        # ======================

        tk.Label(root, text="Placa").grid(row=3, column=0)
        self.entry_placa = tk.Entry(root)
        self.entry_placa.grid(row=3, column=1)

        tk.Label(root, text="Marca").grid(row=4, column=0)
        self.entry_marca = tk.Entry(root)
        self.entry_marca.grid(row=4, column=1)

        tk.Label(root, text="Propietario").grid(row=5, column=0)
        self.entry_propietario = tk.Entry(root)
        self.entry_propietario.grid(row=5, column=1)

        # ======================
        # BOTONES
        # ======================

        tk.Button(root, text="Agregar", command=self.agregar_vehiculo).grid(row=6, column=0)

        tk.Button(root, text="Eliminar", command=self.eliminar_vehiculo).grid(row=6, column=1)

        tk.Button(root, text="Limpiar", command=self.limpiar_campos).grid(row=6, column=2)

        # ======================
        # TABLA
        # ======================

        self.tabla = ttk.Treeview(
            root,
            columns=("placa", "marca", "propietario"),
            show="headings"
        )

        self.tabla.heading("placa", text="Placa")
        self.tabla.heading("marca", text="Marca")
        self.tabla.heading("propietario", text="Propietario")

        self.tabla.grid(row=7, column=0, columnspan=3, pady=10)

        # Cargar vehículos guardados
        self.cargar_datos()

    def agregar_vehiculo(self):

        placa = self.entry_placa.get()
        marca = self.entry_marca.get()
        propietario = self.entry_propietario.get()

        if placa == "" or marca == "" or propietario == "":
            messagebox.showerror("Error", "Debe completar todos los campos")
            return

        resultado = self.servicio.agregar_vehiculo(placa, marca, propietario)

        if not resultado:
            messagebox.showerror("Error", "La placa ya está registrada")
            return

        self.tabla.insert("", "end", values=(placa, marca, propietario))

        messagebox.showinfo("Éxito", "Vehículo registrado correctamente")

        self.limpiar_campos()

    def eliminar_vehiculo(self):

        seleccion = self.tabla.selection()

        if not seleccion:
            messagebox.showerror("Error", "Debe seleccionar un vehículo")
            return

        datos = self.tabla.item(seleccion)

        placa = datos["values"][0]

        self.servicio.eliminar_vehiculo(placa)

        self.tabla.delete(seleccion)

        messagebox.showinfo("Éxito", "Vehículo eliminado")

    def limpiar_campos(self):

        self.entry_placa.delete(0, tk.END)
        self.entry_marca.delete(0, tk.END)
        self.entry_propietario.delete(0, tk.END)

    def cargar_datos(self):

        vehiculos = self.servicio.listar_vehiculos()

        for v in vehiculos:

            self.tabla.insert(
                "",
                "end",
                values=(v["placa"], v["marca"], v["propietario"])
            )