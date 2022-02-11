import time
import os

#Case cellule morte (empty) ou vivante (shape)
shape = "█"
empty = "▒"

##Tableau vide au démarrage
hauteur = 22
largeur = 36
Board = [[empty]*largeur for i in range(hauteur)]

## Initialisation pour le canon
Board[5][0]=shape
Board[6][0]=shape
Board[5][1]=shape
Board[6][1]=shape
Board[5][10]=shape
Board[6][10]=shape
Board[7][10]=shape
Board[4][11]=shape
Board[8][11]=shape
Board[3][12]=shape
Board[9][12]=shape
Board[3][13]=shape
Board[9][13]=shape
Board[6][14]=shape
Board[4][15]=shape
Board[8][15]=shape
Board[5][16]=shape
Board[6][16]=shape
Board[7][16]=shape
Board[6][17]=shape
Board[3][20]=shape
Board[4][20]=shape
Board[5][20]=shape
Board[3][21]=shape
Board[4][21]=shape
Board[5][21]=shape
Board[2][22]=shape
Board[6][22]=shape
Board[1][24]=shape
Board[2][24]=shape
Board[6][24]=shape
Board[7][24]=shape
Board[3][34]=shape
Board[4][34]=shape
Board[3][35]=shape
Board[4][35]=shape  

boucle = 0

## Pour vider la console
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

## Affichage du jeu
def printGame(b) :
    cls()
    ligne = "" 
    plateau = "╔" + largeur * "═" + "╗\n"
    print("_______"+ str(boucle) + "________")
    for i in range(len(b)) :
        for j in range(len(b[i])):
            ligne += b[i][j]
        plateau += "║" + ligne+ "║ \n"
        ligne = ""
    plateau += "╚" + largeur * "═" + "╝"
    print(plateau)

def getnbvoisinVivant(x,y,b) :
    count = 0
    if x== 0 :
        if y == 0 : #Corner topleft
            #print("TOPLEFT | x:" + str(x) + " y:" + str(y))
            if (b[x+1][y]) == shape :
                count += 1
            if (b[x+1][y+1]) == shape :
                count += 1
            if (b[x][y+1]) == shape :
                count += 1
        else :
            if y == largeur - 1 : #Corner topright
                #print("TOPRIGHT | x:" + str(x) + " y:" + str(y))
                if (b[x+1][y]) == shape :
                    count += 1
                if (b[x+1][y-1]) == shape :
                    count += 1
                if (b[x][y-1]) == shape :
                    count += 1
            else : #side Top
                #print("SIDETOP | x:" + str(x) + " y:" + str(y))
                if (b[x][y-1]) == shape :
                    count += 1
                if (b[x][y+1]) == shape :
                    count += 1
                if (b[x+1][y-1]) == shape :
                    count += 1
                if (b[x+1][y]) == shape :
                    count += 1
                if (b[x+1][y+1]) == shape :
                    count += 1
    else :
        if x == hauteur - 1 :
            if y == 0 : #Corner downleft
                #print("DOWNLEFT | x:" + str(x) + " y:" + str(y))
                if (b[x-1][y]) == shape :
                    count += 1
                if (b[x-1][y+1]) == shape :
                    count += 1
                if (b[x][y+1]) == shape :
                    count += 1
            else :
                if y == largeur - 1 : #Corner downright
                    #print("DOWNRIGHT | x:" + str(x) + " y:" + str(y))
                    if (b[x-1][y]) == shape :
                        count += 1
                    if (b[x-1][y-1]) == shape :
                        count += 1
                    if (b[x][y-1]) == shape :
                        count += 1
                else : #side down
                    #print("SIDEDOWN | x:" + str(x) + " y:" + str(y))
                    if (b[x][y-1]) == shape :
                        count += 1
                    if (b[x][y+1]) == shape :
                        count += 1
                    if (b[x-1][y-1]) == shape :
                        count += 1
                    if (b[x-1][y]) == shape :
                        count += 1
                    if (b[x-1][y+1]) == shape :
                        count += 1
    if y == 0 and x != 0 and x != hauteur - 1 : #side left
        #print("SIDELEFT | x:" + str(x) + " y:" + str(y))
        if (b[x-1][y]) == shape :
           count += 1
        if (b[x+1][y]) == shape :
           count += 1
        if (b[x-1][y+1]) == shape:
           count += 1
        if (b[x][y+1]) == shape :
           count += 1
        if (b[x+1][y+1]) == shape :
           count += 1
    else :
        if y == largeur - 1 and x != 0 and x != hauteur - 1 : #side right
            #print("SIDERIGHT | x:" + str(x) + " y:" + str(y))
            if (b[x-1][y]) == shape :
               count += 1
            if (b[x+1][y]) == shape :
               count += 1
            if (b[x-1][y-1]) == shape :
               count += 1
            if (b[x][y-1]) == shape :
               count += 1
            if (b[x+1][y-1]) == shape :
               count += 1
    if y != 0 and y != largeur - 1 and x != 0 and x != hauteur - 1 : #Center
        #print("CENTER | x:" + str(x) + " y:" + str(y))
        if (b[x-1][y]) == shape :
            count += 1
        if (b[x+1][y]) == shape :
            count += 1
        if (b[x-1][y-1]) == shape :
           count += 1
        if (b[x][y-1]) == shape :
           count += 1
        if (b[x+1][y-1]) == shape :
           count += 1
        if (b[x-1][y+1]) == shape:
           count += 1
        if (b[x][y+1]) == shape :
           count += 1
        if (b[x+1][y+1]) == shape :
           count += 1
    return count

def doAction(b):
    printGame(b)
    newb = [[empty]*largeur for i in range(hauteur)]
    for i in range(len(b)) :
        for j in range(len(b[i])):
            if (b[i][j]) == shape :
                #Cellule Vivante
                nbVoisinVivant = getnbvoisinVivant(int(i),int(j),b)
                if nbVoisinVivant > 1 and nbVoisinVivant <4 :
                    #Reste Vivante
                    #print("ALIVE | i:" + str(i) + " j:" + str(j) + " | nbVoisinVivant : " + str(nbVoisinVivant))
                    newb[i][j] = shape
                else :
                    #Deviens Morte
                    #print("DIE   | i:" + str(i) + " j:" + str(j) + " | nbVoisinVivant : " + str(nbVoisinVivant))
                    newb[i][j] = empty
            else :
                nbVoisinVivant = getnbvoisinVivant(int(i),int(j),b)
                if nbVoisinVivant == 3 :
                    #print("BORN  | i:" + str(i) + " j:" + str(j) + " | nbVoisinVivant : " + str(nbVoisinVivant))
                    newb[i][j] = shape
    return newb

while True:
    Board = doAction(Board)
    boucle = boucle + 1
    if boucle >= 1000 :
        break
    time.sleep(0.02)
