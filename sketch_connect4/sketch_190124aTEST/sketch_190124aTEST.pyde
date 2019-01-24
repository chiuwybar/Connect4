  
x = 0
y_pos2 = 50

def setup():
    size(900, 700)
    #noLoop()

def draw():
    background(204)
   # line(x, 0, x, height)
    
    #blue square board
    fill("#0000FF")
    rect (150, 85, 600, 500)
    
    #legs of board
    fill("#0000FF")
    rect(150, 585, 18, 100)
    rect(732, 585, 18, 100)
    
    # 7(horizonal) x 6 (vertical)
    #fill("#FFFFFF")
    
    # y position for first circle
    y_pos = 140
    for columns in range (1, 7):
    # x position for first circle
        x_pos = 210
        # White color
        fill ("#FFFFFF")
        #Row of circles initally white
        for i in range (1, 8):
            ellipse (x_pos, y_pos, 70, 70)
            x_pos = x_pos + 80
        y_pos = y_pos + 80
    fill("#FFFF00")
    ellipse (210, y_pos2, 70, 70)
    fill("#FFFF00")
    ellipse (mouseX, 50 , 70, 70)
    print ("THe value of x = " + str(mouseX))
def mousePressed():
    global x, y_pos2
    if y_pos2 == 50:
        y_pos2 += 90
    else:
        y_pos2 += 80
    x += 10
    redraw()
