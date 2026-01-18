#def pozdrav(jmeno1, jmeno2, jmeno3): #funkce
#   print("ahoj", jmeno1)
#   print("hi", jmeno2)
#   print("salamalaikum", jmeno1)
#   print("bismillah", jmeno3)

#pozdrav("mohi", "profi", "damian")
#pozdrav("sobeslav", "zlomysl", "ivo")

zadani = int(input("zadej km: "))

def metr(km):
    mile = km * 0.62
    return mile

vysledek = metr(zadani)

print(zadani, "km je", vysledek, "mil")

print(f"{zadani}km je {vysledek} mil") #string na vypsani
