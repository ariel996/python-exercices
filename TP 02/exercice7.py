L = [1, 2, 5, 8, 6, 2, 5, 9, 1, 8, 8]

for valeur in L:
  while L.count(valeur) > 1:
    L.remove(valeur)

L.sort()
print(L)
