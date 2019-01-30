
#cells 2d-array helps us track the circles .. white (#FFFFFF) is the default color ... 
cells = [["#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF"],["#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF"],
         ["#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF"],["#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF"],
         ["#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF"],["#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF"],
         ["#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF"]]

#y_pos2 = 50
global x_pos2
x_pos2=0
colorCount = 1
global colorCode
colorCode = "#FF0000"
global currentColor
currentColor = "#FFFF00"
screen = "Main menu"
global initialMove
initialMove = False
global gameStarted
gameStarted = False
def setup():
    size(900, 700)
    #noLoop()

def main_menu():
    global gameStarted
    global screen
    if screen == "Main menu":
        background("#0000FF")
        textSize(64)
        fill(255)
        text("Connect 4", 280, 200)
        fill(0)
        rect(285,350,300,75)
        if 585 > mouseX > 285 and 425 > mouseY > 350:
            fill(255,255,0)
            text("Start", 360, 410)
            if mousePressed:
                #start game if start is clicked
                screen = "Game"
        else:
            fill(165, 165, 0)
            text("Start", 360, 410)
        
        fill(0)
        rect(285,450,300,75)
        textSize(46)
        if 585 > mouseX > 285 and 525 > mouseY > 450:
            fill(255, 0, 0)
            text("Instructions", 305, 505)
            if mousePressed:
                #instructions screen
                screen = "Instructions"
    
        else:
            fill(165, 0, 0)
            text("Instructions", 305, 505)

def instructions():
    global screen
    if screen == "Instructions":
        background ("#0000FF")
        textSize(30)
        fill (255)
        text("""-2 player game
            
    -4 in a row to win (Diagonally, 
    Vertically, or Horizontally)
    
    -Click on piece to change turns (red and yellow)
    
    -Random choice on who goes first""",100, 100)

        if 90 > mouseX > 10 and 40 > mouseY > 10:
            fill(205)
            rect(10, 10, 80, 30)
            if mousePressed:
                screen = "Main menu"
        else:
            fill(255)
            rect(10, 10, 80, 30)
        fill(0)
        #back button
        text("Back", 16, 35)    


def draw():
    main_menu()
    game()
    instructions()
    
    
def game():    
    global screen
    global gameStarted
    global initialMove
    global x_pos2
    if screen == "Game":
        global x_pos2, rows, columns
        background(204)
    # line(x, 0, x, height)
        #blue square board
        fill("#0000FF")
        rect (150, 85, 600, 500)
        
        #legs of board
    
        rect(150, 585, 18, 100)
        rect(732, 585, 18, 100)
        
        # 7(horizonal) x 6 (vertical)
        # initial Board is 7 x 6 white circles
        # y position for first circle
        y_pos = 140
        for rows in range (0, 6):
        # x position for first circle
            x_pos = 210
            # White color
            #fill ("#FFFFFF")
            if (checkHorizontal(rows, "#FFFF00")== "WINNER"):
                    exit()
            if (checkHorizontal(rows, "#FF0000")== "WINNER"):
                    exit()
            #Row of circles initally white
            for columns in range (0, 7):
                #print ("Color at (" + str(rows) + ","  + str(columns) + ") = " + str(cells[rows][columns]))
            #   print cells
                fill(cells[columns][rows])
                ellipse (x_pos, y_pos, 70, 70)
                x_pos = x_pos + 80
                if (cells[columns][rows] == "#FFFF00" or cells[columns][rows] == "#FF0000"):
                #  print "CHECKING at column " + str(columns)
                    if (checkVertical(columns, cells[columns][rows])== "WINNER"):
                        exit()
            y_pos = y_pos + 80

            
        # board creation end
        # identify which circle is filled and what color it is 
        # when the peg is clicked check if the circle is over one of the columns
    
    
        # player places circle over one of the columns and click
        # once clicked if the column is full then error
        # else find the lowest circle in the column that has no color 
        # get the y coordinate and drop the circle to that spot
        # x-positions of the columns 690, 610, 530, 450, 370, 290, 210
        # y-positions of the rows 540,460,380,300,220,140 
        
        fill(currentColor)
        # player piece across the top of the board
        ellipse (mouseX, 50 , 70, 70)
        if (175< mouseX < 245):
            x_pos2 = 210
        elif (255< mouseX < 325):
            x_pos2 = 290
        elif (335< mouseX < 405):
            x_pos2 = 370
        elif (415< mouseX < 485):
            x_pos2 = 450
        elif (495< mouseX < 565):
            x_pos2 = 530
        elif (575< mouseX < 645):
            x_pos2 = 610
        elif (655< mouseX < 725):
            x_pos2 = 690
        gameStarted = True
      
def mouseClicked():
    global x_pos2
    global gameStarted
    global initialMove
    if (gameStarted == True) :
        # if the circle is outside the board on either side then raise a error and have 
        # the player put the piece inside the board before clicking
        #
        global colorCount
        colorCount +=1
        global col_dict
        col_dict = { 210:0, 290:1, 370:2, 450:3, 530:4, 610:5, 690:6}
        global rowdict
        row_dict = {0:140, 1:220, 2:300, 3:380, 4:460, 5:540}
        fillColumn(x_pos2)
        initialMove = True
        if (checkRightAngle("#FFFF00")== "WINNER"):
            exit()
        if (checkRightAngle("#FF0000")== "WINNER"):
            exit()
        if (checkLeftAngle("#FFFF00")== "WINNER"):
            exit()
        if (checkLeftAngle("#FF0000")== "WINNER"):
            exit()
        redraw()
        
    
def fillColumn(xpos):
    # this drops the game piece down once the player clicks mouse
    # game must be started already and first time you enter after you click from main menu identified by the initialMove flag
    if (gameStarted==True and initialMove == True):
        global colorCode, currentColor
        column = col_dict[xpos]
        if (colorCode == "#FF0000"):
            colorCode = "#FFFF00"
            currentColor = "#FF0000"
        elif (colorCode == "#FFFF00"):
            colorCode = "#FF0000"
            currentColor = "#FFFF00"
        # check to see if the cells under that column are empty
        for i in range(0,6):
        # check for the first non-white circle
            if (cells[column][i] != "#FFFFFF"):
                # set the cell above (i-1) the non-white circle to the new color
                if (i != 0) :
                    cells[column][i-1] = colorCode
                   # print "Col = " + str(column) + ", Row = " + str(i - 1) + " -> Color = " + cells[column][i - 1]
                    break
                # if the top cell already has a non-white circle then raise an error the player needs to choose another column
                else:
                    print ("ERROR THIS COLUMN IS FULL")
                    print cells
                    # reset the color code back to the original so that player can go again
                    if (colorCode == "#FF0000"):
                        colorCode = "#FFFF00"
                        currentColor = "#FF0000"
                    elif (colorCode == "#FFFF00"):
                        colorCode = "#FF0000"
                        currentColor = "#FFFF00"
                    break
            # if we reach the bottom of the column (i==5) then I know the column is all white circles, set the last cell to the new color     
            elif (i == 5):
            # y_pos2 = rowdict[i]
                cells[column][i] = colorCode
              #  print "Col = " + str(column) + ", Row = " + str(i) + " -> Color = " + cells[column][i]

#def checkIfWin():
    # start on bottom left position ... check for the color of the circle 
    # if it is white then dont bother looking in that column ... move onto the next circle on the right
    # keep going until you find the first non white circle ... the column position becomes our most left check 
    # place holders for left angle, right angle , horizontal, verticle... 
    # for each redLeftAngle, redRightAngle, redVertical, redHorizontal, yelLeftAngle, yelRightAngle, yelVertical, yelHorizontal
    # 

def checkVertical(colNum, colorCheck):
    
    colorCount = 0
    for row in reversed(range(0,6)):
        if (cells[colNum][row] == colorCheck):
            colorCount = colorCount + 1
         #   print ("VERTICAL cell ( " + str(colNum) + " ," + str(row) + ") = " + cells[colNum][row] + " COLOR COUNT = " + str(colorCount))
            if (colorCount == 4):
                if (colorCheck == "#FF0000"):
                    print ("RED WINS")
                elif (colorCheck == "#FFFF00"): 
                    print ("YELLOW WINS")
                return "WINNER"    
                exit
        else:
            #reset yelCount to 0 if the color is not yellow
            colorCount = 0 

def checkHorizontal(row, colorCheck):
    
    colorCount = 0
    for colNum in range(0,7):
        if (cells[colNum][row] == colorCheck):
            colorCount = colorCount + 1
         #   print ("VERTICAL cell ( " + str(colNum) + " ," + str(row) + ") = " + cells[colNum][row] + " COLOR COUNT = " + str(colorCount))
            if (colorCount == 4):
                if (colorCheck == "#FF0000"):
                    print ("RED WINS")
                elif (colorCheck == "#FFFF00"): 
                    print ("YELLOW WINS")
                return "WINNER"    
                exit
        else:
            #reset yelCount to 0 if the color is not yellow
            colorCount = 0 
            
def checkRightAngle(colorCheck):
    
    colorCount1 = 0
    colorCount2 = 0
    colorCount3 = 0 
    colorCount4 = 0 
    colorCount5 = 0 
    colorCount6 = 0 
    for colNum in range(0,7):
        for row in reversed(range(0,6)):
            if ((colNum==0 and row ==5) or (colNum==1 and row ==4) or (colNum==2 and row ==3) or (colNum==3 and row ==2) or (colNum==4 and row ==1) 
                    or (colNum==5 and row ==0)) :
                if (cells[colNum][row] == colorCheck):
                    colorCount1 = colorCount1 + 1
                    #print "color count =" + str(colorCount) + " for " + colorCheck
                #   print ("VERTICAL cell ( " + str(colNum) + " ," + str(row) + ") = " + cells[colNum][row] + " COLOR COUNT = " + str(colorCount))
                    if (colorCount1 == 4):
                        if (colorCheck == "#FF0000"):
                            print ("RED WINS")
                        elif (colorCheck == "#FFFF00"): 
                            print ("YELLOW WINS")
                        return "WINNER"    
                        exit
                else:
                    #reset yelCount to 0 if the color is not yellow
                    colorCount1 = 0     
            # colorCount2
            if ((colNum==0 and row ==4) or (colNum==1 and row ==3) or (colNum==2 and row ==2) or (colNum==3 and row ==1) or (colNum==4 and row ==0)) :
                if (cells[colNum][row] == colorCheck):
                    colorCount2 = colorCount2 + 1
                #    print "color count =" + str(colorCount) + " for " + colorCheck
                #   print ("VERTICAL cell ( " + str(colNum) + " ," + str(row) + ") = " + cells[colNum][row] + " COLOR COUNT = " + str(colorCount))
                    if (colorCount2 == 4):
                        if (colorCheck == "#FF0000"):
                            print ("RED WINS")
                        elif (colorCheck == "#FFFF00"): 
                            print ("YELLOW WINS")
                        return "WINNER"    
                        exit
                else:
                    #reset yelCount to 0 if the color is not yellow
                    colorCount2 = 0     
                    
            # colorCount3
            if ((colNum==0 and row ==3) or (colNum==1 and row ==2) or (colNum==2 and row ==1) or (colNum==3 and row ==0)) :
                if (cells[colNum][row] == colorCheck):
                    colorCount3 = colorCount3 + 1
                #    print "color count =" + str(colorCount) + " for " + colorCheck
                #   print ("VERTICAL cell ( " + str(colNum) + " ," + str(row) + ") = " + cells[colNum][row] + " COLOR COUNT = " + str(colorCount))
                    if (colorCount3 == 4):
                        if (colorCheck == "#FF0000"):
                            print ("RED WINS")
                        elif (colorCheck == "#FFFF00"): 
                            print ("YELLOW WINS")
                        return "WINNER"    
                        exit
                else:
                    #reset yelCount to 0 if the color is not yellow
                    colorCount3 = 0     
            
            # colorCount4
            if ((colNum==1 and row ==5) or (colNum==2 and row ==4) or (colNum==3 and row ==3) or (colNum==4 and row ==2) or (colNum==5 and row ==1) 
                    or (colNum==6 and row ==0)) :
                if (cells[colNum][row] == colorCheck):
                    colorCount4 = colorCount4 + 1
                    if (colorCount4 == 4):
                        if (colorCheck == "#FF0000"):
                            print ("RED WINS")
                        elif (colorCheck == "#FFFF00"): 
                            print ("YELLOW WINS")
                        return "WINNER"    
                        exit
                else:
                    #reset Count to 0 
                    colorCount4 = 0   
              
            # colorCount5
            if ((colNum==2 and row ==5) or (colNum==3 and row ==4) or (colNum==4 and row ==3) or (colNum==5 and row ==2) or (colNum==6 and row ==1) ) :
                if (cells[colNum][row] == colorCheck):
                    colorCount5 = colorCount5 + 1
                    if (colorCount5 == 4):
                        if (colorCheck == "#FF0000"):
                            print ("RED WINS")
                        elif (colorCheck == "#FFFF00"): 
                            print ("YELLOW WINS")
                        return "WINNER"    
                        exit
                else:
                    #reset Count to 0 
                    colorCount5 = 0     
                    
            # colorCount6
            if ((colNum==3 and row ==5) or (colNum==4 and row ==4) or (colNum==5 and row ==3) or (colNum==6 and row ==2)  ) :
                if (cells[colNum][row] == colorCheck):
                    colorCount6 = colorCount6 + 1
                    if (colorCount6 == 4):
                        if (colorCheck == "#FF0000"):
                            print ("RED WINS")
                        elif (colorCheck == "#FFFF00"): 
                            print ("YELLOW WINS")
                        return "WINNER"    
                        exit
                else:
                    #reset Count to 0 
                    colorCount6 = 0    
                    
def checkLeftAngle(colorCheck):
    
    colorCount1 = 0
    colorCount2 = 0
    colorCount3 = 0 
    colorCount4 = 0 
    colorCount5 = 0 
    colorCount6 = 0 
    for colNum in reversed(range(0,7)):
        for row in reversed(range(0,6)):
            if ((colNum==6 and row ==5) or (colNum==5 and row ==4) or (colNum==4 and row ==3) or (colNum==3 and row ==2) or (colNum==2 and row ==1) 
                    or (colNum==1 and row ==0)) :
                if (cells[colNum][row] == colorCheck):
                    colorCount1 = colorCount1 + 1
                    if (colorCount1 == 4):
                        if (colorCheck == "#FF0000"):
                            print ("RED WINS")
                        elif (colorCheck == "#FFFF00"): 
                            print ("YELLOW WINS")
                        return "WINNER"    
                        exit
                else:
                    #reset yelCount to 0 if the color is not yellow
                    colorCount1 = 0     
            # colorCount2
            if ((colNum==6 and row ==4) or (colNum==5 and row ==3) or (colNum==4 and row ==2) or (colNum==3 and row ==1) or (colNum==2 and row ==0)) :
                if (cells[colNum][row] == colorCheck):
                    colorCount2 = colorCount2 + 1
                    if (colorCount2 == 4):
                        if (colorCheck == "#FF0000"):
                            print ("RED WINS")
                        elif (colorCheck == "#FFFF00"): 
                            print ("YELLOW WINS")
                        return "WINNER"    
                        exit
                else:
                    #reset yelCount to 0 if the color is not yellow
                    colorCount2 = 0     
                    
            # colorCount3
            if ((colNum==6 and row ==3) or (colNum==5 and row ==2) or (colNum==4 and row ==1) or (colNum==3 and row ==0)) :
                if (cells[colNum][row] == colorCheck):
                    colorCount3 = colorCount3 + 1
                    if (colorCount3 == 4):
                        if (colorCheck == "#FF0000"):
                            print ("RED WINS")
                        elif (colorCheck == "#FFFF00"): 
                            print ("YELLOW WINS")
                        return "WINNER"    
                        exit
                else:
                    #reset yelCount to 0 if the color is not yellow
                    colorCount3 = 0     
            
            # colorCount4
            if ((colNum==5 and row ==5) or (colNum==4 and row ==4) or (colNum==3 and row ==3) or (colNum==2 and row ==2) or (colNum==1 and row ==1) 
                    or (colNum==0 and row ==0)) :
                if (cells[colNum][row] == colorCheck):
                    colorCount4 = colorCount4 + 1
                    if (colorCount4 == 4):
                        if (colorCheck == "#FF0000"):
                            print ("RED WINS")
                        elif (colorCheck == "#FFFF00"): 
                            print ("YELLOW WINS")
                        return "WINNER"    
                        exit
                else:
                    #reset Count to 0 
                    colorCount4 = 0   
              
            # colorCount5
            if ((colNum==4 and row ==5) or (colNum==3 and row ==4) or (colNum==2 and row ==3) or (colNum==1 and row ==2) or (colNum==0 and row ==1) ) :
                if (cells[colNum][row] == colorCheck):
                    colorCount5 = colorCount5 + 1
                    if (colorCount5 == 4):
                        if (colorCheck == "#FF0000"):
                            print ("RED WINS")
                        elif (colorCheck == "#FFFF00"): 
                            print ("YELLOW WINS")
                        return "WINNER"    
                        exit
                else:
                    #reset Count to 0 
                    colorCount5 = 0     
                    
            # colorCount6
            if ((colNum==3 and row ==5) or (colNum==2 and row ==4) or (colNum==1 and row ==3) or (colNum==0 and row ==2)  ) :
                if (cells[colNum][row] == colorCheck):
                    colorCount6 = colorCount6 + 1
                    if (colorCount6 == 4):
                        if (colorCheck == "#FF0000"):
                            print ("RED WINS")
                        elif (colorCheck == "#FFFF00"): 
                            print ("YELLOW WINS")
                        return "WINNER"    
                        exit
                else:
                    #reset Count to 0 
                    colorCount6 = 0    
 

        

    
    
