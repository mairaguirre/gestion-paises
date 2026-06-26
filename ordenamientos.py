# ============================================================================
# Módulo de ordenamientos

# Funciones para ordenar datos.
# Ordena por nombre, población o superficie.
# Se puede ordenar de forma ascendente o descendente.
# ============================================================================

# >> Importar funciones

from datos import mostrar_paises
from validaciones import pedir_opcion

# >> Funciones

# La función sorted() recibe una función auxiliar.
# Esa función le indica qué dato debe usar para comparar los países.
# En un caso devuelve el nombre, en otro la población y en otro la superficie.


# 1) Ordenar por nombre


# Función auxiliar
def obtener_nombre(pais):
    return pais["nombre"].lower()


# Función principal
def ordenar_por_nombre(paises, descendente=False):
    return sorted(paises, key=obtener_nombre, reverse=descendente)


# 2) Ordenar por población


# Función auxiliar
def obtener_poblacion(pais):
    return pais["poblacion"]


# Función principal
def ordenar_por_poblacion(paises, descendente=False):
    return sorted(paises, key=obtener_poblacion, reverse=descendente)


# 3) Ordenar por superficie


# Función auxiliar
def obtener_superficie(pais):
    return pais["superficie"]


# Función principal
def ordenar_por_superficie(paises, descendente=False):
    return sorted(paises, key=obtener_superficie, reverse=descendente)


# 4) Pedir al usuario el orden ascendente o descendente


def pedir_orden():
    print("""
--- TIPO DE ORDEN ---
1. Ascendente
2. Descendente
""")

    opcion = pedir_opcion("Elija una opción: ", ["1", "2"])

    opcion = int(opcion)

    if opcion == 1:
        return False
    else:
        return True


# >> Menú y ejecución


def menu_ordenamientos(paises):
    while True:
        print("""
----- MENÚ DE ORDENAMIENTOS -----
1. Ordenar por nombre
2. Ordenar por población
3. Ordenar por superficie
4. Volver al menú principal
""")
        # Elegir opción del menú
        opcion = pedir_opcion("Elija una opción: ", ["1", "2", "3", "4"])

        opcion = int(opcion)

        # En caso de opción 4 --> Volver al menú
        if opcion == 4:
            break

        # Pedir al usuario el orden (asc/desc)
        descendente = pedir_orden()

        # Procesar las selecciones del usuario
        if opcion == 1:
            resultados = ordenar_por_nombre(paises, descendente)
        elif opcion == 2:
            resultados = ordenar_por_poblacion(paises, descendente)
        elif opcion == 3:
            resultados = ordenar_por_superficie(paises, descendente)

        mostrar_paises(resultados)
