# Based on Gob's Program by aplassard (Github: https://gist.github.com/aplassard/a368fef46387c16fd19f), Updated to Python 3 by me
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
