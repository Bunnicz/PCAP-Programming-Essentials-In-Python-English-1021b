from os import strerror

d = {chr(x): 0 for x in range(ord('a'), ord('z')+1)}
srcname = input("Enter the source file name: ")
try:
    src = open(srcname, 'rt', encoding="utf-8")
    for line in src:
        line = line.lower()
        for ch in line:
            if ch in d:
                i = d.get(ch)
                d[ch] = i+1

    for value, key in d.items():
        if key != 0:
            print(value, "->", key)

except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))
    exit(e.errno)
