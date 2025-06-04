load_skinov = open("ALL_SKINS.txt", "r", encoding="UTF-8")

for info in load_skinov:
    skin, rarity, collection, date = (info.split(","))
    print(skin)
    print(rarity)
    print(collection)
    print(date)