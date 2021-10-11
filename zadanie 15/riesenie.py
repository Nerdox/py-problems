from random import randrange

try:
    val = int(input("zadaj n: "))
    
    for x in range(val):
        a = randrange(100)
        b = randrange(100)
        
        if a > b:
            c = a-b
        else:
            c = b-a
            
        print("Prvý bod na priamke je {}, druhý bod {}. Ich vzdialenosť je {}".format(a, b, c))
except:
    print("Cele cislo iba")