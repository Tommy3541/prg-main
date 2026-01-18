from sys import exit
import datetime as dt
import json
import os
from nicegui import ui, app
from PIL import Image


cas = dt.datetime.now()

zprava = None
obrazek = None
spritesheet = Image.open("sendvic2/cat.png")

kohout = {}
default_kohout = {}

#kohout = {
#    "jmeno": "silver",
#    "hlad": 50,
#    "zizen": 0,
#    "vek": 0,
#    "zivoty": 100,
#    "cistota": 100,
#    "barva": "pink",
#    "energie": 90,
#    "zije": True,
#    "nestastnost": False,
#    "nemoc": False,
#}

def krmeni():
    global zprava
    kohout["hlad"] -= 10
    print(f"{kohout['jmeno']} vypadá šťastně.\nHlad je {kohout['hlad']}.")
    zprava.text = (f"{kohout['jmeno']} vypadá šťastně.\nHlad je {kohout['hlad']}.")
    ui.notify("mnam")
    obrazek.source = vystrihni_obrazek(4, 59)
    zkontroluj_status()

def napit():
    global zprava
    kohout["zizen"] -= 10
    print(f"{kohout["jmeno"]} vypadá šťastně.\nŽízeň je {kohout["zizen"]}.")
    zprava.text = (f"{kohout["jmeno"]} vypadá šťastně.\nŽízeň je {kohout["zizen"]}.")
    ui.notify("glop glop")
    obrazek.source = vystrihni_obrazek(0, 7)
    zkontroluj_status()

def umyt():
    global zprava
    if kohout["cistota"] <= 90:
        kohout["cistota"] += 10
        print(f"{kohout["jmeno"]} vypadá čistě.\nČistota je {kohout["cistota"]}.")
        zprava.text = (f"{kohout["jmeno"]} vypadá šťastně.\nČistota je {kohout["cistota"]}.")
        ui.notify("kshshhhhhhhhhhh")
        obrazek.source = vystrihni_obrazek(0, 13)
        zkontroluj_status()
    else:
        ui.notify("Silver odmítá další sprchy, je už dostatečně čistý")


def zkontroluj_status():
    global zprava
    if kohout["hlad"] > 120 or kohout["hlad"] < -20:
        kohout["zivoty"] -= 10
    
    if kohout["zizen"] > 120 or kohout["zizen"] < -20:
        kohout["zivoty"] -= 10

    if kohout["zivoty"] <= 0:
        kohout["zije"] = False
        print(f"{kohout["jmeno"]} se nedostal do sněmovny. (died)")
        death.open()

    
    starnuti()
    hladoveni()
    aktualizuj_ukazatele()


def hra():
    global zprava
    if kohout["nestastnost"] == True:
        kohout["nestastnost"] = False
        kohout["energie"] -= 10
        kohout["hlad"] += 10
        kohout["zizen"] += 10
        kohout["cistota"] -= 10
        print(f"{kohout["jmeno"]} je vic happy, jeho energie je {kohout["energie"]}")
        zprava.text = (f"{kohout["jmeno"]} je vic happy, jeho energie je {kohout["energie"]}")
        ui.notify("hahahahhahahaha")
        obrazek.source = vystrihni_obrazek(2, 64)
        zkontroluj_status()
    else:
        ui.notify("silver je az moc stastny, nechce si hrat")


def insult():
    global zprava
    kohout["nestastnost"] = True
    print(f"{kohout["jmeno"]} je nestastny")
    zprava.text = (f"{kohout["jmeno"]} je nestastny")
    ui.notify("ahsabdfiubfaoihrapirw")
    obrazek.source = vystrihni_obrazek(0, 61)
    zkontroluj_status()
    save()

def harakiri():
    global zprava
    kohout["zije"] == False
    print(f"{kohout["jmeno"]} zemřel")
    zprava.text = (f"{kohout["jmeno"]} zemřel")
    ui.notify("zemřel....")
    zprava.text = "KONEC HRY"
    obrazek.source = vystrihni_obrazek(0, 55)
    death.open()
    status()
    save()

def spanek():
    global zprava
    if kohout["energie"] != 100:
        kohout["energie"] = 100
        kohout["zivoty"] += 10
        print(f"{kohout["jmeno"]} se vyspinkal, jeho energie je {kohout["energie"]}")
        zprava.text = (f"{kohout["jmeno"]} se vyspinkal, jeho energie je {kohout["energie"]}")
        ui.notify("ZzzzzzzzzzzzZzzzzzzzzz")
        obrazek.source = vystrihni_obrazek(0, 45)
        zkontroluj_status()
    else:
        ui.notify("Silver uz nechce spát...")

def hladoveni():
    global cas
    global zprava

    ted = dt.datetime.now()

    if ted > cas + dt.timedelta(seconds=10):
        kohout["hlad"] += 10
        print(f"{kohout["jmeno"]} zacina mit hlad")
        cas = ted

def starnuti():
    global cas
    global zprava

    ted = dt.datetime.now()

    if ted > cas + dt.timedelta(hours=10):
        kohout["vek"] += 1
        print(f"{kohout["jmeno"]} ma narozeniny")
        cas = ted

def aktualizuj_ukazatele():
    hlad_bar.value = max(0, min(1, (100 - kohout["hlad"]) / 100))
    zizen_bar.value = max(0, min(1, (100 - kohout["zizen"]) / 100))
    energie_bar.value = max(0, min(1, kohout["energie"] / 100))
    zivoty_bar.value = max(0, min(1, kohout["zivoty"] / 100))
    
    if kohout["hlad"] > 80: hlad_bar.props('color=red')
    else: hlad_bar.props('color=orange')

    if kohout["zivoty"] < 30: zivoty_bar.props('color=grey-9')
    else: zivoty_bar.props('color=red')

def status():
    global zprava
    print(f"{kohout["jmeno"]} me energii {kohout["energie"]} \n hlad {kohout["hlad"]} \n zizen {kohout["zizen"]} \n {kohout["jmeno"]} je {"stastny" if kohout["nestastnost"] == False else "nestastny"} \n zije? {kohout["zije"]} \n nemoc {kohout["nemoc"]} \n je stary {kohout["vek"]}")
    if kohout["zije"] == False:
        with ui.dialog() as dialog, ui.card():
            ui.label('Hello world!')
            ui.button('Close', on_click=dialog.close)
        
        ui.button('Open a dialog', on_click=dialog.open)


        
def load():
    # TODO roset hry, kontrola existence save
    global kohout
    global zprava
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
    global death
    global energie_bar
    global zizen_bar
    global hlad_bar
    global zivoty_bar

    tlacitka1 = {
        "krmeni": krmeni,
        "napit": napit,
    }
    tlacitka2 = {
        "hra": hra,
        "spanek": spanek,
        "umyt": umyt,
    }
    tlacitka3 = {
        "insult": insult,
    }
    tlacitka4 = {
        "harakiri": harakiri,
    }

    load()

    with ui.dialog().props('persistent') as death:
        with ui.card().classes('items-center p-10 bg-zinc-900 text-white border-4 border-red-700'):
            ui.label('WASTED').classes('text-7xl font-black text-red-600 tracking-tighter')
            ui.label(f'Silver už to nezvládl...').classes('text-lg opacity-80')
            ui.button('ZKUSIT ZNOVU', on_click=lambda: (reset(), ui.navigate.reload())).props('color=red icon=refresh')
        
    with ui.element("div").classes("w-full h-screen flex items-center justify-center flex-col gap-5"):
        ui.image("sendvic2/Gemini_Generated_Image_xxerbyxxerbyxxer.png").classes("absolute top-0 left-0 w-full h-full")
       
        obrazek = ui.image(vystrihni_obrazek(0, 1)).classes("h-90 w-90 image-rendering: pixelated; image-rendering: -moz-crisp-edges; image-rendering: crisp-edges;").style('top: 190px;')

#        with ui.element("div").classes("absolute top-35 w-full flex justify-center z-5"):
#            zprava = ui.label("Co chceš dělat?").classes("text-white text-5xl font-black text-center").style('text-shadow: 2px 2px 10px rgba(0,0,0,0.9); width: 80%;')
 
        with ui.element("div").classes("absolute top-0 w-full flex justify-center p-6 z-10"):
            with ui.card().classes('bg-black/40 backdrop-blur-md border-b-2 border-white/20 p-4 min-w-[500px] items-center'):
                zprava = ui.label("Co chceš dělat?").classes("text-white text-2xl font-medium uppercase tracking-wider")
                
                with ui.row().classes('w-full justify-around mt-4 gap-4'):
                    with ui.column().classes('items-center g-0'):
                        ui.label('HLAD').classes('text-[10px] text-white/60 font-bold')
                        hlad_bar = ui.linear_progress(value=0.5).classes('w-32 h-8').props('color=orange show-value format=%.0f%%')
                    
                    with ui.column().classes('items-center g-0'):
                        ui.label('ŽÍZEŇ').classes('text-[10px] text-white/60 font-bold')
                        zizen_bar = ui.linear_progress(value=0.5).classes('w-32 h-8').props('color=blue show-value format=%.0f%%')
                    
                    with ui.column().classes('items-center g-0'):
                        ui.label('ENERGIE').classes('text-[10px] text-white/60 font-bold')
                        energie_bar = ui.linear_progress(value=0.9).classes('w-32 h-8').props('color=green show-value format=%.0f%%')
                    
                    with ui.column().classes('items-center'):
                        ui.label('ŽIVOTY').classes('text-[10px] text-red-400 font-bold')
                        zivoty_bar = ui.linear_progress(value=1.0).classes('w-32 h-8 rounded-full').props('color=red show-value show-value format=%.0f%%')

        with ui.grid(columns=2):
            for jmeno, funkce in tlacitka1.items():
                ui.button(jmeno, on_click=funkce, color="#9F6553").style('top: 110px;')
        with ui.grid(columns=3):
            for jmeno, funkce in tlacitka2.items():
                ui.button(jmeno, on_click=funkce, color="#A0AE9F").style('top: 110px;')
        with ui.grid(columns=2):
            for jmeno, funkce in tlacitka3.items():
                ui.button(jmeno, on_click=funkce, color="red").style('top: 110px;').classes("rounded-full")
            for jmeno, funkce in tlacitka4.items():
                ui.button(jmeno, on_click=funkce, color="black").style('color: white; top: 110px;').classes("rounded-full animate-pulse")
    
    ui.button(on_click=lambda: app.native.main_window.toggle_fullscreen()).props('icon=fullscreen flat color=white').classes('absolute top-5 right-5 z-30')

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


    ui.run(native=True, title="Kohout Silver")


main()
