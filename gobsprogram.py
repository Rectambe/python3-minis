from time import sleep
from random import uniform
from sys import argv

while (True):
    print("Gob's program: Y/N? ")
    ans = input ("? ")

    #Check for a yes or D (for debug) response, then run the program.
    if ans == "Y" or ans == "y" or ans == "D" or ans == "d":
        def penus(num = 60):
            for linenum in range(0, int(num)):
                #Creates a random delay, rounded to 3 decimal places, to emulate the feel of an old computer
                sleeptime = round(uniform(0.001, 0.125), 3)
                print('PENUS    PENUS    PENUS    PENUS    PENUS')
                if ans == "D" or ans == "d":
                    #Adds the length of the delay and the current line number
                    print(f"Delay: {sleeptime}, Line: {linenum + 1}")
                sleep(sleeptime)

        if len(argv) == 2:
            try:
                int(argv[1])
            except:
                print("Error: Number of lines is not an integer, defaulting to 60 lines")
                penus()
            else:
                penus(argv[1])
            finally:
                break
        else:
            penus()
            break

    elif ans == "N" or ans == "n":
        break

    else:
        print("\a")
