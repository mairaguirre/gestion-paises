#=========================================================================
# Gestión de Datos de Países - Trabajo Práctico Integrador Programación 1

# Punto de entrada del programa. Carga los datos desde el CSV, muestra el
# menú principal y pasa cada opción al módulo correspondiente.

# El flujo sigue el diagrama de la estructura general:
# cargar CSV -> validar -> menú -> procesar opción -> repetir / salir
#=========================================================================

import datos
import busquedas
import filtros
import ordenamientos
import estadisticas
import validaciones

RUTA_CSV = "paises.csv"


def mostrar_menu():
    #Imprime el menú principal con las 7 opciones disponibles
    print("\n===== GESTIÓN DE PAÍSES =====")
    print("1. Agregar país")
    print("2. Actualizar país")
    print("3. Buscar país por nombre")
    print("4. Filtrar países")
    print("5. Ordenar países")
    print("6. Estadísticas")
    print("7. Salir")


def main():
    #Carga los datos y ejecuta el bucle principal del menú
    paises = datos.cargar_csv(RUTA_CSV)

    #Si el CSV no es válido, no se continúa
    if not paises:
        print("No se pudieron cargar datos válidos. Revisá el archivo CSV.")
        return

    while True:
        mostrar_menu()
        opcion = validaciones.pedir_opcion(
            "Elegí una opción (1-7): ",
            ["1", "2", "3", "4", "5", "6", "7"],
        )

        if opcion == "1":
            datos.agregar_pais(paises)
        elif opcion == "2":
            datos.actualizar_pais(paises)
        elif opcion == "3":
            busquedas.menu_busqueda(paises)
        elif opcion == "4":
            filtros.menu_filtros(paises)
        elif opcion == "5":
            ordenamientos.menu_ordenamientos(paises)
        elif opcion == "6":
            estadisticas.menu_estadisticas(paises)
        elif opcion == "7":
            print("Hasta luego!")
            break


if __name__ == "__main__":
    main()
