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
    src.close()

    dest_name = srcname[:-4] + "_hist.txt"
    dest = open(dest_name, "wt")
    d_sorted = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
    for key, value in d_sorted.items():
        if value != 0:
            dest.write(key + " -> " + str(value) + "\n")
    dest.close()

except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))
    exit(e.errno)
