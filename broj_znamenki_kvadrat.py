while True:
    try:
        broj = int(input("Unesi pozitivan broj: "))
        brojac = 0
    except ValueError:
        print("Pogreška! Nisi unio broj!")
        continue
    else:
        if broj > 0:
            print("Kvadrat pojedinih znamenki broja " + str(broj) + " je: ")
            break
        else:
            print("Pogreška! Unio si broj manji od 1!")

brojevi = [int(i) for i in str(broj)]

for x in reversed(brojevi):
    print(x**2)

print ("\nBroj znamenki: ",len(str(abs(broj))))