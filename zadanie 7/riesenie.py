try:
    value = int(input("zadaj n: "))
    valus = str(value)
    
    summ = 0
    for x in range(len(valus)):
        print("cifra {}".format(valus[x]))
        
        summ = summ+int(valus[x])
    print("ciferný súčet je {}".format(summ))
except:
    print("Cele cislo iba")