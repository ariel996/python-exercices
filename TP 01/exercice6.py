a = int(input("Donnez le nombre 1 : "))
b = int(input("Donnez le nombre 2 : "))

if (a > 0 and b > 0) or (a < 0 and b < 0):
    print("Le produit est positif")
elif a == 0 or b == 0:
    print("Le produit est nul")
else:
    print("Le produit est négatif")
