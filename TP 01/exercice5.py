def pair_detector(n):
  if(n%2 == 0):
    return "Ce nombre est pair"
  elif (n%3 == 0):
    return "Ce nombre est impair, mais est multiple de 3"
  else:
    return "Ce nombre n'est ni pair ni multiple de 3"



print(pair_detector(11))
