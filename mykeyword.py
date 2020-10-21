def keyword(text,string_key):
    test_string = ""

    key = [ord(char)-65 for char in string_key.upper()]
    key_counter = 0

    for char in text.upper():
        if ord(char) in range(65,92):
            test_string += chr(((ord(char)-65-key[key_counter])%26)+65)
            key_counter = (key_counter + 1) % len(key)
        else:
            test_string += char

    return test_string

print(keyword("TWWBFXGM","CULT"))
print(keyword("TWWBFXGM","LAMBDA"))
print(keyword("TWWBFXGM","PURPLE"))
print(keyword("TWWBFXGM","SLACK"))
print(keyword("TWWBFXGM","PASSWORD"))
