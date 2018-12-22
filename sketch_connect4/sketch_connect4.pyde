x = 0

def setup():
    size (640, 480)

def draw():
    global x
    if x >= 640:
        x = 0
    x += 5
    background(244, 222, 179) 
    #clouds
    ellipse(x, 50, 80, 80)
    
    rect (0, 95, 800, 355)
