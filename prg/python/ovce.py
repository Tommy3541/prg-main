import random

def animals(n):
    if n > 10:
        cislo_ruzova_ovce = random.randint(1, n)
    for cislo_ovce in range(n):
        if cislo_ovce == cislo_ruzova_ovce:
            print("ruzova ovce")
        else:
            print("ovce")
    print("pes")

animals(15)