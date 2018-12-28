x = 0
y = 0
def setup():
    size (900, 700)

def draw():
    global x
    global y
    #if x >= 640:
        #x = 0
    y += 5
    if y >= 541:
        y = 541
    
        
    background(244, 222, 179) 
    
    #pieces?
    #fill ("#B22222")
    #ellipse(x, 50, 80, 80)
    

    
    #(x, y, width, height)
    
    #blue square board
    fill ("#0000FF")
    rect (150, 85, 600, 500)
    
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
        
        #Red and yellow poeces
        
        #Instructions screen
        
        #You win screen
        
        #You lose screen
        
        #You tied screen
        
        #Animations
        
        #Beige backround
        
        fill ("#FF0000")
        ellipse (210, y, 70, 70)
        
