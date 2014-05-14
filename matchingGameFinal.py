#import the appropriate libraries for use with this program
import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *
from PIL import Image
import tkFileDialog
from random import randint
from open import imageopen, imageopen_forPIL

#initialize the pygame library/engine
pygame.init()
#Boolean to keep the main game loop running
done = False

#Variables for game logic
doneC=False   #A looping variable for the shuffling logic
myCard=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]  #An array to hold the values of the cards
myLogic=[0, 0, 0, 0, 0, 0, 0, 0] #Makes sure cards aren't placed more than once during a shuffle.
m=0 #Counter variable for shuffling
k=0 #Counter variable for checking win condition.
click_throttle = 0
click_delay = 2000 #wait 2 full seconds between clicks
wait_time = 100
kickout=0 #Method to check vicory clause
WHITE = (255,255,255)
TEXTCOLOR = (67, 118, 45)

#Holder values for matching check
temp=0 #Variable that holds the last clicked card.
tempName="None" #Variable that holds a string related to the last clicked value.
match=[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False] #Array that holds which cards are matched.

#To manage how fast to update the screen
clock = pygame.time.Clock()

#Load the image using PIL as well to determine width and height of picture
imgPIL = imageopen_forPIL()

#Use pygame to load the image
im = imageopen()
cardBack = pygame.image.load(im)

#Find width and height of  image
imgSize = imgPIL.size

#Victory Picture to be loaded
victory = pygame.image.load("victory2.jpg")

#Victory Flag that, when it is true you win
vict = False

#Mouse variable to hold location of mouse as a tuple (in an array)
mouse_pos = [0,0]

#Divider of background image logic
threefourthswidth = imgSize[0] * 0.75
onefourthswidth = imgSize[0] * 0.25
onefourthsheight = imgSize[1] * 0.25
threefourthsheight = imgSize[1] * 0.75
halfwidth = imgSize[0] / 2
halfheight = imgSize[1] / 2

#Card switches/flags
#When flag is true the card is "flipped"
Card1 = False
Card2 = False
Card3 = False
Card4 = False
Card5 = False
Card6 = False
Card7 = False
Card8 = False
Card9 = False
Card10 = False
Card11 = False
Card12 = False
Card13 = False
Card14 = False
Card15 = False
Card16 = False

#Regions
#Card 1
area1x_start = 0
area1x_end = onefourthswidth
area1y_start = 0
area1y_end = onefourthsheight

#Card 2
area2x_start = onefourthswidth + 1
area2x_end = halfwidth
area2y_start = 0
area2y_end = 2 * onefourthsheight

#Card 3
area3x_start = halfwidth + 1
area3x_end = halfwidth + onefourthswidth
area3y_start = 0
area3y_end = onefourthsheight

#Card 4
area4x_start = halfwidth + onefourthswidth + 1
area4x_end = halfwidth + halfwidth
area4y_start = 0
area4y_end = onefourthsheight

#Card 5
area5x_start = 0
area5x_end = onefourthswidth
area5y_start = onefourthsheight + 1
area5y_end = halfheight

#Card 6
area6x_start = onefourthswidth + 1
area6x_end = halfwidth
area6y_start = onefourthsheight + 1
area6y_end = halfheight

#Card 7
area7x_start = halfwidth + 1
area7x_end = halfwidth + onefourthswidth
area7y_start = onefourthsheight + 1
area7y_end = halfheight

#Card 8
area8x_start = halfwidth + onefourthswidth + 1
area8x_end = halfwidth + halfwidth
area8y_start = onefourthsheight + 1
area8y_end = halfheight

#Card 9
area9x_start = 0
area9x_end = onefourthswidth
area9y_start = halfheight + 1
area9y_end = halfheight + onefourthsheight

#Card 10
area10x_start = onefourthswidth + 1
area10x_end = halfwidth
area10y_start = halfheight + 1
area10y_end = halfheight + onefourthsheight

#Card 11
area11x_start = halfwidth + 1
area11x_end = halfwidth + onefourthswidth
area11y_start = halfheight + 1
area11y_end = halfheight + onefourthsheight

#Card 12
area12x_start = halfwidth + onefourthswidth + 1
area12x_end = halfwidth + halfwidth
area12y_start = halfheight + 1
area12y_end = halfheight + onefourthsheight

#Card 13
area13x_start = 0
area13x_end = onefourthswidth
area13y_start = halfheight + onefourthsheight
area13y_end = halfheight + halfheight

#Card 14
area14x_start = onefourthswidth + 1
area14x_end = halfwidth
area14y_start = halfheight + onefourthsheight
area14y_end = halfheight + halfheight

#Card 15
area15x_start = halfwidth + 1
area15x_end = halfwidth + onefourthswidth
area15y_start = halfheight + onefourthsheight
area15y_end = halfheight + halfheight

#Card 16
area16x_start = halfwidth + onefourthswidth
area16x_end = halfwidth + halfwidth
area16y_start = halfheight + onefourthsheight
area16y_end = halfheight + halfheight

#Set size of the window
screen = pygame.display.set_mode(imgSize)

#set the game window title
pygame.display.set_caption("Epic Time Machine Matching Game That Deserves an A+ Grade")

#-------Main Program Loop-------------

#--ALL EVENT PROCESSING BELOW THIS LINE----

#While the bool variable (done) is still False (Game is still going)
#Keep the main game loop going

while not done:
    #Keep checking to see if the user did something
    for event in pygame.event.get():
        #If the event that happened was a quit command
        if event.type == pygame.QUIT:
            done = True
        #if you press the left mouse button
        if (pygame.mouse.get_pressed()[0]):
            #store the x and y coordinates of the mouse into an array variable
            mouse_pos = pygame.mouse.get_pos()

#---ALL EVENT PROCESSING ABOVE THIS LINE---

#---ALL GAME LOGIC BELOW THIS LINE ---
    for e in myCard:
        if m<e:
            while not doneC:
                myCard[m]=randint(1,8)

                #Code for setting up pairs to be plaed on the board.
                if(myCard[m]==1):
                    if(myLogic[0]<2):
                        myLogic[0]+=1
                        doneC=True
                if(myCard[m]==2):
                    if(myLogic[1]<2):
                        myLogic[1]+=1
                        doneC=True
                if(myCard[m]==3):
                    if(myLogic[2]<2):
                        myLogic[2]+=1
                        doneC=True
                if(myCard[m]==4):
                    if(myLogic[3]<2):
                        myLogic[3]+=1
                        doneC=True
                if(myCard[m]==5):
                    if(myLogic[4]<2):
                        myLogic[4]+=1
                        doneC=True
                if(myCard[m]==6):
                    if(myLogic[5]<2):
                        myLogic[5]+=1
                        doneC=True
                if(myCard[m]==7):
                    if(myLogic[6]<2):
                        myLogic[6]+=1
                        doneC=True
                if(myCard[m]==8):
                    if(myLogic[7]<2):
                        myLogic[7]+=1
                        doneC=True
            #Debug code shows all the assigned values.
            #print "Card ", m+1, " ",  myCard[m]
            m+=1
            doneC=False
    #Check to see where the mouse click happened.
    if(pygame.mouse.get_pressed()[0]) and click_throttle == 0:
        if (mouse_pos[0] >= area1x_start and mouse_pos[0] <= area1x_end):
            if (mouse_pos[1] >= area1y_start and mouse_pos[1] <= area1y_end):
                #Check to make sure card hasn't been matched already.
                if(match[0]!=True):
                    #Set show card to true.
                    Card1 = True
                    #If first card selected remember it.
                    if(temp==0):
                        temp=myCard[0]
                        pygame.time.wait(wait_time)
                        tempName="card1"
                    #If second card see if it matches the first.
                    elif(myCard[0]==temp):
                        if(tempName!="card1"):
                            match[0]=True
                            if(tempName=="card2"):
                                match[1]=True
                            if(tempName=="card3"):
                                match[2]=True
                            if(tempName=="card4"):
                                match[3]=True
                            if(tempName=="card5"):
                                match[4]=True
                            if(tempName=="card6"):
                                match[5]=True
                            if(tempName=="card7"):
                                match[6]=True
                            if(tempName=="card8"):
                                match[7]=True
                            if(tempName=="card9"):
                                match[8]=True
                            if(tempName=="card10"):
                                match[9]=True
                            if(tempName=="card11"):
                                match[10]=True
                            if(tempName=="card12"):
                                match[11]=True
                            if(tempName=="card13"):
                                match[12]=True
                            if(tempName=="card14"):
                                match[13]=True
                            if(tempName=="card15"):
                                match[14]=True
                            if(tempName=="card16"):
                                match[15]=True
                            #reset the value
                            temp=0
                            pygame.time.wait(wait_time)
                            tempName="None"
                    #If the cards don't match do this.
                    elif(temp!=myCard[0] and match[0] != True):
                        Card1=False
                        if(tempName=="card2"):
                                Card2=False
                        if(tempName=="card3"):
                                Card3=False
                        if(tempName=="card4"):
                                Card4=False
                        if(tempName=="card5"):
                                Card5=False
                        if(tempName=="card6"):
                                Card6=False
                        if(tempName=="card7"):
                                Card7=False
                        if(tempName=="card8"):
                                Card8=False
                        if(tempName=="card9"):
                                Card9=False
                        if(tempName=="card10"):
                                Card10=False
                        if(tempName=="card11"):
                                Card11=False
                        if(tempName=="card12"):
                                Card12=False
                        if(tempName=="card13"):
                                Card13=False
                        if(tempName=="card14"):
                                Card14=False
                        if(tempName=="card15"):
                                Card15=False
                        if(tempName=="card16"):
                                Card16=False
                        temp=0
                        pygame.time.wait(wait_time)
                        tempName="None"
        #Following code is the same structure as above.
        if (mouse_pos[0] >= area2x_start and mouse_pos[0] <= area2x_end):
            if (mouse_pos[1] >= area2y_start and mouse_pos[1] <= area2y_end):
                if(match[1]!=True):
                    Card2 = True
                    if(temp==0 and match[1]!=True):
                        temp=myCard[1]
                        pygame.time.wait(wait_time)
                        tempName="card2"
                    elif(myCard[1]==temp and match[1]!=True):
                        if(tempName!="card2"):
                            match[1]=True
                            if(tempName=="card1"):
                                match[0]=True
                            if(tempName=="card3"):
                                match[2]=True
                            if(tempName=="card4"):
                                match[3]=True
                            if(tempName=="card5"):
                                match[4]=True
                            if(tempName=="card6"):
                                match[5]=True
                            if(tempName=="card7"):
                                match[6]=True
                            if(tempName=="card8"):
                                match[7]=True
                            if(tempName=="card9"):
                                match[8]=True
                            if(tempName=="card10"):
                                match[9]=True
                            if(tempName=="card11"):
                                match[10]=True
                            if(tempName=="card12"):
                                match[11]=True
                            if(tempName=="card13"):
                                match[12]=True
                            if(tempName=="card14"):
                                match[13]=True
                            if(tempName=="card15"):
                                match[14]=True
                            if(tempName=="card16"):
                                match[15]=True
                            temp=0
                            pygame.time.wait(wait_time)
                            tempName="None"
                    elif(temp!=myCard[1] and match[1]!=True):
                        Card2=False
                        if(tempName=="card1"):
                                Card1=False
                        if(tempName=="card3"):
                                Card3=False
                        if(tempName=="card4"):
                                Card4=False
                        if(tempName=="card5"):
                                Card5=False
                        if(tempName=="card6"):
                                Card6=False
                        if(tempName=="card7"):
                                Card7=False
                        if(tempName=="card8"):
                                Card8=False
                        if(tempName=="card9"):
                                Card9=False
                        if(tempName=="card10"):
                                Card10=False
                        if(tempName=="card11"):
                                Card11=False
                        if(tempName=="card12"):
                                Card12=False
                        if(tempName=="card13"):
                                Card13=False
                        if(tempName=="card14"):
                                Card14=False
                        if(tempName=="card15"):
                                Card15=False
                        if(tempName=="card16"):
                                Card16=False
                        temp=0
                        pygame.time.wait(wait_time)
                        tempName="None"
        if (mouse_pos[0] >= area3x_start and mouse_pos[0] <= area3x_end):
            if (mouse_pos[1] >= area3y_start and mouse_pos[1] <= area3y_end):
                if(match[2]!=True):
                    Card3 = True
                    if(temp==0):
                        temp=myCard[2]
                        pygame.time.wait(wait_time)
                        tempName="card3"
                    elif(myCard[2]==temp):
                        if(tempName!="card3"):
                            match[2]=True
                            if(tempName=="card2"):
                                match[1]=True
                            if(tempName=="card1"):
                                match[0]=True
                            if(tempName=="card4"):
                                match[3]=True
                            if(tempName=="card5"):
                                match[4]=True
                            if(tempName=="card6"):
                                match[5]=True
                            if(tempName=="card7"):
                                match[6]=True
                            if(tempName=="card8"):
                                match[7]=True
                            if(tempName=="card9"):
                                match[8]=True
                            if(tempName=="card10"):
                                match[9]=True
                            if(tempName=="card11"):
                                match[10]=True
                            if(tempName=="card12"):
                                match[11]=True
                            if(tempName=="card13"):
                                match[12]=True
                            if(tempName=="card14"):
                                match[13]=True
                            if(tempName=="card15"):
                                match[14]=True
                            if(tempName=="card16"):
                                match[15]=True
                            temp=0
                            pygame.time.wait(wait_time)
                            tempName="None"
                    elif(temp!=myCard[2] and match[2] != True):
                        Card3=False
                        if(tempName=="card2"):
                                Card2=False
                        if(tempName=="card1"):
                                Card1=False
                        if(tempName=="card4"):
                                Card4=False
                        if(tempName=="card5"):
                                Card5=False
                        if(tempName=="card6"):
                                Card6=False
                        if(tempName=="card7"):
                                Card7=False
                        if(tempName=="card8"):
                                Card8=False
                        if(tempName=="card9"):
                                Card9=False
                        if(tempName=="card10"):
                                Card10=False
                        if(tempName=="card11"):
                                Card11=False
                        if(tempName=="card12"):
                                Card12=False
                        if(tempName=="card13"):
                                Card13=False
                        if(tempName=="card14"):
                                Card14=False
                        if(tempName=="card15"):
                                Card15=False
                        if(tempName=="card16"):
                                Card16=False
                        temp=0
                        pygame.time.wait(wait_time)
                        tempName="None"
        if (mouse_pos[0] >= area4x_start and mouse_pos[0] <= area4x_end):
            if (mouse_pos[1] >= area4y_start and mouse_pos[1] <= area4y_end):
                if(match[3]!=True):
                    Card4 = True
                    if(temp==0):
                        temp=myCard[3]
                        pygame.time.wait(wait_time)
                        tempName="card4"
                    elif(myCard[3]==temp):
                        if(tempName!="card4"):
                            match[3]=True
                            if(tempName=="card2"):
                                match[1]=True
                            if(tempName=="card1"):
                                match[0]=True
                            if(tempName=="card3"):
                                match[2]=True
                            if(tempName=="card5"):
                                match[4]=True
                            if(tempName=="card6"):
                                match[5]=True
                            if(tempName=="card7"):
                                match[6]=True
                            if(tempName=="card8"):
                                match[7]=True
                            if(tempName=="card9"):
                                match[8]=True
                            if(tempName=="card10"):
                                match[9]=True
                            if(tempName=="card11"):
                                match[10]=True
                            if(tempName=="card12"):
                                match[11]=True
                            if(tempName=="card13"):
                                match[12]=True
                            if(tempName=="card14"):
                                match[13]=True
                            if(tempName=="card15"):
                                match[14]=True
                            if(tempName=="card16"):
                                match[15]=True
                            temp=0
                            pygame.time.wait(wait_time)
                            tempName="None"
                    elif(temp!=myCard[3] and match[3] != True):
                        Card4=False
                        if(tempName=="card2"):
                                Card2=False
                        if(tempName=="card1"):
                                Card1=False
                        if(tempName=="card3"):
                                Card3=False
                        if(tempName=="card5"):
                                Card5=False
                        if(tempName=="card6"):
                                Card6=False
                        if(tempName=="card7"):
                                Card7=False
                        if(tempName=="card8"):
                                Card8=False
                        if(tempName=="card9"):
                                Card9=False
                        if(tempName=="card10"):
                                Card10=False
                        if(tempName=="card11"):
                                Card11=False
                        if(tempName=="card12"):
                                Card12=False
                        if(tempName=="card13"):
                                Card13=False
                        if(tempName=="card14"):
                                Card14=False
                        if(tempName=="card15"):
                                Card15=False
                        if(tempName=="card16"):
                                Card16=False
                        temp=0
                        pygame.time.wait(wait_time)
                        tempName="None"
        if (mouse_pos[0] >= area5x_start and mouse_pos[0] <= area5x_end):
            if (mouse_pos[1] >= area5y_start and mouse_pos[1] <= area5y_end):
                if(match[4]!=True):
                    Card5 = True
                    if(temp==0):
                        temp=myCard[4]
                        pygame.time.wait(wait_time)
                        tempName="card5"
                    elif(myCard[4]==temp):
                        if(tempName!="card5"):
                            match[4]=True
                            if(tempName=="card2"):
                                match[1]=True
                            if(tempName=="card1"):
                                match[0]=True
                            if(tempName=="card3"):
                                match[2]=True
                            if(tempName=="card5"):
                                match[4]=True
                            if(tempName=="card6"):
                                match[5]=True
                            if(tempName=="card7"):
                                match[6]=True
                            if(tempName=="card8"):
                                match[7]=True
                            if(tempName=="card9"):
                                match[8]=True
                            if(tempName=="card10"):
                                match[9]=True
                            if(tempName=="card11"):
                                match[10]=True
                            if(tempName=="card12"):
                                match[11]=True
                            if(tempName=="card13"):
                                match[12]=True
                            if(tempName=="card14"):
                                match[13]=True
                            if(tempName=="card15"):
                                match[14]=True
                            if(tempName=="card16"):
                                match[15]=True
                            temp=0
                            pygame.time.wait(wait_time)
                            tempName="None"
                    elif(temp!=myCard[4] and match[4] != True):
                        Card5=False
                        if(tempName=="card2"):
                                Card2=False
                        if(tempName=="card1"):
                                Card1=False
                        if(tempName=="card3"):
                                Card3=False
                        if(tempName=="card4"):
                                Card4=False
                        if(tempName=="card6"):
                                Card6=False
                        if(tempName=="card7"):
                                Card7=False
                        if(tempName=="card8"):
                                Card8=False
                        if(tempName=="card9"):
                                Card9=False
                        if(tempName=="card10"):
                                Card10=False
                        if(tempName=="card11"):
                                Card11=False
                        if(tempName=="card12"):
                                Card12=False
                        if(tempName=="card13"):
                                Card13=False
                        if(tempName=="card14"):
                                Card14=False
                        if(tempName=="card15"):
                                Card15=False
                        if(tempName=="card16"):
                                Card16=False
                        temp=0
                        pygame.time.wait(wait_time)
                        tempName="None"
        if (mouse_pos[0] >= area6x_start and mouse_pos[0] <= area6x_end):
            if (mouse_pos[1] >= area6y_start and mouse_pos[1] <= area6y_end):
                if(match[5]!=True):
                    Card6 = True
                    if(temp==0):
                        temp=myCard[5]
                        pygame.time.wait(wait_time)
                        tempName="card6"
                    elif(myCard[5]==temp):
                        if(tempName!="card6"):
                            match[5]=True
                            if(tempName=="card2"):
                                match[1]=True
                            if(tempName=="card1"):
                                match[0]=True
                            if(tempName=="card3"):
                                match[2]=True
                            if(tempName=="card4"):
                                match[3]=True
                            if(tempName=="card5"):
                                match[4]=True
                            if(tempName=="card7"):
                                match[6]=True
                            if(tempName=="card8"):
                                match[7]=True
                            if(tempName=="card9"):
                                match[8]=True
                            if(tempName=="card10"):
                                match[9]=True
                            if(tempName=="card11"):
                                match[10]=True
                            if(tempName=="card12"):
                                match[11]=True
                            if(tempName=="card13"):
                                match[12]=True
                            if(tempName=="card14"):
                                match[13]=True
                            if(tempName=="card15"):
                                match[14]=True
                            if(tempName=="card16"):
                                match[15]=True
                            temp=0
                            pygame.time.wait(wait_time)
                            tempName="None"
                    elif(temp!=myCard[5] and match[5] != True):
                        Card6=False
                        if(tempName=="card2"):
                                Card2=False
                        if(tempName=="card1"):
                                Card1=False
                        if(tempName=="card3"):
                                Card3=False
                        if(tempName=="card5"):
                                Card5=False
                        if(tempName=="card4"):
                                Card4=False
                        if(tempName=="card7"):
                                Card7=False
                        if(tempName=="card8"):
                                Card8=False
                        if(tempName=="card9"):
                                Card9=False
                        if(tempName=="card10"):
                                Card10=False
                        if(tempName=="card11"):
                                Card11=False
                        if(tempName=="card12"):
                                Card12=False
                        if(tempName=="card13"):
                                Card13=False
                        if(tempName=="card14"):
                                Card14=False
                        if(tempName=="card15"):
                                Card15=False
                        if(tempName=="card16"):
                                Card16=False
                        temp=0
                        pygame.time.wait(wait_time)
                        tempName="None"
        if (mouse_pos[0] >= area7x_start and mouse_pos[0] <= area7x_end):
            if (mouse_pos[1] >= area7y_start and mouse_pos[1] <= area7y_end):
                if(match[6]!=True):
                    Card7 = True
                    if(temp==0):
                        temp=myCard[6]
                        pygame.time.wait(wait_time)
                        tempName="card7"
                    elif(myCard[6]==temp):
                        if(tempName!="card7"):
                            match[6]=True
                            if(tempName=="card2"):
                                match[1]=True
                            if(tempName=="card1"):
                                match[0]=True
                            if(tempName=="card3"):
                                match[2]=True
                            if(tempName=="card5"):
                                match[4]=True
                            if(tempName=="card6"):
                                match[5]=True
                            if(tempName=="card4"):
                                match[3]=True
                            if(tempName=="card8"):
                                match[7]=True
                            if(tempName=="card9"):
                                match[8]=True
                            if(tempName=="card10"):
                                match[9]=True
                            if(tempName=="card11"):
                                match[10]=True
                            if(tempName=="card12"):
                                match[11]=True
                            if(tempName=="card13"):
                                match[12]=True
                            if(tempName=="card14"):
                                match[13]=True
                            if(tempName=="card15"):
                                match[14]=True
                            if(tempName=="card16"):
                                match[15]=True
                            temp=0
                            pygame.time.wait(wait_time)
                            tempName="None"
                    elif(temp!=myCard[6] and match[6] != True):
                        Card7=False
                        if(tempName=="card2"):
                                Card2=False
                        if(tempName=="card1"):
                                Card1=False
                        if(tempName=="card3"):
                                Card3=False
                        if(tempName=="card5"):
                                Card5=False
                        if(tempName=="card6"):
                                Card6=False
                        if(tempName=="card7"):
                                Card7=False
                        if(tempName=="card8"):
                                Card8=False
                        if(tempName=="card9"):
                                Card9=False
                        if(tempName=="card10"):
                                Card10=False
                        if(tempName=="card11"):
                                Card11=False
                        if(tempName=="card12"):
                                Card12=False
                        if(tempName=="card13"):
                                Card13=False
                        if(tempName=="card14"):
                                Card14=False
                        if(tempName=="card15"):
                                Card15=False
                        if(tempName=="card16"):
                                Card16=False
                        temp=0
                        pygame.time.wait(wait_time)
                        tempName="None"
        if (mouse_pos[0] >= area8x_start and mouse_pos[0] <= area8x_end):
            if (mouse_pos[1] >= area8y_start and mouse_pos[1] <= area8y_end):
                if(match[7]!=True):
                    Card8 = True
                    if(temp==0):
                        temp=myCard[7]
                        pygame.time.wait(wait_time)
                        tempName="card8"
                    elif(myCard[7]==temp):
                        if(tempName!="card8"):
                            match[7]=True
                            if(tempName=="card2"):
                                match[1]=True
                            if(tempName=="card1"):
                                match[0]=True
                            if(tempName=="card3"):
                                match[2]=True
                            if(tempName=="card5"):
                                match[4]=True
                            if(tempName=="card6"):
                                match[5]=True
                            if(tempName=="card7"):
                                match[6]=True
                            if(tempName=="card4"):
                                match[3]=True
                            if(tempName=="card9"):
                                match[8]=True
                            if(tempName=="card10"):
                                match[9]=True
                            if(tempName=="card11"):
                                match[10]=True
                            if(tempName=="card12"):
                                match[11]=True
                            if(tempName=="card13"):
                                match[12]=True
                            if(tempName=="card14"):
                                match[13]=True
                            if(tempName=="card15"):
                                match[14]=True
                            if(tempName=="card16"):
                                match[15]=True
                            temp=0
                            pygame.time.wait(wait_time)
                            tempName="None"
                    elif(temp!=myCard[7] and match[7] != True):
                        Card8=False
                        if(tempName=="card2"):
                                Card2=False
                        if(tempName=="card1"):
                                Card1=False
                        if(tempName=="card3"):
                                Card3=False
                        if(tempName=="card5"):
                                Card5=False
                        if(tempName=="card6"):
                                Card6=False
                        if(tempName=="card7"):
                                Card7=False
                        if(tempName=="card8"):
                                Card8=False
                        if(tempName=="card9"):
                                Card9=False
                        if(tempName=="card10"):
                                Card10=False
                        if(tempName=="card11"):
                                Card11=False
                        if(tempName=="card12"):
                                Card12=False
                        if(tempName=="card13"):
                                Card13=False
                        if(tempName=="card14"):
                                Card14=False
                        if(tempName=="card15"):
                                Card15=False
                        if(tempName=="card16"):
                                Card16=False
                        temp=0
                        pygame.time.wait(wait_time)
                        tempName="None"
        if (mouse_pos[0] >= area9x_start and mouse_pos[0] <= area9x_end):
            if (mouse_pos[1] >= area9y_start and mouse_pos[1] <= area9y_end):
                if(match[8]!=True):
                    Card9 = True
                    if(temp==0):
                        temp=myCard[8]
                        pygame.time.wait(wait_time)
                        tempName="card9"
                    elif(myCard[8]==temp):
                        if(tempName!="card9"):
                            match[8]=True
                            if(tempName=="card2"):
                                match[1]=True
                            if(tempName=="card1"):
                                match[0]=True
                            if(tempName=="card3"):
                                match[2]=True
                            if(tempName=="card5"):
                                match[4]=True
                            if(tempName=="card6"):
                                match[5]=True
                            if(tempName=="card7"):
                                match[6]=True
                            if(tempName=="card8"):
                                match[7]=True
                            if(tempName=="card4"):
                                match[3]=True
                            if(tempName=="card10"):
                                match[9]=True
                            if(tempName=="card11"):
                                match[10]=True
                            if(tempName=="card12"):
                                match[11]=True
                            if(tempName=="card13"):
                                match[12]=True
                            if(tempName=="card14"):
                                match[13]=True
                            if(tempName=="card15"):
                                match[14]=True
                            if(tempName=="card16"):
                                match[15]=True
                            temp=0
                            pygame.time.wait(wait_time)
                            tempName="None"
                    elif(temp!=myCard[8] and match[8] != True):
                        Card9=False
                        if(tempName=="card2"):
                                Card2=False
                        if(tempName=="card1"):
                                Card1=False
                        if(tempName=="card3"):
                                Card3=False
                        if(tempName=="card5"):
                                Card5=False
                        if(tempName=="card6"):
                                Card6=False
                        if(tempName=="card7"):
                                Card7=False
                        if(tempName=="card8"):
                                Card8=False
                        if(tempName=="card4"):
                                Card4=False
                        if(tempName=="card10"):
                                Card10=False
                        if(tempName=="card11"):
                                Card11=False
                        if(tempName=="card12"):
                                Card12=False
                        if(tempName=="card13"):
                                Card13=False
                        if(tempName=="card14"):
                                Card14=False
                        if(tempName=="card15"):
                                Card15=False
                        if(tempName=="card16"):
                                Card16=False
                        temp=0
                        pygame.time.wait(wait_time)
                        tempName="None"
        if (mouse_pos[0] >= area10x_start and mouse_pos[0] <= area10x_end):
            if (mouse_pos[1] >= area10y_start and mouse_pos[1] <= area10y_end):
                if(match[9]!=True):
                    Card10 = True
                    if(temp==0):
                        temp=myCard[9]
                        pygame.time.wait(wait_time)
                        tempName="card10"
                    elif(myCard[9]==temp):
                        if(tempName!="card10"):
                            match[9]=True
                            if(tempName=="card2"):
                                match[1]=True
                            if(tempName=="card1"):
                                match[0]=True
                            if(tempName=="card3"):
                                match[2]=True
                            if(tempName=="card5"):
                                match[4]=True
                            if(tempName=="card6"):
                                match[5]=True
                            if(tempName=="card7"):
                                match[6]=True
                            if(tempName=="card8"):
                                match[7]=True
                            if(tempName=="card9"):
                                match[8]=True
                            if(tempName=="card4"):
                                match[3]=True
                            if(tempName=="card11"):
                                match[10]=True
                            if(tempName=="card12"):
                                match[11]=True
                            if(tempName=="card13"):
                                match[12]=True
                            if(tempName=="card14"):
                                match[13]=True
                            if(tempName=="card15"):
                                match[14]=True
                            if(tempName=="card16"):
                                match[15]=True
                            temp=0
                            pygame.time.wait(wait_time)
                            tempName="None"
                    elif(temp!=myCard[9] and match[9] != True):
                        Card10=False
                        if(tempName=="card2"):
                                Card2=False
                        if(tempName=="card1"):
                                Card1=False
                        if(tempName=="card3"):
                                Card3=False
                        if(tempName=="card5"):
                                Card5=False
                        if(tempName=="card6"):
                                Card6=False
                        if(tempName=="card7"):
                                Card7=False
                        if(tempName=="card8"):
                                Card8=False
                        if(tempName=="card9"):
                                Card9=False
                        if(tempName=="card4"):
                                Card4=False
                        if(tempName=="card11"):
                                Card11=False
                        if(tempName=="card12"):
                                Card12=False
                        if(tempName=="card13"):
                                Card13=False
                        if(tempName=="card14"):
                                Card14=False
                        if(tempName=="card15"):
                                Card15=False
                        if(tempName=="card16"):
                                Card16=False
                        temp=0
                        pygame.time.wait(wait_time)
                        tempName="None"
        if (mouse_pos[0] >= area11x_start and mouse_pos[0] <= area11x_end):
            if (mouse_pos[1] >= area11y_start and mouse_pos[1] <= area11y_end):
                if(match[10]!=True):
                    Card11 = True
                    if(temp==0):
                        temp=myCard[10]
                        pygame.time.wait(wait_time)
                        tempName="card11"
                    elif(myCard[10]==temp):
                        if(tempName!="card11"):
                            match[10]=True
                            if(tempName=="card2"):
                                match[1]=True
                            if(tempName=="card1"):
                                match[0]=True
                            if(tempName=="card3"):
                                match[2]=True
                            if(tempName=="card5"):
                                match[4]=True
                            if(tempName=="card6"):
                                match[5]=True
                            if(tempName=="card7"):
                                match[6]=True
                            if(tempName=="card8"):
                                match[7]=True
                            if(tempName=="card9"):
                                match[8]=True
                            if(tempName=="card10"):
                                match[9]=True
                            if(tempName=="card4"):
                                match[3]=True
                            if(tempName=="card12"):
                                match[11]=True
                            if(tempName=="card13"):
                                match[12]=True
                            if(tempName=="card14"):
                                match[13]=True
                            if(tempName=="card15"):
                                match[14]=True
                            if(tempName=="card16"):
                                match[15]=True
                            temp=0
                            pygame.time.wait(wait_time)
                            tempName="None"
                    elif(temp!=myCard[10] and match[10] != True):
                        Card11=False
                        if(tempName=="card2"):
                                Card2=False
                        if(tempName=="card1"):
                                Card1=False
                        if(tempName=="card3"):
                                Card3=False
                        if(tempName=="card5"):
                                Card5=False
                        if(tempName=="card6"):
                                Card6=False
                        if(tempName=="card7"):
                                Card7=False
                        if(tempName=="card8"):
                                Card8=False
                        if(tempName=="card9"):
                                Card9=False
                        if(tempName=="card10"):
                                Card10=False
                        if(tempName=="card4"):
                                Card4=False
                        if(tempName=="card12"):
                                Card12=False
                        if(tempName=="card13"):
                                Card13=False
                        if(tempName=="card14"):
                                Card14=False
                        if(tempName=="card15"):
                                Card15=False
                        if(tempName=="card16"):
                                Card16=False
                        temp=0
                        pygame.time.wait(wait_time)
                        tempName="None"
        if (mouse_pos[0] >= area12x_start and mouse_pos[0] <= area12x_end):
            if (mouse_pos[1] >= area12y_start and mouse_pos[1] <= area12y_end):
                if(match[11]!=True):
                    Card12 = True
                    if(temp==0):
                        temp=myCard[11]
                        pygame.time.wait(wait_time)
                        tempName="card12"
                    elif(myCard[11]==temp):
                        if(tempName!="card12"):
                            match[11]=True
                            if(tempName=="card2"):
                                match[1]=True
                            if(tempName=="card1"):
                                match[0]=True
                            if(tempName=="card3"):
                                match[2]=True
                            if(tempName=="card5"):
                                match[4]=True
                            if(tempName=="card6"):
                                match[5]=True
                            if(tempName=="card7"):
                                match[6]=True
                            if(tempName=="card8"):
                                match[7]=True
                            if(tempName=="card9"):
                                match[8]=True
                            if(tempName=="card10"):
                                match[9]=True
                            if(tempName=="card11"):
                                match[10]=True
                            if(tempName=="card4"):
                                match[3]=True
                            if(tempName=="card13"):
                                match[12]=True
                            if(tempName=="card14"):
                                match[13]=True
                            if(tempName=="card15"):
                                match[14]=True
                            if(tempName=="card16"):
                                match[15]=True
                            temp=0
                            pygame.time.wait(wait_time)
                            tempName="None"
                    elif(temp!=myCard[11] and match[11] != True):
                        Card12=False
                        if(tempName=="card2"):
                                Card2=False
                        if(tempName=="card1"):
                                Card1=False
                        if(tempName=="card3"):
                                Card3=False
                        if(tempName=="card5"):
                                Card5=False
                        if(tempName=="card6"):
                                Card6=False
                        if(tempName=="card7"):
                                Card7=False
                        if(tempName=="card8"):
                                Card8=False
                        if(tempName=="card9"):
                                Card9=False
                        if(tempName=="card10"):
                                Card10=False
                        if(tempName=="card11"):
                                Card11=False
                        if(tempName=="card4"):
                                Card4=False
                        if(tempName=="card13"):
                                Card13=False
                        if(tempName=="card14"):
                                Card14=False
                        if(tempName=="card15"):
                                Card15=False
                        if(tempName=="card16"):
                                Card16=False
                        temp=0
                        pygame.time.wait(wait_time)
                        tempName="None"
        if (mouse_pos[0] >= area13x_start and mouse_pos[0] <= area13x_end):
            if (mouse_pos[1] >= area13y_start and mouse_pos[1] <= area13y_end):
                if(match[12]!=True):
                    Card13 = True
                    if(temp==0):
                        temp=myCard[12]
                        pygame.time.wait(wait_time)
                        tempName="card13"
                    elif(myCard[12]==temp):
                        if(tempName!="card13"):
                            match[12]=True
                            if(tempName=="card2"):
                                match[1]=True
                            if(tempName=="card1"):
                                match[0]=True
                            if(tempName=="card3"):
                                match[2]=True
                            if(tempName=="card5"):
                                match[4]=True
                            if(tempName=="card6"):
                                match[5]=True
                            if(tempName=="card7"):
                                match[6]=True
                            if(tempName=="card8"):
                                match[7]=True
                            if(tempName=="card9"):
                                match[8]=True
                            if(tempName=="card10"):
                                match[9]=True
                            if(tempName=="card11"):
                                match[10]=True
                            if(tempName=="card12"):
                                match[11]=True
                            if(tempName=="card4"):
                                match[3]=True
                            if(tempName=="card14"):
                                match[13]=True
                            if(tempName=="card15"):
                                match[14]=True
                            if(tempName=="card16"):
                                match[15]=True
                            temp=0
                            pygame.time.wait(wait_time)
                            tempName="None"
                    elif(temp!=myCard[12] and match[12] != True):
                        Card13=False
                        if(tempName=="card2"):
                                Card2=False
                        if(tempName=="card1"):
                                Card1=False
                        if(tempName=="card3"):
                                Card3=False
                        if(tempName=="card5"):
                                Card5=False
                        if(tempName=="card6"):
                                Card6=False
                        if(tempName=="card7"):
                                Card7=False
                        if(tempName=="card8"):
                                Card8=False
                        if(tempName=="card9"):
                                Card9=False
                        if(tempName=="card10"):
                                Card10=False
                        if(tempName=="card11"):
                                Card11=False
                        if(tempName=="card12"):
                                Card12=False
                        if(tempName=="card4"):
                                Card4=False
                        if(tempName=="card14"):
                                Card14=False
                        if(tempName=="card15"):
                                Card15=False
                        if(tempName=="card16"):
                                Card16=False
                        temp=0
                        pygame.time.wait(wait_time)
                        tempName="None"
        if (mouse_pos[0] >= area14x_start and mouse_pos[0] <= area14x_end):
            if (mouse_pos[1] >= area14y_start and mouse_pos[1] <= area14y_end):
                if(match[13]!=True):
                    Card14 = True
                    if(temp==0):
                        temp=myCard[13]
                        pygame.time.wait(wait_time)
                        tempName="card14"
                    elif(myCard[13]==temp):
                        if(tempName!="card14"):
                            match[13]=True
                            if(tempName=="card2"):
                                match[1]=True
                            if(tempName=="card1"):
                                match[0]=True
                            if(tempName=="card3"):
                                match[2]=True
                            if(tempName=="card5"):
                                match[4]=True
                            if(tempName=="card6"):
                                match[5]=True
                            if(tempName=="card7"):
                                match[6]=True
                            if(tempName=="card8"):
                                match[7]=True
                            if(tempName=="card9"):
                                match[8]=True
                            if(tempName=="card10"):
                                match[9]=True
                            if(tempName=="card11"):
                                match[10]=True
                            if(tempName=="card12"):
                                match[11]=True
                            if(tempName=="card13"):
                                match[12]=True
                            if(tempName=="card4"):
                                match[3]=True
                            if(tempName=="card15"):
                                match[14]=True
                            if(tempName=="card16"):
                                match[15]=True
                            temp=0
                            pygame.time.wait(wait_time)
                            tempName="None"
                    elif(temp!=myCard[13] and match[13] != True):
                        Card14=False
                        if(tempName=="card2"):
                                Card2=False
                        if(tempName=="card1"):
                                Card1=False
                        if(tempName=="card3"):
                                Card3=False
                        if(tempName=="card5"):
                                Card5=False
                        if(tempName=="card6"):
                                Card6=False
                        if(tempName=="card7"):
                                Card7=False
                        if(tempName=="card8"):
                                Card8=False
                        if(tempName=="card9"):
                                Card9=False
                        if(tempName=="card10"):
                                Card10=False
                        if(tempName=="card11"):
                                Card11=False
                        if(tempName=="card12"):
                                Card12=False
                        if(tempName=="card13"):
                                Card13=False
                        if(tempName=="card4"):
                                Card4=False
                        if(tempName=="card15"):
                                Card15=False
                        if(tempName=="card16"):
                                Card16=False
                        temp=0
                        pygame.time.wait(wait_time)
                        tempName="None"
        if (mouse_pos[0] >= area15x_start and mouse_pos[0] <= area15x_end):
            if (mouse_pos[1] >= area15y_start and mouse_pos[1] <= area15y_end):
                if(match[14]!=True):
                    Card15 = True
                    if(temp==0):
                        temp=myCard[14]
                        pygame.time.wait(wait_time)
                        tempName="card15"
                    elif(myCard[14]==temp):
                        if(tempName!="card15"):
                            match[14]=True
                            if(tempName=="card2"):
                                match[1]=True
                            if(tempName=="card1"):
                                match[0]=True
                            if(tempName=="card3"):
                                match[2]=True
                            if(tempName=="card5"):
                                match[4]=True
                            if(tempName=="card6"):
                                match[5]=True
                            if(tempName=="card7"):
                                match[6]=True
                            if(tempName=="card8"):
                                match[7]=True
                            if(tempName=="card9"):
                                match[8]=True
                            if(tempName=="card10"):
                                match[9]=True
                            if(tempName=="card11"):
                                match[10]=True
                            if(tempName=="card12"):
                                match[11]=True
                            if(tempName=="card13"):
                                match[12]=True
                            if(tempName=="card14"):
                                match[13]=True
                            if(tempName=="card4"):
                                match[3]=True
                            if(tempName=="card16"):
                                match[15]=True
                            temp=0
                            pygame.time.wait(wait_time)
                            tempName="None"
                    elif(temp!=myCard[14] and match[14] != True):
                        Card15=False
                        if(tempName=="card2"):
                                Card2=False
                        if(tempName=="card1"):
                                Card1=False
                        if(tempName=="card3"):
                                Card3=False
                        if(tempName=="card5"):
                                Card5=False
                        if(tempName=="card6"):
                                Card6=False
                        if(tempName=="card7"):
                                Card7=False
                        if(tempName=="card8"):
                                Card8=False
                        if(tempName=="card9"):
                                Card9=False
                        if(tempName=="card10"):
                                Card10=False
                        if(tempName=="card11"):
                                Card11=False
                        if(tempName=="card12"):
                                Card12=False
                        if(tempName=="card13"):
                                Card13=False
                        if(tempName=="card14"):
                                Card14=False
                        if(tempName=="card4"):
                                Card4=False
                        if(tempName=="card16"):
                                Card16=False
                        temp=0
                        pygame.time.wait(wait_time)
                        tempName="None"
        if (mouse_pos[0] >= area16x_start and mouse_pos[0] <= area16x_end):
            if (mouse_pos[1] >= area16y_start and mouse_pos[1] <= area16y_end):
                if(match[15]!=True):
                    Card16 = True
                    if(temp==0):
                        temp=myCard[15]
                        pygame.time.wait(wait_time)
                        tempName="card16"
                    elif(myCard[15]==temp):
                        if(tempName!="card16"):
                            match[15]=True
                            if(tempName=="card2"):
                                match[1]=True
                            if(tempName=="card1"):
                                match[0]=True
                            if(tempName=="card3"):
                                match[2]=True
                            if(tempName=="card5"):
                                match[4]=True
                            if(tempName=="card6"):
                                match[5]=True
                            if(tempName=="card7"):
                                match[6]=True
                            if(tempName=="card8"):
                                match[7]=True
                            if(tempName=="card9"):
                                match[8]=True
                            if(tempName=="card10"):
                                match[9]=True
                            if(tempName=="card11"):
                                match[10]=True
                            if(tempName=="card12"):
                                match[11]=True
                            if(tempName=="card13"):
                                match[12]=True
                            if(tempName=="card14"):
                                match[13]=True
                            if(tempName=="card15"):
                                match[14]=True
                            if(tempName=="card4"):
                                match[3]=True
                            temp=0
                            pygame.time.wait(wait_time)
                            tempName="None"
                    elif(temp!=myCard[15] and match[15] != True):
                        Card16=False
                        if(tempName=="card2"):
                                Card2=False
                        if(tempName=="card1"):
                                Card1=False
                        if(tempName=="card3"):
                                Card3=False
                        if(tempName=="card5"):
                                Card5=False
                        if(tempName=="card6"):
                                Card6=False
                        if(tempName=="card7"):
                                Card7=False
                        if(tempName=="card8"):
                                Card8=False
                        if(tempName=="card9"):
                                Card9=False
                        if(tempName=="card10"):
                                Card10=False
                        if(tempName=="card11"):
                                Card11=False
                        if(tempName=="card12"):
                                Card12=False
                        if(tempName=="card13"):
                                Card13=False
                        if(tempName=="card14"):
                                Card14=False
                        if(tempName=="card15"):
                                Card15=False
                        if(tempName=="card4"):
                                Card4=False
                        temp=0
                        pygame.time.wait(wait_time)
                        tempName="None"
        #Logic to determine if all cards are flipped. If they are then the vict flag is set to true and the game is won.
        if Card1 == True and Card2 == True and Card3 == True and Card4 == True and Card5 == True and Card6 == True and Card7 == True and Card8 == True and Card9 == True and Card10 == True and Card11 == True and Card12 == True and Card13 == True and Card14 == True and Card15 == True and Card16 == True:
            vict = True

#---ALL GAME LOGIC ABOVE THIS LINE ---

#---ALL CODE TO DRAW BELOW THIS LINE ---

    #Clears the screen with white color
    screen.fill([0,0,0])
    #Make a font for the text (card values) on screen
    myFont = pygame.font.Font(None, 50)
    #Store the card values into a variable and eventually print them on screen depending on card value
    cardvaluetext_one = myFont.render("1", True, TEXTCOLOR)
    cardvaluetext_two = myFont.render("2", True, TEXTCOLOR)
    cardvaluetext_three = myFont.render("3", True, TEXTCOLOR)
    cardvaluetext_four = myFont.render("4", True, TEXTCOLOR)
    cardvaluetext_five = myFont.render("5", True, TEXTCOLOR)
    cardvaluetext_six = myFont.render("6", True, TEXTCOLOR)
    cardvaluetext_seven = myFont.render("7", True, TEXTCOLOR)
    cardvaluetext_eight = myFont.render("8", True, TEXTCOLOR)
    cardvaluetext_nine = myFont.render("9", True, TEXTCOLOR)
    cardvaluetext_ten = myFont.render("10", True, TEXTCOLOR)
    cardvaluetext_eleven = myFont.render("11", True, TEXTCOLOR)
    cardvaluetext_twelve = myFont.render("12", True, TEXTCOLOR)
    cardvaluetext_thirteen = myFont.render("13", True, TEXTCOLOR)
    cardvaluetext_fourteen = myFont.render("14", True, TEXTCOLOR)
    cardvaluetext_fifteen = myFont.render("15", True, TEXTCOLOR)
    cardvaluetext_sixteen = myFont.render("16", True, TEXTCOLOR)
    #Print the background image to the screen, to be used as the background for all the cards.
    screen.blit(cardBack, (0, 0, 0, 0))
    #Draw the width lines to divide up the picture
    pygame.draw.line(cardBack, [0,0,0], ((imgSize[0]/2), 0), (imgSize[0]/2, imgSize[1])) #middle cut
    pygame.draw.line(cardBack, [0,0,0], ((imgSize[0]/4), 0), (imgSize[0]/4, imgSize[1])) #left width cut
    pygame.draw.line(cardBack, [0,0,0], (threefourthswidth, 0), (threefourthswidth, imgSize[1])) #right width cut
    #Draw the horizontal lines to divide up the picture
    pygame.draw.line(cardBack, [0,0,0], (0, imgSize[1]/2), (imgSize[0], imgSize[1]/2)) #middle cut
    pygame.draw.line(cardBack, [0,0,0], (0, onefourthsheight), (imgSize[0], onefourthsheight)) #left width cut
    pygame.draw.line(cardBack, [0,0,0], (0, threefourthsheight), (imgSize[0], threefourthsheight)) #right width cut
    #If the Card flags are flipped, then draw the "front/value" of the card
    if Card1:
        pygame.draw.rect(screen, WHITE, (0,0, area1x_end, area1y_end))
        if myCard[0] == 1:
            screen.blit(cardvaluetext_one, (area1x_start+15, area1y_start+15))
        if myCard[0] == 2:
            screen.blit(cardvaluetext_two, (area1x_start+15, area1y_start+15))
        if myCard[0] == 3:
            screen.blit(cardvaluetext_three, (area1x_start+15, area1y_start+15))
        if myCard[0] == 4:
            screen.blit(cardvaluetext_four, (area1x_start+15, area1y_start+15))
        if myCard[0] == 5:
            screen.blit(cardvaluetext_five, (area1x_start+15, area1y_start+15))
        if myCard[0] == 6:
            screen.blit(cardvaluetext_six, (area1x_start+15, area1y_start+15))
        if myCard[0] == 7:
            screen.blit(cardvaluetext_seven, (area1x_start+15, area1y_start+15))
        if myCard[0] == 8:
            screen.blit(cardvaluetext_eight, (area1x_start+15, area1y_start+15))
        if myCard[0] == 9:
            screen.blit(cardvaluetext_nine, (area1x_start+15, area1y_start+15))
        if myCard[0] == 10:
            screen.blit(cardvaluetext_ten, (area1x_start+15, area1y_start+15))
        if myCard[0] == 11:
            screen.blit(cardvaluetext_eleven, (area1x_start+15, area1y_start+15))
        if myCard[0] == 12:
            screen.blit(cardvaluetext_twelve, (area1x_start+15, area1y_start+15))
        if myCard[0] == 13:
            screen.blit(cardvaluetext_thirteen, (area1x_start+15, area1y_start+15))
        if myCard[0] == 14:
            screen.blit(cardvaluetext_fourteen, (area1x_start+15, area1y_start+15))
        if myCard[0] == 15:
            screen.blit(cardvaluetext_fifteen, (area1x_start+15, area1y_start+15))
        if myCard[0] == 16:
            screen.blit(cardvaluetext_sixteen, (area1x_start+15, area1y_start+15))
    if Card2:
        pygame.draw.rect(screen, WHITE, (area2x_start,area2y_start, onefourthswidth, onefourthsheight))
        if myCard[1] == 1:
            screen.blit(cardvaluetext_one, (area2x_start+15, area2y_start+15))
        if myCard[1] == 2:
            screen.blit(cardvaluetext_two, (area2x_start+15, area2y_start+15))
        if myCard[1] == 3:
            screen.blit(cardvaluetext_three, (area2x_start+15, area2y_start+15))
        if myCard[1] == 4:
            screen.blit(cardvaluetext_four, (area2x_start+15, area2y_start+15))
        if myCard[1] == 5:
            screen.blit(cardvaluetext_five, (area2x_start+15, area2y_start+15))
        if myCard[1] == 6:
            screen.blit(cardvaluetext_six, (area2x_start+15, area2y_start+15))
        if myCard[1] == 7:
            screen.blit(cardvaluetext_seven, (area2x_start+15, area2y_start+15))
        if myCard[1] == 8:
            screen.blit(cardvaluetext_eight, (area2x_start+15, area2y_start+15))
        if myCard[1] == 9:
            screen.blit(cardvaluetext_nine, (area2x_start+15, area2y_start+15))
        if myCard[1] == 10:
            screen.blit(cardvaluetext_ten, (area2x_start+15, area2y_start+15))
        if myCard[1] == 11:
            screen.blit(cardvaluetext_eleven, (area2x_start+15, area2y_start+15))
        if myCard[1] == 12:
            screen.blit(cardvaluetext_twelve, (area2x_start+15, area2y_start+15))
        if myCard[1] == 13:
            screen.blit(cardvaluetext_thirteen, (area2x_start+15, area2y_start+15))
        if myCard[1] == 14:
            screen.blit(cardvaluetext_fourteen, (area2x_start+15, area2y_start+15))
        if myCard[1] == 15:
            screen.blit(cardvaluetext_fifteen, (area2x_start+15, area2y_start+15))
        if myCard[1] == 16:
            screen.blit(cardvaluetext_sixteen, (area2x_start+15, area2y_start+15))
    if Card3:
        pygame.draw.rect(screen, WHITE, (area3x_start, area3y_start, onefourthswidth, onefourthsheight))
        if myCard[2] == 1:
            screen.blit(cardvaluetext_one, (area3x_start+15, area3y_start+15))
        if myCard[2] == 2:
            screen.blit(cardvaluetext_two, (area3x_start+15, area3y_start+15))
        if myCard[2] == 3:
            screen.blit(cardvaluetext_three, (area3x_start+15, area3y_start+15))
        if myCard[2] == 4:
            screen.blit(cardvaluetext_four, (area3x_start+15, area3y_start+15))
        if myCard[2] == 5:
            screen.blit(cardvaluetext_five, (area3x_start+15, area3y_start+15))
        if myCard[2] == 6:
            screen.blit(cardvaluetext_six, (area3x_start+15, area3y_start+15))
        if myCard[2] == 7:
            screen.blit(cardvaluetext_seven, (area3x_start+15, area3y_start+15))
        if myCard[2] == 8:
            screen.blit(cardvaluetext_eight, (area3x_start+15, area3y_start+15))
        if myCard[2] == 9:
            screen.blit(cardvaluetext_nine, (area3x_start+15, area3y_start+15))
        if myCard[2] == 10:
            screen.blit(cardvaluetext_ten, (area3x_start+15, area3y_start+15))
        if myCard[2] == 11:
            screen.blit(cardvaluetext_eleven, (area3x_start+15, area3y_start+15))
        if myCard[2] == 12:
            screen.blit(cardvaluetext_twelve, (area3x_start+15, area3y_start+15))
        if myCard[2] == 13:
            screen.blit(cardvaluetext_thirteen, (area3x_start+15, area3y_start+15))
        if myCard[2] == 14:
            screen.blit(cardvaluetext_fourteen, (area3x_start+15, area3y_start+15))
        if myCard[2] == 15:
            screen.blit(cardvaluetext_fifteen, (area3x_start+15, area3y_start+15))
        if myCard[2] == 16:
            screen.blit(cardvaluetext_sixteen, (area3x_start+15, area3y_start+15))
    if Card4:
        pygame.draw.rect(screen, WHITE, (area4x_start, area4y_start, onefourthswidth, onefourthsheight))
        if myCard[3] == 1:
            screen.blit(cardvaluetext_one, (area4x_start+15, area4y_start+15))
        if myCard[3] == 2:
            screen.blit(cardvaluetext_two, (area4x_start+15, area4y_start+15))
        if myCard[3] == 3:
            screen.blit(cardvaluetext_three, (area4x_start+15, area4y_start+15))
        if myCard[3] == 4:
            screen.blit(cardvaluetext_four, (area4x_start+15, area4y_start+15))
        if myCard[3] == 5:
            screen.blit(cardvaluetext_five, (area4x_start+15, area4y_start+15))
        if myCard[3] == 6:
            screen.blit(cardvaluetext_six, (area4x_start+15, area4y_start+15))
        if myCard[3] == 7:
            screen.blit(cardvaluetext_seven, (area4x_start+15, area4y_start+15))
        if myCard[3] == 8:
            screen.blit(cardvaluetext_eight, (area4x_start+15, area4y_start+15))
        if myCard[3] == 9:
            screen.blit(cardvaluetext_nine, (area4x_start+15, area4y_start+15))
        if myCard[3] == 10:
            screen.blit(cardvaluetext_ten, (area4x_start+15, area4y_start+15))
        if myCard[3] == 11:
            screen.blit(cardvaluetext_eleven, (area4x_start+15, area4y_start+15))
        if myCard[3] == 12:
            screen.blit(cardvaluetext_twelve, (area4x_start+15, area4y_start+15))
        if myCard[3] == 13:
            screen.blit(cardvaluetext_thirteen, (area4x_start+15, area4y_start+15))
        if myCard[3] == 14:
            screen.blit(cardvaluetext_fourteen, (area4x_start+15, area4y_start+15))
        if myCard[3] == 15:
            screen.blit(cardvaluetext_fifteen, (area4x_start+15, area4y_start+15))
        if myCard[3] == 16:
            screen.blit(cardvaluetext_sixteen, (area4x_start+15, area4y_start+15))
    if Card5:
        pygame.draw.rect(screen, WHITE, (area5x_start, area5y_start, onefourthswidth, onefourthsheight))
        if myCard[4] == 1:
            screen.blit(cardvaluetext_one, (area5x_start+15, area5y_start+15))
        if myCard[4] == 2:
            screen.blit(cardvaluetext_two, (area5x_start+15, area5y_start+15))
        if myCard[4] == 3:
            screen.blit(cardvaluetext_three, (area5x_start+15, area5y_start+15))
        if myCard[4] == 4:
            screen.blit(cardvaluetext_four, (area5x_start+15, area5y_start+15))
        if myCard[4] == 5:
            screen.blit(cardvaluetext_five, (area5x_start+15, area5y_start+15))
        if myCard[4] == 6:
            screen.blit(cardvaluetext_six, (area5x_start+15, area5y_start+15))
        if myCard[4] == 7:
            screen.blit(cardvaluetext_seven, (area5x_start+15, area5y_start+15))
        if myCard[4] == 8:
            screen.blit(cardvaluetext_eight, (area5x_start+15, area5y_start+15))
        if myCard[4] == 9:
            screen.blit(cardvaluetext_nine, (area5x_start+15, area5y_start+15))
        if myCard[4] == 10:
            screen.blit(cardvaluetext_ten, (area5x_start+15, area5y_start+15))
        if myCard[4] == 11:
            screen.blit(cardvaluetext_eleven, (area5x_start+15, area5y_start+15))
        if myCard[4] == 12:
            screen.blit(cardvaluetext_twelve, (area5x_start+15, area5y_start+15))
        if myCard[4] == 13:
            screen.blit(cardvaluetext_thirteen, (area5x_start+15, area5y_start+15))
        if myCard[4] == 14:
            screen.blit(cardvaluetext_fourteen, (area5x_start+15, area5y_start+15))
        if myCard[4] == 15:
            screen.blit(cardvaluetext_fifteen, (area5x_start+15, area5y_start+15))
        if myCard[4] == 16:
            screen.blit(cardvaluetext_sixteen, (area5x_start+15, area5y_start+15))
    if Card6:
        pygame.draw.rect(screen, WHITE, (area6x_start, area6y_start, onefourthswidth, onefourthsheight))
        if myCard[5] == 1:
            screen.blit(cardvaluetext_one, (area6x_start+15, area6y_start+15))
        if myCard[5] == 2:
            screen.blit(cardvaluetext_two, (area6x_start+15, area6y_start+15))
        if myCard[5] == 3:
            screen.blit(cardvaluetext_three, (area6x_start+15, area6y_start+15))
        if myCard[5] == 4:
            screen.blit(cardvaluetext_four, (area6x_start+15, area6y_start+15))
        if myCard[5] == 5:
            screen.blit(cardvaluetext_five, (area6x_start+15, area6y_start+15))
        if myCard[5] == 6:
            screen.blit(cardvaluetext_six, (area6x_start+15, area6y_start+15))
        if myCard[5] == 7:
            screen.blit(cardvaluetext_seven, (area6x_start+15, area6y_start+15))
        if myCard[5] == 8:
            screen.blit(cardvaluetext_eight, (area6x_start+15, area6y_start+15))
        if myCard[5] == 9:
            screen.blit(cardvaluetext_nine, (area6x_start+15, area6y_start+15))
        if myCard[5] == 10:
            screen.blit(cardvaluetext_ten, (area6x_start+15, area6y_start+15))
        if myCard[5] == 11:
            screen.blit(cardvaluetext_eleven, (area6x_start+15, area6y_start+15))
        if myCard[5] == 12:
            screen.blit(cardvaluetext_twelve, (area6x_start+15, area6y_start+15))
        if myCard[5] == 13:
            screen.blit(cardvaluetext_thirteen, (area6x_start+15, area6y_start+15))
        if myCard[5] == 14:
            screen.blit(cardvaluetext_fourteen, (area6x_start+15, area6y_start+15))
        if myCard[5] == 15:
            screen.blit(cardvaluetext_fifteen, (area6x_start+15, area6y_start+15))
        if myCard[5] == 16:
            screen.blit(cardvaluetext_sixteen, (area6x_start+15, area6y_start+15))
    if Card7:
        pygame.draw.rect(screen, WHITE, (area7x_start, area7y_start, onefourthswidth, onefourthsheight))
        if myCard[6] == 1:
            screen.blit(cardvaluetext_one, (area7x_start+15, area7y_start+15))
        if myCard[6] == 2:
            screen.blit(cardvaluetext_two, (area7x_start+15, area7y_start+15))
        if myCard[6] == 3:
            screen.blit(cardvaluetext_three, (area7x_start+15, area7y_start+15))
        if myCard[6] == 4:
            screen.blit(cardvaluetext_four, (area7x_start+15, area7y_start+15))
        if myCard[6] == 5:
            screen.blit(cardvaluetext_five, (area7x_start+15, area7y_start+15))
        if myCard[6] == 6:
            screen.blit(cardvaluetext_six, (area7x_start+15, area7y_start+15))
        if myCard[6] == 7:
            screen.blit(cardvaluetext_seven, (area7x_start+15, area7y_start+15))
        if myCard[6] == 8:
            screen.blit(cardvaluetext_eight, (area7x_start+15, area7y_start+15))
        if myCard[6] == 9:
            screen.blit(cardvaluetext_nine, (area7x_start+15, area7y_start+15))
        if myCard[6] == 10:
            screen.blit(cardvaluetext_ten, (area7x_start+15, area7y_start+15))
        if myCard[6] == 11:
            screen.blit(cardvaluetext_eleven, (area7x_start+15, area7y_start+15))
        if myCard[6] == 12:
            screen.blit(cardvaluetext_twelve, (area7x_start+15, area7y_start+15))
        if myCard[6] == 13:
            screen.blit(cardvaluetext_thirteen, (area7x_start+15, area7y_start+15))
        if myCard[6] == 14:
            screen.blit(cardvaluetext_fourteen, (area7x_start+15, area7y_start+15))
        if myCard[6] == 15:
            screen.blit(cardvaluetext_fifteen, (area7x_start+15, area7y_start+15))
        if myCard[6] == 16:
            screen.blit(cardvaluetext_sixteen, (area7x_start+15, area7y_start+15))
    if Card8:
        pygame.draw.rect(screen, WHITE, (area8x_start, area8y_start, onefourthswidth, onefourthsheight))
        if myCard[7] == 1:
            screen.blit(cardvaluetext_one, (area8x_start+15, area8y_start+15))
        if myCard[7] == 2:
            screen.blit(cardvaluetext_two, (area8x_start+15, area8y_start+15))
        if myCard[7] == 3:
            screen.blit(cardvaluetext_three, (area8x_start+15, area8y_start+15))
        if myCard[7] == 4:
            screen.blit(cardvaluetext_four, (area8x_start+15, area8y_start+15))
        if myCard[7] == 5:
            screen.blit(cardvaluetext_five, (area8x_start+15, area8y_start+15))
        if myCard[7] == 6:
            screen.blit(cardvaluetext_six, (area8x_start+15, area8y_start+15))
        if myCard[7] == 7:
            screen.blit(cardvaluetext_seven, (area8x_start+15, area8y_start+15))
        if myCard[7] == 8:
            screen.blit(cardvaluetext_eight, (area8x_start+15, area8y_start+15))
        if myCard[7] == 9:
            screen.blit(cardvaluetext_nine, (area8x_start+15, area8y_start+15))
        if myCard[7] == 10:
            screen.blit(cardvaluetext_ten, (area8x_start+15, area8y_start+15))
        if myCard[7] == 11:
            screen.blit(cardvaluetext_eleven, (area8x_start+15, area8y_start+15))
        if myCard[7] == 12:
            screen.blit(cardvaluetext_twelve, (area8x_start+15, area8y_start+15))
        if myCard[7] == 13:
            screen.blit(cardvaluetext_thirteen, (area8x_start+15, area8y_start+15))
        if myCard[7] == 14:
            screen.blit(cardvaluetext_fourteen, (area8x_start+15, area8y_start+15))
        if myCard[7] == 15:
            screen.blit(cardvaluetext_fifteen, (area8x_start+15, area8y_start+15))
        if myCard[7] == 16:
            screen.blit(cardvaluetext_sixteen, (area8x_start+15, area8y_start+15))
    if Card9:
        pygame.draw.rect(screen, WHITE, (area9x_start, area9y_start, onefourthswidth, onefourthsheight))
        if myCard[8] == 1:
            screen.blit(cardvaluetext_one, (area9x_start+15, area9y_start+15))
        if myCard[8] == 2:
            screen.blit(cardvaluetext_two, (area9x_start+15, area9y_start+15))
        if myCard[8] == 3:
            screen.blit(cardvaluetext_three, (area9x_start+15, area9y_start+15))
        if myCard[8] == 4:
            screen.blit(cardvaluetext_four, (area9x_start+15, area9y_start+15))
        if myCard[8] == 5:
            screen.blit(cardvaluetext_five, (area9x_start+15, area9y_start+15))
        if myCard[8] == 6:
            screen.blit(cardvaluetext_six, (area9x_start+15, area9y_start+15))
        if myCard[8] == 7:
            screen.blit(cardvaluetext_seven, (area9x_start+15, area9y_start+15))
        if myCard[8] == 8:
            screen.blit(cardvaluetext_eight, (area9x_start+15, area9y_start+15))
        if myCard[8] == 9:
            screen.blit(cardvaluetext_nine, (area9x_start+15, area9y_start+15))
        if myCard[8] == 10:
            screen.blit(cardvaluetext_ten, (area9x_start+15, area9y_start+15))
        if myCard[8] == 11:
            screen.blit(cardvaluetext_eleven, (area9x_start+15, area9y_start+15))
        if myCard[8] == 12:
            screen.blit(cardvaluetext_twelve, (area9x_start+15, area9y_start+15))
        if myCard[8] == 13:
            screen.blit(cardvaluetext_thirteen, (area9x_start+15, area9y_start+15))
        if myCard[8] == 14:
            screen.blit(cardvaluetext_fourteen, (area9x_start+15, area9y_start+15))
        if myCard[8] == 15:
            screen.blit(cardvaluetext_fifteen, (area9x_start+15, area9y_start+15))
        if myCard[8] == 16:
            screen.blit(cardvaluetext_sixteen, (area9x_start+15, area9y_start+15))
    if Card10:
        pygame.draw.rect(screen, WHITE, (area10x_start, area10y_start, onefourthswidth, onefourthsheight))
        if myCard[9] == 1:
            screen.blit(cardvaluetext_one, (area10x_start+15, area10y_start+15))
        if myCard[9] == 2:
            screen.blit(cardvaluetext_two, (area10x_start+15, area10y_start+15))
        if myCard[9] == 3:
            screen.blit(cardvaluetext_three, (area10x_start+15, area10y_start+15))
        if myCard[9] == 4:
            screen.blit(cardvaluetext_four, (area10x_start+15, area10y_start+15))
        if myCard[9] == 5:
            screen.blit(cardvaluetext_five, (area10x_start+15, area10y_start+15))
        if myCard[9] == 6:
            screen.blit(cardvaluetext_six, (area10x_start+15, area10y_start+15))
        if myCard[9] == 7:
            screen.blit(cardvaluetext_seven, (area10x_start+15, area10y_start+15))
        if myCard[9] == 8:
            screen.blit(cardvaluetext_eight, (area10x_start+15, area10y_start+15))
        if myCard[9] == 9:
            screen.blit(cardvaluetext_nine, (area10x_start+15, area10y_start+15))
        if myCard[9] == 10:
            screen.blit(cardvaluetext_ten, (area10x_start+15, area10y_start+15))
        if myCard[9] == 11:
            screen.blit(cardvaluetext_eleven, (area10x_start+15, area10y_start+15))
        if myCard[9] == 12:
            screen.blit(cardvaluetext_twelve, (area10x_start+15, area10y_start+15))
        if myCard[9] == 13:
            screen.blit(cardvaluetext_thirteen, (area10x_start+15, area10y_start+15))
        if myCard[9] == 14:
            screen.blit(cardvaluetext_fourteen, (area10x_start+15, area10y_start+15))
        if myCard[9] == 15:
            screen.blit(cardvaluetext_fifteen, (area10x_start+15, area10y_start+15))
        if myCard[9] == 16:
            screen.blit(cardvaluetext_sixteen, (area10x_start+15, area10y_start+15))
    if Card11:
        pygame.draw.rect(screen, WHITE, (area11x_start, area11y_start, onefourthswidth, onefourthsheight))
        if myCard[10] == 1:
            screen.blit(cardvaluetext_one, (area11x_start+15, area11y_start+15))
        if myCard[10] == 2:
            screen.blit(cardvaluetext_two, (area11x_start+15, area11y_start+15))
        if myCard[10] == 3:
            screen.blit(cardvaluetext_three, (area11x_start+15, area11y_start+15))
        if myCard[10] == 4:
            screen.blit(cardvaluetext_four, (area11x_start+15, area11y_start+15))
        if myCard[10] == 5:
            screen.blit(cardvaluetext_five, (area11x_start+15, area11y_start+15))
        if myCard[10] == 6:
            screen.blit(cardvaluetext_six, (area11x_start+15, area11y_start+15))
        if myCard[10] == 7:
            screen.blit(cardvaluetext_seven, (area11x_start+15, area11y_start+15))
        if myCard[10] == 8:
            screen.blit(cardvaluetext_eight, (area11x_start+15, area11y_start+15))
        if myCard[10] == 9:
            screen.blit(cardvaluetext_nine, (area11x_start+15, area11y_start+15))
        if myCard[10] == 10:
            screen.blit(cardvaluetext_ten, (area11x_start+15, area11y_start+15))
        if myCard[10] == 11:
            screen.blit(cardvaluetext_eleven, (area11x_start+15, area11y_start+15))
        if myCard[10] == 12:
            screen.blit(cardvaluetext_twelve, (area11x_start+15, area11y_start+15))
        if myCard[10] == 13:
            screen.blit(cardvaluetext_thirteen, (area11x_start+15, area11y_start+15))
        if myCard[10] == 14:
            screen.blit(cardvaluetext_fourteen, (area11x_start+15, area11y_start+15))
        if myCard[10] == 15:
            screen.blit(cardvaluetext_fifteen, (area11x_start+15, area11y_start+15))
        if myCard[10] == 16:
            screen.blit(cardvaluetext_sixteen, (area11x_start+15, area11y_start+15))
    if Card12:
        pygame.draw.rect(screen, WHITE, (area12x_start, area12y_start, onefourthswidth, onefourthsheight))
        if myCard[11] == 1:
            screen.blit(cardvaluetext_one, (area12x_start+15, area12y_start+15))
        if myCard[11] == 2:
            screen.blit(cardvaluetext_two, (area12x_start+15, area12y_start+15))
        if myCard[11] == 3:
            screen.blit(cardvaluetext_three, (area12x_start+15, area12y_start+15))
        if myCard[11] == 4:
            screen.blit(cardvaluetext_four, (area12x_start+15, area12y_start+15))
        if myCard[11] == 5:
            screen.blit(cardvaluetext_five, (area12x_start+15, area12y_start+15))
        if myCard[11] == 6:
            screen.blit(cardvaluetext_six, (area12x_start+15, area12y_start+15))
        if myCard[11] == 7:
            screen.blit(cardvaluetext_seven, (area12x_start+15, area12y_start+15))
        if myCard[11] == 8:
            screen.blit(cardvaluetext_eight, (area12x_start+15, area12y_start+15))
        if myCard[11] == 9:
            screen.blit(cardvaluetext_nine, (area12x_start+15, area12y_start+15))
        if myCard[11] == 10:
            screen.blit(cardvaluetext_ten, (area12x_start+15, area12y_start+15))
        if myCard[11] == 11:
            screen.blit(cardvaluetext_eleven, (area12x_start+15, area12y_start+15))
        if myCard[11] == 12:
            screen.blit(cardvaluetext_twelve, (area12x_start+15, area12y_start+15))
        if myCard[11] == 13:
            screen.blit(cardvaluetext_thirteen, (area12x_start+15, area12y_start+15))
        if myCard[11] == 14:
            screen.blit(cardvaluetext_fourteen, (area12x_start+15, area12y_start+15))
        if myCard[11] == 15:
            screen.blit(cardvaluetext_fifteen, (area12x_start+15, area12y_start+15))
        if myCard[11] == 16:
            screen.blit(cardvaluetext_sixteen, (area12x_start+15, area12y_start+15))
    if Card13:
        pygame.draw.rect(screen, WHITE, (area13x_start, area13y_start, onefourthswidth, onefourthsheight))
        if myCard[12] == 1:
            screen.blit(cardvaluetext_one, (area13x_start+15, area13y_start+15))
        if myCard[12] == 2:
            screen.blit(cardvaluetext_two, (area13x_start+15, area13y_start+15))
        if myCard[12] == 3:
            screen.blit(cardvaluetext_three, (area13x_start+15, area13y_start+15))
        if myCard[12] == 4:
            screen.blit(cardvaluetext_four, (area13x_start+15, area13y_start+15))
        if myCard[12] == 5:
            screen.blit(cardvaluetext_five, (area13x_start+15, area13y_start+15))
        if myCard[12] == 6:
            screen.blit(cardvaluetext_six, (area13x_start+15, area13y_start+15))
        if myCard[12] == 7:
            screen.blit(cardvaluetext_seven, (area13x_start+15, area13y_start+15))
        if myCard[12] == 8:
            screen.blit(cardvaluetext_eight, (area13x_start+15, area13y_start+15))
        if myCard[12] == 9:
            screen.blit(cardvaluetext_nine, (area13x_start+15, area13y_start+15))
        if myCard[12] == 10:
            screen.blit(cardvaluetext_ten, (area13x_start+15, area13y_start+15))
        if myCard[12] == 11:
            screen.blit(cardvaluetext_eleven, (area13x_start+15, area13y_start+15))
        if myCard[12] == 12:
            screen.blit(cardvaluetext_twelve, (area13x_start+15, area13y_start+15))
        if myCard[12] == 13:
            screen.blit(cardvaluetext_thirteen, (area13x_start+15, area13y_start+15))
        if myCard[12] == 14:
            screen.blit(cardvaluetext_fourteen, (area13x_start+15, area13y_start+15))
        if myCard[12] == 15:
            screen.blit(cardvaluetext_fifteen, (area13x_start+15, area13y_start+15))
        if myCard[12] == 16:
            screen.blit(cardvaluetext_sixteen, (area13x_start+15, area13y_start+15))
    if Card14:
        pygame.draw.rect(screen, WHITE, (area14x_start, area14y_start, onefourthswidth, onefourthsheight))
        if myCard[13] == 1:
            screen.blit(cardvaluetext_one, (area14x_start+15, area14y_start+15))
        if myCard[13] == 2:
            screen.blit(cardvaluetext_two, (area14x_start+15, area14y_start+15))
        if myCard[13] == 3:
            screen.blit(cardvaluetext_three, (area14x_start+15, area14y_start+15))
        if myCard[13] == 4:
            screen.blit(cardvaluetext_four, (area14x_start+15, area14y_start+15))
        if myCard[13] == 5:
            screen.blit(cardvaluetext_five, (area14x_start+15, area14y_start+15))
        if myCard[13] == 6:
            screen.blit(cardvaluetext_six, (area14x_start+15, area14y_start+15))
        if myCard[13] == 7:
            screen.blit(cardvaluetext_seven, (area14x_start+15, area14y_start+15))
        if myCard[13] == 8:
            screen.blit(cardvaluetext_eight, (area14x_start+15, area14y_start+15))
        if myCard[13] == 9:
            screen.blit(cardvaluetext_nine, (area14x_start+15, area14y_start+15))
        if myCard[13] == 10:
            screen.blit(cardvaluetext_ten, (area14x_start+15, area14y_start+15))
        if myCard[13] == 11:
            screen.blit(cardvaluetext_eleven, (area14x_start+15, area14y_start+15))
        if myCard[13] == 12:
            screen.blit(cardvaluetext_twelve, (area14x_start+15, area14y_start+15))
        if myCard[13] == 13:
            screen.blit(cardvaluetext_thirteen, (area14x_start+15, area14y_start+15))
        if myCard[13] == 14:
            screen.blit(cardvaluetext_fourteen, (area14x_start+15, area14y_start+15))
        if myCard[13] == 15:
            screen.blit(cardvaluetext_fifteen, (area14x_start+15, area14y_start+15))
        if myCard[13] == 16:
            screen.blit(cardvaluetext_sixteen, (area14x_start+15, area14y_start+15))
    if Card15:
        pygame.draw.rect(screen, WHITE, (area15x_start, area15y_start, onefourthswidth, onefourthsheight))
        if myCard[14] == 1:
            screen.blit(cardvaluetext_one, (area15x_start+15, area15y_start+15))
        if myCard[14] == 2:
            screen.blit(cardvaluetext_two, (area15x_start+15, area15y_start+15))
        if myCard[14] == 3:
            screen.blit(cardvaluetext_three, (area15x_start+15, area15y_start+15))
        if myCard[14] == 4:
            screen.blit(cardvaluetext_four, (area15x_start+15, area15y_start+15))
        if myCard[14] == 5:
            screen.blit(cardvaluetext_five, (area15x_start+15, area15y_start+15))
        if myCard[14] == 6:
            screen.blit(cardvaluetext_six, (area15x_start+15, area15y_start+15))
        if myCard[14] == 7:
            screen.blit(cardvaluetext_seven, (area15x_start+15, area15y_start+15))
        if myCard[14] == 8:
            screen.blit(cardvaluetext_eight, (area15x_start+15, area15y_start+15))
        if myCard[14] == 9:
            screen.blit(cardvaluetext_nine, (area15x_start+15, area15y_start+15))
        if myCard[14] == 10:
            screen.blit(cardvaluetext_ten, (area15x_start+15, area15y_start+15))
        if myCard[14] == 11:
            screen.blit(cardvaluetext_eleven, (area15x_start+15, area15y_start+15))
        if myCard[14] == 12:
            screen.blit(cardvaluetext_twelve, (area15x_start+15, area15y_start+15))
        if myCard[14] == 13:
            screen.blit(cardvaluetext_thirteen, (area15x_start+15, area15y_start+15))
        if myCard[14] == 14:
            screen.blit(cardvaluetext_fourteen, (area15x_start+15, area15y_start+15))
        if myCard[14] == 15:
            screen.blit(cardvaluetext_fifteen, (area15x_start+15, area15y_start+15))
        if myCard[14] == 16:
            screen.blit(cardvaluetext_sixteen, (area15x_start+15, area15y_start+15))
    if Card16:
        pygame.draw.rect(screen, WHITE, (area16x_start, area16y_start, onefourthswidth, onefourthsheight))
        if myCard[15] == 1:
            screen.blit(cardvaluetext_one, (area16x_start+15, area16y_start+15))
        if myCard[15] == 2:
            screen.blit(cardvaluetext_two, (area16x_start+15, area16y_start+15))
        if myCard[15] == 3:
            screen.blit(cardvaluetext_three, (area16x_start+15, area16y_start+15))
        if myCard[15] == 4:
            screen.blit(cardvaluetext_four, (area16x_start+15, area16y_start+15))
        if myCard[15] == 5:
            screen.blit(cardvaluetext_five, (area16x_start+15, area16y_start+15))
        if myCard[15] == 6:
            screen.blit(cardvaluetext_six, (area16x_start+15, area16y_start+15))
        if myCard[15] == 7:
            screen.blit(cardvaluetext_seven, (area16x_start+15, area16y_start+15))
        if myCard[15] == 8:
            screen.blit(cardvaluetext_eight, (area16x_start+15, area16y_start+15))
        if myCard[15] == 9:
            screen.blit(cardvaluetext_nine, (area16x_start+15, area16y_start+15))
        if myCard[15] == 10:
            screen.blit(cardvaluetext_ten, (area16x_start+15, area16y_start+15))
        if myCard[15] == 11:
            screen.blit(cardvaluetext_eleven, (area16x_start+15, area16y_start+15))
        if myCard[15] == 12:
            screen.blit(cardvaluetext_twelve, (area16x_start+15, area16y_start+15))
        if myCard[15] == 13:
            screen.blit(cardvaluetext_thirteen, (area16x_start+15, area16y_start+15))
        if myCard[15] == 14:
            screen.blit(cardvaluetext_fourteen, (area16x_start+15, area16y_start+15))
        if myCard[15] == 15:
            screen.blit(cardvaluetext_fifteen, (area16x_start+15, area16y_start+15))
        if myCard[15] == 16:
            screen.blit(cardvaluetext_sixteen, (area16x_start+15, area16y_start+15))
    if vict:    #If we won the game, print the victory image to the screen
        screen.blit(victory, (0, 0))
    #Draw all the stuff to the screen now (without this line there will be nothing that prints to screen)
    pygame.display.flip()

#---ALL CODE TO DRAW ABOVE THIS LINE ---

    #Set Frames per second for game
    delta = clock.tick(20)
    # throttle down to 0
    #throttle the mouse clicking so that we do not double click therefore messing up our clicking/matching/game logic
    if click_throttle > 0:
        click_throttle = max(0, click_throttle - delta)

#User has clicked close, and this will close the game window
pygame.quit()