notes = []
coefs = []
somme = 0

for i in range(1,5):
  notes.append(float(input(f"note {i} : ")))
  coefs.append(float(input(f"coefficient {i} : ")))

for i in range(0,4):
  somme += notes[i]*coefs[i]

moyenne = somme/10

if(moyenne >= 10):
  print(f"moyenne de ces 4 notes : {somme}, semestre validé")
elif(moyenne > 7 and moyenne < 10):
  print(f"moyenne de ces 4 notes : {somme}, semestre rattrapage")
else:
  print(f"moyenne de ces 4 notes : {somme}, semestre non validé")


