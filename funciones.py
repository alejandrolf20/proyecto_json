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
    total_pokemon_tipo = len(pokemon_tipo)
    nombres_pokemon_tipo = ", ".join(pokemon_tipo)
    return f"Total de Pokémon de tipo {tipo}: {total_pokemon_tipo}\nPokémon: {nombres_pokemon_tipo}"


def buscar_info_relacionada(nombre_pokemon):
    pokemon_list = data["pokemon"]
    for pokemon in pokemon_list:
        if pokemon['Nombre'].lower() == nombre_pokemon.lower():
            evolucion_previa = pokemon.get('prev_evolution', 'Ninguna')
            evolucion_posterior = pokemon.get('next_evolution', 'Ninguna')
            
            evolucion_previa_str = ", ".join([f"{evo['Número']} - {evo['Nombre']}" for evo in evolucion_previa]) if isinstance(evolucion_previa, list) else evolucion_previa
            
            evolucion_posterior_str = ", ".join([f"{evo['Número']} - {evo['Nombre']}" for evo in evolucion_posterior]) if isinstance(evolucion_posterior, list) else evolucion_posterior
            
            return f"Nombre: {pokemon['Nombre']}\nEvolución Previa: {evolucion_previa_str}\nEvolución Posterior: {evolucion_posterior_str}"
    return "El Pokémon no se encuentra en la Pokédex."

def informacion_pokemon(data, nombre_pokemon):
    pokemon_list = data["pokemon"]
    for pokemon in pokemon_list:
        if pokemon['Nombre'].lower() == nombre_pokemon.lower():
            nombre = pokemon['Nombre']
            numero_pokedex = pokemon['id']
            tipo_actual = [t.lower() for t in pokemon['type']]
            tipo = ", ".join(pokemon['type'])
            debilidades = ", ".join(pokemon.get('weaknesses', ['Ninguna']))
            altura = pokemon.get('height', 'Desconocida')
            peso = pokemon.get('weight', 'Desconocido')
            pokemon_mismo_tipo = [p for p in pokemon_list if all(tipo in [t.lower() for t in p['type']] for tipo in tipo_actual) and p['Nombre'].lower() != nombre_pokemon.lower()]
            total_tipo = len(pokemon_mismo_tipo)
            nombres_tipo = ", ".join([p['Nombre'] for p in pokemon_mismo_tipo])
            
            evolucion_previa = pokemon.get('prev_evolution', 'Ninguna')
            evolucion_posterior = pokemon.get('next_evolution', 'Ninguna')
            if isinstance(evolucion_previa, list):
                evolucion_previa = ", ".join([f"{evo['Número']} - {evo['Nombre']}" for evo in evolucion_previa])
            if isinstance(evolucion_posterior, list):
                evolucion_posterior = ", ".join([f"{evo['Número']} - {evo['Nombre']}" for evo in evolucion_posterior])
            
            return f"Nombre: {nombre}\nNúmero en la Pokédex: {numero_pokedex}\nTipo: {tipo}\nDebilidades: {debilidades}\nAltura: {altura}\nPeso: {peso}\nEvolución Previa: {evolucion_previa}\nEvolución Posterior: {evolucion_posterior}\nPokémon del mismo tipo ({tipo}): {total_tipo}\n{nombres_tipo}"
    return "El Pokémon no se encuentra en la Pokédex."
