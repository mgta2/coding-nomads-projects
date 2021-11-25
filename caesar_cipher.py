# Caesar Cipher Shift Project
secret = "I hear the gooseberries are doing well this year, and so are the mangoes."
cipher = 7
secret = secret.lower()
# Use 'ord' and 'chr' to switch between numbers and characters.
sol = ""
for char in secret:
    if char.isalpha():
        new_index = (ord(char) - 97 + cipher) % 26 # Note ord('a') = 97.
        sol += chr(new_index + 97) # 'chr' is inverse to 'ord'.
    else:
        sol += char
print(sol)