import random
zvire = [
    "Capybara", "Pferd", "Pes", "Kocka", "Lenochod" 
]

vec = [
    "brambora", "spalovací motor", "kost", "hůl", "Vicodin" 
]

sloveso = [
    "běžel", "říkal", "skákal", "šel", "psal" 
]

aktivita = [
    "lezl", "spal", "procházel", "hrál", "vyprazdňoval" 
]

for cislo in range(3):
        nahodne_cislo1 = random.randint(0, 4)
        nahodne_cislo2 = random.randint(0, 4)
        nahodne_cislo3 = random.randint(0, 4)
        nahodne_cislo4 = random.randint(0, 4)
        print(f"Prisel jsem pozde, protoze {zvire[nahodne_cislo1]} {sloveso[nahodne_cislo2]} muj/moji {vec[nahodne_cislo3]} zatimco jsem {aktivita[nahodne_cislo4]}")

print(f"Prisel jsem pozde, protoze {len(f"{zvire[nahodne_cislo1]} {sloveso[nahodne_cislo2]} muj/moji {vec[nahodne_cislo3]} zatimco jsem {aktivita[nahodne_cislo4]}")}")

x = len(f"{zvire[nahodne_cislo1]} {sloveso[nahodne_cislo2]} muj/moji {vec[nahodne_cislo3]} zatimco jsem {aktivita[nahodne_cislo4]}")

if x > 50:
    print("💩")
elif x > 45:
    print("❤️")
else:
    print("🤬")
