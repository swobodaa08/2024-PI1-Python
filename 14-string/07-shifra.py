while True:
    text = input("Zadaj input: ")
    for i in range(len(text)):
        i += 1
        print(ord(text[i]))
