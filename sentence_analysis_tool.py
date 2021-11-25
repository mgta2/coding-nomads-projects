# Project: Sentence Analysis Tool

user_input = input("Enter a sentence: ")

my_dict = {}
my_str = ""

# Remove spaces.
for char in user_input:
    if char != " ":
        my_str += char

lowers = 0
uppers = 0
puncts = 0

for char in my_str:
    if char.islower():
        lowers += 1
    if char.isupper():
        uppers += 1
    if char in (",.;:'?!" + '"'):
        puncts += 1

my_dict["Upper case"] = uppers
my_dict["Lower case"] = lowers
my_dict["Punctuation"] = puncts
my_dict["Total chars"] = len(my_str)

for key, value in my_dict.items():
    print(f"{key}: {value}")