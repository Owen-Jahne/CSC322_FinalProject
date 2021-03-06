from OpenGL.GL import *
from OpenGL.GLUT import *
from math import *
import random

width, height = 800, 800  # window size

s = random.randint(0, 10)
s2 = random.randint(0, 10)
s3 = random.randint(0, 10)
rand = s / 10
rand2 = s2 / 10
rand3 = s3 / 10
s4 = random.randint(0, 700)


def drawSun(posx, posy, sides, radius):
    glBegin(GL_POLYGON)
    for i in range(100):
        cosine = radius * cos(i * 2 * pi / sides) + posx
        sine = radius * sin(i * 2 * pi / sides) + posy
        glVertex2f(cosine, sine)
    glEnd()

def drawCloud(posx, posy, sides, radius):
    glBegin(GL_POLYGON)
    for i in range(50):
        cosine = radius * cos(i * 2 * pi / sides) + posx
        sine = radius * sin(i * 2 * pi / sides) + posy
        glVertex2f(cosine, sine)
    glEnd()

def drawSquare(x, y, width, height):
    glBegin(GL_QUADS)  # start drawing a square
    glVertex2f(x, y)  # bottom left point
    glVertex2f(x + width, y)  # bottom right point
    glVertex2f(x + width, y + height)  # top right point
    glVertex2f(x, y + height)  # top left point
    glEnd()  # done drawing

def drawTriangle(x, y, width, height):
    glBegin(GL_TRIANGLES)
    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x + width, y + height)
    glEnd()

def drawTriangle2(x, y, width, height):
    glBegin(GL_TRIANGLES)
    glVertex2f(x, y)
    glVertex2f(x, y + height)
    glVertex2f(x + width, y)
    glEnd()

def drawTrunk(x, y, width, height):  # tree trunk
    glBegin(GL_QUADS)  # start drawing a square
    glVertex2f(x, y)  # bottom left point
    glVertex2f(x + width, y)  # bottom right point
    glVertex2f(x + width, y + height)  # top right point
    glVertex2f(x, y + height)  # top left point
    glEnd()  # done drawing

def drawLeaves(posx, posy, sides, radius):
    glBegin(GL_POLYGON)
    for i in range(100):
        cosine = radius * cos(i * 2 * pi / sides) + posx
        sine = radius * sin(i * 2 * pi / sides) + posy
        glVertex2f(cosine, sine)
    glEnd()

def drawBirds(x, y, width, height):
    glBegin(GL_LINES)
    glVertex2f(x, y)
    glVertex2f(x + width, y + height)
    glEnd()

def drawBirds2(x, y, width, height):
    glBegin(GL_LINES)
    glVertex2f(x + width, y + height)
    glVertex2f(x, y)
    glEnd()

def drawScene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # clear the screen
    glLoadIdentity()  # reset position
    refresh2d(width, height)

    glColor3f(0.5, 0.5, 1.0)  # set color to blue
    drawSquare(0, 100, 1000, 1000)
    glColor3f(1.0, 1.0, 0.0)  # sun color yellow

    drawSun(650, 700, 32, 50)

    glColor3f(0.0, 0.7, 0.0)  # set color to green
    drawSquare(0, 0, 1000, 400)

    glColor3f(rand, rand2, rand3)  # tallest mountain in back
    drawTriangle(300, 350, 150, 290)
    drawTriangle2(450, 350, 150, 290)

    glColor3f(rand2, rand3, rand)  # left mountain
    drawTriangle(350, 350, 200, 240)
    drawTriangle2(550, 350, 200, 240)

    glColor3f(rand3, rand, rand2)  # right mountain
    drawTriangle(100, 350, 200, 260)
    drawTriangle2(300, 350, 200, 260)



    glColor3f(0.4, 0.0, 0.0)  # set color to green
    drawTrunk(617, 320, 20, 150)  # draw the tree stump on the screen

    glColor3f(0.0, 0.5, 0.0)  # set color to darkgreen
    drawLeaves(625, 450, 50, 50)  # draw the tree leaves on the screen

    glColor3f(1.0, 1.0, 1.0) #set color to white
    drawCloud(200,500, 32, 50)

def drawParallax(x_mouse, y_mouse):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # clear the screen
    glLoadIdentity()  # reset position
    refresh2d(width, height)


    triangleX = (x_mouse - 400) * 0.0625
    triangleY = (y_mouse - 400) * 0.0625

    triangleX2 = (x_mouse - 400) * 0.025
    triangleY2 = (y_mouse - 400) * 0.025

    triangleX3 = (x_mouse - 400) * 0.0425
    triangleY3 = (y_mouse - 400) * 0.0425

    # tree
    treeX = (x_mouse - 400) * 0.15
    treeY = (y_mouse - 400) * 0.15

    # sun
    layer1X = (x_mouse - 400) * 0.02
    layer1Y = (y_mouse - 400) * 0.02
    layer2X = (x_mouse - 400) * 0.34
    layer3X = (x_mouse - 400) * 0.32
    layer2Y = (y_mouse - 400) * 0.05
    layer3Y = (y_mouse - 400) * 0.08


    if(s4 < 300):
        glColor3f(0.0, 0.0, 0.3)  # set color to dark blue
        drawSquare(0, 0, 800, 800)
        i = 0
        h = 0
        w = 0
        while (i < 4):
            i += 1
            h += 160
            w += 3
            glColor3f(1.0, 1.0, 1.0)
            drawCloud(h, 750 - w, 32, 3)

        i2 = 0
        h2 = 0
        w2 = 0
        while (i2 < 3):
            i2 += 1
            h2 += 250
            w2 += 5
            glColor3f(1.0, 1.0, 1.0)
            drawCloud(h2, 650 + w2, 32, 3)

        drawCloud( 25,  550 , 32, 1)
        drawCloud( 40, 400, 32, 2)
        drawCloud( 300,  500, 32, 3)
        drawCloud( 700, 450, 32, 2)
        drawCloud( 750,  550, 32, 1)
        drawCloud( 600,  520, 32, 2)
        drawCloud( 400, 570, 32, 3)
        glColor3f(1.0, 1.0, 0.0)  # color yellow
        drawSun(layer1X + 650, layer1Y + 600, 32, 50)
        glColor3f(0.0, 0.0, 0.3)  # color dark blue
        drawSun(layer1X + 670, layer1Y + 600, 32, 50)


        glColor3f(0.5, 0.5, 0.5)  # set color to white
        drawCloud(layer2X + 200, layer3Y + 600, 32, 25)
        drawCloud(layer2X + 220, layer2Y + 600, 32, 25)
        drawCloud(layer2X + 240, layer3Y + 600, 32, 25)
        drawCloud(layer2X + 260, layer2Y + 600, 32, 25)
        drawCloud(layer3X + 205, layer3Y + 615, 32, 25)
        drawCloud(layer3X + 225, layer2Y + 615, 32, 25)
        drawCloud(layer3X + 245, layer3Y + 615, 32, 25)
        drawCloud(layer3X + 265, layer2Y + 615, 32, 25)
        drawCloud(layer2X + 270, layer3Y + 600, 32, 25)

        drawCloud(layer2X + 400, layer3Y + 715, 32, 25)
        drawCloud(layer2X + 420, layer2Y + 715, 32, 25)
        drawCloud(layer2X + 440, layer3Y + 715, 32, 25)
        drawCloud(layer2X + 460, layer2Y + 715, 32, 25)
        drawCloud(layer3X + 405, layer3Y + 700, 32, 25)
        drawCloud(layer3X + 425, layer2Y + 700, 32, 25)
        drawCloud(layer3X + 445, layer3Y + 700, 32, 25)
        drawCloud(layer3X + 465, layer2Y + 700, 32, 25)
        drawCloud(layer2X + 470, layer3Y + 715, 32, 25)



        glColor3f(rand, rand2, rand3)  # tallest mountain in back
        drawTriangle(triangleX2 + 300, 250 + triangleY2, 150, 290)
        drawTriangle2(triangleX2 + 450, 250 + triangleY2, 150, 290)

        glColor3f(rand2, rand3, rand)  # right mountain
        drawTriangle(triangleX3 + 350, triangleY3 + 250, 200, 240)
        drawTriangle2(triangleX3 + 550, triangleY3 + 250, 200, 240)

        glColor3f(rand3, rand, rand2)  # left mountain
        drawTriangle(triangleX + 100, triangleY + 250, 200, 260)
        drawTriangle2(triangleX + 300, triangleY + 250, 200, 260)

        glColor3f(0.0, 0.3, 0.0)  # set color to green
        drawSquare(-100 + treeX, -100 + treeY, 1000, 400)
        x = 0
        n = -100
        while (x < 240):  # loop for 240 blades of grass
            x += 1
            n += 5
            glColor3f(0.0, 0.3, 0.0)
            drawSquare(n + treeX, 300 + treeY, 2, 8)


    if (  300 <= s4 <= 450 ):
        glColor3f(1.0, 0.5, 0.0)  # set color to orange
        drawSquare(0, 0, 800, 800)
        glColor3f(1.0, 0.8, 0.0)  # sun color yellow/orange
        drawSun(layer1X + 650, s4, 32, 50)

        glColor3f(1.0, 0.7, 1.0)  # set color to white
        drawCloud(layer2X + 200, layer3Y + 600, 32, 25)
        drawCloud(layer2X + 220, layer2Y + 600, 32, 25)
        drawCloud(layer2X + 240, layer3Y + 600, 32, 25)
        drawCloud(layer2X + 260, layer2Y + 600, 32, 25)
        drawCloud(layer3X + 205, layer3Y + 615, 32, 25)
        drawCloud(layer3X + 225, layer2Y + 615, 32, 25)
        drawCloud(layer3X + 245, layer3Y + 615, 32, 25)
        drawCloud(layer3X + 265, layer2Y + 615, 32, 25)
        drawCloud(layer2X + 270, layer3Y + 600, 32, 25)

        drawCloud(layer2X + 400, layer3Y + 715, 32, 25)
        drawCloud(layer2X + 420, layer2Y + 715, 32, 25)
        drawCloud(layer2X + 440, layer3Y + 715, 32, 25)
        drawCloud(layer2X + 460, layer2Y + 715, 32, 25)
        drawCloud(layer3X + 405, layer3Y + 700, 32, 25)
        drawCloud(layer3X + 425, layer2Y + 700, 32, 25)
        drawCloud(layer3X + 445, layer3Y + 700, 32, 25)
        drawCloud(layer3X + 465, layer2Y + 700, 32, 25)
        drawCloud(layer2X + 470, layer3Y + 715, 32, 25)

        glColor3f(rand, rand2, rand3)  # tallest mountain in back
        drawTriangle(triangleX2 + 300, 250 + triangleY2, 150, 290)
        drawTriangle2(triangleX2 + 450, 250 + triangleY2, 150, 290)

        glColor3f(rand2, rand3, rand)  # right mountain
        drawTriangle(triangleX3 + 350, triangleY3 + 250, 200, 240)
        drawTriangle2(triangleX3 + 550, triangleY3 + 250, 200, 240)

        glColor3f(rand3, rand, rand2)  # left mountain
        drawTriangle(triangleX + 100, triangleY + 250, 200, 260)
        drawTriangle2(triangleX + 300, triangleY + 250, 200, 260)

        glColor3f(0.0, 0.6, 0.0)  # set color to green
        drawSquare(-100 + treeX, -100 + treeY, 1000, 400)
        x = 0
        n = -100
        while (x < 240):  # loop for 240 blades of grass
            x += 1
            n += 5
            glColor3f(0.0, 0.6, 0.0)
            drawSquare(n + treeX, 300 + treeY, 2, 8)

    if (  s4 >= 450 ):
        glColor3f(0.0, 0.0, 1.0)  # set color to blue
        drawSquare(0, 0, 800, 800)
        glColor3f(1.0, 1.0, 0.0)  # sun color yellow
        drawSun(layer1X + 650, s4, 32, 50)

        glColor3f(1.0, 1.0, 1.0)  # set color to white
        drawCloud(layer2X + 200, layer3Y + 600, 32, 25)
        drawCloud(layer2X + 220, layer2Y + 600, 32, 25)
        drawCloud(layer2X + 240, layer3Y + 600, 32, 25)
        drawCloud(layer2X + 260, layer2Y + 600, 32, 25)
        drawCloud(layer3X + 205, layer3Y + 615, 32, 25)
        drawCloud(layer3X + 225, layer2Y + 615, 32, 25)
        drawCloud(layer3X + 245, layer3Y + 615, 32, 25)
        drawCloud(layer3X + 265, layer2Y + 615, 32, 25)
        drawCloud(layer2X + 270, layer3Y + 600, 32, 25)

        drawCloud(layer2X + 400, layer3Y + 715, 32, 25)
        drawCloud(layer2X + 420, layer2Y + 715, 32, 25)
        drawCloud(layer2X + 440, layer3Y + 715, 32, 25)
        drawCloud(layer2X + 460, layer2Y + 715, 32, 25)
        drawCloud(layer3X + 405, layer3Y + 700, 32, 25)
        drawCloud(layer3X + 425, layer2Y + 700, 32, 25)
        drawCloud(layer3X + 445, layer3Y + 700, 32, 25)
        drawCloud(layer3X + 465, layer2Y + 700, 32, 25)
        drawCloud(layer2X + 470, layer3Y + 715, 32, 25)

        glColor3f(rand, rand2, rand3)  # tallest mountain in back
        drawTriangle(triangleX2 + 300, 250 + triangleY2, 150, 290)
        drawTriangle2(triangleX2 + 450, 250 + triangleY2, 150, 290)

        glColor3f(rand2, rand3, rand)  # right mountain
        drawTriangle(triangleX3 + 350, triangleY3 + 250, 200, 240)
        drawTriangle2(triangleX3 + 550, triangleY3 + 250, 200, 240)

        glColor3f(rand3, rand, rand2)  # left mountain
        drawTriangle(triangleX + 100, triangleY + 250, 200, 260)
        drawTriangle2(triangleX + 300, triangleY + 250, 200, 260)

        glColor3f(0.0, 1.0, 0.0)  # set color to green
        drawSquare(-100 + treeX, -100 + treeY, 1000, 400)
        x = 0
        n = -100
        while (x < 240):  # loop for 240 blades of grass
            x += 1
            n += 5
            glColor3f(0.0, 1.0, 0.0)
            drawSquare(n + treeX, 300 + treeY, 2, 8)

    glColor3f(0.4, 0.0, 0.0)  # set color to brown
    drawTrunk(treeX + 617, treeY + 220, 20, 150)  # draw the tree stump on the screen

    glColor3f(0.0, 0.5, 0.0)  # set color to darkgreen
    drawLeaves(treeX + 625, treeY + 350, 50, 50)  # draw the tree leaves on the screen

    i = 0
    j = 150
    y2 = 700
    s5 = random.randint(1,2)
    movement =+ s5
    while (i < 5):    #loop for 5 birds
        i += 1
        j += 35
        y2 += 8
        glColor(0, 0, 0)
        drawBirds(j + s5, y2, 5, 5)
        drawBirds2(j + 5 + s5, y2 + 5, 5, -5)



    glutSwapBuffers()  # important for double buffering


def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


# initialization

glutInit()  # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH | GLUT_DOUBLE)
glutInitWindowSize(width, height)  # set window size
glutInitWindowPosition(0, 0)  # set window position
wind = glutCreateWindow("Landscape")  # create window with title
glutDisplayFunc(drawScene)  # set showScreen function callback
glutIdleFunc(drawScene)
glutPassiveMotionFunc(drawParallax)
# draw all the time
glutMainLoop()  # start everything
