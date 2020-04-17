PENUS = 'PENUS'
while(True):
    print ("Gob's program: Y/N?")
    s = input("? ")
    if s.lower() == "y":
        while(True):
            print("\t".join([PENUS for a in range(6)]))
    elif s.lower() == "n":
        break
    print("\a")
