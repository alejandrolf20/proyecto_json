import os
import json

ruta = os.path.join(os.path.dirname(__file__), 'pokemon.json')
with open(ruta) as file:
    data = json.load(file)

def menu():
    print("Introduce un número del siguiente menú para acceder a la opción deseada.")
    print("-------------------------------------------------------------------")
    print("1. Listar todos los Pokémon presentes en la Pokédex")
    print("2. Mostrar las debilidades de los Pokémon")
    print("3. Buscar los Pokémon por su tipo")
    print("4. Buscar información relacionada a las evoluciones de un Pokémon")
    print("5. Mostrar información detallada de un Pokémon")
    print("6. Salir de la Pokédex")
    print("-------------------------------------------------------------------")
    opcion = int(input("Opción deseada: "))
    return opcion

def listar_pokemon():
    pokemon_list = data["pokemon"]
    for pokemon in pokemon_list:
        print(f"{pokemon['id']}. {pokemon['Nombre']}")

def contar_debilidad_por_tipo(tipo):
    try:
        debilidades = []

        for pokemon in data["pokemon"]:
            if tipo.lower() in [debilidad.lower() for debilidad in pokemon.get("weaknesses", [])]:
                debilidades.append(pokemon["Nombre"])

        print(f"Total de Pokémon con debilidad al tipo '{tipo}': {len(debilidades)}")
        if debilidades:
            print("Pokémon con debilidad al tipo:")
            for nombre in debilidades:
                print("-", nombre)
        return len(debilidades)
    except Exception as e:
        print(f"Error al contar las debilidades de los Pokémon al tipo '{tipo}': {str(e)}")
        return 0
  
def buscar_por_tipo(tipo):
    tipo = tipo.capitalize()
    pokemon_list = data["pokemon"]
    pokemon_tipo = [pokemon['Nombre'] for pokemon in pokemon_list if tipo in pokemon['type']]
    return pokemon_tipo

def buscar_info_relacionada(nombre_pokemon):
    pokemon_list = data["pokemon"]
    for pokemon in pokemon_list:
        if pokemon['Nombre'].lower() == nombre_pokemon.lower():
            print(f"Nombre: {pokemon['Nombre']}")
            print(f"Evolución Previa: {pokemon.get('prev_evolution', 'Ninguna')}")
            print(f"Evolución Posterior: {pokemon.get('next_evolution', 'Ninguna')}")
            return
    print("El Pokémon no se encuentra en la Pokédex.")

def informacion_pokemon(nombre_pokemon):
    pokemon_list = data["pokemon"]
    for pokemon in pokemon_list:
        if pokemon['Nombre'].lower() == nombre_pokemon.lower():
            print(f"Nombre: {pokemon['Nombre']}")
            print(f"Número en la Pokédex: {pokemon['id']}")
            print(f"Tipo: {pokemon['type']}")
            print(f"Debilidades: {pokemon.get('weaknesses', 'Ninguna')}")
            print(f"Altura: {pokemon.get('height', 'Desconocida')}")
            print(f"Peso: {pokemon.get('weight', 'Desconocido')}")
            print(f"Evolución Previa: {pokemon.get('prev_evolution', 'Ninguna')}")
            print(f"Evolución Posterior: {pokemon.get('next_evolution', 'Ninguna')}")
            return
    print("El Pokémon no se encuentra en la Pokédex.")