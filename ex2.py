import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU as glu
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

def display():
    global alfa
    gl.glClearColor(0, 0, 0, 0) # preto
    gl.glClear(gl.GL_COLOR_BUFFER_BIT|gl.GL_DEPTH_BUFFER_BIT)

    gl.glLoadIdentity()
    # your rendering goes here
    # [...]

    alfa = alfa + delta
    gl.glPushMatrix()
    gl.glTranslate(-0.8,0.8,0)
    gl.glScalef(0.2,0.2,1)    
    gl.glRotatef(90,0,0,1)
    triangulo()
    gl.glPopMatrix()

    gl.glPushMatrix()
    gl.glTranslate(0.7,0.7,0)
    gl.glScalef(0.3,0.3,1)    
    triangulo()
    gl.glPopMatrix()

    gl.glPushMatrix()
    gl.glTranslate(0.0,-0.4,0)
    gl.glScalef(0.5,0.5,1)    
    gl.glRotatef(180,0,0,1)
    triangulo()
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