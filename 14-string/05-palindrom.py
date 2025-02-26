# Palindrom je retazec ktory je rovnaky pri citani od zaciatku alebo od konca

while True:
    ret = str(input("Zadaj slovo/vetu: "))
    ret2 = ret[::-1]
    if ret == "exit":
        exit()
    if ret == ret2:
        print(f"Input {ret} je palindrom")
    else:
        print(f"Input {ret} nieje palindrom")