def mysplit(strng):
    strng = strng.lstrip()
    list = []
    word = ""
    for ch in strng:
        if ch == " ":
            if word != "":
                list.append(word)
            word = ""
            continue
        else:
            word += ch
    return list


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
print(mysplit(" ab  ab  ab "))