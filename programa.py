from funciones import *

print("¡Bienvenido a la Pokédex!")
print("-------------------------------------------------------------------")
opcion = menu()
while opcion != 6:
    if opcion == 1:
        print("\nLista de Pokémon:")
        listar_pokemon()
    elif opcion == 2:
        tipo = input("Introduce el tipo de Pokémon para contar su debilidad: ")
        contar_debilidad_por_tipo(tipo)
    elif opcion == 3:
        tipo = input("\nIngrese el tipo de Pokémon que desea buscar: ")
        pokemon_tipo = buscar_por_tipo(tipo)
        print(f"\nPokémon del tipo {tipo.capitalize()}: {pokemon_tipo}")
    elif opcion == 4:
        nombre_pokemon = input("Ingrese el nombre del Pokémon que desea buscar: ")
        informacion_relacionada = buscar_info_relacionada(nombre_pokemon)
        print(informacion_relacionada)
    elif opcion == 5:
        nombre_pokemon = input("Ingrese el nombre del Pokémon del que desea obtener información detallada: ")
        informacion_detallada = informacion_pokemon(data, nombre_pokemon)
        print(informacion_detallada)
    else:
        print("\nOpción inválida. Por favor, ingrese un número válido del menú.")
    
    opcion = menu()
