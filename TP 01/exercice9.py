nbr_articles = 2
tva = 0.2
total_facture = 0
articles = []
quantity = []
prix = []


for i in range(1,nbr_articles+1):
  articles.append(input(f"Donner le nom du {i} article : "))
  quantity.append(int(input(f"Donner la quantity du {i} article : ")))
  prix.append(float(input(f"Donner le prix unitaire du {i} article : ")))

for i in range(0,nbr_articles):
  p = prix[i]*quantity[i]
  total_facture += p+ p*tva
  print(f"Total de l'article {articles[i]} : {p} dh (ht)")

print(f"Le total de votre facture est : {total_facture} (TTC)")

