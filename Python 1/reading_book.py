print("*** Reading E-Book ***")
text,character = input("Text , Highlight : ").split(",")
for i in range(len(text)):
    if text[i] == character:
        print("[" + character +"]", end ="")
    else:
        print(text[i], end ="")