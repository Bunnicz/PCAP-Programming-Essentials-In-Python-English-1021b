word = input("Write the word to find: ")
word = word.upper()
text = input("Write text in which you search for a word: ")
text = text.upper()

start = 0
for a in word:
    index = text.find(a, start)
    if index >= 0:
        pass
    else:
        print("Not Found")
        break
    start = index + 1
else:
    print("Found")
