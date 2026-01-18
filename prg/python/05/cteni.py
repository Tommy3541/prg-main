with open("ukazka.txt", "r", encoding="utf-8") as soubor:
    #obsah = soubor.read()
    #obsah = soubor.read().splitlines()
    obsah = soubor.readlines()

print(obsah)
print(obsah[1].strip()) #strip vymaze neviditelny znaky ze stringu

for radek in obsah:
    print(radek.strip())

