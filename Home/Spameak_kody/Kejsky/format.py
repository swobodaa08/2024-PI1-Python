# Program prepisujuci format skinov v subore

# Otvorenie suboru s povodnymi skinmi
with open('skiny.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Spracovanie liniek - nahradenie tabulatorov medzerami '-'
new_lines = []
for line in lines:
    # Odstranenie znaku noveho riadku a nahradenie tabulatorov pomlckami
    new_line = line.strip().replace('\t', ',')
    new_lines.append(new_line)

# Zapis noveho formatu do noveho suboru
with open('ALL_SKINS.txt', 'w', encoding='utf-8') as f:
    for new_line in new_lines:
        f.write(new_line + '\n')

print("Hotovo! Vystup zapisany do suboru skiny-new.txt.")