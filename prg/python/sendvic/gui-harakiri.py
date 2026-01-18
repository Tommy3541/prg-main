from sys import exit
import datetime as dt
import json
import os
from nicegui import ui, app
from PIL import Image


cas = dt.datetime.now()

zprava = None
obrazek = None
spritesheet = Image.open("prg/python/sendvic/cat.png")

kohout = {}
default_kohout = {}

default_kohoutkohout = {
    "jmeno": "silver",
    "hlad": 50,
    "zizen": 0,
    "vek": 0,
    "zivoty": 100,
    "cistota": 100,
    "barva": "pink",
    "energie": 90,
    "zije": True,
    "nestastnost": False,
    "nemoc": False,
}

def krmeni():
    kohout["hlad"] -= 10
    print(f"{kohout["jmeno"]} vypadá šťastně.\nHlad je {kohout["hlad"]}.")
    zprava.text = (f"{kohout["jmeno"]} vypadá šťastně.\nHlad je {kohout["hlad"]}.")
    ui.notify("mnam")
    obrazek.source = vystrihni_obrazek(4, 59)
    zkontroluj_status()


def zkontroluj_status():
    if kohout["hlad"] > 120 or kohout["hlad"] < -20:
        kohout["zivoty"] -= 10
    
    if kohout["zizen"] > 120 or kohout["zizen"] < -20:
        kohout["zivoty"] -= 10

    if kohout["zivoty"] <= 0:
        kohout["zije"] = False
        print(f"{kohout["jmeno"]} se nedostal do sněmovny. (died)")
        app.shutdown()

    
    starnuti()
    hladoveni()


def hra():
    if kohout["nestastnost"] == True:
        kohout["nestastnost"] = False
        kohout["energie"] -= 10
        kohout["hlad"] -= 10
        kohout["zizen"] -= 10
        print(f"{kohout["jmeno"]} je vic happy, jeho energie je {kohout["energie"]}")
        zprava.text = (f"{kohout["jmeno"]} je vic happy, jeho energie je {kohout["energie"]}")
        ui.notify("hahahahhahahaha")
        obrazek.source = vystrihni_obrazek(2, 64)
        zkontroluj_status()
    else:
        ui.notify("silver je az moc stastny, nechce si hrat")


def insult():
    kohout["nestastnost"] = True
    print(f"{kohout["jmeno"]} je nestastny")
    zprava.text = (f"{kohout["jmeno"]} je nestastny")
    ui.notify("ahsabdfiubfaoihrapirw")
    obrazek.source = vystrihni_obrazek(0, 61)
    zkontroluj_status()

def spanek():
    kohout["energie"] = 100
    print(f"{kohout["jmeno"]} se vyspinkal, jeho energie je {kohout["energie"]}")
    zprava.text = (f"{kohout["jmeno"]} se vyspinkal, jeho energie je {kohout["energie"]}")
    ui.notify("ZzzzzzzzzzzzZzzzzzzzzz")
    obrazek.source = vystrihni_obrazek(0, 45)
    zkontroluj_status()

def hladoveni():
    global cas

    ted = dt.datetime.now()

    if ted > cas + dt.timedelta(seconds=10):
        kohout["hlad"] += 10
        print(f"{kohout["jmeno"]} zacina mit hlad")
        cas = ted

def starnuti():
    global cas

    ted = dt.datetime.now()

    if ted > cas + dt.timedelta(hours=10):
        kohout["vek"] += 1
        print(f"{kohout["jmeno"]} ma narozeniny")
        cas = ted

def status():
    print(f"{kohout["jmeno"]} me energii {kohout["energie"]} \n hlad {kohout["hlad"]} \n zizen {kohout["zizen"]} \n {kohout["jmeno"]} je {"stastny" if kohout["nestastnost"] == False else "nestastny"} \n zije? {kohout["zije"]} \n nemoc {kohout["nemoc"]} \n je stary {kohout["vek"]}")
        
def load():
    # TODO roset hry, kontrola existence save
    global kohout

    if os.path.isfile("sendvic2/tamagoci.json"):
        with open("sendvic2/tamagoci.json", "r", encoding="utf-8") as f:
            kohout = json.load(f)
    else:
        kohout = default_kohout
        save()


def save():
    global kohout
    with open("tamagoci.json", "w", encoding="utf-8") as f:
        json.dump(kohout, f, ensure_ascii=False, indent=4)

def reset():
    global kohout, default_kohout
    kohout = default_kohout
    save()

def vystrihni_obrazek(x, y):
    x = x * 64
    y = y * 64
    return spritesheet.crop((x, y, x + 64, y + 64))

def main():
    global zprava
    global obrazek
    tlacitka = {
        "krmeni": krmeni,
        "hra": hra,
        "spanek": spanek,
        "insult": insult,
    }

    load()

    with ui.element("div").classes("w-full h-screen flex items-center justify-center flex-col gap-5"):
        obrazek = ui.image(vystrihni_obrazek(0, 1)).classes("h-32 w-32")
        zprava = ui.label("vitej")
        with ui.grid(columns=3):
            for jmeno, funkce in tlacitka.items():
                ui.button(jmeno, on_click=funkce)

    print("čau lidi")
    print("""
        |\\---/|
        | o_o |
         \\_^_/
          """)
    hladoveni()

    print(f"Pro nakrmeni {kohout["jmeno"]} stiskni k. \nPro ukončení napiš konec. \nPro happy dejte h \nPro urazit dejte i \nPro spanek dej s \nPro reset hry dejte reset ")

    starnuti()
    zkontroluj_status()
    save()


    ui.run(native=True)


main()
