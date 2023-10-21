L = [1, 3, 5, 7, 9]
val = int(input("Donner un nombre : "))

index = 0
while index < len(L) and L[index] < val:
    index += 1

L.insert(index, val)

print(f"L = {L}")