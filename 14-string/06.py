# string v pythone je immutable, tzn. nemenitelny

ret = "Ahoj svet"
# ret[0] = "a" # toto nieje mozne lebo je immutable
ret = "a" + ret[1:] # ak chceme zmenit nejaky znak, treba takto
print(ret)

# retazce vieme porovnavat

print("a" == "b")
print(ord("a")) # ord() je funkcia ktora vrati ordinalnu (ciselnu) hodnotu znaku 
print(ord("A"))
print(chr(132)) # chr() je funkcia ktora na zakladne ordinalnej hodnoty vrati znak