from sys import exit

def handleinput(string):
    try:
        if string.isnumeric():
            respond = int(input("zadaj n: "))
        else:
            respond = input("zadaj slovo: ")

        return respond
    except:
        print("Nespravna hodnota")
        exit()


word = handleinput("s")
value = handleinput("1")

c = int(0)
for x in range(value):
    spaces = "".ljust(c%4*4)
    c = c+1

    print("{}{}".format(spaces, word))