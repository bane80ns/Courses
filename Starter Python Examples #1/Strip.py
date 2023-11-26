# Using .lstrip or .rightstrip method, for striping part of string variable

dan = input("Unesite dan: ").lstrip("0")
mesec = input("Unesite mesec: ").lstrip("0")
godina = input("Unesite godinu: ")

datum = dan+"."+mesec+"."+godina+"."
print(datum)