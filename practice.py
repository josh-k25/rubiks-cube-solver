def multiply(a, b):
    return a * b

def isEven(c):
    if c % 2 == 0:
        return True
    else:
        return False

def rotateLeft(d):
    e = d.copy()
    temp = e[0]

    for i in range(len(e) - 1):
        e[i] = e[i + 1]

    e[len(e) - 1] = temp

    return e



