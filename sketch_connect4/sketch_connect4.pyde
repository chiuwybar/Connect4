x = 0

def setup():
    size (900, 700)

def draw():
    global x
    if x >= 640:
        x = 0
    x += 1
    background(244, 222, 179) 
    
    #pieces?
    #fill ("#B22222")
    #ellipse(x, 50, 80, 80)
    
    #(x, y, width, height)
    
    #blue square board
    fill ("#0000FF")
    rect (150, 85, 600, 600)
    
    # 7(horizonal) x 6 (vertical)
    fill ("#FFFFFF")
    #ellipse (210, 140, 70, 70)
    #ellipse (290, 140, 70, 70)
    x_pos = 210
    for i in range (1, 8):
        ellipse (x_pos, 140, 70, 70)
        x_pos = x_pos + 80
    
