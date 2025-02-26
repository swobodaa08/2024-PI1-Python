# String je reťazec znakov napr. "Ahoj"
# Retazec zaciname a koncime "" alebo ''
# \n - novy riadok (enter),  \t - 4 medzery (tabulator), \" - "" (uvodzovky)
# funkcia "len"() - vrati dlzku retazca - kolko tam je znakov
# znaky v retazci su indexovane
# index piseme do hranatych zatvoriek [] - AltGr + G, F

retazec = "Ahoj Svet"

# for i in range(len(retazec)):
#     print(retazec[i])

for znak in retazec: # postupne vybera znaky z retazca do premennej znak
    print(znak)