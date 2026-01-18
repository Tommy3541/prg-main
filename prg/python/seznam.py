jmena = [
    "Jan", "Eva", "Tomáš", "Lucie", "David", "Anna", 
    "Jakub", "Petra", "Martin", "Michaela", "Ondřej", 
    "Tereza", "Pavel", "Klára", "Radek", "Veronika", 
    "Karel", "Jitka", "Vojtěch", "Barbora"
]

print(jmena[2]) #pocitani (od 0 takze 0, 1, 2)
print(jmena[-1], jmena[-3])
print(jmena[1:4]) #ne vcetne
print(jmena[:11])
print(jmena[10:])

jmena.append("radek") #pridat
print(jmena)

jmena[2] = "emil" #prejmenovat
print(jmena)

jmena.insert(0, "max") #vlozit na konec
print(jmena)

delete_value = jmena.pop(4) #odstraniut
print(jmena)
print(f"odebral jsem {delete_value}")

jmena.remove("Pavel") #odebrat konkretne
print(jmena)

for i, jmeno in enumerate(jmena):
    print(f"{i+1}. {jmeno}")

student = {"jmeno":"Jarmil", "prijmeni":"bayinga"}