from curses import window
import sys, pygame
from turtle import width
from pygame.locals import *
from pygame.constants import *
from OpenGL.GL import *
from OpenGL.GLU import *
from sympy import centroid


# -X PARA FRENTE
# Y PARA CIMA
# IMPORT OBJECT LOADER
from obj_loader import *
#inicializadno o pygame
pygame.init()
width = 800
height = 600
viewport = (width, height)

#gerando display pelo pigame
srf = pygame.display.set_mode(viewport, OPENGL | DOUBLEBUF)

##defindo as luzes##
#
luz_specular = [1.0, 1.0, 1.0, 1.0]
especularidade = [1.0, 1.0, 1.0, 1.0]
#similar a rugosidade do material
spc_material = 10
#definindo caracteristicas dos materiis
glMaterialfv(GL_FRONT, GL_SPECULAR, especularidade)
glMaterialfv(GL_FRONT, GL_SHININESS, spc_material)
#arrays em rgba
glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1.0)) #
glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.5, 0.5, 1.0)) #define as sombras do obj
glLightfv(GL_LIGHT0, GL_SPECULAR, luz_specular)




glEnable(GL_LIGHT0)
glEnable(GL_LIGHTING)
glEnable(GL_COLOR_MATERIAL)
glEnable(GL_DEPTH_TEST)
glShadeModel(GL_SMOOTH)

centro = ObjLoader('models/centro_historico.obj')
helice = ObjLoader('models/ventilador_helice.obj')
porta = ObjLoader('models/porta.obj')
janela = ObjLoader('models/janela.obj')

clock = pygame.time.Clock()

glMatrixMode(GL_PROJECTION)
glLoadIdentity()
#define a exibicao do mundo em frustro
gluPerspective(90.0, width/float(height), 1, 100.0)
glMatrixMode(GL_MODELVIEW)

rx, ry = (0,0)
tx, ty = (0,0)
zpos = 5
rotate = move = False
door_angle = 0
door_translate = 0
window_angle = 0
window_translate = 0
helice_rotate = 0

while True:
    helice_rotate += 1
    clock.tick(60)
    for e in pygame.event.get():
        if e.type == QUIT:
            sys.exit()
        elif e.type == KEYDOWN and e.key == K_ESCAPE:
            sys.exit()
        elif e.type == KEYDOWN and e.key == K_F1:
            if door_angle == 0:
                door_angle = 90
                door_translate = 0.6
                window_angle = 90
                window_translate = 0.6
            else:
                door_angle = 0
                door_translate = 0
                window_angle = 0
                window_translate = 0
        elif e.type == MOUSEBUTTONDOWN:
            if e.button == 4: zpos = zpos - 1   
            elif e.button == 5: zpos = zpos + 1
            elif e.button == 1: rotate = True
            elif e.button == 3: move = True
        elif e.type == MOUSEBUTTONUP:
            if e.button == 1: rotate = False
            elif e.button == 3: move = False
        elif e.type == MOUSEMOTION:
            i, j = e.rel
            
            if rotate:
                rx += i
                ry += j
            if move:
                tx += i
                ty -= j
    

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()


    # RENDER OBJECT
    #dividido para mudar menos
    glTranslate(tx/20, ty/20, - zpos)
    glRotate(ry, 1, 0, 0)
    glRotate(rx, 0, 1, 0)
    glCallList(centro.gl_list)

    glPushMatrix()
    glTranslate(-5.5, 0.7, -0.1)   
    glRotate(90, 0, 1, 0)
    glRotate(door_angle, 0, 1 ,0)
    glTranslate(0, 0, door_translate)
    glCallList(porta.gl_list)
    glPopMatrix()

    glPushMatrix()
    glTranslate(-5.5, 0.7, -2.5)   
    glRotate(90, 0, 1, 0)
    glRotate(door_angle, 0, 1 ,0)
    glTranslate(0, 0, door_translate)
    glCallList(porta.gl_list)
    glPopMatrix()

    glPushMatrix()
    glTranslate(-5.5, 0.7, 2.5)   
    glRotate(90, 0, 1, 0)
    glRotate(door_angle, 0, 1 ,0)
    glTranslate(0, 0, door_translate)
    glCallList(porta.gl_list)
    glPopMatrix()

    glPushMatrix()
    glTranslate(-5.7, 3.8, -0.1)   
    
    glRotate(window_angle, 0, 1 ,0)
    glTranslate(0, 0, window_translate)
    glCallList(janela.gl_list)
    glPopMatrix()

    glPushMatrix()
    
    glTranslate(3.2, 3.85, 0)
    glRotate(helice_rotate, 0, 1, 0)
    glCallList(helice.gl_list)  
    glPopMatrix()
    #flipando o buffer
    pygame.display.flip()

