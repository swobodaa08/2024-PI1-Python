teploty = [10, 13, 15, 20]
# print(teploty)
# print(teploty[0])

nakup = ["chlieb", "maslo", "mlieko"]

zviera = ["pes", "Dunčo", 2020, "hnedá", 10.7] # do listu mozeme ukladat hodnoty roznych typov (int, str, bool-...)
print(zviera)
print(zviera[2])

# v pythone su listy dynamicke, to znamena ze nemusia mat definovanu velkost
prazdny = []
prazdny.append(25)
print(prazdny)

# listy vieme aj spocitat(zretazit)
nakupyazvierata = nakup + zviera
print(nakupyazvierata)

# narozdiel od stringu su listy v pythone mutable (menitelna), tzn. ze mozem prepisat hodnotu prvku

hodnoty = [15, 30, 80, 50, 100, 1]
print(max(hodnoty))