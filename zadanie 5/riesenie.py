try:
    value = int(input("zadaj n: "))

    for x in range(value):
        string = "*".rjust(value-x)

        if x > 0:
            for _ in range(x):
                string = "{}**".format(string)
        print(string)
except:
    print("Cele cislo iba")