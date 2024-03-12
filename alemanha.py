import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU as glu

def bandeira():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)

    gl.glColor3f(1.0, 0.0, 0.0)
    gl.glBegin(gl.GL_QUADS)
    gl.glVertex2f(-1.0, 0.33)
    gl.glVertex2f(1.0, 0.33)
    gl.glVertex2f(1.0, -0.33)
    gl.glVertex2f(-1.0, -0.33)
    gl.glEnd()

    gl.glColor3f(1.0, 1.0, 0.0)
    gl.glBegin(gl.GL_QUADS)
    gl.glVertex2f(-1.0, -0.33)
    gl.glVertex2f(1.0, -0.33)
    gl.glVertex2f(1.0, -1.0)
    gl.glVertex2f(-1.0, -1.0)
    gl.glEnd()

    glut.glutSwapBuffers()

def main():

    glut.glutInit()
    glut.glutInitDisplayMode(glut.GLUT_RGBA | glut.GLUT_DOUBLE)
    glut.glutInitWindowSize(400, 300)
    glut.glutCreateWindow(b'Bandeira da Alemanha')
    glut.glutDisplayFunc(bandeira)
    gl.glClearColor(0.0, 0.0, 0.0, 0.0)
    glut.glutMainLoop()

if __name__ == "__main__":
    main()
