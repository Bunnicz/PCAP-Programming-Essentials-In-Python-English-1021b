while True:
    word_1 = input("Write first word: ")
    word_1 = word_1.upper().strip()
    word_2 = input("Write second word: ")
    word_2 = word_2.upper().strip()

    if len(word_1) != 0 and len(word_2) != 0:
        break
    else:
        print("Word cant be blank")

list_1 = list(word_1)
list_1 = sorted(list_1)
list_2 = list(word_2)
list_2 = sorted(list_2)

if list_1 == list_2:
    print("Anagrams")
else:
    print("Not anagrams")
