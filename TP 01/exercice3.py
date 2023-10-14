distance = float(input(("Donnez la distance en kilometre : ")))
temps = float(input(("Donnez le temps en minute : ")))

vitesse = (distance * 1000) / (temps*60)

print (f"La vitesse est : {vitesse}")
