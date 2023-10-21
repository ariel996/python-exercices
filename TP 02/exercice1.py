n = int(input("Donner n : "))

somme = 0
chiffres = [n, n*10 + n, n*10 + n, n*1000 + n*100 + n*10 + n]

for chiffre in chiffres:
  print(chiffre)
  somme += chiffre

print(f"La somme est : {somme}")