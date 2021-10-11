import math
from sys import exit

def handleinput(string):
    try:
        return int(input("zadaj {}: ".format(string)))
    except:
        print("Cele cislo iba")
        exit()
    
valuf = handleinput("od")
valut = handleinput("do")
valuk = handleinput("krok")

if valut < valuf:
    print("Druhe cislo musi byt vacsie nez prve")
    exit()

if valuk > (valut-valuf):
    print("Krok musi byt vacsi nez rozdiel medzi od a do")
    exit()

for x in range(valuf, valut, valuk):
    sin = math.sin(math.radians(x))**2
    cos = math.cos(math.radians(x))**2
    summ = cos+sin
    
    print("{}\tsin**2 = {}\tcos**2 = {}\tsúčet = {}".format(x, round(sin,4), round(cos,4), summ))