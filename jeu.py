# -*- coding: cp1252 -*-
#! /usr/bin/env python

import pygame
from data import *
import sys
import menu
import Projet

import data

pygame.init()

choix=0
largeur=0
hauteur=0

largeur, hauteur=taille_ecran()  #résolution de l'écran avec la def taille_ecran dans data.py


#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((0,0), FULLSCREEN)  #création de la fenetre
#fenetre = pygame.display.set_mode((1920,1080))

#Chargement et collage du fond
fond = pygame.image.load(filepath("menu.jpg")).convert_alpha()  #appelle l'image de fond
fond = pygame.transform.scale(fond, (largeur,hauteur))      #mets l'image a la taille de l'écran
fenetre.blit(fond, (0,0))                               #recolle le fond


continuer = 1
while continuer:
    if choix==0:        #menu principal
        choix = menu.menu(fenetre,choix,largeur,hauteur,fond)
    elif choix==1:      #menu des arenes
        choix = menu.arenes(fenetre,choix,largeur,hauteur,fond)
    elif choix==2:      #menu des meilleurs scores
        choix = menu.scores(fenetre,choix,largeur,hauteur,fond)
    elif choix==3:      #menu des instructions
        choix = menu.instructions(fenetre,choix,largeur,hauteur,fond)
    elif choix==4:      #quitter le jeu
        continuer=0
    elif choix==5:      #arene 1
        Projet.grosse_def(fenetre,choix)
        choix =0
    elif choix==6:      #arene 2
        Projet.grosse_def(fenetre,choix)
        choix=0
    elif choix==7:      #arene 3
        Projet.grosse_def(fenetre,choix)
        choix=0



#quitter le jeu
pygame.quit()
sys.exit()
