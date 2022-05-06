# Caesar cipher.
text = input("Enter your message: ")
while True:
    shift = int(input("Enter shift value: "))
    if 0 < shift < 26:
        break
    else:
        print("Wrong Input: Shift should be 1-25")
cipher = ''
for char in text:
    if not char.isalpha():
        cipher += char
        continue
    # char = char.upper()
    code = ord(char) + shift
    # A-Z 65-90; a-z 97-122;
    if char.isupper() and ord('Z') < code:
        difference = code - ord('Z') - 1
        code = ord('A') + difference
    elif char.islower() and ord('z') < code:
        difference = code - ord('z') - 1
        code = ord('a') + difference
    cipher += chr(code)

print(cipher)
