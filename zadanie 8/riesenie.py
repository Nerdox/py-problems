try:
    value = int(input("zadaj n: "))
    
    retazec = "* "
    for x in range(1, value):
        retazec = "{}{} ".format(retazec, "*"*(x+1))
    print(retazec)
except:
    print("Cele cislo iba")