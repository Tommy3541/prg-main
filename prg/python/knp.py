import random

zadani = input("zadej kamen, nuzky nebo papir :")
print(zadani)

pocitac = random.randint(1, 3)
print(pocitac)

if zadani == "papir":
    clovek = 1
if zadani == "nuzky":
    clovek = 2
if zadani == "kamen":
    clovek = 3

if pocitac == 1 and clovek == 2:
    print("clovek vyhral")
if pocitac == 1 and clovek == 3:
    print("pocitac vyhral")
if pocitac == 2 and clovek == 1:
    print("pocitac vyhral")
if pocitac == 2 and clovek == 3:
    print("clovek vyhral")
if pocitac == 3 and clovek == 2:
    print("pocitac vyhral")
if pocitac == 3 and clovek == 1:
    print("clovek vyhral")
if pocitac == 1 and clovek == 1:
    print("remiza")
if pocitac == 2 and clovek == 2:
    print("remiza")
if pocitac == 3 and clovek == 3:
    print("remiza")