#variables
x = 0
y = 45
screen = "Main menu"
turn = "N/A"
time = 0

def setup():
    # window of game size
    size(900, 700)

#main menu
def main_menu():
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
    
    
def game():
    global screen, x, y, turn, time
    if screen == "Game":
        background(244, 222, 179)
        #pieces?
    #fill ("#B22222")
    #ellipse(x, 50, 80, 80)
    

    
    #(x, y, width, height)
    
    #blue square board
        fill("#0000FF")
        rect (150, 85, 600, 500)
    
    #legs of board
        fill("#0000FF")
        rect(150, 585, 18, 100)
        rect(732, 585, 18, 100)
    
    # 7(horizonal) x 6 (vertical)
        fill("#FFFFFF")
    
    # y position for first circle
        y_pos = 140
        for columns in range (1, 7):
        # x position for first circle
            x_pos = 210

            fill ("#FFFFFF")
        #Row of circles initally white
            for i in range (1, 8):
                
                '''if ((x_pos == 210) and (y_pos == 540)):
                    fill("#FFFF00")
                else:
                    fill("#FFFFFF")'''
                ellipse (x_pos, y_pos, 70, 70)
                x_pos = x_pos + 80
            y_pos = y_pos + 80
        
        #2 player game
        
        #Still tryna figure out how to make player turns
        
        #Red and yellow pieces
        
        #Instructions screen
        
        #You win screen
        
        #You lose screen
        
        #You tied screen
        
        #Animations
        
        #Beige backround
       
    #red piece
        #fill ("#FF0000")
        #ellipse (210, y, 70, 70)
        

    #yellow piece (moves horizontally with mouse)
        if turn == "yellow":
            
            # if i am over the bottom left circle then make the color yellow
            if overCircle(210, 540, 70):
                fill ("#FFFF00")
        elif turn == "red":
            fill ("#FF0000")
            drop(210,460)
        #piece follows mouse
        ellipse (mouseX, 50 , 70, 70)
        #Changes turns (2 players)  #every 0.50 second, turn can be made
        if mousePressed == True and time + 500 <= millis():
            time = millis()
            if turn == "yellow":
                
                turn = "red"
            else:
                turn = "yellow"
def drop(x,y):
    for i in range(50,540):    
        ellipse (x, i , 70, 70)
        i = i + 40
        
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
    
def overCircle(x, y, diameter):
    distance = dist(x, y, mouseX, mouseY)
    return distance < diameter / 2
