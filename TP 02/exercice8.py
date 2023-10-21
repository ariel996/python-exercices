liste = [7, 9, 1, 3, 5, 2, 7, 4, 8, 9, 4, 9]

n = int(input("Entrez le nombre que vous souhaitez rechercher : "))

occurrences = []
indices = []

for i in range(len(liste)):
  if liste[i] == n:
    occurrences.append(i)
    indices.append(i) 

if len(occurrences) == 0:
  print(f"Le nombre {n} n'a pas été trouvé dans la liste.")
else:
  print("Le nombre", n, "a été trouvé", len(occurrences), "fois aux indices:", indices)
