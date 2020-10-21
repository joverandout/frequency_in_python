import frequency

freq = frequency.Freq("emails/email1.enc")


mapper0 = {
    "A" : "G",
    "B" : "Y",
    "C" : "O",
    "D" : "R",
    "E" : "D",
    "F" : "Q",
    "G" : "C",
    "H" : "V",
    "I" : "X",
    "J" : "K",
    "K" : "T",
    "L" : "L",
    "M" : "E",
    "N" : "N",
    "O" : "P",
    "P" : "U",
    "Q" : "B",
    "R" : "J",
    "S" : "S",
    "T" : "A",
    "U" : "H",
    "V" : "W",
    "W" : "M",
    "X" : "Z",
    "Y" : "F",
    "Z" : "I"
}

def replace(text):
    test_string = ""
    tempy=0
    for char in text:
        if char in mapper0:
            newChar = mapper0[char]
            inty = ord(newChar)-tempy
            if inty < 65:
                inty = 91-(65-inty)
            finalChar = chr(inty)
            test_string += finalChar
        elif char == ' ':
            tempy+=1
            test_string += char
        else:
            test_string += char
    return test_string

def main():
    with open("emails/email1.enc","rt") as f:
        cipher_text = f.read()
        print(cipher_text)

    new_string = replace(cipher_text)
    print(freq.ordered())

    with open("emails/output.txt","wt") as f:
        f.write(new_string)

    print(new_string)

main()
