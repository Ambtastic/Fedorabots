from Myro import *
init(port)
setName("SEB")

degrees = 0
left = 0
right = 0
degW = .35

def scan():
    while getObstacle(1) <= 6399: #starts moving with 6400 IR detection
      forward(1) 
        beep(<1>, <420>)
      getObstacle(1) #No obj found
      #checks for obstacle if none found, continues moving and checking
    else: #if obj is found
        stop()
        beep(<2>, <450>)        
        while getObstacle(1) >= 6399: #Scans again if osbstacle detected
            turnBy(5, "deg")#Rotates to scan right
            getObstacle(1) #Scans
            degrees += 5 #Keeps track of degs
            right += 1 #keeps track of how many times it has to turn right to determine which side is longer
            beep(<.5>, <530>)
        else:
            turnBy(- degrees, "deg")
        while getObstacle(1) >=6399: #Scans again if obstacle detected
            turnBy(-5, "deg")#Rotates to scan left
            getObstacle(1) #Scans
            degrees -= 5 #Keeps track of degs
            left += 1 #keeps track of how many times it has to turn left to determine which side is longer
        else:
            turnBy(- degrees, "deg")#straighten out
            if right < left:
                turnBy(90, "deg")#turn right
                dist = right*degW
                forward(1, dist + 1)
                turnBy(-90, "deg")#cont on path
                scan()#Restarts entire function
                beep(<1>, <500>)
            elif left < right:
                turnBy(-90, "deg")#turn left
                dist = left*degW
                forward(1,dist + 1)
                turnBy(90, "deg")#cont on path
                scan()#restart function
                beep(<1, <520>)
scan()

#beep(<time, frequency>)
#speak(<something>)
