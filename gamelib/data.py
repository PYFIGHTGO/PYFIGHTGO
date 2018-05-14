# -*- coding: cp1252 -*-

import os, pygame, time
from pygame.locals import *

pygame.init()

data_py = os.path.abspath(os.path.dirname(__file__))                #C:\...\Super-Mario-Bros-Python-v0.1release\gamelib
data_dir = os.path.normpath(os.path.join(data_py, '..', 'data'))    #C:\...\Super-Mario-Bros-Python-v0.1release\data

def filepath(filename):     #filename entre ""
    return os.path.join(data_dir, filename)             #donne le path du fichier

def taille_ecran():     #recherche la resolution de l'ecran
    largeur, hauteur = pygame.display.Info().current_w, pygame.display.Info().current_h
    return largeur, hauteur

def barre_vie1(fenetre,largeur,hauteur,vie1):


    rect12=pygame.Rect(90,90, 720,90)       #cree la surface rect
    pygame.gfxdraw.box(fenetre,rect12,(255,196,0)) #cree le rectangle en or
    rect11=pygame.Rect(100,100, 700,70)
    pygame.gfxdraw.box(fenetre,rect11,(255,0,0))    #cree le rectangle en rouge
    rect1=pygame.Rect(100+700-vie1*7,100, vie1*7,70)
    pygame.gfxdraw.box(fenetre,rect1,(0,255,0))      #dessine un rectangle vert
    

    return fenetre

def barre_vie2(fenetre,largeur,hauteur,vie2):

    rect22=pygame.Rect(largeur-810,90, 720,90)
    pygame.gfxdraw.box(fenetre,rect22,(255,196,0)) 
    rect21=pygame.Rect((largeur-800),100,700,70)
    pygame.gfxdraw.box(fenetre,rect21,(255,0,0))
    rect2=pygame.Rect((largeur-800),100,vie2*7,70)
    pygame.gfxdraw.box(fenetre,rect2,(0,255,0))

    return fenetre



