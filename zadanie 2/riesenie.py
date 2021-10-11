try:
    string = input("zadaj slovo: ")
    string = string.replace(" ", "")
    
    for x in range(len(string)):
        print(string[x] * (x+1))
except:
    print("Error, zadajte slovo")