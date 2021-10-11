try:
    value = int(input("zadaj n: "))

    for x in range(1, value+1):
        print("*" * x)
except:
    print("Cele cislo iba")