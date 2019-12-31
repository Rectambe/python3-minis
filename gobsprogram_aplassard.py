PENUS = 'PENUS'
while(True):
    print ("Gob's program: Y/N?")
    s = input("? ")
    if s == "y" or s == "Y":
        while(True):
            print("\t".join([PENUS for a in range(6)]))
    elif s == "n" or s == "N":
        break
    print("\a")