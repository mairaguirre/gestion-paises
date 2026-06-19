#============================================================================
# Módulo de validaciones

# Funciones reutilizables para pedir datos al usuario por consola
# repite la pregunta hasta recibir una entrada válida evitando que
# el programa se rompa ante entradas invalidas
#============================================================================


def pedir_entero(mensaje, minimo=0):
    #Pide un número entero por consola y lo devuelve
    # Repite hasta que la entrada sea un entero válido y mayor o igual
    # que 'minimo'. Por defecto no acepta negativos (minimo=0).
    while True:
        entrada = input(mensaje).strip()
        try:
            numero = int(entrada)
        except ValueError:
            print("Entrada inválida: ingresá un número entero.")
            continue
        if numero < minimo:
            print(f"El valor debe ser mayor o igual a {minimo}.")
            continue
        return numero


def pedir_texto_no_vacio(mensaje):
    #Pide un texto por consola y lo devuelve
    # Repite hasta que el usuario ingrese algo distinto de vacío
    while True:
        entrada = input(mensaje).strip()
        if entrada == "":
            print("Este campo no puede quedar vacío.")
            continue
        return entrada


def pedir_opcion(mensaje, opciones_validas):
    #Pide una opción de menú y la devuelve
    # 'opciones_validas' es una lista de strings aceptados (ej: ['1','2','3'])
    # Repite hasta que la entrada coincida con alguna opción válida
    
    while True:
        entrada = input(mensaje).strip()
        if entrada in opciones_validas:
            return entrada
        print("Opción inválida. Intentá de nuevo.")
