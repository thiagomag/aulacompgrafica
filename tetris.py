import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU as glu
import random
import time
import os

def millis():
    return round(time.time() * 1000)

class Peca:
    cores = {
        1: (0.0, 1.0, 0.0),
        2: (0.0, 0.0, 1.0),
        3: (1.0, 0.0, 0.0),
        4: (1.0, 1.0, 0.0), 
        5: (1.0, 0.5, 0.0),
        6: (0.5, 0.0, 0.5), 
        7: (0.5, 0.5, 0.5),
    }
    formas = [
        [[1, 1, 1],
         [0, 1, 0]],

        [[0, 2, 2],
         [2, 2, 0]],

        [[3, 3, 0],
         [0, 3, 3]],

        [[4, 0, 0],
         [4, 4, 4]],

        [[0, 0, 5],
         [5, 5, 5]],

        [[6, 6],
         [6, 6]],

        [[7, 7, 7, 7]]
    ]

    def __init__(self):
        self.forma = random.choice(Peca.formas)
        self.cor = Peca.cores[next(valor for linha in self.forma for valor in linha if valor != 0)]
        self.x = int(largura_tabuleiro / 2 - len(self.forma[0]) / 2)
        self.y = altura_tabuleiro - 1

    def rotacionar(self):
        self.forma = [list(row) for row in zip(*self.forma[::-1])]

largura_tabuleiro = 10
altura_tabuleiro = 20
tamanho_celula = 20

tabuleiro = [[0 for _ in range(largura_tabuleiro)] for _ in range(altura_tabuleiro)]

peca_atual = Peca()
tempo_ultima_queda = millis()
velocidade_queda = 500

def desenharCelula(x, y):
    gl.glBegin(gl.GL_QUADS)
    gl.glVertex2f(x, y)
    gl.glVertex2f(x + tamanho_celula, y)
    gl.glVertex2f(x + tamanho_celula, y + tamanho_celula)
    gl.glVertex2f(x, y + tamanho_celula)
    gl.glEnd()

def desenharTabuleiro():
    for y, linha in enumerate(tabuleiro):
        for x, valor in enumerate(linha):
            if valor:
                gl.glColor3f(*Peca.cores[valor])
                desenharCelula(x * tamanho_celula, y * tamanho_celula)

def desenharPeca():
    gl.glColor3f(*peca_atual.cor)
    for y, linha in enumerate(peca_atual.forma):
        for x, valor in enumerate(linha):
            if valor:
                desenharCelula((peca_atual.x + x) * tamanho_celula, (peca_atual.y - y) * tamanho_celula)

def colisao(peca, x, y):
    for i, linha in enumerate(peca.forma):
        for j, valor in enumerate(linha):
            if valor and (x + j < 0 or x + j >= largura_tabuleiro or
                          y - i < 0 or y - i >= altura_tabuleiro or
                          tabuleiro[y - i][x + j]):
                return True
    return False

def moverPeca(dx):
    global peca_atual
    if not colisao(peca_atual, peca_atual.x + dx, peca_atual.y):
        peca_atual.x += dx

def rotacionarPeca():
    global peca_atual
    peca_atual.rotacionar()
    if colisao(peca_atual, peca_atual.x, peca_atual.y):
        for _ in range(3):
            peca_atual.rotacionar()

def derrubarPeca():
    global peca_atual
    while not colisao(peca_atual, peca_atual.x, peca_atual.y - 1):
        peca_atual.y -= 1
    fixarPeca()

def fixarPeca():
    global peca_atual
    for y, linha in enumerate(peca_atual.forma):
        for x, valor in enumerate(linha):
            if valor and peca_atual.y - y >= 0:
                tabuleiro[peca_atual.y - y][peca_atual.x + x] = valor

def removerLinhasCompletas():
    global tabuleiro
    novas_linhas = [linha for linha in tabuleiro if any(valor == 0 for valor in linha)]
    linhas_removidas = altura_tabuleiro - len(novas_linhas)
    for _ in range(linhas_removidas):
        novas_linhas.insert(0, [0 for _ in range(largura_tabuleiro)])
    tabuleiro = novas_linhas

def teclado(tecla, x, y):
    global peca_atual, game_over
    if tecla == b'\x1b':
        os._exit(0)
    elif not game_over:
        if tecla == b'a':
            moverPeca(-1)
        elif tecla == b'd':
            moverPeca(1)
        elif tecla == b's':
            if not colisao(peca_atual, peca_atual.x, peca_atual.y - 1):
                peca_atual.y -= 1
            else:
                fixarPeca()
                removerLinhasCompletas()
                peca_atual = Peca()
                if colisao(peca_atual, peca_atual.x, peca_atual.y):
                    print("Game Over")
                    game_over = True
        elif tecla == b'w':
            rotacionarPeca()
        elif tecla == b' ':
            derrubarPeca()
    glut.glutPostRedisplay()

game_over = False
timer_id = None 

def atualizar(valor):
    global peca_atual, tempo_ultima_queda, game_over, timer_id
    if not game_over:
        tempo_atual = millis()
        if tempo_atual - tempo_ultima_queda > velocidade_queda:
            if not colisao(peca_atual, peca_atual.x, peca_atual.y - 1):
                peca_atual.y -= 1
            else:
                fixarPeca()
                removerLinhasCompletas()
                peca_atual = Peca()
                if colisao(peca_atual, peca_atual.x, peca_atual.y):
                    print("Game Over")
                    game_over = True
                    glut.glutTimerFunc(10000, reiniciarJogo, 0)

            tempo_ultima_queda = tempo_atual
        glut.glutPostRedisplay()
        timer_id = glut.glutTimerFunc(velocidade_queda // 10, atualizar, 0)

def reiniciarJogo(valor):
    global tabuleiro, peca_atual, game_over, tempo_ultima_queda
    tabuleiro = [[0 for _ in range(largura_tabuleiro)] for _ in range(altura_tabuleiro)]
    peca_atual = Peca()
    game_over = False
    tempo_ultima_queda = millis()
    glut.glutTimerFunc(0, atualizar, 0)

def desenharCena():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    desenharTabuleiro()
    desenharPeca()
    glut.glutSwapBuffers()

def inicializar():
    gl.glClearColor(0.0, 0.0, 0.0, 1.0)

def redimensionar(w, h):
    gl.glViewport(0, 0, w, h)
    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()
    glu.gluOrtho2D(0, largura_tabuleiro * tamanho_celula, 0, altura_tabuleiro * tamanho_celula)
    gl.glMatrixMode(gl.GL_MODELVIEW)
    gl.glLoadIdentity()

def main():
    glut.glutInit()
    glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB | glut.GLUT_DEPTH)
    glut.glutInitWindowSize(largura_tabuleiro * tamanho_celula, altura_tabuleiro * tamanho_celula)
    glut.glutCreateWindow("Tetris")
    inicializar()
    glut.glutDisplayFunc(desenharCena)
    glut.glutReshapeFunc(redimensionar)
    glut.glutKeyboardFunc(teclado)
    glut.glutTimerFunc(0, atualizar, 0)
    glut.glutMainLoop()

if __name__ == "__main__":
    main()
