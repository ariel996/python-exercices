def euro_to_mad(euro):
  return euro * 10.86

def mad_to_euro(mad):
  return mad * 0.092

choix = input("Choisissez la direction de conversion (euro-mad ou mad-euro) : ").lower()

valeurs = []

while True:
  valeur = float(input("Saisissez une valeur (nombre négatif pour arrêter) : "))
  if valeur < 0:
    break
  valeurs.append(valeur)

converted_valeurs = []

for valeur in valeurs:
  if choix == "euro-mad":
    converted_valeurs.append(euro_to_mad(valeur))
  elif choix == "mad-euro":
    converted_valeurs.append(mad_to_euro(valeur))

print("Valeurs converties :")
for i in range(len(valeurs)):
  print(f"{valeurs[i]} {'euro' if choix == 'euro-mad' else 'mad'} = {converted_valeurs[i]} {'euro' if choix == 'mad-euro' else 'mad'}")
