import random
noslepanais_skaitlis=random.randint(1,50)
uzminets=False

print("Es izvēlējos skaitli no 1 līdz 50. Tev ir 5 mēģinājumi!")

for meginajums in range(1,6):
    skaitlis=int(input(f"{meginajums}.mēģinājums. Ievadi skaitli:"))

    if skaitlis==noslepanais_skaitlis:
        print("Apsveicu! Tu uzminēji skaitli!")
        uzminets=True
        break
    elif skaitlis<noslepanais_skaitlis:
        print("Meklētais skaitlis ir lielāks.")
    else:
        print("Meklētais skaitlis ir mazāks.")

if not uzminets:
    print("Mēģinājumi beidzās! Noslēptais skaitlis bija", noslepanais_skaitlis)