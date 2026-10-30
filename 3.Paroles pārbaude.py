parole=input("Ievadi paroli:")

ir_pietiekami_gara=len(parole)>=8
ir_cipars=any(simbols.isdigit() for simbols in parole)

if ir_pietiekami_gara and ir_cipars:
    print("Parole ir droša!")
else:
    print("Parole nav pietiekami droša.")
    if not ir_pietiekami_gara:
        print("Parolei jābūt vismaz 8 simbolus garai.")
    if not ir_cipars:
        print("Parolē jābūt vismaz vienam ciparam.")
        