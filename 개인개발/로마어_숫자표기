def myFunc(n):

    value = 0

    I = 1
    V = 5
    X = 10
    L = 50
    C = 100
    D = 500
    M = 1000

    l = []
    for i in range(len(k)):
        l.append(k[i])

    if "IV" in n:
        value += 4
        l.remove("I")
        l.remove("V")
    if "IX" in n:
        l.remove("I")
        l.remove("X")
        value += 9
    if "CM" in n:
        l.remove("C")
        l.remove("M")
        value += 900
    if "XC" in n:
        l.remove("X")
        l.remove("C")
        value += 90

    if "I" in k:
        value += (1 * l.count("I"))
    if "V" in k:
        value += (5 * l.count("V")) 
    if "X" in k:
        value += (10 * l.count("X"))
    if "L" in k:
        value += (50 * l.count("L"))
    if "C" in k:
        value += (100 * l.count("C"))
    if "D" in k:
        value += (500 * l.count("D"))
    if "M" in k:
        value += (1000 * l.count("M"))

    print(value)

k = str(input())

myFunc(k)
