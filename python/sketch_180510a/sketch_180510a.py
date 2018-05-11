t = 0

c1 = color(200, 125, 60, 50)
c2 = color(40, 25, 250, 25)
c3 = color(250, 30, 150, 25)
c4 = color(200, 25, 25, 25)
c5 = color(250, 75, 50, 165)
    
def setup():
    size(800, 820)
    background(110, 25, 30)
    noLoop()
    noStroke()
    
    
def add_border():
    noFill()
    stroke(250, 250, 250)
    strokeWeight(25)
    rect(0, 0, width, height)
    

def draw_pointilism_rectangle(r, c):
    r_start_x = random(50, 100)
    r_start_y = random(50, 100)
    r_length = random(width / 2, width)
    r_height = random(height / 2, height)
    
    fill(c)
    
    for i in range(r):
        x = random(r_start_x, r_start_x + r_length)
        y = random(r_start_y, r_start_y + r_height)
        
        ellipse(x, y, 16, 16)


def draw_noise_rectangles(r, c):
    global t
    
    fill(c)

    l = random(0, width)
    h = random(0, height)
    
    for i in range(r):
        x = map(noise(t), 0, 1, random(0, width / 2), width)
        y = map(noise(t), 0, 1, random(0, height / 2), height)
        
        rect(x, y, l, h)
        
        t += 0.5
        
        
def draw_scribble_wave(c):
    global c1, c4
    
    fill(c)
    
    w = random(100, 500)
    rect(0, 0, w, height)
    
    strokeWeight(5)
    stroke(blendColor(c1, c4, BLEND), random(20, 100))
    
    xoff = 0.0
    
    for i in range(1000):
        xoff = xoff + .01
        n = noise(xoff) * i
        line(n, height, random(0, w), n)
        
        
def draw_sun():
    noStroke()
    fill(c5)
    ellipse(
            random(0, width * .5), 
            random(0, height * .75), 
            random(400, width), 
            random(400, height)
            )
        

def draw_grass():
    x = 0
    h = height * .33
    c = color(10, 175, 80, 75)
    
    strokeWeight(5)
    stroke(c)
    
    for i in range(width / 5):
        # x1, y1, x2, y2
        line(x, height, x + 55, height - (h + (x * .05)))
        x += 10
        
    noStroke()


def draw():
    draw_noise_rectangles(250, c4)
    draw_pointilism_rectangle(5000, c2)
    draw_scribble_wave(blendColor(c1, c4, OVERLAY))
    
    rotate(radians(2))
    fill(20, 60, 200)
    rect(0, random(0, height), width + 100, random(25, 175))
    resetMatrix()
    
    draw_sun()
    draw_grass()
    
    add_border()
    noStroke()
    
def mousePressed():
    loop()
    
def mouseReleased():
    noLoop()