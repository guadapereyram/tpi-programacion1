# Gestión de Datos de Países en Python

## Trabajo Práctico Integrador – Programación 1

### Integrante

- Guadalupe Pereyra

---

## Descripción

Este proyecto consiste en una aplicación desarrollada en Python que permite gestionar información de países utilizando listas, diccionarios, funciones y archivos CSV.

El sistema permite realizar operaciones de alta, actualización, búsqueda, filtrado, ordenamiento y generación de estadísticas sobre un conjunto de países almacenados en un archivo CSV.

---

## Funcionalidades

### Gestión de países

- Mostrar países cargados.
- Agregar nuevos países.
- Actualizar población y superficie de un país existente.
- Buscar países por nombre (coincidencia exacta o parcial).

### Filtros

- Filtrar por continente.
- Filtrar por rango de población.
- Filtrar por rango de superficie.

### Ordenamientos

- Ordenar por nombre.
- Ordenar por población.
- Ordenar por superficie.
- Ordenamiento ascendente o descendente.

### Estadísticas

- País con mayor población.
- País con menor población.
- Promedio de población.
- Promedio de superficie.
- Cantidad de países por continente.
- País con mayor densidad poblacional.
- País con menor densidad poblacional.

### Funcionalidades adicionales

- Persistencia de datos en archivo CSV.
- Exportación de resultados filtrados u ordenados a un nuevo archivo CSV.

---

## Estructura del proyecto

```text
TPI/
│
├── main.py
├── paises.csv
├── README.md
└── Informe_TPI.pdf
```

---

## Requisitos

- Python 3.x

No se requieren librerías externas.

---

## Ejecución

Ubicarse en la carpeta del proyecto y ejecutar:

```bash
py main.py
```

o

```bash
python main.py
```

---

## Dataset utilizado

El archivo `paises.csv` contiene información de países con los siguientes campos:

- nombre
- poblacion
- superficie
- continente

Ejemplo:

```csv
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,America
Brasil,213993437,8515767,America
```

---

## Ejemplos de uso

### Buscar un país

```text
Ingrese el nombre o parte del nombre:
arg
```

Resultado:

```text
Argentina
```

### Filtrar por continente

```text
Seleccione continente:
1. America
```

Resultado:

```text
Argentina
Brasil
Estados Unidos
México
Colombia
```

---

## Limitaciones

El archivo CSV utiliza la coma (,) como separador de campos.

Por este motivo, los nombres de países ingresados por el usuario no deben contener comas.

---

## Video demostrativo

Link al video:

[PENDIENTE DE AGREGAR]

---

## Documentación PDF

Link al informe:

[PENDIENTE DE AGREGAR]

---

## Repositorio

Link al repositorio:

[PENDIENTE DE AGREGAR]