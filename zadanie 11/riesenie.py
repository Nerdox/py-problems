try:
    value = int(input("zadaj počet: "))

    o = 0
    for x in range(1, value * 2, 4):
        o = (o + (1/x) - (1/(x+2)))
    print("pi = {}".format(o*4))
except:
    print("Cele cislo iba")