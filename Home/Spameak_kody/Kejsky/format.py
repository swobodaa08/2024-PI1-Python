# # Program prepisujuci format skinov v subore

# # Otvorenie suboru s povodnymi skinmi
# with open('skiny.txt', 'r', encoding='utf-8') as f:
#     lines = f.readlines()

# # Spracovanie liniek - nahradenie tabulatorov medzerami '-'
# new_lines = []
# for line in lines:
#     # Odstranenie znaku noveho riadku a nahradenie tabulatorov pomlckami
#     new_line = line.strip().replace('\t', ',')
#     new_lines.append(new_line)

# # Zapis noveho formatu do noveho suboru
# with open('ALL_SKINS.txt', 'w', encoding='utf-8') as f:
#     for new_line in new_lines:
#         f.write(new_line + '\n')

# print("Hotovo! Vystup zapisany do suboru skiny-new.txt.")


# def rozdel_skyny(vstupny_subor):
#     skiny = []
#     rarity = []
#     kolekcie = []
#     datumy = []

#     with open(vstupny_subor, 'r', encoding='utf-8') as f:
#         for riadok in f:
#             casti = [c.strip() for c in riadok.strip().split(',')]
#             if len(casti) == 4:
#                 skiny.append(casti[0])
#                 rarity.append(casti[1])
#                 kolekcie.append(casti[2])
#                 datumy.append(casti[3])
#             else:
#                 print(f"⚠️ Riadok preskočený (nesprávny formát): {riadok.strip()}")

#     # Uloženie do samostatných súborov
#     with open('skin_list.txt', 'w', encoding='utf-8') as f:
#         f.write('\n'.join(skiny))
#     with open('rarity_list.txt', 'w', encoding='utf-8') as f:
#         f.write('\n'.join(rarity))
#     with open('collection_list.txt', 'w', encoding='utf-8') as f:
#         f.write('\n'.join(kolekcie))
#     with open('date_list.txt', 'w', encoding='utf-8') as f:
#         f.write('\n'.join(datumy))

#     print("✅ Dáta boli rozdelené do jednotlivých súborov.")

# # Spustenie
# rozdel_skyny('ALL_SKINS.txt')


# def odstran_duplikaty(subor):
#     try:
#         with open(subor, 'r', encoding='utf-8') as f:
#             lines = f.readlines()

#         unique_lines = sorted(set(line.strip() for line in lines if line.strip()))

#         with open(subor, 'w', encoding='utf-8') as f:
#             f.write('\n'.join(unique_lines))

#         print(f"✅ Duplikáty boli odstránené zo súboru: {subor}")
#     except FileNotFoundError:
#         print(f"❌ Súbor {subor} neexistuje.")

# # Zoznam súborov na čistenie
# subory = [
#     'skin_list.txt',
#     'rarity_list.txt',
#     'collection_list.txt',
#     'date_list.txt'
# ]

# for subor in subory:
#     odstran_duplikaty(subor)
