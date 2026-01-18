from nicegui import ui

def hokus():
    ui.notify("butt hokus") 

def locus():
    ui.notify("butt locus")

def pokus():
    ui.notify("butt pokus")

tlacitka = {
    "prvni": hokus,
    "druhe": pokus,
    "treti": locus
}

with ui.element("div").classes("w-full h-screen flex items-center justify-center flex-col gap-5"):
    
    ui.label("ahoj").classes("text-blue-400 font-bold text-4xl")
    ui.label("Bye").style("color: blue")
    ui.button("click", on_click=hokus)


    with ui.grid(columns=3):
        for jmeno, funkce in tlacitka.items():
            ui.button(jmeno, on_click=funkce)





ui.run(native=True)