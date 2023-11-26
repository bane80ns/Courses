izbor = input("Izaberite sta zelite da pretvarate:\n\ta - celzijusi u farenhajte\n\te - farenhajte u celzijuse\n\t: ").lower()
if izbor == "a":
    celzijusi = float(input("Unesite temperaturu u Celzijusima: "))
    farenhajti = 1.8*celzijusi+32
    print("Temperatura u celzijusima: ",celzijusi)
    print("Temperatura u farenhajtima: ",farenhajti)
elif izbor == "e":
    farenhajti = float(input("Unesite temperaturu u Farenhajtima: "))
    celzijusi = (farenhajti-32)/1.8
    print("Temperatura u celzijusima: ",celzijusi)
    print("Temperatura u farenhajtima: ",farenhajti)

else:
    print("Uneli ste pogresno slovo.")