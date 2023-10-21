import random

print("####################################################")
print("#####      ON VA JOUR UN PETIT JEU             #####")
print("##### JE VOUS GENERER UN NOMBRE ENTRE 1 ET 100 #####")
print("#####    ET TU VAS LE DEVENEZ EN 7 ESSAIS      #####")
print("####################################################")
print("####################################################")

number_generated = random.randint(1,101)

for i in range(1,8):
  number = int(input("Entrer un nombre : "))
  if(number > 100 or number < 0):
    print("OUPS , vous avez choisi un nomber en dehors de l'entervallle!")
  
  elif(number > number_generated):
    print("Oups, entrer un nombre plus petit")

  elif(number < number_generated):
    print("Oups, entrer un nombre plus grad")

  elif(number == number_generated):
    print(f"Bravo, {number_generated} est le nombre qui j'ai choisit")
    print(f"vous l'avez devine {8-i} essais")
    break;

if(i == 7):
  print("J'ai gange, je suis le MEILLEU")
  print(f"Le nombre que j'ai devine est {number_generated}")
  print("Au revoir")