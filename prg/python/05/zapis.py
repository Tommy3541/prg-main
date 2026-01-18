seznam = ["ciao", "guten tag", "bonjour"]

# "w" - prepise cely soubor, "a" dopise do souboru
with open("ukazka2.txt", "w", encoding="utf-8") as soubor:
    soubor.write("Ahoj!\n")
    soubor.write("Bye!\n")
    #soubor.writelines(seznam)
    for radek in seznam:
        soubor.write(radek + "\n")