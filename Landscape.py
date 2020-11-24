###
### Adopted from https://stackabuse.com/brief-introduction-to-opengl-in-python-with-pyopengl/
### CSC 322 Fall 2020

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
import random



window = 0
width, height = 800, 800  # window size

s = random.randint(0,10)
s2 = random.randint(0,10)
s3 = random.randint(0,10)
rand = s/10
rand2 = s2/10
rand3 = s3/10

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
    glVertex2f(x, y + height )
    glVertex2f(x + width, y)
    glEnd()

def drawBirds(x,y, width, height):
    glBegin(GL_LINES)
    glVertex2f(x,y)
    glVertex2f(x+width,y+height)
    glEnd()

def drawBirds2(x,y, width, height):
    glBegin(GL_LINES)
    glVertex2f(x+width,y+height)
    glVertex2f(x,y)
    glEnd()

def drawSun(posx, posy, sides, radius):
    glBegin(GL_POLYGON)
    for i in range(100):
        cosine = radius * cos(i * 2 * pi / sides) + posx
        sine = radius * sin(i * 2 * pi / sides) + posy
        glVertex2f(cosine, sine)
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
        cosine = radius * cos(i * 2 * pi / sides ) + posx
        sine = radius * sin(i * 2 * pi / sides ) + posy
        glVertex2f(cosine, sine)
    glEnd()

def drawScene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # clear the screen
    glLoadIdentity()  # reset position
    refresh2d(width, height)

# background

    glColor3f(0.5, 0.5, 1.0)  # set color to blue
    drawSquare(0, 100, 1000, 1000)

    glColor3f(0.0, 0.7, 0.0)  # set color to green
    drawSquare(0,0 , 1000, 400)

#layer 1

    glColor3f(rand, rand2, rand3)        # tallest mountain in back
    drawTriangle(300, 400, 150, 290)
    drawTriangle2(450, 400, 150, 290)

#layer 2

    glColor3f(rand2, rand3, rand)        # left mountain
    drawTriangle(350, 400, 200, 240)
    drawTriangle2(550, 400, 200, 240)

    glColor3f(rand3, rand, rand2)  # right mountain
    drawTriangle(100, 400, 200, 260)
    drawTriangle2(300, 400, 200, 260)

#layer3

    x = 0
    n = 0
    while (x < 160):
        x += 1
        n += 5
        glColor3f(0.0, 1.0, 0.0)
        drawSquare(n, 400, 2, 8)

    glColor3f(0.4, 0.0, 0.0)  # set color to green
    drawTrunk(610, 320, 35, 150)  # draw the tree stump on the screen

    glColor3f(0.0, 0.5, 0.0)  # set color to green
    drawLeaves(625, 450, 50, 50)  # draw the tree stump on the screen


#layer 4

    glColor3f(1.0, 1.0, 0.0)  # sun color yellow
    drawSun(650, 700, 32, 50)

#birds

    i = 0
    j = 150
    y2 = 700
    while(i<5):
        i+=1
        j+=35
        y2+= 8
        glColor(0,0,0)
        drawBirds(j,y2,5,5)
        drawBirds2(j+5,y2+5,5,-5)

#parallax
def drawParallax(x_mouse, y_mouse):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # clear the screen
    glLoadIdentity()  # reset position
    refresh2d(width, height)

    foregroundX = (x_mouse - 250) * 0.5
    foregroundY = (y_mouse - 250) * 0.5
    triangleX = (x_mouse - 250) * 0.25
    triangleY = (y_mouse - 250) * 0.25
    # trunk
    trunkX = (x_mouse - 250) * 0.5
    trunkY = (y_mouse - 250) * 0.5
    # sun
    layer1X = (x_mouse - 250) * 0.02
    layer1Y = (y_mouse - 250) * 0.02
    # leaves
    leavesX = (x_mouse - 250) * 0.02
    leavesY = (x_mouse - 250) * 0.02

    glColor3f(0.0, 0.0, 1.0)  # set color to blue
    drawSquare(0, 0, 800, 800)

    glColor3f(0.0, 1.0, 0.0)  # set color to green
    drawSquare(0, 0, 1000, 400)

    glColor3f(0.7, 0.1, 0.1)  # tallest mountain in back
    drawTriangle(triangleX + 300, triangleY, 150, 290)
    drawTriangle2(triangleX + 450, triangleY, 150, 290)

    glColor3f(1.0, 0.1, 0.2)  # left mountain
    drawTriangle(triangleX + 350, triangleY + 400, 200, 240)
    drawTriangle2(triangleX + 550, triangleY + 400, 200, 240)

    glColor3f(1.0, 0.4, 1.0)  # right mountain
    drawTriangle(triangleX + 100, triangleY + 400, 200, 260)
    drawTriangle2(triangleX + 300, triangleY + 400, 200, 260)

    glColor3f(1.0, 1.0, 0.0)  # sun color yellow
    drawSun(layer1X + 650, layer1Y + 700, 32, 50)

    glColor3f(0.4, 0.0, 0.0)  # set color to brown
    drawTrunk(trunkX + 617, trunkY + 120, 20, 150)  # draw the tree stump on the screen

    glColor3f(0.0, 0.5, 0.0)  # set color to darkgreen
    drawLeaves(leavesX + 625, leavesY + 250, 50, 50)  # draw the tree leaves on the screen

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
wind = glutCreateWindow("CSC 322 Fall 2020 Final Project")  # create window with title
glutDisplayFunc(drawScene)  # set showScreen function callback
glutIdleFunc(drawScene)  # draw all the time
glutMainLoop()  # start everything
