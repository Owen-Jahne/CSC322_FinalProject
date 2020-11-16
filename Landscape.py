from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import*
window = 0
width, height = 800, 800  # window size

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

def drawSphere(self):
    for i in range(0,self.lats + 1):
        lat0 = pi * (-0.5 + float(float(i-1)/float(self.lats)))
        z0 = sin(lat0)
        zr0 = cos(lat0)

        lat1 = pi *(-0.5 + float(float(i)/float(self.lats)))
        z1 = sin(lat1)
        zr1 = cos(lat0)

        glBegin(GL_QUAD_STRIP)

        for j in range(0,self.longs + 1):
            lng = 2 * pi * float(float(j-1)/float(self.longs))
            x = cos(lng)
            y = sin(lng)
            glNormal3f(x * zr0, y * zr0, z0)
            glVertex3f(x * zr0, y * zr0, z0)
            glNormal3f(x * zr1, y * zr1, z1)
            glVertex3f(x * zr1, y * zr1, z1)

        glEnd()


def drawScene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # clear the screen
    glLoadIdentity()  # reset position
    refresh2d(width, height)

    glColor3f(0.0, 0.0, 1.0)  # set color to blue
    drawSquare(0, 100, 1000, 1000)

    glColor3f(0.0, 1.0, 0.0)  # set color to green
    drawSquare(0,0 , 1000, 400)

    glColor3f(0.7, 0.1, 0.1)        # tallest mountain in back
    drawTriangle(300, 400, 150, 290)
    drawTriangle2(450, 400, 150, 290)

    glColor3f(1.0, 0.1, 0.2)        # left mountain
    drawTriangle(350, 400, 200, 240)
    drawTriangle2(550, 400, 200, 240)

    glColor3f(1.0, 0.4, 0.0)  # right mountain
    drawTriangle(100, 400, 200, 260)
    drawTriangle2(300, 400, 200, 260)

    x = 0
    n = 0
    while(x<160):
        x+=1
        n+=5
        glColor3f(0.0,1.0,0.0)
        drawSquare(n, 400,2,8)

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
wind = glutCreateWindow("CSC 322 Fall 2020 HW1")  # create window with title
glutDisplayFunc(drawScene)  # set showScreen function callback
glutIdleFunc(drawScene)  # draw all the time