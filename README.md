# 📦 Gestión de Inventario por Sucursal

## Descripción del proyecto

Este programa es una aplicación de escritorio desarrollada en Python que permite administrar un inventario de productos mediante una interfaz gráfica.

El sistema permite agregar productos, registrar su precio y existencia, y consultar los productos que se encuentran registrados en el inventario.

La aplicación utiliza programación orientada a objetos para organizar la información de cada producto.

## Funcionalidades principales

* **Agregar productos:** permite registrar el nombre, precio y cantidad disponible de un producto.
* **Validar información:** verifica que todos los campos estén completos, que el precio sea numérico y que la existencia sea un número entero.
* **Mostrar inventario:** presenta una lista de todos los productos registrados.
* **Salir:** permite cerrar la aplicación.

## Tecnologías utilizadas

* **Python:** lenguaje de programación utilizado para desarrollar el sistema.
* **Tkinter:** biblioteca utilizada para crear la interfaz gráfica.
* **Messagebox:** herramienta de Tkinter para mostrar mensajes de información y errores.

## Estructura del proyecto

```text
Proyecto/
│
├── main.py
│
└── clases/
    └── Producto.py
```

## Descripción de las clases

### Clase Producto

Se encuentra en el archivo `Producto.py`.

Esta clase representa cada producto del inventario y contiene los siguientes atributos privados:

* `nombre`: nombre del producto.
* `precio`: precio del producto.
* `stock`: cantidad disponible.

También incluye métodos para obtener y modificar los atributos:

**Getters:**

* `get_nombre()`
* `get_precio()`
* `get_stock()`

**Setters:**

* `set_nombre()`
* `set_precio()`
* `set_stock()`

Los métodos `set_precio()` y `set_stock()` incluyen una validación para evitar valores negativos.

Además, cuenta con el método `__str__()`, que permite mostrar la información del producto en un formato legible.

## Interfaz gráfica

La aplicación cuenta con un menú principal que contiene tres opciones:

1. Agregar Producto a Inventario.
2. Mostrar Inventario.
3. Salir.

Al seleccionar la opción de agregar productos, se abre una ventana donde se capturan los siguientes datos:

* Nombre del producto.
* Precio del producto.
* Existencia.

Después de guardar correctamente un producto, este se agrega al inventario y se muestra un mensaje de confirmación.

## Instalación y ejecución

### Requisitos

* Tener Python instalado.
* Contar con soporte para Tkinter.

No se requieren bibliotecas externas adicionales, ya que el programa utiliza herramientas incluidas en Python.

### Pasos para ejecutar

1. Descargar o copiar los archivos del proyecto.
2. Verificar que la carpeta `clases` contenga el archivo `Producto.py`.
3. Abrir una terminal en la carpeta principal del proyecto.
4. Ejecutar el siguiente comando:

```bash
python main.py
```

## Almacenamiento de información

Los productos se guardan temporalmente en una lista dentro del programa.

**Importante:** actualmente, el sistema no utiliza una base de datos ni archivos externos para guardar el inventario. Por lo tanto, al cerrar la aplicación, los productos registrados se pierden.

## Objetivo del proyecto

Desarrollar una aplicación sencilla para gestionar productos de un inventario, aplicando conceptos de programación orientada a objetos, encapsulamiento, métodos, validación de datos e interfaces gráficas con Python.
