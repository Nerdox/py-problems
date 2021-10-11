from sys import exit

def handleinput(string):
    try:
        return int(input("zadaj {}: ".format(string)))
    except:
        print("Cele cislo iba")
        exit()

valuf = handleinput("od")
valut = handleinput("do")

if valut < valuf:
    print("Druhe cislo musi byt vacsie nez prve")
    exit()

for x in range(valut - valuf + 1):
    a = valuf + x

    a_n = a
    string = a
    for y in range(3):
        a_n = a_n*a
        string = "{}\t{}".format(string, a_n)
    print(string)