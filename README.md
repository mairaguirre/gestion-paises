# Gestión de Datos de Países en Python

Trabajo Práctico Integrador — Programación 1
Tecnicatura Universitaria en Programación a Distancia (TUPAD) — UTN

## Integrantes
- Maira Aguirre Gusmán - Comisión 14
- Matias Burgos - Comisión 20


## Descripción
Aplicación de consola en Python para gestionar información de países
(nombre, población, superficie y continente) desde un archivo CSV.
Permite agregar y actualizar países, buscarlos por nombre, filtrarlos,
ordenarlos y generar estadísticas.


## Estructura del proyecto
- `main.py` — menú principal y bucle del programa
- `datos.py` — carga del CSV, alta y actualización de países
- `validaciones.py` — funciones reutilizables de validación de entrada
- `busquedas.py` — busqueda de países por nombre
- `filtros.py` — filtros por continente y por rangos
- `ordenamientos.py` — ordenamientos por distintos criterios
- `estadisticas.py` — cálculo de estadisticas
- `paises.csv` — dataset base

## Diagrama de flujo general del proyecto

![Diagrama de flujo general](diagrama_flujo_final.png)

## Instrucciones de uso

### Requisitos

- Tener instalado Python 3.x.
- No es necesario instalar librerías externas, el programa incluye las funciones necesarias definidas.
- Es necesario respetar la estructura del proyecto para su correcto funcionamiento.
- Si se quiere modificar la estructura del proyecto, hay que cambiar las rutas relativas.

### Descargar el proyecto

Clonar el repositorio desde GitHub:

```bash
git clone https://github.com/mairaguirre/gestion-paises.git
```
### Consideraciones

- El programa fue desarrollado en Python 3.
- Los datos se leen desde el archivo `paises.csv`.
- Todas las entradas del usuario cuentan con validaciones para evitar errores durante la ejecución.


## Ejemplo de uso
Al ejecutar el programa se presenta el menú principal:

![Menú Principal](ej-de-uso/0_menu.png)

El usuario selecciona una opción ingresando el número correspondiente.

### Búsqueda de un país

![Realizar una búsqueda](ej-de-uso/3_busqueda.png)

El sistema muestra la información del país solicitado.

### Filtrado de países

![Aplicar un filtro](ej-de-uso/4_filtros.png)

Se listan únicamente los países que cumplen con el criterio seleccionado.

### Ordenamientos

![Ordenar por criterio](ej-de-uso/5_ordenamientos.png)

### Estadísticas

![Mostrar estadísticas](ej-de-uso/6_estadisticas.png)

El programa calcula y muestra distintos indicadores del dataset.

## Enlaces
- Documentación en PDF: [Documento PDF](TPI_Programacion1_MairaAguirreGusman_MatiasBurgos.pdf)
- Video explicativo: [![Video explicativo TPI](https://img.youtube.com/vi/VIDEO_ID/0.jpg)](https://www.youtube.com/watch?v=uJnZkPtHoeY)

