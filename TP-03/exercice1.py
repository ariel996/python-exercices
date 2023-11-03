def somme(n, m):
  s = 0
  for i in range(n,m+1):
    s += i
  return s


x = int(input("Donner n = "))
y = int(input("Donner m (m>n) = "))
print(f"somme({x},{y}) donne {somme(x,y)}")