import requests

# Obtenemos el fichero JSON de la web:
response = requests.get("https://pokeapi.co/api/v2/pokemon/1/")
pokemon_data = response.json()

# Función 1: Listar nombre, peso y altura.
def listar_info():
    print("Nombre:", pokemon_data["name"])
    print("Peso:", pokemon_data["weight"])
    print("Altura:", pokemon_data["height"])

# Función 2: Contar tipos de Pokemon.
def contar_tipos():
    print("Hay", len(pokemon_data["types"]), "tipos de Pokemon.")

# Función 3: Buscar información sobre un movimiento.
def buscar_movimiento():
    movimiento = input("Introduce el nombre de un movimiento: ")
    for move in pokemon_data["moves"]:
        if move["move"]["name"] == movimiento:
            print("Efecto:", move["effect_entries"][0]["short_effect"])
            print("Potencia:", move["power"])
            print("Precisión:", move["accuracy"])
            return
    print("No se encontró información sobre ese movimiento.")

# Función 4: Buscar información sobre tipos de Pokemon débiles contra el tipo del Pokemon.
def buscar_debilidades():
    tipo_pokemon = pokemon_data["types"][0]["type"]["name"]
    response = requests.get(f"https://pokeapi.co/api/v2/type/{tipo_pokemon}")
    type_data = response.json()
    debilidades = [t["name"] for t in type_data["damage_relations"]["double_damage_from"]]
    print("Los siguientes tipos de Pokemon son débiles contra", tipo_pokemon + ":")
    print(", ".join(debilidades))

# Función 5: Mostrar información del siguiente Pokemon en la Pokédex-
def siguiente_pokemon():
    siguiente_id = pokemon_data["id"] + 1
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{siguiente_id}/")
    if response.status_code == 404:
        print("No hay Pokemon siguiente en la Pokédex.")
        return
    siguiente_pokemon_data = response.json()
    print("Nombre:", siguiente_pokemon_data["name"])
    print("Peso:", siguiente_pokemon_data["weight"])
    print("Altura:", siguiente_pokemon_data["height"])
    print("Tipos:", ", ".join([t["type"]["name"] for t in siguiente_pokemon_data["types"]]))

def menu():
    while True:
        print("\n*** Menú ***")
        print("1. Listar nombre, peso y altura del Pokemon")
        print("2. Contar tipos de Pokemon")
        print("3. Buscar información sobre un movimiento")
        print("4. Buscar información sobre tipos de Pokemon débiles")
        print("5. Mostrar información del siguiente Pokemon en la Pokédex")
        print("0. Salir")
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            listar_info()
        elif opcion == "2":
            contar_tipos()
        elif opcion == "3":
            buscar_movimiento()
        elif opcion == "4":
            buscar_debilidades()
        elif opcion == "5":
            siguiente_pokemon()
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
