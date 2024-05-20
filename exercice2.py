import csv

def pokémons_csv(fichier):
    attribues_pokemon = {}
    with open(fichier, newline='') as fichier_csv:
        lecteur = csv.reader(fichier_csv)
        for ligne in lecteur:
            nom_pokemon = ligne[0]
            attribues = [int(attribue) for attribue in ligne[1:]]
            attribues_pokemon[nom_pokemon] = attribues
    return attribues_pokemon


fichier = 'pokemon.csv'
pkmn = pokémons_csv(fichier)
for nom, attribues in pkmn.items():
    print(f"{nom}: {attribues}")

pkmn = pokémons_csv(fichier)
print(isinstance(pkmn, dict))
print(isinstance(pkmn["Pikachu"], list))
print(isinstance(pkmn["Pikachu"][0], int))



