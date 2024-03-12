import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU as glu

def casa():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)

    gl.glColor3f(0.0, 0.0, 0.0)

    gl.glBegin(gl.GL_LINE_LOOP)
    gl.glVertex2f(0.0, 0.8)
    gl.glVertex2f(-0.7, 0.0)
    gl.glVertex2f(0.7, 0.0)
    gl.glEnd()

    gl.glBegin(gl.GL_LINE_LOOP)
    gl.glVertex2f(-0.5, 0.0)
    gl.glVertex2f(0.5, 0.0)
    gl.glVertex2f(0.5, -1.0)
    gl.glVertex2f(-0.5, -1.0)
    gl.glEnd()

    gl.glBegin(gl.GL_LINE_LOOP)
    gl.glVertex2f(-0.15, -1.0)
    gl.glVertex2f(0.15, -1.0)
    gl.glVertex2f(0.15, -0.65)
    gl.glVertex2f(-0.15, -0.65)
    gl.glEnd()

    glut.glutSwapBuffers()

def main():
    
    glut.glutInit()
    glut.glutInitDisplayMode(glut.GLUT_RGBA | glut.GLUT_DOUBLE)
    glut.glutInitWindowSize(400, 400)
    glut.glutCreateWindow(b'Casa Simples')
    glut.glutDisplayFunc(casa)
    gl.glClearColor(1.0, 1.0, 1.0, 1.0)
    glut.glutMainLoop()

if __name__ == "__main__":
    main()
    