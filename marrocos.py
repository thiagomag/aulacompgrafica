import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU as glu
import math
import sys

glut.glutInit()


def estrela():
    gl.glLineWidth(15)
    gl.glBegin(gl.GL_LINE_LOOP)
    gl.glVertex2f(-0.3, -0.5)
    gl.glVertex2f(0, 0.5)
    gl.glVertex2f(0, 0.5)
    gl.glVertex2f(0.3, -0.5)
    gl.glVertex2f(0.3, -0.5)
    gl.glVertex2f(-0.45, 0.2)
    gl.glVertex2f(-0.45, 0.2)
    gl.glVertex2f(0.45, 0.2)
    gl.glVertex2f(0.45, 0.2)
    gl.glVertex2f(-0.3, -0.5)
    gl.glEnd()

def display():
    gl.glClearColor(1, 0, 0, 0)
    gl.glClear(gl.GL_COLOR_BUFFER_BIT|gl.GL_DEPTH_BUFFER_BIT)

    gl.glLoadIdentity()

    gl.glPushMatrix()
    gl.glTranslate(0,0,0)
    gl.glScalef(0.6,0.6,0.6)
    gl.glColor3f(0.5,0.5,0)
    estrela()
    gl.glPopMatrix()

    glut.glutSwapBuffers()
    glut.glutPostRedisplay()

def main():
    glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGBA)
    glut.glutInitWindowSize(300, 280)
    glut.glutCreateWindow(b'window')
    glut.glutDisplayFunc(display)
    glut.glutMainLoop()

if __name__=='__main__':
    main()