import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU as glu
import math
import sys

glut.glutInit()

alfa = 0.0
delta = 0.3

def triangulo():
    gl.glPointSize(10)
    gl.glColor3f(1,1,0)
    gl.glBegin(gl.GL_TRIANGLE_STRIP)

    gl.glColor3f(1,0,0)
    gl.glVertex2f(-0.7,-0.7)

    gl.glColor3f(0,1,0)
    gl.glVertex2f(0.7,-0.7)

    gl.glColor3f(0,0,1)
    gl.glVertex2f(0.0,0.7)

    gl.glEnd()

def quadrado(fill:bool=False):
    gl.glBegin(gl.GL_POLYGON if fill else gl.GL_LINE_LOOP)
    gl.glVertex2f(-1, -1)
    gl.glVertex2f(-1, 1)
    gl.glVertex2f(1, 1)
    gl.glVertex2f(1, -1)
    gl.glEnd()

def cruz(fill:bool=False):
    gl.glBegin(gl.GL_POLYGON if fill else gl.GL_LINE_LOOP)
    gl.glVertex2f(-0.1, 0.3)
    gl.glVertex2f(-0.1, 0.1)
    gl.glVertex2f(-0.4, 0.1)
    gl.glVertex2f(-0.4, -0.1)
    gl.glVertex2f(-0.1, -0.1)
    gl.glVertex2f(-0.1, -0.8)
    gl.glVertex2f(0.1, -0.8)
    gl.glVertex2f(0.1, -0.1)
    gl.glVertex2f(0.4, -0.1)
    gl.glVertex2f(0.4, 0.1)
    gl.glVertex2f(0.1, 0.1)
    gl.glVertex2f(0.1, 0.3)
    gl.glEnd()

def poligono(vertices:int, fill:bool=False):
    gl.glBegin(gl.GL_POLYGON if fill else gl.GL_LINE_LOOP)
    delta = 2*math.pi/vertices
    for i in range(vertices):
        gl.glVertex2f(math.cos(i*delta), math.sin(i*delta))
    gl.glEnd()

def circulo(fill:bool=False):
    poligono(10000, fill)

def display():
    global alfa
    gl.glClearColor(0, 0, 0, 0) # preto
    gl.glClear(gl.GL_COLOR_BUFFER_BIT|gl.GL_DEPTH_BUFFER_BIT)

    gl.glLoadIdentity()
    # your rendering goes here
    # [...]

    gl.glPushMatrix()
    gl.glTranslate(-0.7,0.7,0)
    gl.glScalef(0.2,0.2,1)    
    gl.glColor3f(0.5,0.5,1)
    quadrado(True)
    gl.glLineWidth(3)
    gl.glColor3f(1,1,1)
    quadrado(False)
    gl.glPopMatrix()

    gl.glPushMatrix()
    gl.glTranslate(0.7,0.7,0)
    gl.glScalef(0.3,0.3,1)    
    cruz(True)
    gl.glLineWidth(3)
    gl.glColor3f(0.6,1,0.2)
    cruz(False)
    gl.glPopMatrix()

    gl.glPushMatrix()
    gl.glTranslate(-0.4,-0.4,0)
    gl.glScalef(0.5,0.5,1)    
    gl.glRotatef(180,0,0,1)
    poligono(5)
    gl.glPopMatrix()

    gl.glPushMatrix()
    gl.glTranslate(0.4,-0.4,0)
    gl.glScalef(0.5,0.5,1)    
    gl.glRotatef(180,0,0,1)
    circulo()
    gl.glPopMatrix()

    glut.glutSwapBuffers()
    glut.glutPostRedisplay()

def main():
    glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGBA)
    glut.glutInitWindowSize(500, 500)
    glut.glutCreateWindow(b'window')
    glut.glutDisplayFunc(display)
    glut.glutMainLoop()

if __name__=='__main__':
    main()