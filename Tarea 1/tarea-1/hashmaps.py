mapa_ciudades = {
    "Mexico": ["Monterrey", "Guadalajara", "CDMX"],
    "EUA": ["Los Angeles", "Nueva York", "Austin"],
    "Canada": ["Calgary", "Vancouver", "Toronto"]
}

print()
print("Diccionario completo: \n", mapa_ciudades.items(), "\n")
print("Llaves del diccionario: ", mapa_ciudades.keys(), "\n")
print("Valores del diccionario: ", mapa_ciudades.values(), "\n")

print("Diccionario con formato:")
for pais in mapa_ciudades:
    print(f"País: {pais}, ciudades: {(", ".join(mapa_ciudades[pais]))}.")