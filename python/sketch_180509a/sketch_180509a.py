def setup():
    size(1000, 1050)
    background(255, 60, 20)
    noLoop()
    
def add_border():
    stroke(250, 250, 250)
    strokeWeight(25)
    rect(0, 0, width, height)

def draw():
    
    # Background circle accents
    noFill()
    noStroke()
    translate(width / 2, height / 2)
    
    x = 0
    y = 0
    for i in range(2000):
        rotate(radians(45))
        fill(random(50, 255), random(110, 150), 50, random(0, 250))
        ellipse(random(width / 5, x), random(height / 5, y), 5, 5)
        x += 1
        y += 1
        
    resetMatrix()
    
    xoff = 0.0
    strokeWeight(1)
    for i in range(1000):
        
        # Blue noise field
        xoff = xoff + .01
        n = noise(xoff) * i
        stroke(random(20, 75), 50, random(100, 175), random(0, 50))
        line(n, height, n, random(0, height / 2))
    
        translate(height / 2, width / 2)
        rotate(radians(random(0, 90)))
        noStroke()
        fill(random(50, 50), 20, random(50, 20), random(0, 255))
        rect(random(0, width), random(0, height), 25, 25)
        
        resetMatrix()
        
    a = 0.0
    inc = TWO_PI / 25.0
    for i in range(0, 1000, 5):
        fill(random(100, 150), random(0, 75), random(60, 95), random(0, 25))
        rect(i, height / random(0, height), i, height + sin(a) * 40.0)
        a = a + inc
    
    for i in range(5):
        fill(random(175, 150), random(100, 150), 20, random(0, 75))
        ellipse(width / random(0, 5), height / random(0, 5), width, height)
        noFill()
        
    rotate(radians(2))
    fill(255, 25, 25, random(75, 255))
    rect(random(0, width / 2), random(0, height / 2), 80, 750)
    
    resetMatrix()
    
    rotate(radians(45))
    fill(30, 25, 255, 100)
    ellipse(0, height / 3, width, height / 2)
    noFill()
    
    resetMatrix()
    
    add_border()
        
    
def mousePressed():
    loop()
    
def mouseReleased():
    noLoop()