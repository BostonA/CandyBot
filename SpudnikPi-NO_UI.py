#import RPi.GPIO as GPIO
import time
CurrentAnglePos = 0
CurrentHeadingPos = 0
OldAnglePos = 1
OldHeadingPos = 1
State = "U"

import Math
#MotorMove
def ToString (List): # Coverts List to String
    return ''.join(List)
while True:
    Free = False
    #Code = []
    Expanded_Line =[]
    reading_file=open('DataStore.txt', 'r') #Opens File
    lines=reading_file.readlines()
    GoodLine = lines[len(lines) - 1]
    OldGood = GoodLine
    oldLinesGood = lines #Sets up lines for comparison
    print "Waiting For Data..." #Fancy Command Line thing
    while True:
        time.sleep(1)
        reading_file=open('DataStore.txt', 'r')
        lines=reading_file.readlines()
        reading_file.close()
        if OldAnglePos == CurrentAnglePos and OldHeadingPos == CurrentHeadingPos:
            pass
        else:
            if len(str(CurrentAnglePos)) == 1:
                StrAnglePos = "00" + str(CurrentAnglePos)
            elif len (str(CurrentAnglePos)) == 2:
                StrAnglePos = "0" + str(CurrentAnglePos)
            else:
                StrAnglePos = str(CurrentAnglePos)
            if len(str(CurrentHeadingPos)) == 1:
                StrHeadingPos = "00" + str(CurrentHeadingPos)
            elif len (str(CurrentHeadingPos)) == 2:
                StrHeadingPos = "0" + str(CurrentHeadingPos)
            else:
                StrAnglePos = str(CurrentAnglePos)
            Data = StrAnglePos + " " + StrHeadingPos + " " + State
            writing_file=open('SendBack.txt','ab')
            writing_file.write('\n' + Data)
            writing_file.close()
            OldAnglePos = CurrentAnglePos
            OldHeadingPos = CurrentHeadingPos
        GoodLine = lines[len(lines) - 1] #GoodLine is the last line of the file!
        if len(lines) > len(oldLinesGood): # If there are more lines in the new one one was added. So then that line should be read
            break # So it leaves the inner "While True" Loop
        OldGood = GoodLine # Resets Vars For comparison
        oldLinesGood = lines
    print "Infomation Receved From Server"
    x = 0
    Heading = [] #list of everything in heading.
    Distance = [] #list of everything in distance.
    #First Num
    for char in GoodLine:

        if char == " ": #Looking for spacebar
            break
        x = x + 1
    y = 0
    for char in GoodLine:
        if y == x: #When len is the same as the first loop
            break #END
        Heading.append(char) #adding it to a list
        y = y + 1
        OldY = y
# Second Num
    x = 0
    y = 0
    z = False
    for char in GoodLine:
        if char == " ": #Skips the first space
            if z:
                break # Then it breaks
            z = True
        x = x + 1
    for char in GoodLine:
        if y == x:
            break
        if y> OldY:
            Distance.append(char) #It only prints after the first space
        y = y + 1
    UserUnit = GoodLine[y+1]
    print ToString(Distance)
    if UserUnit == "F": # Converstion to Feet
        Distance = float(ToString(Distance)) * 0.3048
    elif UserUnit == "M":
        Distance = ToString(Distance)
    else:
        print "Error: Feet Meter Conversion" #Then Just Prints Stuff!
    print " - All In Meters - "
    print "Heading at " + ToString(Heading) + "degrees."
    print "Distance of " + str(Distance)
    Angle = Distance
    #Angle = Math.Maths(Distance)
    CurrentAnglePos = int(Angle) - CurrentAnglePos
    CurrentHeadingPos = int(ToString(Heading)) - CurrentHeadingPos
    #MotorMove.Control(ToString(Heading), Angle)
"""
restTime = .5
flashPattern = [12, 3, 8, 3]
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
def flashLEDon ():
    print "LED on"
    GPIO.output(4, GPIO.HIGH)
def flashLEDoff ():
    print "LED off"
    GPIO.output(4, GPIO.LOW)
while True:
    Free = False
    Code = []
    Expanded_Line =[]

    reading_file=open('/tmp/newfile.txt', 'r')

    lines=reading_file.readlines()
    GoodLine = lines[len(lines) - 1]
    OldGood = GoodLine
    oldLinesGood = lines
    while True:
        time.sleep(1)
        # Change the Loacation Not sure where
        reading_file=open('/tmp/newfile.txt', 'r')
        lines=reading_file.readlines()
        print lines
        GoodLine = lines[len(lines) - 1]
        print
        if len(GoodLine)==14 and len(lines) > len(oldLinesGood):
            break
        OldGood = GoodLine
        oldLinesGood = lines
    for x in GoodLine:
        Expanded_Line.append(x)
        #print Expanded_Line
    if Expanded_Line[0] + Expanded_Line[1] == "03":
        Code.append(3)
        print "3 Hours"
    elif Expanded_Line[0] + Expanded_Line[1] == "08":
        Code.append(8)
        print "8 Hours"
    elif Expanded_Line[0] + Expanded_Line[1] == "12":
        Code.append(12)
        print "12 Hours"
    elif Expanded_Line[0] + Expanded_Line[1] == "24":
        Code.append(24)
        print "24 Hours"
    else:
        Code.append(0)
        print "Empty"
    if Expanded_Line[3] + Expanded_Line[4] == "03":
        Code.append(3)
        print "3 Hours"
    elif Expanded_Line[3] + Expanded_Line[4] == "08":
        Code.append(8)
        print "8 Hours"
    elif Expanded_Line[3] + Expanded_Line[4] == "12":
        Code.append(12)
        print "12 Hours"
    elif Expanded_Line[3] + Expanded_Line[4] == "24":
        Code.append(24)
        print "24 Hours"
    else:
        Code.append(0)
        print "Empty"
    if Expanded_Line[6] + Expanded_Line[7] == "03":
        Code.append(3)
        print "3 Hours"
    elif Expanded_Line[6] + Expanded_Line[7] == "08":
        Code.append(8)
        print "8 Hours"
    elif Expanded_Line[6] + Expanded_Line[7] == "12":
        Code.append(12)
        print "12 Hours"
    elif Expanded_Line[6] + Expanded_Line[7] == "24":
        Code.append(24)
        print "24 Hours"
    else:
        Code.append(0)
        print "Empty"
    if Expanded_Line[9] + Expanded_Line[10] == "03":
        Code.append(3)
        print "3 Hours"
    elif Expanded_Line[9] + Expanded_Line[10] == "08":
        Code.append(8)
        print "8 Hours"
    elif Expanded_Line[9] + Expanded_Line[10] == "12":
        Code.append(12)
        print "12 Hours"
    elif Expanded_Line[9] + Expanded_Line[10] == "24":
        Code.append(24)
        print "24 Hours"
    else:
        Code.append(0)
        print "Empty"
    if Expanded_Line[12] == "Y":
        print "Free: on"
        Free = True
    elif Expanded_Line[12] == "N":
        Free = False
        print "Free: off"
    else:
        print "Error: php formating incorrect"
    print Code
    flashLEDon()
    time.sleep(1)
    flashLEDoff()
    time.sleep(1)
    for x in Code:
        print x
        flashLEDon ()
        if x == 3:
            time.sleep(1)
            print "on for 1 sec"
        elif x == 8:
            time.sleep(2)
            print "on for 2 sec"
        elif x == 12:
            time.sleep(3)
            print "on for 3 sec"
        elif x == 24:
            time.sleep(4)
            print "on for 4 sec"
        elif x == 0:
            time.sleep(5)
            print "on for 5 sec"
        else:
            print "error"
        flashLEDoff()
        time.sleep(1)
    flashLEDon()
    if Free:
        time.sleep(2)
        print "on for 2 sec"
    else:
        time.sleep(1)
        print "on for 1 sec"
    flashLEDoff()
"""
