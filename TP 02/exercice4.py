L = [1, -30, 0, -2, 500, 4, 2, 100]
M = []

i = 0
for n in L:
  if n < 0:
    M.insert(i, n)
    i += 1
  else:
    M.append(n)

print(M)
