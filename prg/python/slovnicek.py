#slovnik je soubor zparovanych klicu a hodnot
telefonni_seznam = {
    "emil": "123 456 789",
    "andela": "987 654 321",
    "kvido": "147 258 369",
}

print(telefonni_seznam["andela"])

cat = {
    "jmeno": "garfield",
    "vek": 15,
    "barva": "oranzova",
    "zije": True,
    "oblibene_jidlo": "lasagne",
    "kamaradi": ["pes", "dalsi kocka", "kuchar"]
}

print(cat)
print(cat["barva"])
print(cat["kamaradi"][2])

for key in cat:
    print(key)

for key, hodnota in cat.items():
    print(f"klicek {key}, hodnota {hodnota}")

for key in cat:
    print(cat[key])

for hodnota in cat.values():
    print(hodnota)

for kamarad in cat["kamaradi"]:
    print(kamarad)

cat["klubko"] = "6m"

print(cat)

cat["vek"] = 16

print(cat["vek"])

if "oblibene_jidlo" in cat:
    print("ma oblibene jidlo") #najit v seznamu nebo tak
