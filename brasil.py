import random
import OpenGL.GL as gl
import OpenGL.GLUT as glut
import math
import ctypes

glut.glutInit()


def poligono(vertices:int, fill:bool=False):
    gl.glBegin(gl.GL_POLYGON if fill else gl.GL_LINE_LOOP)
    delta = 2*math.pi/vertices
    for i in range(vertices):
        gl.glVertex2f(math.cos(i*delta), math.sin(i*delta))
    gl.glEnd()

def circulo(fill:bool=False):
    poligono(10000, fill)

def faixa():
    gl.glColor3f(1.0, 1.0, 1.0)
    gl.glBegin(gl.GL_QUADS)
    gl.glVertex2f(-0.6 , -0.05)   
    gl.glVertex2f(0.6 , -0.05)   
    gl.glVertex2f(0.6 , 0.05)   
    gl.glVertex2d(-0.6 , 0.05)  
    gl.glEnd()

def texto(text):
    for ch in text:
        glut.glutStrokeCharacter(glut.GLUT_STROKE_ROMAN , ctypes.c_int(ord(ch)))

def estrela():
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

def estrelas(posicoes):
    for posicao in posicoes:
        gl.glPushMatrix()
        gl.glTranslate(posicao[0],posicao[1],0)
        gl.glScale(0.05, 0.05, 0.05)
        gl.glColor3f(1,1,1)
        estrela()
        gl.glPopMatrix()

def display():
    gl.glClearColor(0, 0.5, 0, 0.5)
    gl.glClear(gl.GL_COLOR_BUFFER_BIT|gl.GL_DEPTH_BUFFER_BIT)

    gl.glLoadIdentity()

    gl.glPushMatrix()
    gl.glTranslate(0,0,0)
    gl.glScalef(0.8,0.8,0.8)    
    gl.glColor3f(1, 0.92, 0.23)
    gl.glRotatef(90,0,0,1)
    poligono(4, True)
    gl.glPopMatrix()

    gl.glPushMatrix()
    gl.glTranslate(0,0,0)
    gl.glScalef(0.4,0.5,0.4)
    gl.glColor3f(0, 0, 1)
    circulo(True)
    gl.glPopMatrix()

    gl.glPushMatrix()
    gl.glScalef(0.68,1,0.68)            
    faixa()                     
    gl.glPopMatrix()

    gl.glPushMatrix()
    gl.glTranslate(-0.35,-0.03,0)
    gl.glScale(0.0005,0.0005,0.0005)
    gl.glColor3f(0 , 0 , 0)
    texto("ORDEM E PROGRESSO")
    gl.glPopMatrix()

    star_positions = [
    (0, 0.1), (0.3, -0.2), (-0.2, -0.3), (0.1, -0.35), (-0.3, -0.15), (0.25, -0.25),
    (-0.1, -0.25), (0.35, -0.05), (-0.05, -0.35), (0.15, -0.3), (-0.35, -0.1),
    (0.2, -0.2), (-0.15, -0.25), (0.05, -0.3), (-0.25, -0.15), (0.3, -0.1),
    (-0.2, -0.2), (0.1, -0.15), (-0.3, -0.2), (0.25, -0.05), (-0.1, -0.3),
    (0.35, -0.2), (-0.05, -0.25), (0.15, -0.2), (-0.35, -0.25), (0.2, -0.05),
    (-0.15, -0.1)]
    estrelas(star_positions)
    
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