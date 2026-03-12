# Sistema de Gestión de Garaje 🚗

## Descripción del Proyecto

Mi proyecto consiste en una aplicación de escritorio desarrollada en **Python** utilizando la biblioteca **Tkinter** para la interfaz gráfica.
El sistema permite registrar, administrar y eliminar vehículos que ingresan a un garaje.

La aplicación fue desarrollada siguiendo una **arquitectura modular**, separando el código en diferentes capas para mejorar la organización, el mantenimiento y la comprensión del programa.

El sistema permite:

* Registrar vehículos.
* Visualizar los vehículos registrados en una tabla.
* Validar que no existan placas repetidas.
* Eliminar vehículos del sistema.
* Guardar la información en un archivo **JSON** para que los datos no se pierdan al cerrar el programa.

---

# Tecnologías Utilizadas

Las tecnologías utilizadas para el desarrollo del proyecto fueron:

* **Python 3**
* **Tkinter** (Interfaz gráfica)
* **JSON** (Almacenamiento de datos)

---

# Estructura del Proyecto

Mi proyecto está organizado en carpetas siguiendo una arquitectura modular.

```
garaje_app/
│
├── main.py
├── vehiculos.json
│
├── modelos/
│   └── vehiculo.py
│
├── servicios/
│   └── garaje_servicio.py
│
└── ui/
    └── app_tkinter.py
```

### Descripción de cada carpeta

**main.py**

Archivo principal del programa.
Se encarga de iniciar la aplicación y ejecutar la interfaz gráfica.

**modelos**

Contiene las clases que representan las entidades del sistema.

* `vehiculo.py`: define la clase Vehiculo.

**servicios**

Contiene la lógica del sistema.

* `garaje_servicio.py`: permite agregar, eliminar, listar y guardar vehículos.

**ui**

Contiene la interfaz gráfica desarrollada con Tkinter.

* `app_tkinter.py`: controla la interacción del usuario con el sistema.

**vehiculos.json**

Archivo donde se almacenan los vehículos registrados.

---

# Funcionalidades del Sistema

El sistema cuenta con las siguientes funcionalidades:

### Registrar Vehículo

Permite ingresar:

* Placa
* Marca
* Propietario

El sistema valida que todos los campos estén completos.

---

### Validación de Placa

El sistema verifica que la **placa no esté repetida** antes de registrar el vehículo.

---

### Visualización de Vehículos

Todos los vehículos registrados se muestran en una **tabla dentro de la interfaz gráfica**.

---

### Eliminar Vehículo

Permite seleccionar un vehículo de la tabla y eliminarlo del sistema.

---

### Guardado
