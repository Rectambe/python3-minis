import winsound
from time import sleep
from sys import argv

#Check for an argument and whether it is an integer
if len(argv) == 2:
    try:
        int(argv[1])
    except:
        print("Play number value needs to be an integer greater than 0, defaulting to 10 plays")
        plays = 10
    else:
        plays = argv[1]
else:
    plays = 10

for playnum in range(0, int(plays)):
    winsound.Beep(1000, 150)
    sleep(0.5)
