# ------------------------------------------------------------
# Gestión de Datos de Países en Python
# Trabajo Práctico Integrador - Programación 1
# Alumna: María Guadalupe Pereyra
# ------------------------------------------------------------

ARCHIVO_PAISES = "paises.csv"

# ------------------------------------------------------------
# Normaliza textos para comparar ignorando mayúsculas y espacios
# ------------------------------------------------------------


def normalizar_texto(texto):
    return texto.strip().lower()


# ------------------------------------------------------------
# Solicita un texto obligatorio y valida que no esté vacío
# ------------------------------------------------------------


def pedir_texto_obligatorio(mensaje):
    while True:
        texto = input(mensaje).strip()

        if texto == "":
            print("Error: este campo no puede estar vacío.")
        else:
            return texto


# ------------------------------------------------------------
# Solicita un número entero positivo
# ------------------------------------------------------------


def pedir_entero_positivo(mensaje):
    while True:
        try:
            numero = int(input(mensaje))

            if numero <= 0:
                print("Error: debe ingresar un número entero mayor que cero.")
            else:
                return numero

        except ValueError:
            print("Error: debe ingresar un número entero válido.")


# ------------------------------------------------------------
# Busca países por coincidencia parcial o exacta de nombre
# ------------------------------------------------------------


def buscar_pais_por_nombre(paises, nombre):
    resultados = []
    nombre_normalizado = normalizar_texto(nombre)

    for pais in paises:
        if nombre_normalizado in normalizar_texto(pais["nombre"]):
            resultados.append(pais)

    return resultados


# ------------------------------------------------------------
# Formatea números grandes con separador de miles
# ------------------------------------------------------------


def formatear_numero(numero):
    return f"{numero:,}".replace(",", ".")


# ------------------------------------------------------------
# Permite seleccionar un continente desde una lista cerrada
# ------------------------------------------------------------


def seleccionar_continente():
    continentes = ["America", "Europa", "Asia", "Africa", "Oceania"]

    while True:
        print("\nSeleccione el continente:")
        for indice, continente in enumerate(continentes, start=1):
            print(f"{indice}. {continente}")

        try:
            opcion = int(input("Opción: "))

            if opcion < 1 or opcion > len(continentes):
                print("Error: debe seleccionar una opción válida.")
            else:
                return continentes[opcion - 1]

        except ValueError:
            print("Error: debe ingresar un número entero válido.")


# ------------------------------------------------------------
# Guarda la lista de países en el archivo CSV
# ------------------------------------------------------------


def guardar_paises_en_csv(nombre_archivo, paises):
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write("nombre,poblacion,superficie,continente\n")

        for pais in paises:
            archivo.write(
                f"{pais['nombre']},"
                f"{pais['poblacion']},"
                f"{pais['superficie']},"
                f"{pais['continente']}\n"
            )


# ------------------------------------------------------------
# Exporta una lista de países a un archivo CSV externo
# ------------------------------------------------------------


def exportar_resultados_csv(nombre_archivo, resultados):
    if len(resultados) == 0:
        print("No hay resultados para exportar.")
        return

    guardar_paises_en_csv(nombre_archivo, resultados)
    print(f"Resultados exportados correctamente en '{nombre_archivo}'.")


# ------------------------------------------------------------
# Pregunta al usuario si desea exportar los resultados obtenidos
# ------------------------------------------------------------


def preguntar_exportacion(resultados):
    if len(resultados) == 0:
        return

    respuesta = (
        input("\n¿Desea exportar estos resultados a CSV? (s/n): ").strip().lower()
    )

    if respuesta == "s":
        exportar_resultados_csv("resultados_exportados.csv", resultados)
    elif respuesta == "n":
        print("No se exportaron los resultados.")
    else:
        print("Opción inválida. No se exportaron los resultados.")


# ------------------------------------------------------------
# Agrega un nuevo país validando campos y evitando duplicados
# ------------------------------------------------------------


def agregar_pais(paises):
    print("\n---------------------------------")
    print("AGREGAR PAÍS")
    print("---------------------------------")

    nombre = pedir_texto_obligatorio("Nombre del país: ")

    paises_encontrados = buscar_pais_por_nombre(paises, nombre)

    for pais in paises_encontrados:
        if normalizar_texto(pais["nombre"]) == normalizar_texto(nombre):
            print("Error: ya existe un país con ese nombre.")
            return

    poblacion = pedir_entero_positivo("Población: ")
    superficie = pedir_entero_positivo("Superficie en km²: ")
    continente = seleccionar_continente()

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente,
    }

    paises.append(nuevo_pais)
    guardar_paises_en_csv(ARCHIVO_PAISES, paises)

    print("País agregado correctamente.")


# ------------------------------------------------------------
# Busca países por nombre (exacto o parcial)
# ------------------------------------------------------------


def buscar_pais(paises):
    print("\n---------------------------------")
    print("BUSCAR PAÍS")
    print("---------------------------------")

    nombre = pedir_texto_obligatorio("Ingrese el nombre o parte del nombre del país: ")

    resultados = buscar_pais_por_nombre(paises, nombre)

    if len(resultados) == 0:
        print("No se encontraron países.")
        return

    mostrar_paises(resultados)


# ------------------------------------------------------------
# Actualiza la población y la superficie de un país existente
# ------------------------------------------------------------


def actualizar_pais(paises):
    print("\n---------------------------------")
    print("ACTUALIZAR PAÍS")
    print("---------------------------------")

    nombre = pedir_texto_obligatorio(
        "Ingrese el nombre del país que desea actualizar: "
    )

    resultados = buscar_pais_por_nombre(paises, nombre)

    if len(resultados) == 0:
        print("No se encontró ningún país con ese nombre.")
        return

    if len(resultados) > 1:
        print("Se encontraron varios países. Ingrese un nombre más específico:")
        mostrar_paises(resultados)
        return

    pais = resultados[0]

    print("\nDatos actuales:")
    mostrar_paises([pais])

    nueva_poblacion = pedir_entero_positivo("Nueva población: ")
    nueva_superficie = pedir_entero_positivo("Nueva superficie en km²: ")

    pais["poblacion"] = nueva_poblacion
    pais["superficie"] = nueva_superficie

    guardar_paises_en_csv(ARCHIVO_PAISES, paises)

    print("Datos actualizados correctamente.")


# ------------------------------------------------------------
# Filtra países por continente
# ------------------------------------------------------------


def filtrar_por_continente(paises):
    print("\n---------------------------------")
    print("FILTRAR POR CONTINENTE")
    print("---------------------------------")

    continente = seleccionar_continente()

    resultados = []

    for pais in paises:
        if normalizar_texto(pais["continente"]) == normalizar_texto(continente):
            resultados.append(pais)

    if len(resultados) == 0:
        print("No se encontraron países para ese continente.")
    else:
        mostrar_paises(resultados)
        preguntar_exportacion(resultados)


# ------------------------------------------------------------
# Filtra países por rango de población
# ------------------------------------------------------------


def filtrar_por_poblacion(paises):
    print("\n---------------------------------")
    print("FILTRAR POR RANGO DE POBLACIÓN")
    print("---------------------------------")

    poblacion_minima = pedir_entero_positivo("Población mínima: ")
    poblacion_maxima = pedir_entero_positivo("Población máxima: ")

    if poblacion_minima > poblacion_maxima:
        print("Error: la población mínima no puede ser mayor que la máxima.")
        return

    resultados = []

    for pais in paises:
        if (
            pais["poblacion"] >= poblacion_minima
            and pais["poblacion"] <= poblacion_maxima
        ):
            resultados.append(pais)

    if len(resultados) == 0:
        print("No se encontraron países dentro de ese rango de población.")
    else:
        mostrar_paises(resultados)
        preguntar_exportacion(resultados)


# ------------------------------------------------------------
# Filtra países por rango de superficie
# ------------------------------------------------------------


def filtrar_por_superficie(paises):
    print("\n---------------------------------")
    print("FILTRAR POR RANGO DE SUPERFICIE")
    print("---------------------------------")

    superficie_minima = pedir_entero_positivo("Superficie mínima: ")
    superficie_maxima = pedir_entero_positivo("Superficie máxima: ")

    if superficie_minima > superficie_maxima:
        print("Error: la superficie mínima no puede ser mayor que la máxima.")
        return

    resultados = []

    for pais in paises:
        if (
            pais["superficie"] >= superficie_minima
            and pais["superficie"] <= superficie_maxima
        ):
            resultados.append(pais)

    if len(resultados) == 0:
        print("No se encontraron países dentro de ese rango de superficie.")
    else:
        mostrar_paises(resultados)
        preguntar_exportacion(resultados)


# ------------------------------------------------------------
# Submenú de filtros
# ------------------------------------------------------------


def filtrar_paises(paises):
    while True:
        print("\n---------------------------------")
        print("FILTRAR PAÍSES")
        print("---------------------------------")
        print("1. Por continente")
        print("2. Por rango de población")
        print("3. Por rango de superficie")
        print("4. Volver")

        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                filtrar_por_continente(paises)
                input("\nPresioná Enter para continuar...")

            elif opcion == 2:
                filtrar_por_poblacion(paises)
                input("\nPresioná Enter para continuar...")

            elif opcion == 3:
                filtrar_por_superficie(paises)
                input("\nPresioná Enter para continuar...")

            elif opcion == 4:
                break

            else:
                print("Error: debe ingresar una opción entre 1 y 4.")

        except ValueError:
            print("Error: debe ingresar un número entero válido.")


# ------------------------------------------------------------
# Permite elegir si el ordenamiento será ascendente o descendente
# ------------------------------------------------------------


def seleccionar_tipo_ordenamiento():
    while True:
        print("\n---------------------------------")
        print("TIPO DE ORDENAMIENTO")
        print("---------------------------------")
        print("1. Ascendente")
        print("2. Descendente")

        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                return False

            elif opcion == 2:
                return True

            else:
                print("Error: debe ingresar una opción entre 1 y 2.")

        except ValueError:
            print("Error: debe ingresar un número entero válido.")


# ------------------------------------------------------------
# Ordena los países por nombre, población o superficie
# ------------------------------------------------------------


def ordenar_paises(paises):
    while True:
        print("\n---------------------------------")
        print("ORDENAR PAÍSES")
        print("---------------------------------")
        print("1. Nombre")
        print("2. Población")
        print("3. Superficie")
        print("4. Volver")

        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                descendente = seleccionar_tipo_ordenamiento()
                paises_ordenados = sorted(
                    paises,
                    key=lambda pais: normalizar_texto(pais["nombre"]),
                    reverse=descendente,
                )
                mostrar_paises(paises_ordenados)
                preguntar_exportacion(paises_ordenados)
                input("\nPresioná Enter para continuar...")

            elif opcion == 2:
                descendente = seleccionar_tipo_ordenamiento()
                paises_ordenados = sorted(
                    paises, key=lambda pais: pais["poblacion"], reverse=descendente
                )
                mostrar_paises(paises_ordenados)
                preguntar_exportacion(paises_ordenados)
                input("\nPresioná Enter para continuar...")

            elif opcion == 3:
                descendente = seleccionar_tipo_ordenamiento()
                paises_ordenados = sorted(
                    paises, key=lambda pais: pais["superficie"], reverse=descendente
                )
                mostrar_paises(paises_ordenados)
                preguntar_exportacion(paises_ordenados)
                input("\nPresioná Enter para continuar...")

            elif opcion == 4:
                break

            else:
                print("Error: debe ingresar una opción entre 1 y 4.")

        except ValueError:
            print("Error: debe ingresar un número entero válido.")


# ------------------------------------------------------------
# Calcula la densidad poblacional de un país
# ------------------------------------------------------------


def calcular_densidad(pais):
    return pais["poblacion"] / pais["superficie"]


# ------------------------------------------------------------
# Muestra las estadísticas principales del dataset
# ------------------------------------------------------------


def mostrar_estadisticas(paises):
    if len(paises) == 0:
        print("No hay países cargados para calcular estadísticas.")
        return

    pais_mayor_poblacion = max(paises, key=lambda pais: pais["poblacion"])
    pais_menor_poblacion = min(paises, key=lambda pais: pais["poblacion"])

    pais_mayor_densidad = max(paises, key=calcular_densidad)
    pais_menor_densidad = min(paises, key=calcular_densidad)

    suma_poblacion = 0
    suma_superficie = 0
    cantidad_por_continente = {}

    for pais in paises:
        suma_poblacion += pais["poblacion"]
        suma_superficie += pais["superficie"]

        continente = pais["continente"]

        if continente in cantidad_por_continente:
            cantidad_por_continente[continente] += 1
        else:
            cantidad_por_continente[continente] = 1

    promedio_poblacion = suma_poblacion / len(paises)
    promedio_superficie = suma_superficie / len(paises)

    print("\n---------------------------------")
    print("ESTADÍSTICAS")
    print("---------------------------------")

    print(
        f"País con mayor población: {pais_mayor_poblacion['nombre']} "
        f"({formatear_numero(pais_mayor_poblacion['poblacion'])} habitantes)"
    )

    print(
        f"País con menor población: {pais_menor_poblacion['nombre']} "
        f"({formatear_numero(pais_menor_poblacion['poblacion'])} habitantes)"
    )

    print(
        f"Promedio de población: "
        f"{formatear_numero(int(promedio_poblacion))} habitantes"
    )

    print(
        f"Promedio de superficie: " f"{formatear_numero(int(promedio_superficie))} km²"
    )

    print(
        f"País con mayor densidad poblacional: "
        f"{pais_mayor_densidad['nombre']} "
        f"({calcular_densidad(pais_mayor_densidad):.2f} hab/km²)"
    )

    print(
        f"País con menor densidad poblacional: "
        f"{pais_menor_densidad['nombre']} "
        f"({calcular_densidad(pais_menor_densidad):.2f} hab/km²)"
    )

    print("\nCantidad de países por continente:")

    for continente, cantidad in sorted(cantidad_por_continente.items()):
        print(f"- {continente}: {cantidad}")


# ------------------------------------------------------------
# Lee los países desde el archivo CSV y los carga en una lista
# de diccionarios.
# ------------------------------------------------------------


def cargar_paises_desde_csv(nombre_archivo):
    paises = []

    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            archivo.readline()  # Saltar encabezado

            for linea in archivo:
                datos = linea.strip().split(",")

                if len(datos) != 4:
                    print(f"Error de formato en la línea: {linea.strip()}")
                    continue

                try:
                    pais = {
                        "nombre": datos[0],
                        "poblacion": int(datos[1]),
                        "superficie": int(datos[2]),
                        "continente": datos[3],
                    }

                    paises.append(pais)

                except ValueError:
                    print(f"Error numérico en la línea: {linea.strip()}")
                    continue

    except FileNotFoundError:
        print("Error: no se encontró el archivo paises.csv.")

    return paises


# ------------------------------------------------------------
# Muestra una lista de países en formato tabular.
# ------------------------------------------------------------


def mostrar_paises(paises):
    if len(paises) == 0:
        print("No hay países cargados para mostrar.")
        return

    print("\n---------------------------------")
    print("LISTADO DE PAÍSES")
    print("---------------------------------")

    print(
        f"{'Nombre':<24}"
        f"{'Población':<18}"
        f"{'Superficie':<18}"
        f"{'Continente':<15}"
    )

    print("-" * 75)

    for pais in paises:
        print(
            f"{pais['nombre']:<24}"
            f"{formatear_numero(pais['poblacion']):<18}"
            f"{formatear_numero(pais['superficie']):<18}"
            f"{pais['continente']:<15}"
        )


# ------------------------------------------------------------
# Muestra el menú principal del sistema.
# ------------------------------------------------------------


def mostrar_menu():
    print("\n---------------------------------")
    print("GESTIÓN DE DATOS DE PAÍSES")
    print("---------------------------------")
    print("1. Mostrar países")
    print("2. Agregar país")
    print("3. Actualizar país")
    print("4. Buscar país")
    print("5. Filtrar países")
    print("6. Ordenar países")
    print("7. Mostrar estadísticas")
    print("8. Salir")


# ------------------------------------------------------------
# Función principal del programa.
# ------------------------------------------------------------


def main():
    paises = cargar_paises_desde_csv(ARCHIVO_PAISES)

    while True:
        mostrar_menu()

        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                mostrar_paises(paises)
                input("\nPresioná Enter para continuar...")

            elif opcion == 2:
                agregar_pais(paises)
                input("\nPresioná Enter para continuar...")

            elif opcion == 3:
                actualizar_pais(paises)
                input("\nPresioná Enter para continuar...")

            elif opcion == 4:
                buscar_pais(paises)
                input("\nPresioná Enter para continuar...")

            elif opcion == 5:
                filtrar_paises(paises)

            elif opcion == 6:
                ordenar_paises(paises)

            elif opcion == 7:
                mostrar_estadisticas(paises)
                input("\nPresioná Enter para continuar...")

            elif opcion == 8:
                print("Gracias por utilizar el sistema.")
                break

            else:
                print("Error: debe ingresar una opción entre 1 y 8.")

        except ValueError:
            print("Error: debe ingresar un número entero válido.")


# ------------------------------------------------------------
# Punto de entrada del programa
# ------------------------------------------------------------

if __name__ == "__main__":
    main()
