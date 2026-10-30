teikums=input("Ievadi teikumu: ")
vardi=teikums.split()

print("Vārdu skaits:", len(vardi))

if len(vardi)>0:
    garakais_vards=max(vardi, key=len)
    print("Garākais vārds:", garakais_vards)
else:
    print("Teikumā nav vārdu.")