x = float(input("Donner nombre 1 : "))
y = float(input("Donner nombre 2 : "))
oper = input("Donner  l'operation: ")

if(oper == "+"):
    print(f"{x} + {y} = {x+y}")
elif(oper == "-"):
  print(f"{x} - {y} = {x-y}")
elif(oper == "*"):
  print(f"{x} * {y} = {x*y}")
elif(oper == "/"):
  if(y==0):
    print("Impossible de division par zero")
  else:
    print(f"{x} / {y} = {x/y}")
else:
  print("Operation Impossible (choisir parmi : + , - , * et /)")

