# Projet transversal : Robot cartographe

# Détection d'obstacle, et différentiation d'objet spécifique (plot)
# Transformée de Hough : Détection de droite pour différentition d'objet

#Authors : Alice Malosse

#Utile : 
#https://www.f-legrand.fr/scidoc/docimg/image/extraction/hough/hough.html

#TODO : 
#   Programmation de la transformée de Hough
#   Initialisation pour détection de plot
#   Determination des conditions pour indentifier un plot
#   Mise en forme de fonction pour appel dans le main

import numpy as np
import math
import cmath
import matplotlib.pyplot as plt
import cv2
from scipy import sparse as sp

def max(data):
    xmax=data[0][0]
    ymax=data[0][1]
    for point in data:
        if(point[0]>xmax):
            xmax=point[0]
        if(point[0]>ymax):
            ymax=point[0]
    return (xmax, ymax)

def min(data):
    xmin=data[0][0]
    ymin=data[0][1]
    print(xmin, ymin)
    for point in data:
        if(point[0]<xmin):
            xmin=point[0]
        if(point[0]<ymin):
            ymin=point[0]
    return (xmin, ymin)

def fctHoughTchik(data):
    #On ajuste les données
    (xmin, ymin) = min(data)
    for i in range(len(data)):
        data[i]=[data[i][0]-xmin, data[i][1]-ymin]
    #Initialisation a partir des argument
    (Lx, Ly) = max(data)
    K = len(data)

    #Initialisation des variables de la T. de Hough
    rho = 5.0 #résolution en pixel
    theta = 0.5 #resolution en degré
    Ntheta = int(90.0/theta)
    Nrho = int(math.floor(math.sqrt(Lx*Lx + Ly*Ly))/rho)
    dtheta = math.pi/Ntheta
    drho = math.floor(math.sqrt(Lx*Lx + Ly*Ly))/Nrho
    accum = np.zeros((Ntheta,Nrho))

    #Realisation de la transformee de hough
    for i in range (K):
        x = data[i][0]
        y = data[i][1]

        #pour chaque theta on reccupere la valeur de rho
        for i_theta in range(-Ntheta, Ntheta):
            theta = i_theta*dtheta #init theta
            rho = x*math.cos(theta)+y*math.sin(theta) #init rho
            i_rho = int(rho/drho)  #norm rho

            #incremente dans l'espace accumulateur
                #si les coord sont viable
                #si plusieurs point appartiennent à une même droite
                #  on increment plusieurs fois le meme point de l'accumulateur
            if (i_rho>0) and (i_rho<Nrho):
                accum[i_theta][i_rho] += 1
    
    #Affichage de l'accumulateur
    # plt.figure(1)
    # plt.imshow(accum)
    # plt.show()

    #Reccupération des coordonnees des droites
        #on estime qu'il y a droite si on a plus de 50 points
    ligne = []
    seuil = 10
    for i in range (Ntheta) :
        for j in range (Nrho):
            #seuillage de l'accumulateur
            if accum[i][j] < seuil :
                accum[i][j] = 0
            #recupération des coord des droites
            else : 
                ligne.append((j*drho, i*dtheta, accum[i][j]))
    
    # plt.figure(2)
    # plt.imshow(accum)
    # plt.show()

    print(ligne)

    #Affichage des droites
    plt.figure(3)
    plt.axis([0,Lx, 0, Ly])
    marqueurs=['.','o','v','+','*','h','^','<','>','s','p','h','D','H','1','2','3','4','+','x','d','|','-',',']
    colors = ['k','g','b','r','c','m','y']
    j=0
    for rho, theta, nbpoint in ligne :
        print(theta,rho, nbpoint, colors[j%len(colors)]+marqueurs[j//len(colors)]+'-')
        a = math.cos(theta)
        b = math.sin(theta)
        if(theta<2.92):
            x0 = a*rho
            y0 = b*rho
        else:
            x0 = -a*rho
            y0 = -b*rho
        x1 = int(x0 + 10000*(-b))
        y1 = int(y0 + 10000*(a))
        x2 = int(x0 - 10000*(-b))
        y2 = int(y0 - 10000*(a))
        plt.plot([x1,x2], [y1,y2], colors[j%len(colors)]+marqueurs[j//len(colors)]+'-')
        j+=1
    # for rho, theta in ligne :
    #     a = math.cos(theta)
    #     b = math.sin(theta)
    #     x0 = -a*rho
    #     y0 = -b*rho
    #     x1 = int(x0 + 10000*(-b))
    #     y1 = int(y0 + 10000*(a))
    #     x2 = int(x0 - 10000*(-b))
    #     y2 = int(y0 - 10000*(a))
    #     plt.plot([x1,x2], [y1,y2])
    
    x = []
    y = []
    for i in range (K):
        x.append(data[i][0])
        y.append(data[i][1])
    plt.plot(x,y, "o")
    
    plt.show()



    #MAJ du booléan isCone
        #selon les conditions de présence d'un cone
    """
    present = 0
    if len(ligne)>=2 :
        for seg in ligne : 
            angle = seg[1]
            if (angle <= 0.42 and angle >= 0.40) or (angle <= 2.71 and angle >= 2.70) :
                present += 1
    isCone = False
    if present >= 2 :
        isCone = True
    """

    isCone = False
    for rho, theta in ligne :
        delta = math.pi/2 - theta
        alpha = math.pi - 2*delta
        #print (theta)
        print(alpha)
        if alpha>0.79 and alpha<0.81 :
            isCone = True

    print ("end hough")

    return isCone
    