import pygame, sys, time
## Created By Boston Abrams
##
##
##
## -------------  Info -------------
## Escape(esc) or enter will quit
##
##
## -------------  Options  -------------
## If you want FullScreen on or not.
FullScreen = False
#  ----------------------
# The FilePath is the position of the data storage location
FilePath='DataStore.txt'
# -----------------------
## Functions
def ToString (List): # Coverts List to String
    return ''.join(List)
## Vars - Setup
KeyEntry = []
HeadingList = []
AllHeadingDistance=[]
DistanceList = []
Expanded_Line =[]
num = 3.5
Heading = "NULL"
Distance = "NULL"
StartFire = True
HeadingFirstTime = True
DistanceFirstTime = True
Even = True
Loaded = False
Armed = False
DoneWait = False
Potato1 = True
Tank2 = False
Fire = False
HeadingSel = False
DistanceSel = False
Adder = False
Free = False
## Pygame Setup
pygame.init()
if not FullScreen:
    screen =  pygame.display.set_mode([800,480])
elif FullScreen:
    screen =  pygame.display.set_mode([800,480], pygame.FULLSCREEN )
screen.fill([105,105,105])
pygame.display.set_caption('CandyPi')
Smallfont = pygame.font.Font(None, 25)
font = pygame.font.Font(None, 50)
Bigfont = pygame.font.Font(None, 100)
## File Setup
reading_file=open(FilePath, 'r') #Opens File
lines=reading_file.readlines()
GoodLine = lines[len(lines) - 1]
OldGood = GoodLine
oldLinesGood = lines #Sets up lines for comparison
print "Waiting For Data..." #Fancy Command Line thing
# Render Titles
Title = font.render("CandyPi!", 1, (0, 0, 0))
pygame.display.flip()
while True:
    # Reading Files
    if DoneWait:
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
        if UserUnit == "F": # Converstion from Feet
            Distance = float(ToString(Distance)) * 0.3048
        elif UserUnit == "M":
            Distance = ToString(Distance)
        else:
            print "Error: Feet Meter Conversion" #Then Just Prints Stuff!
        print " - All In Meters - "
        print "Heading at " + ToString(Heading) + "degrees."
        print "Distance of " + str(Distance)
        Angle = Math.Maths(Distance)
        AllHeadingDistance.append([ToString(Heading),Distance, Angle])
        print "Angle " + str(Angle)
        DoneWait = False
    else:
        reading_file=open(FilePath, 'r')
        lines=reading_file.readlines()
        #print lines
        GoodLine = lines[len(lines) - 1] #GoodLine is the last line of the file!
        if len(lines) > len(oldLinesGood): # If there are more lines in the new one one was added. So then that line should be read
            DoneWait = True
        else:
            DoneWait = False
        OldGood = GoodLine # Resets Vars For comparison
        oldLinesGood = lines
    pygame.draw.rect(screen, [0, 0, 0], [10,145, 155, 45], 1)
    pygame.draw.rect(screen, [0, 0, 0], [180,145, 155, 45], 1)
    if HeadingSel:
        if HeadingFirstTime:
            KeyEntry = HeadingList
            HeadingFirstTime = False
        else:
            HeadingList = KeyEntry
        pygame.draw.rect(screen, [0, 0, 0], [5,120, 165, 75], 1)
    elif DistanceSel:
        if DistanceFirstTime:
            KeyEntry = DistanceList
            DistanceFirstTime = False
        else:
            DistanceList = KeyEntry
        pygame.draw.rect(screen, [0, 0, 0], [175,120,165, 75], 1)
    HeadingNumRender = font.render(ToString(HeadingList), 1, (0, 0, 0))
    screen.blit(HeadingNumRender, [10, 145])
    DistanceNumRender = font.render(ToString(DistanceList), 1, (0, 0, 0))
    screen.blit(DistanceNumRender, [180, 145])
    pygame.draw.circle(screen, [255,0,0], [400,165], 40, 0)
    pygame.draw.circle(screen, [0,0,0], [400,165], 33, 1)
    Add = Smallfont.render("Add", 1, (0, 0, 0))
    screen.blit(Add, [385,153])
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_ESCAPE:
                pygame.quit()
                break
            if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                if StartFire:
                    if Armed:
                        print "Firing"
                    if Tank2:
                        Armed = True
                        StartFire = False
                        Potato1 = False
                        Tank2 = False
                        Fire = True
                        num=3.5
                    elif Potato1:
                        Tank2 = True
                    else:
                        Potato1=True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #Screen = font.render("1", 1, (0, 0, 0))
            if 15 < x < 60 and 275 < y < 320:
                KeyEntry.append("1")
            elif 65 < x < 110 and 275 < y < 320:
                KeyEntry.append("2")
            elif 115 < x < 160 and 275 < y < 320:
                KeyEntry.append("3")
            elif 15 < x < 60 and 325 < y < 365:
                KeyEntry.append("4")
    pygame.display.flip()
    screen.fill([105,105,105])

