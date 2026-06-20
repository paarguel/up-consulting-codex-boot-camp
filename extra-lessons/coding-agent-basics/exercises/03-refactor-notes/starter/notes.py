import sys


def process_notes(path):
    f = open(path, "r", encoding="utf-8")
    stuff = f.readlines()
    f.close()
    a = 0
    b = 0
    c = 0
    for x in stuff:
        y = x.strip()
        if y == "":
            continue
        a = a + 1
        if y.lower().startswith("todo:"):
            b = b + 1
        elif y.lower().startswith("done:"):
            c = c + 1
    print("Total notes:", a)
    print("Todo notes:", b)
    print("Done notes:", c)


if __name__ == "__main__":
    process_notes(sys.argv[1])
