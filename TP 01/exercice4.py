number = int(input("Donnez le nombre de secondes : "))

number_en_heure = number // 3600
number_en_minute = (number % 3600) // 60
number_en_seconds = (number % 60)

print(f"{number} sec = {number_en_heure} h {number_en_minute} min {number_en_seconds} s")
