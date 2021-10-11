from sys import exit

def handleinput(str):
    try:
        return int(input("zadaj {}: ".format(str)))
    except:
        print("Cele cislo iba")
        exit()
    
valuf = handleinput("od")
valut = handleinput("do")

if valut < valuf:
    print("Druhe cislo musi byt vacsie nez prve")
    exit()

dif = valut-valuf+1
columns = "####|"
head = "====|" + "="*(5*dif-3)
data = ""

for y in range(dif):
    current_y = valuf+y
    columns = "{}\t{}".format(columns, current_y)
    data = "{}{}\t|".format(data, current_y)
    
    for x in range(dif):
        current_x = valuf+x
        data = "{}\t{}".format(data, current_y * current_x)
        
        if x+1 == dif:
            data = "{}\n".format(data)

print(columns)
print(head)
print(data)