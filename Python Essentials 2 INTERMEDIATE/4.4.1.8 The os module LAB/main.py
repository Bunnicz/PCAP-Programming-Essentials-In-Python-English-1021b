import os


def find(path, dir):
    try:
        os.chdir(path)
    except OSError:
        # Doesn't process a file that isn't a directory.
        return

    current_dir = os.getcwd()
    for entry in os.listdir("."):
        if entry == dir:
            print(os.getcwd() + "\\" + dir)
        find(current_dir + "\\" + entry, dir)


path = ".\\tree"
dirr = "python"
find(path, dirr)