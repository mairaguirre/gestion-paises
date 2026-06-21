# filtros.py - filtros por continente, rango de población y rango de superficie

from datos import mostrar_paises
from validaciones import pedir_entero, pedir_texto_no_vacio, pedir_opcion

# Funciones para filtrar


def filtrar_por_continente(paises):
    continente = pedir_texto_no_vacio("Ingrese el continente: ").lower()

    resultados = []
    for pais in paises:
        if pais["continente"].lower() == continente:
            resultados.append(pais)

    return resultados


def filtrar_por_rango_poblacion(paises):
    minimo = pedir_entero("Ingrese población mínima: ")
    maximo = pedir_entero("Ingrese población máxima: ")

    if minimo > maximo:
        print("\nError: el mínimo no puede ser mayor que el máximo.")
        return []

    resultados = []
    for pais in paises:
        if minimo <= pais["poblacion"] <= maximo:
            resultados.append(pais)

    return resultados


def filtrar_por_rango_superficie(paises):
    minimo = pedir_entero("Ingrese superficie mínima: ")
    maximo = pedir_entero("Ingrese superficie máxima: ")

    if minimo > maximo:
        print("\nError: el mínimo no puede ser mayor que el máximo.")
        return []

    resultados = []
    for pais in paises:
        if minimo <= pais["superficie"] <= maximo:
            resultados.append(pais)

    return resultados


# Menú y ejecución


def menu_filtros(paises):
    while True:
        print("""
----- MENÚ DE FILTROS -----
1. Filtrar por continente
2. Filtrar por rango de población
3. Filtrar por rango de superficie
4. Volver al menú principal
""")

        opcion = pedir_opcion("Elija una opción: ", 1, 4)

        if opcion == 1:
            resultados = filtrar_por_continente(paises)
        elif opcion == 2:
            resultados = filtrar_por_rango_poblacion(paises)
        elif opcion == 3:
            resultados = filtrar_por_rango_superficie(paises)
        else:
            break

        if len(resultados) == 0:
            print("\nNo se encontraron países con el filtro elegido.")
        else:
            mostrar_paises(resultados)
