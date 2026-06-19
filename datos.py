#=========================================================================
# Módulo de datos

# - cargar_csv: lee el dataset desde el CSV.
# - mostrar_paises: imprime una lista de países en formato de tabla
# - agregar_pais / actualizar_pais: alta y modificación (a implementar)

# Modelo de un país (diccionario):
#     {"nombre": str, "poblacion": int, "superficie": int, "continente": str}
#=============================================================================

import csv

COLUMNAS = ["nombre", "poblacion", "superficie", "continente"]


def cargar_csv(ruta):
    #Lee el CSV y devuelve una lista de diccionarios (un país por fila)
    # Valida que el archivo exista y tenga las 4 columnas; convierte
    # poblacion/superficie a int; descarta filas con campos vacíos o
    # tipos inválidos. Devuelve [] si no se puede leer.
    
    paises = []
    try:
        #abre el archivo, lo lee, interpreta con acentos, etc y lo guarda en archivo
        with open(ruta, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            #revisa el encabezado
            if lector.fieldnames is None or not _tiene_columnas(lector.fieldnames):
                print("Error: el CSV no tiene las columnas esperadas:", COLUMNAS)
                return []
            #recorre las filas desde la 2, pasa el encabezado
            for numero_fila, fila in enumerate(lector, start=2):
                pais = _fila_a_pais(fila, numero_fila)
                #si la fila es válida la agrega a la lista sino la saltea
                if pais is not None:
                    paises.append(pais)
    except FileNotFoundError:
        print(f"Error: no se encontró el archivo '{ruta}'.")
        return []
    print(f"Se cargaron {len(paises)} países desde '{ruta}'.")
    return paises


def _tiene_columnas(encabezado):
    #True si el encabezado contiene todas las columnas requeridas
    for columna in COLUMNAS:
        if columna not in encabezado:
            return False
    return True


def _fila_a_pais(fila, numero_fila):
    #Convierte una fila del CSV en un dict de país, o None si es inválida
    nombre = (fila.get("nombre") or "").strip()
    continente = (fila.get("continente") or "").strip()
    poblacion_texto = (fila.get("poblacion") or "").strip()
    superficie_texto = (fila.get("superficie") or "").strip()

    if nombre == "" or continente == "" or poblacion_texto == "" or superficie_texto == "":
        print(f"Fila {numero_fila} descartada: hay campos vacíos.")
        return None

    try:
        poblacion = int(poblacion_texto)
        superficie = int(superficie_texto)
    except ValueError:
        print(f"Fila {numero_fila} descartada: población/superficie no son enteros.")
        return None

    return {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente,
    }


def mostrar_paises(lista_paises):
    #Imprime una lista de países en formato de tabla
    if not lista_paises:
        print("No hay países para mostrar.")
        return
    print(f"\n{'Nombre':<20}{'Población':>15}{'Superficie':>15}  Continente")
    print("-" * 70)
    for pais in lista_paises:
        print(
            f"{pais['nombre']:<20}"
            f"{pais['poblacion']:>15,}"
            f"{pais['superficie']:>15,}"
            f"  {pais['continente']}"
        )


def agregar_pais(paises):
    pass


def actualizar_pais(paises):
    pass
