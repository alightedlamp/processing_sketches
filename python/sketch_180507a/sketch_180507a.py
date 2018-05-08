size(800, 1300)
background(5, 25, 120, 75)
noStroke()

PAINTING_WIDTH = 800
PAINTING_HEIGHT = 1300
    
x = 0
y = 0

for i in range(100):
    fill(5, 75, 175, 150)
    rect(x, y, PAINTING_WIDTH, 17)
    y += 7

x = 0
y = 0

fill(5)
rect(0, PAINTING_HEIGHT / 3, PAINTING_WIDTH, PAINTING_HEIGHT / 2)

for i in range(100):
    fill(250, 50, 25, 225)
    rect(x, y, PAINTING_WIDTH / 2, 75)
    y += 17

x = 0
y = 0

translate(PAINTING_WIDTH / 2, 0)

for i in range(1000):
    rotate(random(1, 5))
    l = PAINTING_WIDTH
    fill(110, 22, 65)
    ellipse(x, y, 15, 15)
    x += 1
    y += 1

resetMatrix()

translate(PAINTING_WIDTH / 2, 0)
rotate(1.5)

fill(255, 0, 0, 100)
rect(0, 0, PAINTING_WIDTH, PAINTING_HEIGHT / 3)

resetMatrix()

translate(PAINTING_HEIGHT / 2, PAINTING_WIDTH / 2)

def blurry_rects(w, h, c, r):
    x = 0
    y = 0

    for i in range(r):
        rotate(random(0, 1))
        fill(c)
        rect(x + w, y + h, w, h)
        x += w * random(0, 3)
        y += h * random(0, 2)

c = color(65, 50, 250, random(50, 75))
blurry_rects(200, 200, c, 100)

c = color(140, 50, 20, 255)
blurry_rects(20, 20, c, 20)

resetMatrix()

fill(40, 40, 40, 200)
rect(0, 0, PAINTING_WIDTH / 2, PAINTING_HEIGHT / 2)

strokeWeight(4)
stroke(255, 130, 0)
a = 0.0
inc = TWO_PI/25.0
for i in range(0, 1000, 4):
    rotate(.3)
    line(i, random(PAINTING_HEIGHT, 200) - 500, i, (PAINTING_HEIGHT / 2) + sin(a) * 40.0)
    a = a + inc
