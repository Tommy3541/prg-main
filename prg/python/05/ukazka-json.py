import json

kohout = {
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


with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

kohout["vek"] += 1

with open("data.json", "w", encoding="utf-8") as f:
   json.dump(kohout, f, ensure_ascii=False, indent=4)