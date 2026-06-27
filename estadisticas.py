# ============================================================================
# Módulo de estadísticas

# Contiene funciones para realizar estadísticas precisas.
# Calcula, verifica y clasifica por: mayor población, menor población, promedio
# de población, promedio de superficie y cantidad de países por continente.
# ============================================================================

# >> Importar funciones

from validaciones import pedir_opcion

# >> Funciones

# 1) Mayor población


def pais_mayor_poblacion(paises):
    mayor = paises[0]

    for pais in paises:
        if pais["poblacion"] > mayor["poblacion"]:
            mayor = pais

    return mayor


# 2) Menor población


def pais_menor_poblacion(paises):
    menor = paises[0]

    for pais in paises:
        if pais["poblacion"] < menor["poblacion"]:
            menor = pais

    return menor


# 3) Promedio de población


def promedio_poblacion(paises):
    acumulativo = 0

    for pais in paises:
        acumulativo += pais["poblacion"]

    return acumulativo / len(paises)


# 4) Promedio de superficie


def promedio_superficie(paises):
    acumulativo = 0

    for pais in paises:
        acumulativo += pais["superficie"]

    return acumulativo / len(paises)


# 5) Cantidad de países por continente


def cantidad_por_continente(paises):

    # Crea un dicc. para almacenar la información
    # Formato --> {"continente":"contador"}
    # Donde 'contador' es un 'int' que contabiliza la cantidad de países

    continentes = {}

    # Busca los continentes
    for pais in paises:
        # Identifica al país y al continente
        continente = pais["continente"]

        # Si el continente ya se encuentra en el diccionario 'continentes',
        # quiere decir que ya se cargó al menos una vez en el diccionario,
        # entonces sumamos 1 al 'contador' de dicho contiente
        if continente in continentes:
            continentes[continente] += 1

        # Si es la primera vez que se agrega el contiente al diccionario
        # 'continentes', se inicializa su contador en 1
        else:
            continentes[continente] = 1

    # Retorna el diccionario con las coincidencias
    return continentes


# >> Menú y ejecución


def menu_estadisticas(paises):

    # Línea de código que evita operar si no hay países cargados
    # Evita el 'ZeroDivisionError' al no permitir avanzar en el programa
    # y evitar dividir si hay 0 países

    if len(paises) == 0:
        print("\nNo hay países cargados.")
        return

    # Incio del flujo normal cuando hay países cargados incialmente

    while True:

        print("""
----- ESTADÍSTICAS -----
1. País con mayor población
2. País con menor población
3. Promedio de población
4. Promedio de superficie
5. Cantidad de países por continente
6. Volver al menú principal
""")

        opcion = pedir_opcion("Elija una opción: ", ["1", "2", "3", "4", "5", "6"])

        opcion = int(opcion)

        # Ejecución de opción elegida por el usuario

        if opcion == 1:
            pais = pais_mayor_poblacion(paises)
            print(
                f"\n{pais['nombre']} tiene la mayor población: {pais['poblacion']} habitantes."
            )

        elif opcion == 2:
            pais = pais_menor_poblacion(paises)
            print(
                f"\n{pais['nombre']} tiene la menor población: {pais['poblacion']} habitantes."
            )

        elif opcion == 3:
            promedio = promedio_poblacion(paises)
            print(f"\nPromedio de población: {promedio:.1f}")

        elif opcion == 4:
            promedio = promedio_superficie(paises)
            print(f"\nPromedio de superficie: {promedio:.1f}")

        elif opcion == 5:
            datos = cantidad_por_continente(paises)

            print("\nCantidad de países por continente:\n")

            for continente, cantidad in datos.items():
                print(f"{continente}: {cantidad}")

        # Opción 6 --> Volver al menú principal
        else:
            break
