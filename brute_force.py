import enchant
import itertools
import dictionaryset
import json

checker = enchant.Dict("en-GB")
#checker = dictionaryset.get_set()

my_dictionary = json.load(open("words_dictionary.json"))

def validate_text(text,threshold):
    common_words = ["THE","YOU","AND","ARE","BUT","ALL","FOR","WAS","CAN","NOW","GET"]
    counter = 0
    for i in range(0,len(text)-3):
        if text[i:i+3] in common_words:
            counter += 1

    return counter >= threshold

def ceaser(text,all=False):
    possible = []
    for i in range(0,26):
        test_string = ""
        for char in text.upper():
            if ord(char) in range(65,92):
                test_string += chr(((ord(char)-65-i)%26)+65)
            elif char != "\n":
                test_string += char

        # if checker.check(test_string):
        #     possible.append(test_string)
        # elif test_string in my_dictionary:
        #     possible.append(test_string)
        possible.append(test_string)

    return possible

def monoalph(text):
    possible = []
    for mapper in itertools.permutations("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        test_string = ""
        for char in text.upper():
            if ord(char) in range(65,92):
                test_string += mapper[ord(char)-65]
            else:
                test_string += char

        if checker.check(test_string):
            possible.append(test_string)


def all_of_them():
    passwords = open("staff_passwords","rt")

    print(len(my_dictionary))

    cracked = 0
    for password in passwords.readlines():
        result = ceaser(password)
        if len(result) == 1:
            cracked += 1

    print("Cracked:", cracked)

    passwords.close()

print(ceaser("TWWBFXGM"))

# with open("emails/email0.enc","rt") as f:
#     cipher = f.read()
#
# out_string = ""
#
# for item in ceaser(cipher):
#     out_string += item + "\n\n\n\n\n\n"
#
# with open("output.txt","wt") as f:
#     f.write(out_string)
