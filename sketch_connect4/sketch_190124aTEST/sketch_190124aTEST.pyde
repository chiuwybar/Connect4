cells = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],["BLUE",0,0,0,0,0]]
print ("CELL 0,5 = " + str(cells[0][5]))


x = 0
y_pos2 = 50
x_pos2=0
colorCount = 1
global colorCode
colorCode = "#FF0000"

def setup():
    size(900, 700)
    #noLoop()

def draw():
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
    #fill("#FFFFFF")
    
    # initial Board is 7 x 8 white circles
    # y position for first circle
    y_pos = 140
    for columns in range (0, 6):
    # x position for first circle
        x_pos = 210
        # White color
        fill ("#FFFFFF")
        #Row of circles initally white
        for rows in range (0, 7):
            ellipse (x_pos, y_pos, 70, 70)
            x_pos = x_pos + 80
        y_pos = y_pos + 80
    # board creation end
    '''
    identify which circle is filled and what color it is 
    when the peg is clicked check if the circle is over one of the columns
    
    
    '''
    
    
    fill("#FFFF00")
    ellipse (x_pos2, y_pos2, 70, 70)
    
    '''if mouseClicked:
        fill(204)
    else:    '''
    # player places circle over one of the columns and click
    # once clicked if the column is full then error
    # else find the lowest circle in the column that has no color 
    # get the y coordinate and drop the circle to that spot
    # x-positions of the columns 690, 610, 530, 450, 370, 290, 210
    # y-positions of the rows 540,460,380,300,220,140 
    fill(colorCode)
    ellipse (mouseX, 50 , 70, 70)
    if (175< mouseX < 245):
        #fill("#0000FF")
        #colorCode = "#0000FF"
        x_pos2 = 210
       # print ("Column 1!!!!!!THe value of x = " + str(mouseX)+ " Y value = " + str(y_pos2))
    elif (255< mouseX < 325):
        #fill("#0000FF")
        #colorCode = "#0000FF"
        x_pos2 = 290
       # print ("290 !!!!!!THe value of x = " + str(mouseX)+ " Y value = " + str(y_pos2))
    elif (335< mouseX < 405):
        #fill("#0000FF")
        #colorCode = "#0000FF"
        x_pos2 = 370
      #  print ("370 !!!!!!THe value of x = " + str(mouseX)+ " Y value = " + str(y_pos2))
    elif (415< mouseX < 485):
        #fill("#0000FF")
        #colorCode = "#0000FF"
        x_pos2 = 450
       # print ("450 !!!!!!THe value of x = " + str(mouseX)+ " Y value = " + str(y_pos2))
    elif (495< mouseX < 565):
        #fill("#0000FF")
        #colorCode = "#0000FF"
        x_pos2 = 530
      #  print ("530 !!!!!!THe value of x = " + str(mouseX)+ " Y value = " + str(y_pos2))
    elif (575< mouseX < 645):
        #fill("#0000FF")
        #colorCode = "#0000FF"
        x_pos2 = 610
       # print ("610 !!!!!!THe value of x = " + str(mouseX)+ " Y value = " + str(y_pos2))
    elif (655< mouseX < 725):
        #fill("#0000FF")
        #colorCode = "#0000FF"
        x_pos2 = 690
       # print ("690 !!!!!!THe value of x = " + str(mouseX) + " Y value = " + str(y_pos2))
def mouseClicked():
    # if the circle is outside the board on either side then raise a error and have 
    # the player put the piece inside the board before clicking
    #
    global colorCode
    global colorCount
    colorCount +=1
    ## if the count is even then YELLOW (FFFF00)
    #if colorCount % 2 > 0:
    #    colorCode = "#FFFFF00"
    ## if count is odd then RED (FF0000)
    #else:
    #    colorCode = "#FF0000"
    global x, y_pos2, x_pos2
    #if y_pos2 == 50:
    #    y_pos2 += 90
    #else:
    #    y_pos2 += 80
    #x += 10
    #coldict = { 210:0, 290:1, 370:2, 450:3, 530:4, 610:5, 690:6}
    coldict = { 0:210, 1:290, 2:370, 3:450, 4:530, 5:610, 6:690}
    #print("coldict = " + str(coldict[370]))
    #rowdict = {140:0, 220:1, 300:2, 380:3, 460:4, 540:5}
    rowdict = {0:140, 1:220, 2:300, 3:380, 4:460, 5:540}
    
    if(x_pos2 == 210):
        print ("XPOS = " + str(x_pos2))
        # check to see if the rows under that column are empty
        for i in range(0,6):
            print ("i = " + str(i) + " cell = " + str(cells[0][i]))
            #for j in range(0:5)
            if (cells[0][i] != 0):
                # if the top row already has a value then raise an error the player needs to choose another column
                if (i != 0) :
                    print (" VALUE = " + str(cells[0][i])) 
                    #listOfItems = rowdict.items()
                    #for item  in listOfItems:
                    #    if (item[1] == i):
                    #       y_pos2=item[0]
                    y_pos2=rowdict[i -1]
                    cells[0][i-1] = "RED"
                    print (" row = " + str(y_pos2))
                    break
                else:
                    print ("ERROR THIS COLUMN IS FULL")
            elif (i == 5):
                y_pos2 = rowdict[i]
                cells[0][i] = "RED"
            print cells[0]  
            
                
        
    
    redraw()
    
#def checkOpenPos():
    # assumes x_pos2 is set ... check the matrix based on the x_pos left to right
    # x_pos2 = 210 ->Column 1
    # x_pos2 = 280 ->Column 2
    # x_pos2 = 370 ->Columns 3
    # x_pos2 = 450 -> COlumn 4
    # x-pos2 = 540 -> column 5
    # x-pos2 = 620 -> column 6
    # x-pos2 = 690 -> column 7
    # y-pos2 = 140 -> row 1
    #
    
    
