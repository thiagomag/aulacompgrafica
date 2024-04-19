import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU as glu
import sys
import math
import random
import os
import ctypes

FONT = glut.GLUT_STROKE_ROMAN

class Ponto:
    def __init__(self, *arg, **kargs):
        self.cor = (1,1,1) if len(arg)<1 else arg[0]
        self.x = 0 if len(arg)<2 else arg[1]
        self.y = 0 if len(arg)<3 else arg[2]
        if "color" in kargs:
            self.cor = kargs["color"]
        if "x" in kargs:
            self.x = kargs["x"]
        if "y" in kargs:
            self.y = kargs["y"]

    def draw(self):
        gl.glColor3f(*self.cor)
        gl.glPointSize(3)
        gl.glBegin(gl.GL_POINTS)
        gl.glVertex2f(self.x, self.y)
        gl.glEnd()

class Linha:
    def __init__(self, *arg, **kargs):
        self.cor = (1,1,1,1) if len(arg)<1 else arg[0]
        self.x1 = 0 if len(arg)<2 else arg[1]
        self.y1 = 0 if len(arg)<3 else arg[2]
        self.x2 = 0 if len(arg)<4 else arg[3]
        self.y2 = 0 if len(arg)<5 else arg[4]
        if "color" in kargs:
            self.cor = kargs["color"]
        if "x1" in kargs:
            self.x1 = kargs["x1"]
        if "y1" in kargs:
            self.y1 = kargs["y1"]
        if "x2" in kargs:
            self.x1 = kargs["x2"]
        if "y2" in kargs:
            self.y1 = kargs["y2"]

    def draw(self):
        gl.glColor3f(*self.cor)
        gl.glPointSize(3)
        gl.glBegin(gl.GL_LINES)
        gl.glVertex2f(self.x1, self.y1)
        gl.glVertex2f(self.x2, self.y2)
        gl.glEnd()

class PoligonoAberto:
    def __init__(self, *args, **kwargs):
        self.cor = (1, 1, 1, 1) if len(args) < 1 else args[0]
        self.vertices = [(0, 0), (0, 0)] if len(args) < 5 else args[1:5]
        
        if "color" in kwargs:
            self.cor = kwargs["color"]
        if "vertices" in kwargs:
            self.vertices = kwargs["vertices"]

    def draw(self):
        gl.glColor4f(*self.cor)
        gl.glPointSize(3)
        gl.glBegin(gl.GL_LINE_STRIP)
        for vertex in self.vertices:
            gl.glVertex2f(*vertex)
        gl.glEnd()

class Cena:
    def __init__(self):
        self.objetos = []

    def add(self,obj):
        self.objetos.append(obj)

    def draw(self):
        for obj in self.objetos:
            obj.draw()

width = 100
height = 100
ajuste=1
rect = (0,0,0,0)
size = 0
xn = 0
yn = 0
vertices = []

glut.glutInit()

pincel = (1,1,1)
preenchimento = (1,1,1,1)
cena = Cena()

def poligono(vertices:int, fill:bool=False):
    gl.glBegin(gl.GL_POLYGON if fill else gl.GL_LINE_LOOP)
    delta = 2*math.pi/vertices
    for i in range(vertices):
        ang = delta*i
        gl.glVertex2f(math.cos(ang),math.sin(ang))
    gl.glEnd()
    
def drawFillRect():
    gl.glBegin(gl.GL_POLYGON)
    gl.glVertex3f(-1,0.5,1)
    gl.glVertex3f( 1,0.5,1)
    gl.glVertex3f( 1,-0.5,1)
    gl.glVertex3f(-1,-0.5,1)
    gl.glEnd()

def drawText(texto):
    gl.glPushMatrix()
    gl.glLineWidth(3)    
    gl.glTranslatef(-0.2,-0.3, 0)
    gl.glScalef(0.007, 0.007, 1)
    for char in texto:
        glut.glutStrokeCharacter(FONT,ctypes.c_int(ord(char)))
    gl.glPopMatrix()

def drawFinishText(texto):
    gl.glPushMatrix()
    gl.glLineWidth(4)    
    gl.glTranslatef(-0.4,0, 0)
    gl.glScalef(0.0009, 0.0009, 1)
    for char in texto:
        glut.glutStrokeCharacter(FONT,ctypes.c_int(ord(char)))
    gl.glPopMatrix()

def display():
    gl.glPushMatrix()

    gl.glClearColor(0, 0, 0, 0) # preto
    gl.glClear(gl.GL_COLOR_BUFFER_BIT|gl.GL_DEPTH_BUFFER_BIT)

    #mostra o pincel corrente
    gl.glPushMatrix()
    gl.glColor3f(1,1,1)
    gl.glTranslatef(-0.95,0.95,0)
    gl.glScalef(0.1,0.1,1)
    drawText("Pincel:")
    gl.glPopMatrix()

    gl.glPushMatrix()
    gl.glTranslatef(-0.6,0.95,0)
    gl.glScalef(0.1,0.07,1)
    gl.glColor3f(*pincel)
    drawFillRect()
    gl.glPopMatrix()

    #mostra o preenchimento corrente
    gl.glPushMatrix()
    gl.glColor3f(1,1,1)
    gl.glTranslatef(-0.2,0.95,0)
    gl.glScalef(0.1,0.1,1)
    drawText("Preenchimento:")
    gl.glPopMatrix()

    gl.glPushMatrix()
    gl.glTranslatef(0.55,0.95,0)
    gl.glScalef(0.1,0.07,1)
    gl.glColor4f(*preenchimento)
    drawFillRect()
    gl.glPopMatrix()

    cena.draw()

    gl.glPopMatrix()

    glut.glutSwapBuffers()
    glut.glutPostRedisplay()
   
def resize(x,y):
    global rect
    global width
    global height
    global size
    global ajuste
    width = x
    height = y
    gl.glViewport(0, 0, x, y)
    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()
    l = x if x<y else y
    size = l
    x0 = (width-l)/2
    y0 = (height-l)/2
    rect = (x0,y0,x0+l,y0+l) 
    if x<y:
        h = y/x
        ajuste = 2.0/width
        gl.glOrtho(-1,1,-h,h,-1,1)
    else:
        w = x/y
        ajuste = 2.0/height
        gl.glOrtho(-w,w,-1,1,-1,1)

def init():
    #https://www.inf.pucrs.br/~pinho/CG/Aulas/OpenGL/LuzesGL.html
    gl.glShadeModel(gl.GL_SMOOTH)
    gl.glMaterialfv(gl.GL_FRONT,gl.GL_SPECULAR, [1.0,1.0,1.0,1.0])
    gl.glMateriali(gl.GL_FRONT,gl.GL_SHININESS,60)

    gl.glLightModelfv(gl.GL_LIGHT_MODEL_AMBIENT, [0.2,0.2,0.2,1.0])


    gl.glLightfv(gl.GL_LIGHT0, gl.GL_AMBIENT, [0.2,0.2,0.2,1.0])
    gl.glLightfv(gl.GL_LIGHT0, gl.GL_DIFFUSE, [0.7,0.7,0.7,1.0] )
    gl.glLightfv(gl.GL_LIGHT0, gl.GL_SPECULAR, [1.0, 1.0, 1.0, 1.0] )
    gl.glLightfv(gl.GL_LIGHT0, gl.GL_POSITION, [50.0, 50.0, 50.0, 1.0] )

    gl.glEnable(gl.GL_COLOR_MATERIAL)
    gl.glEnable(gl.GL_LIGHTING)
    gl.glEnable(gl.GL_LIGHT0)
    gl.glEnable(gl.GL_DEPTH_TEST)

def mouse(button,state,x,y):
    #entra aqui quando clica algum botao do mouse
    global xn, yn
    xm = (x-width/2.0)*ajuste
    ym = (height/2.0-y)*ajuste
    print(f"clicou {button}, {state}, x:{x}, y:{y}")
    if (button == 0 and state == 0):
        xn = xm
        yn = ym
        cena.add(Ponto(pincel,xm,ym))
    elif (button == 0 and state == 1):
        vertices.append((xm,ym))
        cena.add(PoligonoAberto(pincel,vertices))
    elif (button == 1 and state == 0):
         vertices = []

def mouseMove(x,y):
    #entra aqui quando move o mouse
    print(f" moveu x:{x}, y:{y}")

def keyPress(key,x,y):
    global preenchimento
    key = key[0]
    print(f"pressionou {key}, {x}, {y}")
    if key == 27:
        os._exit(0)
    elif key == 48:
        preenchimento = (0.5,0,0,1)
    elif key == 49:
        preenchimento = (1,1,1,1)
    elif key == 50:
        preenchimento = (0,0,1,1)
    elif key == 51:
        preenchimento = (0,1,0,1)
    elif key == 52:
        preenchimento = (1,0,0,1)
    elif key == 53:
        preenchimento = (1,1,0,1)
    elif key == 54:
        preenchimento = (1,0,1,1)
    elif key == 55:
        preenchimento = (0,1,1,1)
    elif key == 56:
        preenchimento = (0.5,0.5,0.5,1)
    elif key == 57:
        preenchimento = (0.3,0,0.3,1)
    elif key == 45:
        preenchimento = (1,1,1,0)
    

def specialKeyPress(key,x,y):
    global pincel
    #entra aqui quando pressiona alguma tecla especial
    print(f"especial {key}, {x}, {y}")
    if key == 1:
        pincel = (1, 1, 1)
    elif key == 2:
        pincel = (0, 0, 1)
    elif key == 3:
        pincel = (0, 1, 0)
    elif key == 4:
        pincel = (1, 0, 0)
    elif key == 5:
        pincel = (1, 1, 0)
    elif key == 6:
        pincel = (1, 0, 1)
    elif key == 7:
        pincel = (0, 1, 1)
    elif key == 8:
        pincel = (0.5, 0.5, 0.5)
    elif key == 9:
        pincel = (0.3, 0, 0.3)
    elif key == 10:
        pincel = (0.5, 0, 0)

def main():
    glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGBA)
    glut.glutInitWindowSize(500, 500)
    glut.glutCreateWindow(b'window')

    glut.glutDisplayFunc(display)
    glut.glutReshapeFunc(resize)
    glut.glutMouseFunc(mouse)
    glut.glutPassiveMotionFunc( mouseMove ) 
    glut.glutKeyboardFunc(keyPress)
    glut.glutSpecialFunc(specialKeyPress)
    #init()
    glut.glutMainLoop()

if __name__=='__main__':
    main()