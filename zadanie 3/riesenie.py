try:
    string = input("zadaj slovo: ")
    string = string.replace(" ", "")
    
    last = ""
    for x in range(len(string)):
        last = "{}{}".format(last, string[x])
        print(last)
except:
    print("Error, zadajte slovo")