# -*- coding: utf-8 -*-

import pygame
from data import*
import data
import pygame.gfxdraw

pygame.init()

def menu(fenetre,choix,largeur,hauteur,fond) :
    choix=0
    
    JOUER = pygame.image.load(filepath("JOUER.png")).convert_alpha()     #ouvre une image
    JOUER = pygame.transform.scale(JOUER, (250,58))                 #change la taille de l'image
    SCORES = pygame.image.load(filepath("SCORES.png")).convert_alpha()     #ouvre une image
    SCORES = pygame.transform.scale(SCORES, (668,58))
    INS = pygame.image.load(filepath("INSTRUCTIONS.png")).convert_alpha()    
    INS = pygame.transform.scale(INS, (527,58))
    QUIT = pygame.image.load(filepath("QUITTER.png")).convert_alpha()
    QUIT = pygame.transform.scale(QUIT, (321,58))
    PY = pygame.image.load(filepath("PYFIGHTGO.png")).convert_alpha()
    PY = pygame.transform.scale(PY, (1096,174))
    
    position_JOUER=[(largeur/2)-(250/2),(hauteur/3.5)+100]                             #defini la position des images
    position_JOUER2=[(largeur/2)-(485/2)+1,(hauteur/3.5)-44+100]
    position_SCORES=[(largeur/2)-(668/2),(hauteur/2.25)+100]                             #defini la position des images
    position_SCORES2=[(largeur/2)-(1166/2)-3,(hauteur/2.25)-91+100]
    position_INS=[(largeur/2)-(527/2),(hauteur/1.66)+5+100]                            
    position_INS2=[(largeur/2)-(944/2)+5,(hauteur/1.84)+5+100]
    position_QUIT=[(largeur/2)-(321/2),(hauteur/1.29)+100]
    position_QUIT2=[(largeur/2)-(599/2)-3,(hauteur/1.36)-1+100]
    position_PY=[(largeur/2)-(1096/2),50]
    
    fenetre.blit(JOUER, position_JOUER)                 #colle les images
    fenetre.blit(SCORES, position_SCORES) 
    fenetre.blit(INS, position_INS)                 
    fenetre.blit(QUIT, position_QUIT)
    fenetre.blit(PY, position_PY)


    #Rafraîchissement de l'écran
    pygame.display.flip()

    continuer = 1
    while continuer:
        for event in pygame.event.get():	#Attente des événements
            if event.type == QUIT:
                continuer=0
            if JOUER.get_rect(topleft = (position_JOUER)).collidepoint(pygame.mouse.get_pos()):      #quand la souris survole "JOUER"
                JOUER = pygame.image.load(filepath("JOUER2.png")).convert_alpha()     #ouvre une image
                JOUER = pygame.transform.scale(JOUER,(485,149))                     #change la taille
 
            else :                      #quand la souris ne survole pas "JOUER"
                JOUER = pygame.image.load(filepath("JOUER.png")).convert_alpha()
                JOUER = pygame.transform.scale(JOUER, (250,58))

            if SCORES.get_rect(topleft = (position_SCORES)).collidepoint(pygame.mouse.get_pos()):      #quand la souris survole "JOUER"
                SCORES = pygame.image.load(filepath("SCORES2.png")).convert_alpha()     #ouvre une image
                SCORES = pygame.transform.scale(SCORES,(1166,245))                     #change la taille
 
            else :                      #quand la souris ne survole pas "JOUER"
                SCORES = pygame.image.load(filepath("SCORES.png")).convert_alpha()
                SCORES = pygame.transform.scale(SCORES, (668,58))

                
            if INS.get_rect(topleft = (position_INS)).collidepoint(pygame.mouse.get_pos()):          #quand la souris survole "INSTRUCTIONS"
                INS = pygame.image.load(filepath("INSTRUCTIONS2.png")).convert_alpha()     
                INS = pygame.transform.scale(INS,(944,197))
 
            else :                      #quand la souris ne survole pas "INSTRUCTIONS"
                INS = pygame.image.load(filepath("INSTRUCTIONS.png")).convert_alpha()     
                INS = pygame.transform.scale(INS, (527,58))

            if QUIT.get_rect(topleft = (position_QUIT)).collidepoint(pygame.mouse.get_pos()):          #quand la souris survole "QUITTER"
                QUIT = pygame.image.load(filepath("QUITTER2.png")).convert_alpha()     
                QUIT = pygame.transform.scale(QUIT,(599,141))

            else :                      #quand la souris ne survole pas "QUITTER"
                QUIT = pygame.image.load(filepath("QUITTER.png")).convert_alpha()     
                QUIT = pygame.transform.scale(QUIT,(321,58))

            if event.type == MOUSEBUTTONDOWN and event.button == 1 and JOUER.get_rect(topleft = (position_JOUER)).collidepoint(pygame.mouse.get_pos()):          #quand on clique sur "JOUER"
                choix=1
                return (choix)

            elif event.type == MOUSEBUTTONDOWN and event.button == 1 and SCORES.get_rect(topleft = (position_SCORES)).collidepoint(pygame.mouse.get_pos()):          #quand on clique sur "JOUER"
                choix=2
                return (choix)

            elif event.type == MOUSEBUTTONDOWN and event.button == 1 and INS.get_rect(topleft = (position_INS)).collidepoint(pygame.mouse.get_pos()):          #quand on clique sur "INSTRUCTIONS"
                choix=3
                return (choix)
            
                
            elif event.type == MOUSEBUTTONDOWN and event.button == 1 and QUIT.get_rect(topleft = (position_QUIT)).collidepoint(pygame.mouse.get_pos()):          #quand on clique sur "QUITTER"
                choix=4
                return (choix)

        #Re-collage de toutes les images en fonction de la position de la souris
        fenetre.blit(fond ,(0,0))
        fenetre.blit(PY, position_PY)
        
        if JOUER.get_rect(topleft = (position_JOUER)).collidepoint(pygame.mouse.get_pos()):
            fenetre.blit(JOUER, position_JOUER2)
        else :
            fenetre.blit(JOUER, position_JOUER)
        if SCORES.get_rect(topleft = (position_SCORES)).collidepoint(pygame.mouse.get_pos()):
            fenetre.blit(SCORES, position_SCORES2)
        else :
            fenetre.blit(SCORES, position_SCORES)
        if INS.get_rect(topleft = (position_INS)).collidepoint(pygame.mouse.get_pos()):
            fenetre.blit(INS, position_INS2)
        else :
            fenetre.blit(INS, position_INS)
        if QUIT.get_rect(topleft = (position_QUIT)).collidepoint(pygame.mouse.get_pos()):
            fenetre.blit(QUIT, position_QUIT2)
        else :
            fenetre.blit(QUIT, position_QUIT)
        
        
        #Rafraichissement
        pygame.display.flip()
        




def arenes(fenetre,choix,largeur,hauteur,fond) :
    choix=0 
    
    #appel de toues les images
    RETOUR = pygame.image.load(filepath("RETOUR.png")).convert_alpha()
    RETOUR = pygame.transform.scale(RETOUR, (307,52))
    ARENES = pygame.image.load(filepath("ARENES.png")).convert_alpha()
    ARENES = pygame.transform.scale(ARENES, (800,186))
    ARENE1 = pygame.image.load(filepath("ARENE1ico1.gif")).convert_alpha()
    ARENE1 = pygame.transform.scale(ARENE1, (500,500))
    ARENE2 = pygame.image.load(filepath("ARENE2ico1.gif")).convert_alpha()
    ARENE2 = pygame.transform.scale(ARENE2, (500,500))
    ARENE3 = pygame.image.load(filepath("ARENE3ico1.gif")).convert_alpha()
    ARENE3 = pygame.transform.scale(ARENE3, (500,500))
    
    #position de chaque image
    position_RETOUR=[(largeur/2)-(307/2),(hauteur/1.15)]
    position_RETOUR2=[(largeur/2)-(551/2)-3,(hauteur/1.22)+2]
    position_ARENES=[(largeur/2)-(800/2),30]
    position_ARENE1 = [100,(hauteur/2)-(500/2)+30]
    position_ARENE2 = [(largeur/2)-(500/2),(hauteur/2)-(500/2)+30]
    position_ARENE3 = [largeur-600,(hauteur/2)-(500/2)+30]

    #collage des images
    fenetre.blit(RETOUR, position_RETOUR)
    fenetre.blit(ARENES, position_ARENES)
    fenetre.blit(ARENE1, position_ARENE1)
    fenetre.blit(ARENE2, position_ARENE2)
    fenetre.blit(ARENE3, position_ARENE3)


    #Rafraîchissement de l'écran
    pygame.display.flip()

    continuer = 1
    while continuer:
        for event in pygame.event.get():	#Attente des événements
            if event.type == QUIT:
                continuer=0

            if ARENE1.get_rect(topleft = (position_ARENE1)).collidepoint(pygame.mouse.get_pos()):          #quand la souris survole la premiere arene
                ARENE1 = pygame.image.load(filepath("ARENE1ico2.gif")).convert_alpha()     
                ARENE1 = pygame.transform.scale(ARENE1,(500,500))
            else :                      #quand la souris ne survole pas la premiere arene
                ARENE1 = pygame.image.load(filepath("ARENE1ico1.gif")).convert_alpha()     
                ARENE1 = pygame.transform.scale(ARENE1,(500,500))
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and ARENE1.get_rect(topleft = (position_ARENE1)).collidepoint(pygame.mouse.get_pos()):          #quand on clique sur la premiere arene
                choix = 5
                return (choix)


            if ARENE2.get_rect(topleft = (position_ARENE2)).collidepoint(pygame.mouse.get_pos()):          #quand la souris survole la deuxieme arene
                ARENE2 = pygame.image.load(filepath("ARENE2ico2.gif")).convert_alpha()     
                ARENE2 = pygame.transform.scale(ARENE2,(500,500))
            else :                      #quand la souris ne survole pas la deuxieme arene
                ARENE2 = pygame.image.load(filepath("ARENE2ico1.gif")).convert_alpha()     
                ARENE2 = pygame.transform.scale(ARENE2,(500,500))
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and ARENE2.get_rect(topleft = (position_ARENE2)).collidepoint(pygame.mouse.get_pos()):          #quand on clique sur la deuxieme arene
                choix = 6
                return (choix)



            if ARENE3.get_rect(topleft = (position_ARENE3)).collidepoint(pygame.mouse.get_pos()):          #quand la souris survole la troisieme arene
                ARENE3 = pygame.image.load(filepath("ARENE3ico2.gif")).convert_alpha()     
                ARENE3 = pygame.transform.scale(ARENE3,(500,500))
            else :                      #quand la souris ne survole pas la troisieme arene
                ARENE3 = pygame.image.load(filepath("ARENE3ico1.gif")).convert_alpha()     
                ARENE3 = pygame.transform.scale(ARENE3,(500,500))
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and ARENE3.get_rect(topleft = (position_ARENE3)).collidepoint(pygame.mouse.get_pos()):          #quand on clique sur la troisieme arene
                choix = 7
                return (choix)




            if RETOUR.get_rect(topleft = (position_RETOUR)).collidepoint(pygame.mouse.get_pos()):          #quand la souris survole "RETOUR"
                RETOUR = pygame.image.load(filepath("RETOUR2.png")).convert_alpha()     
                RETOUR = pygame.transform.scale(RETOUR,(551,149))

            else :                      #quand la souris ne survole pas "RETOUR"
                RETOUR = pygame.image.load(filepath("RETOUR.png")).convert_alpha()     
                RETOUR = pygame.transform.scale(RETOUR,(307,52))
            
                
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and RETOUR.get_rect(topleft = (position_RETOUR)).collidepoint(pygame.mouse.get_pos()):          #quand on clique sur "RETOUR"
                choix = 0
                return (choix)

        #Re-collage des images
        fenetre.blit(fond ,(0,0))
        fenetre.blit(ARENES, position_ARENES)
        fenetre.blit(ARENE2, position_ARENE2)


        if ARENE1.get_rect(topleft = (position_ARENE1)).collidepoint(pygame.mouse.get_pos()):
            fenetre.blit(ARENE1, position_ARENE1)
        else :
            fenetre.blit(ARENE1, position_ARENE1)


        
        if ARENE2.get_rect(topleft = (position_ARENE2)).collidepoint(pygame.mouse.get_pos()):
            fenetre.blit(ARENE2, position_ARENE2)
        else :
            fenetre.blit(ARENE2, position_ARENE2)


        if ARENE3.get_rect(topleft = (position_ARENE3)).collidepoint(pygame.mouse.get_pos()):
            fenetre.blit(ARENE3, position_ARENE3)
        else :
            fenetre.blit(ARENE3, position_ARENE3)
        



        if RETOUR.get_rect(topleft = (position_RETOUR)).collidepoint(pygame.mouse.get_pos()):
            fenetre.blit(RETOUR, position_RETOUR2)
        else :
            fenetre.blit(RETOUR, position_RETOUR)
        
        
        #Rafraichissement
        pygame.display.flip()



def instructions(fenetre,choix,largeur,hauteur,fond) :
    choix=0

    font=pygame.font.Font(filepath("font/segoesc.ttf"), 60)         #defini la police d'ecriture

    #defini tous les texte et leur couleur (noir)
    text = font.render("Le but est de mettre KO l'adversaire le plus vite possible",1,(0,0,0))
    text2 = font.render("Joueur 1",1,(0,0,0))
    text3 = font.render("Joueur 2",1,(0,0,0))
    text4 = font.render("Z : saut",1,(0,0,0))
    text5 = font.render("D : droite",1,(0,0,0))
    text6 = font.render("Q : gauche",1,(0,0,0))
    text7 = font.render("X : pied",1,(0,0,0))
    text8 = font.render("V : poing",1,(0,0,0))
    text9 = font.render("C : contre",1,(0,0,0))
    text10 = font.render("UP: saut",1,(0,0,0))
    text11 = font.render("RIGHT: droite",1,(0,0,0))
    text12 = font.render("LEFT: gauche",1,(0,0,0))
    text13 = font.render("I : pied",1,(0,0,0))
    text14 = font.render("P : poing",1,(0,0,0))
    text15 = font.render("O : contre",1,(0,0,0))
    text16 = font.render("ESC : pause",1,(0,0,0))
    
    
    #appel des images
    RETOUR = pygame.image.load(filepath("RETOUR.png")).convert_alpha()
    RETOUR = pygame.transform.scale(RETOUR, (307,52))
    INS = pygame.image.load(filepath("INSTRUCTIONS3.png")).convert_alpha()
    INS = pygame.transform.scale(INS, (1416,149))

    #position des images
    position_RETOUR=[(largeur/2)-(307/2),(hauteur/1.15)+10]
    position_RETOUR2=[(largeur/2)-(551/2)-3,(hauteur/1.22)+2+10]
    position_INS = [(largeur/2)-(1416/2), 50]

    #collage des images
    fenetre.blit(RETOUR, position_RETOUR)                 
    fenetre.blit(INS, position_INS)
    fenetre.blit(text, (40, 250))
    fenetre.blit(text2, (300, 350))
    fenetre.blit(text3, (300+(largeur/2), 350))


    #Rafraîchissement de l'écran
    pygame.display.flip()

    continuer = 1
    while continuer:
        for event in pygame.event.get():	#Attente des événements
            if event.type == QUIT:
                continuer=0

            if RETOUR.get_rect(topleft = (position_RETOUR)).collidepoint(pygame.mouse.get_pos()):          #quand la souris survole "RETOUR"
                RETOUR = pygame.image.load(filepath("RETOUR2.png")).convert_alpha()     
                RETOUR = pygame.transform.scale(RETOUR,(551,149))

            else :                      #quand la souris ne survole pas "RETOUR"
                RETOUR = pygame.image.load(filepath("RETOUR.png")).convert_alpha()     
                RETOUR = pygame.transform.scale(RETOUR,(307,52))
            
                
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and RETOUR.get_rect(topleft = (position_RETOUR)).collidepoint(pygame.mouse.get_pos()):          #quand on clique sur "RETOUR"
                choix=0 #menu principal
                return (choix)

        #Re-collage des images et textes
        fenetre.blit(fond ,(0,0))
        fenetre.blit(INS, position_INS)
        fenetre.blit(text, (40, 250))
        fenetre.blit(text2, (340, 350))
        fenetre.blit(text3, (340+(largeur/2), 350))
        fenetre.blit(text4, (100, 450))
        fenetre.blit(text5, (100, 550))
        fenetre.blit(text6, (100, 650))
        fenetre.blit(text7, (80+largeur/4, 450))
        fenetre.blit(text8, (80+largeur/4, 550))
        fenetre.blit(text9, (80+largeur/4, 650))
        fenetre.blit(text10, (30+largeur/2, 450))
        fenetre.blit(text11, (29+largeur/2, 550))
        fenetre.blit(text12, (30+largeur/2, 650))
        fenetre.blit(text13, (50+3*largeur/4, 450))
        fenetre.blit(text14, (50+3*largeur/4, 550))
        fenetre.blit(text15, (50+3*largeur/4, 650))
        fenetre.blit(text16, (largeur/2-200, 800))
        
        if RETOUR.get_rect(topleft = (position_RETOUR)).collidepoint(pygame.mouse.get_pos()):
            fenetre.blit(RETOUR, position_RETOUR2)
        else :
            fenetre.blit(RETOUR, position_RETOUR)


        #collages de toutes les lignes
        pygame.gfxdraw.line(fenetre,largeur/2,370,largeur/2,800,[0,0,0])
        pygame.gfxdraw.line(fenetre,largeur/2+1,370,largeur/2+1,800,[0,0,0])
        pygame.gfxdraw.line(fenetre,largeur/2-1,370,largeur/2-1,800,[0,0,0])
        pygame.gfxdraw.line(fenetre,largeur/2+2,370,largeur/2+2,800,[0,0,0])
        pygame.gfxdraw.line(fenetre,largeur/2-2,370,largeur/2-2,800,[0,0,0])

        pygame.gfxdraw.line(fenetre,largeur/4,430,largeur/4,750,[0,0,0])
        pygame.gfxdraw.line(fenetre,largeur/4+1,430,largeur/4+1,750,[0,0,0])
        pygame.gfxdraw.line(fenetre,largeur/4-1,430,largeur/4-1,750,[0,0,0])

        pygame.gfxdraw.line(fenetre,3*largeur/4,430,3*largeur/4,750,[0,0,0])
        pygame.gfxdraw.line(fenetre,3*largeur/4+1,430,3*largeur/4+1,750,[0,0,0])
        pygame.gfxdraw.line(fenetre,3*largeur/4+2,430,3*largeur/4+2,750,[0,0,0])

        
        #Rafraichissement
        pygame.display.flip()

def scores(fenetre,choix,largeur,hauteur,fond) :
    choix=0
    
    #appel des images
    RETOUR = pygame.image.load(filepath("RETOUR.png")).convert_alpha()
    RETOUR = pygame.transform.scale(RETOUR, (307,52))
    SCORES = pygame.image.load(filepath("SCORES.png")).convert_alpha()
    SCORES = pygame.transform.scale(SCORES, (1406,122))

    #position des images
    position_RETOUR=[(largeur/2)-(307/2),(hauteur/1.15)]
    position_RETOUR2=[(largeur/2)-(551/2)-3,(hauteur/1.22)+2]
    position_SCORES = [(largeur/2)-(1406/2), 50]

    #collage des images
    fenetre.blit(RETOUR, position_RETOUR)                 
    fenetre.blit(SCORES, position_SCORES)                 


    #Rafraîchissement de l'écran
    pygame.display.flip()

    continuer = 1
    while continuer:
        for event in pygame.event.get():	#Attente des événements
            if event.type == QUIT:
                continuer=0

            if RETOUR.get_rect(topleft = (position_RETOUR)).collidepoint(pygame.mouse.get_pos()):          #quand la souris survole "RETOUR"
                RETOUR = pygame.image.load(filepath("RETOUR2.png")).convert_alpha()     
                RETOUR = pygame.transform.scale(RETOUR,(551,149))

            else :                      #quand la souris ne survole pas "RETOUR"
                RETOUR = pygame.image.load(filepath("RETOUR.png")).convert_alpha()     
                RETOUR = pygame.transform.scale(RETOUR,(307,52))
            
                
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and RETOUR.get_rect(topleft = (position_RETOUR)).collidepoint(pygame.mouse.get_pos()):          #quand on clique sur "RETOUR"
                choix=0
                return (choix)

        #Re-collage
        fenetre.blit(fond ,(0,0))
        fenetre.blit(SCORES, position_SCORES)
        
        if RETOUR.get_rect(topleft = (position_RETOUR)).collidepoint(pygame.mouse.get_pos()):
            fenetre.blit(RETOUR, position_RETOUR2)
        else :
            fenetre.blit(RETOUR, position_RETOUR)
        
        
        #Rafraichissement
        pygame.display.flip()



