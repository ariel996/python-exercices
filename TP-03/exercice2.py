import math

def delta(a,b,c):
  return pow(b,2) - 4*a*c

def NombreRacine(a,b,c):
  d = delta(a,b,c)
  if(d>0):
    return 2
  elif(d==0):
    return 1
  else:
    return 0

def AfficheNombreRacine(a,b,c):
  print(NombreRacine(a,b,c))

def Racine1(a,b,c):
  return (-b-math.sqrt(delta(a,b,c)))/(2*a)

def Racine2(a,b,c):
  return (-b+math.sqrt(delta(a,b,c)))/(2*a)

def conversion_temps(h, m, s):
  return h*3600 + m*60 + s

def conversion_distance(km, m, cm):
  if(cm == 0):
    return km*1000 + m
  else:
    return km*1000 + m + cm/100
  
def vitesse(km, m, cm, h, min, s): 
  return conversion_distance(km, m, cm) - conversion_temps(h, min, s)

print(f"le temps écoulé entre 1h 32min 45s et 0h 55min 10s (en secondes) est : {conversion_temps(1,32,45)-conversion_temps(0,55,10)}")