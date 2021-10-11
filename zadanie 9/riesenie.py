from sys import exit

def handleinput(string):
    try:
        return int(input("zadaj {}: ".format(string)))
    except:
        print("Cele cislo iba")
        exit()

valuf = handleinput("od")
valut = handleinput("do")

if valut > valuf:
    retazec = "<{}>".format(valuf)
    for x in range(1, valut - valuf + 1):
        retazec = "{}<{}> ".format(retazec, valuf+x)
    print(retazec)
else:
    print("Druhe cislo musi byt vacsie nez prve")