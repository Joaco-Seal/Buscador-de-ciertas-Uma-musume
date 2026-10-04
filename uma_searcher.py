# ============================================================
# UMA MUSUME - Buscador de aptitud/Dist
# ============================================================

UMA_MUSUME = {

    "special week": {
        "pista": {
            "Turf": "A",
            "Dirt": "G"
        },
        "distancia": {
            "Sprint": "F",
            "Mile": "C",
            "Medium": "A",
            "Long": "A"
        },
        "estilo": {
            "Front Runner": "C",
            "Pace Chaser": "A",
            "Late Surger": "B",
            "End Closer": "C"
        }
    },

    "silence suzuka": {
        "pista": {
            "Turf": "A",
            "Dirt": "G"
        },
        "distancia": {
            "Sprint": "D",
            "Mile": "A",
            "Medium": "A",
            "Long": "E"
        },
        "estilo": {
            "Front Runner": "A",
            "Pace Chaser": "D",
            "Late Surger": "G",
            "End Closer": "G"
        }
    },

    "tokai teio": {
        "pista": {
            "Turf": "A",
            "Dirt": "G"
        },
        "distancia": {
            "Sprint": "E",
            "Mile": "C",
            "Medium": "A",
            "Long": "B"
        },
        "estilo": {
            "Front Runner": "D",
            "Pace Chaser": "A",
            "Late Surger": "C",
            "End Closer": "E"
        }
    },

    "mejiro mcqueen": {
        "pista": {
            "Turf": "A",
            "Dirt": "G"
        },
        "distancia": {
            "Sprint": "G",
            "Mile": "F",
            "Medium": "B",
            "Long": "A"
        },
        "estilo": {
            "Front Runner": "B",
            "Pace Chaser": "A",
            "Late Surger": "D",
            "End Closer": "G"
        }
    },

    "gold ship": {
        "pista": {
            "Turf": "A",
            "Dirt": "G"
        },
        "distancia": {
            "Sprint": "G",
            "Mile": "C",
            "Medium": "A",
            "Long": "A"
        },
        "estilo": {
            "Front Runner": "G",
            "Pace Chaser": "G",
            "Late Surger": "B",
            "End Closer": "A"
        }
    },

    "daiwa scarlet": {
        "pista": {
            "Turf": "A",
            "Dirt": "F"
        },
        "distancia": {
            "Sprint": "B",
            "Mile": "A",
            "Medium": "A",
            "Long": "B"
        },
        "estilo": {
            "Front Runner": "A",
            "Pace Chaser": "A",
            "Late Surger": "E",
            "End Closer": "G"
        }
    },

    "vodka": {
        "pista": {
            "Turf": "A",
            "Dirt": "F"
        },
        "distancia": {
            "Sprint": "C",
            "Mile": "A",
            "Medium": "A",
            "Long": "F"
        },
        "estilo": {
            "Front Runner": "B",
            "Pace Chaser": "A",
            "Late Surger": "B",
            "End Closer": "F"
        }
    },

    "rice shower": {
        "pista": {
            "Turf": "A",
            "Dirt": "G"
        },
        "distancia": {
            "Sprint": "G",
            "Mile": "F",
            "Medium": "B",
            "Long": "A"
        },
        "estilo": {
            "Front Runner": "B",
            "Pace Chaser": "A",
            "Late Surger": "C",
            "End Closer": "G"
        }
    },

    "symboli rudolf": {
        "pista": {
            "Turf": "A",
            "Dirt": "G"
        },
        "distancia": {
            "Sprint": "E",
            "Mile": "C",
            "Medium": "A",
            "Long": "A"
        },
        "estilo": {
            "Front Runner": "B",
            "Pace Chaser": "A",
            "Late Surger": "A",
            "End Closer": "B"
        }
    },

    "maruzensky": {
        "pista": {
            "Turf": "A",
            "Dirt": "B"
        },
        "distancia": {
            "Sprint": "A",
            "Mile": "A",
            "Medium": "B",
            "Long": "C"
        },
        "estilo": {
            "Front Runner": "A",
            "Pace Chaser": "B",
            "Late Surger": "D",
            "End Closer": "G"
        }
    }
}


def limpiar_nombre(nombre):
    return " ".join(nombre.lower().strip().split())


def mostrar_uma(nombre, datos):

    print("\n" + "=" * 50)
    print(f" {nombre.title()}")
    print("=" * 50)

    print("\n️ Aptitud de pista")
    print("-" * 30)

    for pista, rango in datos["pista"].items():
        print(f"{pista:<10}: {rango}")

    print("\n Aptitud Por Distancia")
    print("-" * 30)

    for distancia, rango in datos["distancia"].items():
        print(f"{distancia:<10}: {rango}")

    print("\n Estilo de carrera")
    print("-" * 30)

    for estilo, rango in datos["estilo"].items():
        print(f"{estilo:<18}: {rango}")

    print("\n Mejores Distancias")

    mejores = []

    for distancia, rango in datos["distancia"].items():
        if rango == "A":
            mejores.append(distancia)

    if mejores:
        print("   " + ", ".join(mejores))
    else:
        print("   No tiene una distancia con rango A.")

    print("=" * 50)


def buscar_uma():

    nombre = input("\n🔎 Escribe el nombre de la Uma Musume: ")
    nombre = limpiar_nombre(nombre)

    if nombre in UMA_MUSUME:
        mostrar_uma(nombre, UMA_MUSUME[nombre])
        return

    print("\n No encontré esa Uma Musume.")

    coincidencias = []

    for uma in UMA_MUSUME:
        if nombre in uma or uma in nombre:
            coincidencias.append(uma)

    if coincidencias:

        print("\n¿Quizás quisiste decir?")

        for uma in coincidencias:
            print(f"  • {uma.title()}")

    else:

        print("\n Personajes disponibles:")

        for uma in sorted(UMA_MUSUME):
            print(f"  • {uma.title()}")


def listar_umas():

    print("\n" + "=" * 50)
    print(" Umas Disponibles")
    print("=" * 50)

    for numero, nome in enumerate(sorted(UMA_MUSUME), 1):
        print(f"{numero:>2}. {nome.title()}")

    print("=" * 50)


def buscar_por_distancia():

    print("\n Distancias")
    print("1. Sprint")
    print("2. Mile")
    print("3. Medium")
    print("4. Long")

    opcion = input("\nSelecciona una distancia: ")

    distancias = {
        "1": "Sprint",
        "2": "Mile",
        "3": "Medium",
        "4": "Long"
    }

    if opcion not in distancias:
        print("\n Opción inválida.")
        return

    distancia = distancias[opcion]

    print(f"\n Uma Musume aptas para {distancia}")
    print("=" * 50)

    resultados = []

    for nome, datos in UMA_MUSUME.items():

        rango = datos["distancia"][distancia]

        if rango in ["A", "B", "C"]:
            resultados.append((nome, rango))

    if not resultados:
        print("No se encontraron resultados.")
        return

    for nome, rango in sorted(resultados):
        print(f"• {nome.title():<25} {rango}")

    print("=" * 50)


def mostrar_menu():

    while True:

        print("\n")
        print(" 1.  Buscar Uma Musume                   ")
        print(" 2.  Mostrar todas                        ")
        print(" 3.  Buscar por distancia                 ")
        print(" 4.  Salir                                ")
        print("══════════════════════════════════════════")

        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            buscar_uma()

        elif opcion == "2":
            listar_umas()

        elif opcion == "3":
            buscar_por_distancia()

        elif opcion == "4":
            print("\n ¡Hasta luego!")
            break

        else:
            print("\n ¡Opción inválida!")


if __name__ == "__main__":
    mostrar_menu()
    
