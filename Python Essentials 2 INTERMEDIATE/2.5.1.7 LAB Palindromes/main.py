while True:
    text = input("Write your text here: ")
    text = text.upper().split()

    if len(text) != 0:
        break
    else:
        print("Word cant be empty")

words = ""
for word in text:
    words += word

middle = len(words) // 2

# try:
for i in range(middle):
    if words[i] == words[-i - 1]:
        continue
    else:
        print("It's not a palindrome")
        break
        # raise StopIteration
# except StopIteration:
#     print("It's not a palindrome")
else:
    print("It's a palindrome")
