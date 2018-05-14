# -*- coding: utf-8 -*-

import pygame
import time
import pygame.gfxdraw
from pygame.locals import *
from data import *

#Procédure
def marche(x,position):
        if position==sol:
                x+=1
                if x==10:
                        x=0
        else:
                x=0
        return x

def grosse_def(fenetre,choix):
        pygame.init()

        largeur,hauteur=taille_ecran()  #résolution de l'écran avec la def taille_ecran dans data.py
        y=0
        z=0
        personnage2=0
        personnage1=1
        g1=5
        g2=5
        gauche=personnage1
        sol_arret1=0
        sol_arret2=0
        global sol
        sol=hauteur*31/48
        vitesse_personnage1 = [0,0]   #[Horizontal,Vertical]
        vitesse_personnage2 = [0,0]   #[Horizontal,Vertical]
        gravite=hauteur*12/25
        vitesse_saut=-hauteur/22
        reaction1=0
        reaction2=0
        vie1=100
        vie2=100
        j=0
        k=0
        a=1 #Vaut 1 si la touche "flêche droite" est enfoncée, vaut 0 si la touche n'est pas enfoncée
        b=2 #Vaut 1 si la touche "flêche gauche" est enfoncée, vaut 0 si la touche n'est pas enfoncée
        c=1 #Vaut 1 si la touche "Q" est enfoncée, vaut 0 si la touche n'est pas enfoncée
        d=2 #Vaut 1 si la touche "D" est enfoncée, vaut 0 si la touche n'est pas enfoncée
        liste1=[]
        liste2=[]
        bras1=0
        bras2=0
        coup_poing1=0
        coup_poing2=0
        coup_pied1=0
        coup_pied2=0
        bumped1=0
        bumped2=0
        bouclebumped1=0
        bouclebumped2=0
        pospied1=0
        pospied2=0
        contre1=0
        contre2=0
        temps=91
        pause =0

        #defini les police d'ecriture
        font=pygame.font.Font(filepath("font/segoesc.ttf"), int(hauteur/10.8))
        font1=pygame.font.Font(filepath("font/segoesc.ttf"), int(hauteur/2.7))
        font2=pygame.font.Font(filepath("font/segoesc.ttf"), int(hauteur/1.8))

        #Chargement et collage du fond
        if choix==5:
                fond = pygame.image.load(filepath("arene1.gif")).convert()              #chargement de l'image
                fond = pygame.transform.scale(fond,(largeur,hauteur))                   #met l'image a la taille de l'ecran
                fenetre.blit(fond, (0,0))                                       #collage de l'image
        elif choix==6:
                fond = pygame.image.load(filepath("arene2.gif")).convert()
                fond = pygame.transform.scale(fond,(largeur,hauteur))
                fenetre.blit(fond, (0,0))
        elif choix==7:
                fond = pygame.image.load(filepath("arene3.gif")).convert()
                fond = pygame.transform.scale(fond,(largeur,hauteur))
                fenetre.blit(fond, (0,0))

        #Chargement et collage des personnages
        personnage1_transition = pygame.image.load(filepath("1_Personnage_deplacement.png")).convert_alpha()
        personnage1_transition = pygame.transform.scale(personnage1_transition,(largeur/5,hauteur/3))
        personnage1_transition2 = pygame.transform.flip(personnage1_transition,1,0)
        personnage12 = pygame.image.load(filepath("1_personnage.png")).convert_alpha()
        personnage12 = pygame.transform.scale(personnage12,(largeur/5,hauteur/3))
        personnage1 = pygame.transform.flip(personnage12,1,0)
        personnage2_transition = pygame.image.load(filepath("2_Personnage_deplacement.png")).convert_alpha()
        personnage2_transition = pygame.transform.scale(personnage2_transition,(largeur/5,hauteur/3))
        personnage2_transition2 = pygame.transform.flip(personnage2_transition,1,0)
        personnage22 = pygame.image.load(filepath("2_personnage.png")).convert_alpha()
        personnage22 = pygame.transform.scale(personnage22,(largeur/5,hauteur/3))
        personnage2 = pygame.transform.flip(personnage22,1,0)
        position_personnage1=[largeur/7,hauteur*10/24]                                #!!!!!!!!!!!!
        position_personnage2=[largeur*9/14,hauteur*10/24]
        fenetre.blit(personnage1, position_personnage1)
        fenetre.blit(personnage22, position_personnage2)
        
        p1_image_contre = pygame.image.load(filepath("1_Contre.png")).convert_alpha()
        p1_image_contre = pygame.transform.scale(p1_image_contre,(largeur/5,hauteur/3))
        p1_image_contre2 = pygame.transform.flip(p1_image_contre,1,0)
        p1_mouvementpied1 = pygame.image.load(filepath("1_Coup de pied 1.png")).convert_alpha()
        p1_mouvementpied1 = pygame.transform.scale(p1_mouvementpied1,(largeur/5,hauteur/3))
        p1_mouvementpied15 = pygame.transform.flip(p1_mouvementpied1,1,0)
        p1_mouvementpied2 = pygame.image.load(filepath("1_Coup de pied 2.png")).convert_alpha()
        p1_mouvementpied2 = pygame.transform.scale(p1_mouvementpied2,(largeur/5,hauteur/3))
        p1_mouvementpied25 = pygame.transform.flip(p1_mouvementpied2,1,0)
        p1_mouvementcoup1 = pygame.image.load(filepath("1_Coup de poing2.png")).convert_alpha()
        p1_mouvementcoup1 = pygame.transform.scale(p1_mouvementcoup1,(largeur/5,hauteur/3))
        p1_mouvementcoup15 = pygame.transform.flip(p1_mouvementcoup1,1,0)
        p1_mouvementcoup2 = pygame.image.load(filepath("1_Coup de poing3.png")).convert_alpha()
        p1_mouvementcoup2 = pygame.transform.scale(p1_mouvementcoup2,(largeur/5,hauteur/3))
        p1_mouvementcoup25 = pygame.transform.flip(p1_mouvementcoup2,1,0)
        p1_mouvementcoup3 = pygame.image.load(filepath("1_Coup de poing4.png")).convert_alpha()
        p1_mouvementcoup3 = pygame.transform.scale(p1_mouvementcoup3,(largeur/5,hauteur/3))
        p1_mouvementcoup35 = pygame.transform.flip(p1_mouvementcoup3,1,0)
        p1_mouvementcoup4 = pygame.image.load(filepath("1_Coup de poing5.png")).convert_alpha()
        p1_mouvementcoup4 = pygame.transform.scale(p1_mouvementcoup4,(largeur/5,hauteur/3))
        p1_mouvementcoup45 = pygame.transform.flip(p1_mouvementcoup4,1,0)
        p1_mouvementcoup5 = pygame.image.load(filepath("1_Coup de poing6.png")).convert_alpha()
        p1_mouvementcoup5 = pygame.transform.scale(p1_mouvementcoup5,(largeur/5,hauteur/3))
        p1_mouvementcoup55 = pygame.transform.flip(p1_mouvementcoup5,1,0)
        p1_mouvementcoup6 = pygame.image.load(filepath("1_Coup de poingfin.png")).convert_alpha()
        p1_mouvementcoup6 = pygame.transform.scale(p1_mouvementcoup6,(largeur/5,hauteur/3))
        p1_mouvementcoup65 = pygame.transform.flip(p1_mouvementcoup6,1,0)

        p2_image_contre = pygame.image.load(filepath("2_Contre.png")).convert_alpha()
        p2_image_contre = pygame.transform.scale(p2_image_contre,(largeur/5,hauteur/3))
        p2_image_contre2 = pygame.transform.flip(p2_image_contre,1,0)
        p2_mouvementpied1 = pygame.image.load(filepath("2_Coup de pied 1.png")).convert_alpha()
        p2_mouvementpied1 = pygame.transform.scale(p2_mouvementpied1,(largeur/5,hauteur/3))
        p2_mouvementpied15 = pygame.transform.flip(p2_mouvementpied1,1,0)
        p2_mouvementpied2 = pygame.image.load(filepath("2_Coup de pied 2.png")).convert_alpha()
        p2_mouvementpied2 = pygame.transform.scale(p2_mouvementpied2,(largeur/5,hauteur/3))
        p2_mouvementpied25 = pygame.transform.flip(p2_mouvementpied2,1,0)
        p2_mouvementcoup1 = pygame.image.load(filepath("2_Coup de poing2.png")).convert_alpha()
        p2_mouvementcoup1 = pygame.transform.scale(p2_mouvementcoup1,(largeur/5,hauteur/3))
        p2_mouvementcoup15 = pygame.transform.flip(p2_mouvementcoup1,1,0)
        p2_mouvementcoup2 = pygame.image.load(filepath("2_Coup de poing3.png")).convert_alpha()
        p2_mouvementcoup2 = pygame.transform.scale(p2_mouvementcoup2,(largeur/5,hauteur/3))
        p2_mouvementcoup25 = pygame.transform.flip(p2_mouvementcoup2,1,0)
        p2_mouvementcoup3 = pygame.image.load(filepath("2_Coup de poing4.png")).convert_alpha()
        p2_mouvementcoup3 = pygame.transform.scale(p2_mouvementcoup3,(largeur/5,hauteur/3))
        p2_mouvementcoup35 = pygame.transform.flip(p2_mouvementcoup3,1,0)
        p2_mouvementcoup4 = pygame.image.load(filepath("2_Coup de poing5.png")).convert_alpha()
        p2_mouvementcoup4 = pygame.transform.scale(p2_mouvementcoup4,(largeur/5,hauteur/3))
        p2_mouvementcoup45 = pygame.transform.flip(p2_mouvementcoup4,1,0)
        p2_mouvementcoup5 = pygame.image.load(filepath("2_Coup de poing6.png")).convert_alpha()
        p2_mouvementcoup5 = pygame.transform.scale(p2_mouvementcoup5,(largeur/5,hauteur/3))
        p2_mouvementcoup55 = pygame.transform.flip(p2_mouvementcoup5,1,0)
        p2_mouvementcoup6 = pygame.image.load(filepath("2_Coup de poingfin.png")).convert_alpha()
        p2_mouvementcoup6 = pygame.transform.scale(p2_mouvementcoup6,(largeur/5,hauteur/3))
        p2_mouvementcoup65 = pygame.transform.flip(p2_mouvementcoup6,1,0)
        
        p1_mvmentcoup1=[p1_mouvementcoup1,p1_mouvementcoup2,p1_mouvementcoup3,p1_mouvementcoup4,p1_mouvementcoup5,p1_mouvementcoup6,p1_mouvementcoup6,p1_mouvementcoup6]
        p1_mvmentcoup2=[p1_mouvementcoup15,p1_mouvementcoup25,p1_mouvementcoup35,p1_mouvementcoup45,p1_mouvementcoup55,p1_mouvementcoup65,p1_mouvementcoup65,p1_mouvementcoup65]
        p2_mvmentcoup1=[p2_mouvementcoup1,p2_mouvementcoup2,p2_mouvementcoup3,p2_mouvementcoup4,p2_mouvementcoup5,p2_mouvementcoup6,p2_mouvementcoup6,p2_mouvementcoup6]
        p2_mvmentcoup2=[p2_mouvementcoup15,p2_mouvementcoup25,p2_mouvementcoup35,p2_mouvementcoup45,p2_mouvementcoup55,p2_mouvementcoup65,p2_mouvementcoup65,p2_mouvementcoup65]
        
        listecoup1=[]
        listecoup2=[]
        hitbox1=[(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0)]
        hitbox2=[(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0)]
        p1_pieds1=[p1_mouvementpied1,p1_mouvementpied2]
        p1_pieds2=[p1_mouvementpied15,p1_mouvementpied25]
        p2_pieds1=[p2_mouvementpied1,p2_mouvementpied2]
        p2_pieds2=[p2_mouvementpied15,p2_mouvementpied25]
        hitboxpied2=pygame.Rect(0,0,0,0)
        hitboxpied1=pygame.Rect(0,0,0,0)
        


        #Rafraîchissement de l'écran
        pygame.display.flip()

        #INTRO
        #timer
        text = font.render("90",1,(255,196,0))
        fenetre.blit(text, ((largeur/2.152), hauteur/16.615))
                
                
        #vie        
        barre_vie1(fenetre,largeur,hauteur,vie1)
        barre_vie2(fenetre,largeur,hauteur,vie2)

        #joueurs
        text = font.render(("Joueur1"),1,(255,196,0))
        fenetre.blit(text, (largeur/8.73,hauteur/7.2))
        text = font.render(("Joueur2"),1,(255,196,0))
        fenetre.blit(text, (largeur/1.561,hauteur/7.2))

        text = font1.render("3",1,(255,196,0))
        fenetre.blit(text, (largeur/2.35,hauteur/4.5))
        pygame.display.update()
        pygame.time.wait(1000)
        fenetre.blit(fond, (0,0))

        #perso
        fenetre.blit(personnage1, position_personnage1)
        fenetre.blit(personnage22, position_personnage2)



        
        
        #timer
        text = font.render("90",1,(255,196,0))
        fenetre.blit(text, ((largeur/2.152), hauteur/16.615))
                
                
        #vie        
        barre_vie1(fenetre,largeur,hauteur,vie1)
        barre_vie2(fenetre,largeur,hauteur,vie2)

        #joueurs
        text = font.render(("Joueur1"),1,(255,196,0))
        fenetre.blit(text, (largeur/8.73,hauteur/7.2))
        text = font.render(("Joueur2"),1,(255,196,0))
        fenetre.blit(text, (largeur/1.561,hauteur/7.2))

        text = font1.render("2",1,(255,196,0))
        fenetre.blit(text, (largeur/2.35,hauteur/4.5))
        pygame.display.update()
        pygame.time.wait(1000)
        fenetre.blit(fond, (0,0))

        #perso
        fenetre.blit(personnage1, position_personnage1)
        fenetre.blit(personnage22, position_personnage2)



        

        #timer
        text = font.render("90",1,(255,196,0))
        fenetre.blit(text, ((largeur/2.152), hauteur/16.615))
                
                
        #vie        
        barre_vie1(fenetre,largeur,hauteur,vie1)
        barre_vie2(fenetre,largeur,hauteur,vie2)

        #joueurs
        text = font.render(("Joueur1"),1,(255,196,0))
        fenetre.blit(text, (largeur/8.73,hauteur/7.2))
        text = font.render(("Joueur2"),1,(255,196,0))
        fenetre.blit(text, (largeur/1.561,hauteur/7.2))

        text = font1.render("1",1,(255,196,0))
        fenetre.blit(text, (largeur/2.35,hauteur/4.5))
        pygame.display.update()
        pygame.time.wait(1000)
        fenetre.blit(fond, (0,0))

        #perso
        fenetre.blit(personnage1, position_personnage1)
        fenetre.blit(personnage22, position_personnage2)




        

        #timer
        text = font.render("90",1,(255,196,0))
        fenetre.blit(text, ((largeur/2.152), hauteur/16.615))
                
                
        #vie        
        barre_vie1(fenetre,largeur,hauteur,vie1)
        barre_vie2(fenetre,largeur,hauteur,vie2)

        #joueurs
        text = font.render(("Joueur1"),1,(255,196,0))
        fenetre.blit(text, (largeur/8.73,hauteur/7.2))
        text = font.render(("Joueur2"),1,(255,196,0))
        fenetre.blit(text, (largeur/1.561,hauteur/7.2))

        text = font1.render("GO",1,(255,196,0))
        fenetre.blit(text, (largeur/3,hauteur/4.5))
        pygame.display.update()
        pygame.time.wait(1000)
        fenetre.blit(fond, (0,0))

        #perso
        fenetre.blit(personnage1, position_personnage1)
        fenetre.blit(personnage22, position_personnage2)

        

        #BOUCLE INFINIE
        continuer = 1
        while continuer:
                fenetre.blit(fond, (0,0))
                contact1=pygame.Rect(position_personnage2[0],position_personnage2[1],largeur*5/64,hauteur/4)
                contact2=pygame.Rect(position_personnage1[0],position_personnage1[1],largeur*5/64,hauteur/4)
                listehitboxg1=[(position_personnage2[0]+largeur*9/80,position_personnage2[1]+hauteur/19,largeur/32,hauteur/24),(position_personnage2[0]+largeur*11/95,position_personnage2[1]+hauteur/19,largeur/32,hauteur/24),(position_personnage2[0]+largeur/8,position_personnage2[1]+hauteur/19,largeur/32,hauteur/24),(position_personnage2[0]+largeur*15/112,position_personnage2[1]+hauteur/19,largeur/32,hauteur/24),(position_personnage2[0]+largeur*73/528,position_personnage2[1]+hauteur/19,largeur/32,hauteur/24),(position_personnage2[0]+largeur*4/25,position_personnage2[1]+hauteur/19,largeur/32,hauteur/24),(position_personnage2[0]+largeur*4/25,position_personnage2[1]+hauteur/19,largeur/32,hauteur/24),(position_personnage2[0]+largeur*4/25,position_personnage2[1]+hauteur/19,largeur/32,hauteur/24)]
                listehitboxd1=[(position_personnage2[0]+largeur/18,position_personnage2[1]+hauteur/19,largeur/32,hauteur/24),(position_personnage2[0]+largeur/19,position_personnage2[1]+hauteur/19,largeur/32,hauteur/24),(position_personnage2[0]+largeur/23,position_personnage2[1]+hauteur/19,largeur/32,hauteur/24),(position_personnage2[0]+largeur/28,position_personnage2[1]+hauteur/19,largeur/32,hauteur/24),(position_personnage2[0]+largeur/33,position_personnage2[1]+hauteur/19,largeur/32,hauteur/24),(position_personnage2[0]+largeur/100,position_personnage2[1]+hauteur/19,largeur/32,hauteur/24),(position_personnage2[0]+largeur/100,position_personnage2[1]+hauteur/19,largeur/32,hauteur/24),(position_personnage2[0]+largeur/100,position_personnage2[1]+hauteur/19,largeur/32,hauteur/24)]
                listehitboxg2=[(position_personnage1[0]+largeur*9/80,position_personnage1[1]+hauteur/19,largeur/32,hauteur/24),(position_personnage1[0]+largeur*11/95,position_personnage1[1]+hauteur/19,largeur/32,hauteur/24),(position_personnage1[0]+largeur/8,position_personnage1[1]+hauteur/19,largeur/32,hauteur/24),(position_personnage1[0]+largeur*15/112,position_personnage1[1]+hauteur/19,largeur/32,hauteur/24),(position_personnage1[0]+largeur*73/528,position_personnage1[1]+hauteur/19,largeur/32,hauteur/24),(position_personnage1[0]+largeur*4/25,position_personnage1[1]+hauteur/19,largeur/32,hauteur/24),(position_personnage1[0]+largeur*4/25,position_personnage1[1]+hauteur/19,largeur/32,hauteur/24),(position_personnage1[0]+largeur*4/25,position_personnage1[1]+hauteur/19,largeur/32,hauteur/24)]
                listehitboxd2=[(position_personnage1[0]+largeur/18,position_personnage1[1]+hauteur/19,largeur/32,hauteur/24),(position_personnage1[0]+largeur/19,position_personnage1[1]+hauteur/19,largeur/32,hauteur/24),(position_personnage1[0]+largeur/23,position_personnage1[1]+hauteur/19,largeur/32,hauteur/24),(position_personnage1[0]+largeur/28,position_personnage1[1]+hauteur/19,largeur/32,hauteur/24),(position_personnage1[0]+largeur/33,position_personnage1[1]+hauteur/19,largeur/32,hauteur/24),(position_personnage1[0]+largeur/100,position_personnage1[1]+hauteur/19,largeur/32,hauteur/24),(position_personnage1[0]+largeur/100,position_personnage1[1]+hauteur/19,largeur/32,hauteur/24),(position_personnage1[0]+largeur/100,position_personnage1[1]+hauteur/19,largeur/32,hauteur/24)]
                for event in pygame.event.get():#Attente des événements
                        if event.type==KEYDOWN:

                                #PAUSE        
                                if event.key == K_ESCAPE:               #si ESCAPE
                                        pause=1                                        
                                        while pause==1:
                                                text = font1.render("PAUSE",1,(255,196,0))              #texte PAUSE
                                                fenetre.blit(text, (largeur/9.2,-hauteur/21.6))         #collage du texte

                                                text = font.render("ESC pour quitter",1,(255,196,0))    #texte ESC....
                                                fenetre.blit(text, (largeur/3.9,hauteur/1.5))           #collage texte

                                                text = font.render("ESPACE pour continuer",1,(255,196,0))       #texte ESPACE
                                                fenetre.blit(text, (largeur/6.2,hauteur/2))                     #collage texte'                                 
                                                
                                                pygame.display.update()                 #rafraichissement
                                                for event in pygame.event.get():
                                                        if event.type==KEYDOWN:
                                                                if event.key == K_ESCAPE:       #si on appuie sur escape on retourne au menu principal
                                                                        return
                                                                elif event.key == K_SPACE:      #si on appuie sur espace on continue le jeu
                                                                        pause=0
                                                                        
                                if event.key == K_UP:
                                        j=1
                                if event.key == K_RIGHT:
                                        if position_personnage2[0]<largeur*3/4 and bumped2==contre2==0:
                                                vitesse_personnage2[0] = largeur*6/640
                                        liste1.append("a")
                                if event.key == K_LEFT:
                                        if position_personnage2[0]>largeur/64 and bumped2==contre2==0:
                                                vitesse_personnage2[0] = -largeur*6/640
                                        liste1.append("b")
                                if event.key == K_w:
                                        k=1
                                if event.key == K_a:
                                        if position_personnage1[0]>largeur/64 and bumped1==contre1==0:
                                                vitesse_personnage1[0] = -largeur*6/640
                                        liste2.append("d")
                                if event.key == K_d:
                                        if position_personnage1[0]<largeur*3/4 and bumped1==contre1==0:
                                                vitesse_personnage1[0] = largeur*6/640
                                        liste2.append("c")
                                if (event.key == K_KP9 or event.key == K_p) and coup_poing2==coup_pied2==contre2==0:
                                        coup_poing2=1
                                if event.key == K_v and coup_poing1==coup_pied1==contre1==0:
                                        coup_poing1=1
                                if event.key == K_x and coup_poing1==coup_pied1==contre1==0:
                                        coup_pied1=1
                                if (event.key == K_KP7 or event.key == K_i) and coup_poing2==coup_pied2==contre2==0:
                                        coup_pied2=1
                                if event.key == K_c and coup_poing1==coup_pied1==0:
                                        contre1=1
                                if (event.key == K_KP8 or event.key == K_o) and coup_poing2==coup_pied2==0:
                                        contre2=1
                        if event.type==KEYUP:
                                if event.key==K_RIGHT:
                                        liste1.remove("a")
                                if event.key==K_LEFT:
                                        liste1.remove("b")
                                if event.key==K_d:
                                        liste2.remove("c")
                                if event.key==K_a:
                                        liste2.remove("d")
                                if event.key == K_UP:
                                        j=0
                                if event.key == K_w:
                                        k=0
                                if event.key == K_c:
                                        contre1=0
                                if event.key == K_KP8 or event.key==K_o:
                                        contre2=0
                        if event.type == QUIT:
                                continuer=0
                if liste1==[]:
                    vitesse_personnage2[0] = 0
                    y=0
                elif liste1[len(liste1)-1]=="a":
                    if position_personnage2[0]<largeur*3/4 and bumped2==contre2==0:
                        vitesse_personnage2[0] = largeur*6/640
                        y=marche(y,position_personnage2[1])
                    else:
                        vitesse_personnage2[0]=y=0
                elif liste1[len(liste1)-1]=="b":
                    if largeur/64<position_personnage2[0] and bumped2==contre2==0:
                        vitesse_personnage2[0] = -largeur*6/640
                        y=marche(y,position_personnage2[1])
                    else:
                        vitesse_personnage2[0]=y=0
                if liste2==[]:
                    vitesse_personnage1[0]=z=0
                elif liste2[len(liste2)-1]=="c":
                    if position_personnage1[0]<largeur*3/4 and bumped1==contre1==0:
                        vitesse_personnage1[0] = largeur*6/640
                        z=marche(z,position_personnage1[1])
                    else:
                        vitesse_personnage1[0]=z=0
                elif liste2[len(liste2)-1]=="d":
                    if largeur/64<position_personnage1[0] and bumped1==contre1==0:
                        vitesse_personnage1[0] = -largeur*6/640
                        z=marche(z,position_personnage1[1])
                    else:
                        vitesse_personnage1[0]=z=0
                if j==1 and position_personnage2[1]==sol and contre2==0:
                        vitesse_personnage2[1] = vitesse_saut
                if k==1 and position_personnage1[1]==sol and contre1==0:
                        vitesse_personnage1[1] = vitesse_saut
                if position_personnage1[1]==sol:
                        reaction1=-gravite
                        if sol_arret1==0:
                                vitesse_personnage1[1]=0
                                sol_arret1=1
                else:
                        reaction1=0
                        sol_arret1=0
                if position_personnage2[1]==sol:
                        reaction2=-gravite
                        if sol_arret2==0:
                                vitesse_personnage2[1]=0
                                sol_arret2=1
                else:
                        reaction2=0
                        sol_arret2=0
                vitesse_personnage1[1]+=(gravite+reaction1)/140
                vitesse_personnage2[1]+=(gravite+reaction2)/140
                if vitesse_personnage1[1]>=sol-position_personnage1[1]:
                        position_personnage1[1]=sol
                else:
                        position_personnage1[1]+=vitesse_personnage1[1]
                if vitesse_personnage2[1]>=sol-position_personnage2[1]:
                         position_personnage2[1]=sol
                else:
                        position_personnage2[1]+=vitesse_personnage2[1]
                if coup_poing2==1:
                        if gauche==personnage1 and bras2==0:
                                listecoup1=p2_mvmentcoup1
                                g1=personnage1
                        elif gauche==personnage2 and bras2==0:
                                listecoup1=p2_mvmentcoup2
                                g1=personnage2
                        if position_personnage2[1]==sol:
                                vitesse_personnage2[0]=0
                        bras2+=1
                        fenetre.blit(listecoup1[bras2], position_personnage2)
                        if bras2==7:
                                bras2+=1
                                coup_poing2=2
                if coup_poing2==2:
                        if position_personnage2[1]==sol:
                                vitesse_personnage2[0]=0
                        bras2-=1
                        if bras2==-1:
                                coup_poing2=0
                                bras2=0
                        else:
                                fenetre.blit(listecoup1[bras2], position_personnage2)
                if coup_poing1==1:
                        if gauche==personnage2 and bras1==0:
                                listecoup2=p1_mvmentcoup1
                                g2=personnage2
                        elif gauche==personnage1 and bras1==0:
                                listecoup2=p1_mvmentcoup2
                                g2=personnage1
                        if position_personnage1[1]==sol:
                                vitesse_personnage1[0]=0
                        bras1+=1
                        fenetre.blit(listecoup2[bras1], position_personnage1)
                        if bras1==7:
                                bras1+=1
                                coup_poing1=2
                if coup_poing1==2:
                        if position_personnage1[1]==sol:
                                vitesse_personnage1[0]=0
                        bras1-=1
                        if bras1==-1:
                                coup_poing1=0
                                bras1=0
                        else:
                                fenetre.blit(listecoup2[bras1], position_personnage1)
                if coup_pied2!=0:
                        if coup_pied2==1:
                                if gauche==personnage2:
                                        pospied2=p2_pieds2
                                else:
                                        pospied2=p2_pieds1
                        coup_pied2+=1
                        if coup_pied2<6:
                                fenetre.blit(pospied2[0], position_personnage2)
                        elif coup_pied2<12:
                                fenetre.blit(pospied2[1], position_personnage2)
                        elif coup_pied2<18:
                                fenetre.blit(pospied2[0], position_personnage2)
                        else:
                                coup_pied2=0
                        if position_personnage2[1]==sol:
                                vitesse_personnage2[0]=0
                        if pospied2==p2_pieds2:
                                hitboxpied2=pygame.Rect(position_personnage2[0]+largeur/10,position_personnage2[1]+hauteur*2/13,largeur/10,hauteur/6)
                        if pospied2==p2_pieds1:
                                hitboxpied2=pygame.Rect(position_personnage2[0],position_personnage2[1]+hauteur*2/13,largeur/10,hauteur/6)


                if coup_pied1!=0:
                        if coup_pied1==1:
                                if gauche==personnage1:
                                        pospied1=p1_pieds2
                                else:
                                        pospied1=p1_pieds1
                        coup_pied1+=1
                        if coup_pied1<6:
                                fenetre.blit(pospied1[0], position_personnage1)
                        elif coup_pied1<12:
                                fenetre.blit(pospied1[1], position_personnage1)
                        elif coup_pied1<18:
                                fenetre.blit(pospied1[0], position_personnage1)
                        else:
                                coup_pied1=0
                        if position_personnage1[1]==sol:
                                vitesse_personnage1[0]=0
                        if pospied1==p1_pieds2:
                                hitboxpied1=pygame.Rect(position_personnage1[0]+largeur/10,position_personnage1[1]+hauteur*2/13,largeur/10,hauteur/6)
                        if pospied1==p1_pieds1:
                                hitboxpied1=pygame.Rect(position_personnage1[0],position_personnage1[1]+hauteur*2/13,largeur/10,hauteur/6)

                if g1==personnage1:
                        hitbox1=listehitboxd1
                else:
                        hitbox1=listehitboxg1
                if g2==personnage1:
                        hitbox2=listehitboxg2
                else:
                        hitbox2=listehitboxd2
                
                if position_personnage1[0]<position_personnage2[0]:
                        gauche=personnage1
                        corps2=pygame.Rect(position_personnage2[0]+largeur*9/128,position_personnage2[1]+hauteur/50,largeur*12/128,hauteur*5/16)
                        corps1=pygame.Rect(position_personnage1[0]+largeur/28,position_personnage1[1]+hauteur/50,largeur*12/128,hauteur*5/16)
                else:
                        gauche=personnage2
                        corps2=pygame.Rect(position_personnage2[0]+largeur/28,position_personnage2[1]+hauteur/50,largeur*12/128,hauteur*5/16)
                        corps1=pygame.Rect(position_personnage1[0]+largeur*9/128,position_personnage1[1]+hauteur/50,largeur*12/128,hauteur*5/16)
                hitboxmain2=pygame.Rect(hitbox1[bras2])
                hitboxmain1=pygame.Rect(hitbox2[bras1])

                if contact2.colliderect(contact1):
                        if vitesse_personnage1[0]!=0 and vitesse_personnage2[0]!=0:
                                if vitesse_personnage1[0]/abs(vitesse_personnage1[0])==-vitesse_personnage2[0]/abs(vitesse_personnage2[0]) and (position_personnage2[0]<position_personnage1[0] and vitesse_personnage1[0]<0 or position_personnage2[0]>position_personnage1[0] and vitesse_personnage2[0]<0):
                                        vitesse_personnage1[0]=vitesse_personnage2[0]=0
                        else:
                                if vitesse_personnage1[0]<0 and position_personnage2[0]<position_personnage1[0]:
                                    if largeur/64<position_personnage2[0]:
                                        vitesse_personnage1[0]=vitesse_personnage2[0]=-largeur/700
                                    else:
                                        vitesse_personnage1[0]=vitesse_personnage2[0]=0
                                elif vitesse_personnage1[0]>0 and position_personnage1[0]<position_personnage2[0]:
                                    if position_personnage2[0]<largeur*3/4:
                                        vitesse_personnage1[0]=vitesse_personnage2[0]=largeur/700
                                    else:
                                        vitesse_personnage1[0]=vitesse_personnage2[0]=0
                                if vitesse_personnage2[0]<0 and position_personnage1[0]<position_personnage2[0]:
                                    if largeur/64<position_personnage1[0]:
                                        vitesse_personnage1[0]=vitesse_personnage2[0]=-largeur/700
                                    else:
                                        vitesse_personnage1[0]=vitesse_personnage2[0]=0
                                elif vitesse_personnage2[0]>0 and position_personnage2[0]<position_personnage1[0]:
                                    if position_personnage1[0]<largeur*3/4:
                                        vitesse_personnage1[0]=vitesse_personnage2[0]=largeur/700
                                    else:
                                        vitesse_personnage1[0]=vitesse_personnage2[0]=0
                if hitboxmain2.colliderect(corps1) and coup_poing2!=0 and bumped1==0 and contre1==0:
                        bumped1=1
                        vie1-=5
                if hitboxpied2.colliderect(corps1) and coup_pied2!=0 and bumped1==0 and contre1==0:
                        bumped1=1
                        vie1-=8
                if bumped1==1:
                        if bouclebumped1==0:
                                vitesse_personnage1[1]=-hauteur/30
                        bouclebumped1+=1
                        if bouclebumped1<30 and (largeur/64<position_personnage1[0]<largeur*3/4 or position_personnage2[0]<=position_personnage1[0]<=largeur/64 or largeur*3/4<=position_personnage1[0]<=position_personnage2[0]):
                                vitesse_personnage1[0]=(position_personnage1[0]-position_personnage2[0])/abs(position_personnage1[0]-position_personnage2[0])*largeur/150
                        elif bouclebumped1>=30:
                                bumped1=0
                                bouclebumped1=0
                if hitboxmain1.colliderect(corps2) and coup_poing1!=0 and bumped2==0 and contre2==0:
                        bumped2=1
                        vie2-=5
                if hitboxpied1.colliderect(corps2) and coup_pied1!=0 and bumped2==0 and contre2==0:
                        bumped2=1
                        vie2-=8
                if bumped2==1:
                        if bouclebumped2==0:
                                vitesse_personnage2[1]=-hauteur/30
                        bouclebumped2+=1
                        if bouclebumped2<30 and (largeur/64<position_personnage2[0]<largeur*3/4 or position_personnage1[0]<=position_personnage2[0]<=largeur/64 or largeur*3/4<=position_personnage2[0]<=position_personnage1[0]):
                                vitesse_personnage2[0]=(position_personnage2[0]-position_personnage1[0])/abs(position_personnage2[0]-position_personnage1[0])*largeur/150
                        elif bouclebumped2>=30:
                                bumped2=0
                                bouclebumped2=0
                if contre2!=0:
                        if hitboxmain1.colliderect(corps2) and coup_poing1!=0 or hitboxpied1.colliderect(corps2) and coup_pied1!=0:
                                if (largeur/64<position_personnage2[0]<largeur*3/4 or position_personnage1[0]<=position_personnage2[0]<=largeur/64 or largeur*3/4<=position_personnage2[0]<=position_personnage1[0]):
                                        vitesse_personnage2[0]=(position_personnage2[0]-position_personnage1[0])/abs(position_personnage2[0]-position_personnage1[0])*largeur/400
                        contre2+=1
                        if gauche==personnage2:
                                fenetre.blit(p2_image_contre2,position_personnage2)
                        else:
                                fenetre.blit(p2_image_contre,position_personnage2)
                        if contre2==150:
                                contre2=0
                if contre1!=0:
                        if hitboxmain2.colliderect(corps1) and coup_poing2!=0 or hitboxpied2.colliderect(corps1) and coup_pied2!=0:
                                if (largeur/64<position_personnage1[0]<largeur*3/4 or position_personnage2[0]<=position_personnage1[0]<=largeur/64 or largeur*3/4<=position_personnage1[0]<=position_personnage2[0]):
                                        vitesse_personnage1[0]=(position_personnage1[0]-position_personnage2[0])/abs(position_personnage1[0]-position_personnage2[0])*largeur/400
                        contre1+=1
                        if gauche==personnage1:
                                fenetre.blit(p1_image_contre2,position_personnage1)
                        else:
                                fenetre.blit(p1_image_contre,position_personnage1)
                        if contre1==150:
                                contre1=0
                #timer
                temps-=0.02
                text = font.render(str(int(temps)),1,(255,196,0))
                if temps>10:
                        fenetre.blit(text, ((largeur/2)-68, 65))
                elif temps<10:
                        fenetre.blit(text, ((largeur/2)-33, 65))
                if int(temps)==0:
                        continuer=0

                if vie1<=0 or vie2<=0:
                        continuer=0
                
                #vie        
                barre_vie1(fenetre,largeur,hauteur,vie1)
                barre_vie2(fenetre,largeur,hauteur,vie2)

                #joueurs
                text = font.render(("Joueur1"),1,(255,196,0))
                fenetre.blit(text, (largeur/8.73,hauteur/7.2))
                text = font.render(("Joueur2"),1,(255,196,0))
                fenetre.blit(text, (largeur/1.561,hauteur/7.2))
                
                if gauche==personnage1:
                        if coup_poing1==0 and coup_pied1==0 and contre1==0:
                                if 5<z<=10:
                                        fenetre.blit(personnage1_transition2, position_personnage1)
                                else:
                                        fenetre.blit(personnage1, position_personnage1)
                        if coup_poing2==0 and coup_pied2==0 and contre2==0:
                                if 5<y<=10:
                                        fenetre.blit(personnage2_transition, position_personnage2)
                                else:
                                        fenetre.blit(personnage22, position_personnage2)
                elif gauche==personnage2:
                        if coup_poing1==0 and coup_pied1==0 and contre1==0:
                                if 5<z<=10:
                                        fenetre.blit(personnage1_transition, position_personnage1)
                                else:
                                        fenetre.blit(personnage12, position_personnage1)
                        if coup_poing2==0 and coup_pied2==0 and contre2==0:
                                if 5<y<=10:
                                        fenetre.blit(personnage2_transition2, position_personnage2)
                                else:
                                        fenetre.blit(personnage2, position_personnage2)
                
                position_personnage1[0]+=vitesse_personnage1[0]
                position_personnage2[0]+=vitesse_personnage2[0]
                #Rafraichissement
                pygame.display.update()
                pygame.time.Clock().tick(70)

        fenetre.blit(fond, (0,0))


        if vie1<vie2:                                                           #si le joueur1 n'a plus de vie
                text = font1.render("Victoire",1,(255,196,0))
                fenetre.blit(text, (largeur/18,-hauteur/35))
                text = font1.render("Joueur 2",1,(255,196,0))
                fenetre.blit(text, (0,hauteur/2.5))
        elif vie1>vie2:                                                         #si le joueur2 n'a plus de vie
                text = font1.render("Victoire",1,(255,196,0))
                fenetre.blit(text, (largeur/18,-hauteur/35))
                text = font1.render("Joueur 1",1,(255,196,0))
                fenetre.blit(text, (0,hauteur/2.5))
        elif vie1==vie2:                                                        #si les deux joueurs ont la meme vie
                text = font1.render("Match",1,(255,196,0))
                fenetre.blit(text, (largeur/7,-hauteur/21.6))
                text = font1.render("Nul",1,(255,196,0))
                fenetre.blit(text, (largeur/3.7,hauteur/3))
                
        pygame.display.update()
        pygame.time.wait(5000)

#fenetre = pygame.display.set_mode((0,0), FULLSCREEN)  #création de la fenetre
#choix = 6
#grosse_def(fenetre,choix)
