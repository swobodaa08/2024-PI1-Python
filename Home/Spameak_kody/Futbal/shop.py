from pathlib import Path

absolute_path = Path("C:/2024-PI1-Python-1/Home/Spameak_kody/Futbal/ceny.txt")
current_dir = Path.cwd()
relative_path = absolute_path.relative_to(current_dir)

def nacitaj_ceny(subor):
    items = []
    with open(subor, "r") as f:
        for riadok in f:
            item, price = riadok.strip().split(',')
            items.append((item, float(price)))
    return items

items = nacitaj_ceny(relative_path)

for item in items:
    print(items)