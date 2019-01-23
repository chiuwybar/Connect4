#def startScreen():
    #background (0)
    #textAlign(CENTER)
    #text ("Click to start", height/2, width/2)
    
#def startScreen():
    #background (255)    
#variables
x = 0
y = 50
w = 900
h = 700

#set up
def setup():
    size (w, h)

def draw():
    global x
    global y
    #if x >= 640:
        #x = 0
    #y += 5
    #if y >= 541:
        #y = 541
        
    background(244, 222, 179) 
    
    #pieces?
    #fill ("#B22222")
    #ellipse(x, 50, 80, 80)
    

    
    #(x, y, width, height)
    
    #blue square board
    fill ("#0000FF")
    rect (150, 85, 600, 500)
    
    #legs of board
    fill ("#0000FF")
    rect (150, 585, 18, 100)
    rect (732, 585, 18, 100)
    
    # 7(horizonal) x 6 (vertical)
    fill ("#FFFFFF")
    
    # y position for first circle
    y_pos = 140
    for columns in range (1, 7):
        # x position for first circle
        x_pos = 210

        fill ("#FFFFFF")
        #Row of circles
        for i in range (1, 8):
            ellipse (x_pos, y_pos, 70, 70)
            x_pos = x_pos + 80
        y_pos = y_pos + 80
        
        #2 player game
        
        #Still tryna figure out how to make player turns
        
        #Red and yellow pieces (done)
        
        #Instructions screen(not done)
        
        #You win screen(not done)
        
        #You lose screen(not done)
        
        #You tied screen(not done)
        
        #Animations(somewhat done)
        
        #Beige backround(done)
       
    #red piece
    fill ("#FF0000")
    ellipse (210, y, 70, 70)
        

    #yellow piece (moves horizontally with mouse)
    fill ("#FFFF00")
    ellipse (mouseX, y, 70, 70)
