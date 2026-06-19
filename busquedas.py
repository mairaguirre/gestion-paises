# busquedas.py - búsqueda de países por nombre (parcial o exacta).

import datos

def buscar_por_nombre(paises, texto):
    texto = texto.lower()
    resultado = []
    for pais in paises:
        if texto in pais["nombre"].lower():
            resultado.append(pais)
    return resultado


def menu_busqueda(paises):
    texto = input("¿Qué país buscás? ")
    resultado = buscar_por_nombre(paises, texto)
    if resultado:
        datos.mostrar_paises(resultado)
    else:
        print("No hay coincidencias")


if __name__ == "__main__":
    import datos
    paises = datos.cargar_csv("paises.csv")
    print(buscar_por_nombre(paises, "arg"))