choix = input("Triangle de symboles(S) ou Triangle de chiffres(C) (Entrer S ou C) : ")
n = int(input("Entrer un nombre:  "))

if(choix == "S" or choix == "s"):
  for i in range(1,n+1):
    for j in range(1,i+1):
      print("*",end=" ")
    print("")
  
elif(choix == "C" or choix == "c"):
  for i in range(1,n+1):
    for j in range(1,i+1):
      print(i,end=" ")
    print("")
else:
  print("Choisir S ou C")

