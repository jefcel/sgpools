import random
import datetime

### toto system 7 generator function ###
def numgentoto():
    numgentoto = []
    for num in range (0,7):
        numgentoto.append(random.randint(1,49))
    print(numgentoto)
now = datetime.datetime.today().weekday()
print(now)

### 4D generator function ###
def numgen4d():
    numgen4d = []
    for num in range (0,4):
        numgen4d.append(random.randint(0,9))
    print(numgen4d)


### monday and thursday toto day, so its 0, 3 ###
if ((now == 1) or (now == 3)):
    print ('today is TOTO DAY')
    numgentoto()
    
### wed,sat,sunday 4d day, so its 2, 5, 6 ###
elif ((now == 2) or (now == 5) or (now == 6)):
    print ('today is 4D DAY')
    numgen4d()
    
else :
    print ('today is not SGPOOLS DAY')
