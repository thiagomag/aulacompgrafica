import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU as glu
import math
import sys

glut.glutInit()


def poligono(vertices:int, fill:bool=False):
    gl.glBegin(gl.GL_POLYGON if fill else gl.GL_LINE_LOOP)
    delta = 2*math.pi/vertices
    for i in range(vertices):
        gl.glVertex2f(math.cos(i*delta), math.sin(i*delta))
    gl.glEnd()

def circulo(fill:bool=False):
    poligono(10000, fill)

def display():
    gl.glClearColor(1, 1, 1, 1)
    gl.glClear(gl.GL_COLOR_BUFFER_BIT|gl.GL_DEPTH_BUFFER_BIT)

    gl.glLoadIdentity()

    gl.glPushMatrix()
    gl.glTranslate(0,0,0)
    gl.glScalef(0.5,0.5,0.5)
    gl.glRotatef(180,0,0,1)
    gl.glColor3f(1,0,0)
    circulo(True)
    gl.glPopMatrix()

    glut.glutSwapBuffers()
    glut.glutPostRedisplay()

def main():
    glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGBA)
    glut.glutInitWindowSize(300, 200)
    glut.glutCreateWindow(b'window')
    glut.glutDisplayFunc(display)
    glut.glutMainLoop()

if __name__=='__main__':
    main()