from os import strerror


class StudentsDataException(Exception):
    pass


class BadLine(StudentsDataException):
    pass


class FileEmpty(StudentsDataException):
    pass


s = {}
srcname = input("Enter the source file name: ")
try:
    src = open(srcname, 'rt', encoding="utf-8")
    for line in src:
        words = line.split()
        student = words[0] + " " + words[1]
        if student in s:
            i = s[student]
            score = float(words[2]) + i
        else:
            score = float(words[2])
        s[student] = score
    src.close()

    s_sorted = dict(sorted(s.items()))
    for key, value in s_sorted.items():
        print(key, "\t", value)


except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))
    exit(e.errno)
