L1 = [1, 3, 6, 78, 35, 88, 55]
L2 = [12, 24, 35, 24, 88, 120, 155]
L3 = []

for element in L1:
  if element in L2 and element not in L3:
    L3.append(element)

print("Intersection des listes L1 et L2 :", L3)
