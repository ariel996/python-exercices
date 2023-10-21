L1 = [1, 2, 3, 4, 5, 1, 1, 2, 3]
L2 =[]

n = int(input("Choisissez un nombre à supprimer : "))

for nombre in L1:
  if nombre != n:
    L2.append(nombre)

print(L2)
