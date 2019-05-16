## DEBRAY Julie & FONTAINE Mallaury
##TP5
##21/10/2015
## http://www.fil.univ-lille1.fr/~L2S3API/CoursTP/tp_listes_tris_csv.html
import sys
import competitor
import Time
import list1
import csv
##import enum

sys.setrecursionlimit (3000)

def read_competitors(fichier):
    ouverture= open (fichier,'r')
    ligne= ouverture.readline()
    ligne= ouverture.readline()
    l=[]
    liste=[]
    compt=0 ## Le premier dossard est numéroté 1
    while ligne!='':
        for i in range(len(ligne)):
            l=str(ligne).split(';')
        compt+=1
        liste= liste + [competitor.create(l[0],l[1],l[2],compt)]
        l=[]
        ligne= ouverture.readline()
    ouverture.close()
    return liste
    
                                

##>>> read_competitors('small_inscrits.csv')
##[{'performance': None, 'last_name': 'Robert', 'num': 26, 'first_name': 'Sidney', 'sex': 'M'}, {'performance': None, 'last_name': 'Gilbert', 'num': 53, 'first_name': 'Paien', 'sex': 'M'}, {'performance': None, 'last_name': 'Riquier', 'num': 81, 'first_name': 'Vincent', 'sex': 'M'}, {'performance': None, 'last_name': 'Marier', 'num': 109, 'first_name': 'Saville', 'sex': 'M'}, {'performance': None, 'last_name': 'Lereau', 'num': 133, 'first_name': 'Namo', 'sex': 'M'}, {'performance': None, 'last_name': 'Hughes', 'num': 161, 'first_name': 'Romaine', 'sex': 'F'}, {'performance': None, 'last_name': 'Rivard', 'num': 188, 'first_name': 'Archard', 'sex': 'M'}, {'performance': None, 'last_name': 'Chassé', 'num': 214, 'first_name': 'Cheney', 'sex': 'M'}, {'performance': None, 'last_name': 'CinqMars', 'num': 244, 'first_name': 'Avelaine', 'sex': 'F'}, {'performance': None, 'last_name': 'Charest', 'num': 270, 'first_name': 'Sidney', 'sex': 'M'}]
##>>> l=read_competitors('small_inscrits.csv')
##>>> len(l)
##10
##>>> len(l[0])
##5
##>>> len(l[1])
##5
##>>> len(l[9])
##5

def read_performances(fichier):
    ouverture= open (fichier,'r')
    ligne= ouverture.readline()
    ligne= ouverture.readline()
    liste=[]
    l=[]
    while ligne!='':
        l=str(ligne).split(';')
        l[3]=l[3][:(len(l[3])-1)]
        liste = liste + [(l[0],l[1],l[2],l[3])]
        ligne= ouverture.readline()
    ouverture.close()
    return liste

##read_performances('small_performances.csv')
##[('1', '1', '8', '55'), ('3', '1', '21', '23'), ('4', '0', '56', '29'), ('5', '1', '6', '20'), ('6', '1', '17', '8'), ('7', '0', '46', '31'), ('8', '0', '48', '10'), ('10', '1', '6', '38')]
##>>> len(l)
##8
##>>> len(l[0])
##4
##>>> len(l[7])
##4
##>>> len(l[2])
##4

def duree(h,m,sec):
    s=str()
    s= str(h)+":"+ str(m)+":"+ str(sec)
    return s

def set_performances(l_inscrits,l_performances):
    for i in range (len(l_performances)):
        for y in range(len(l_inscrits)):
            if int(l_performances[i][0])== int(competitor.get_bibnum(l_inscrits[y])):
                d=duree(l_performances[i][1],l_performances[i][2],l_performances[i][3])
                competitor.set_perf (l_inscrits[y], d)
##>>> l1
##[{'performance': '1:8:55', 'first_name': 'Sidney', 'num': 1, 'last_name': 'Robert', 'sex': 'M'}, {'performance': None, 'first_name': 'Paien', 'num': 2, 'last_name': 'Gilbert', 'sex': 'M'}, {'performance': '1:21:23', 'first_name': 'Vincent', 'num': 3, 'last_name': 'Riquier', 'sex': 'M'}, {'performance': '0:56:29', 'first_name': 'Saville', 'num': 4, 'last_name': 'Marier', 'sex': 'M'}, {'performance': '1:6:20', 'first_name': 'Namo', 'num': 5, 'last_name': 'Lereau', 'sex': 'M'}, {'performance': '1:17:8', 'first_name': 'Romaine', 'num': 6, 'last_name': 'Hughes', 'sex': 'F'}, {'performance': '0:46:31', 'first_name': 'Archard', 'num': 7, 'last_name': 'Rivard', 'sex': 'M'}, {'performance': '0:48:10', 'first_name': 'Cheney', 'num': 8, 'last_name': 'Chassé', 'sex': 'M'}, {'performance': None, 'first_name': 'Avelaine', 'num': 9, 'last_name': 'CinqMars', 'sex': 'F'}, {'performance': '1:6:38', 'first_name': 'Sidney', 'num': 10, 'last_name': 'Charest', 'sex': 'M'}]
##>>> l2
##[('1', '1', '8', '55'), ('3', '1', '21', '23'), ('4', '0', '56', '29'), ('5', '1', '6', '20'), ('6', '1', '17', '8'), ('7', '0', '46', '31'), ('8', '0', '48', '10'), ('10', '1', '6', '38')]
##>>> l1[0]
##{'performance': '1:8:55', 'first_name': 'Sidney', 'num': 1, 'last_name': 'Robert', 'sex': 'M'}
##>>> l1[3]
##{'performance': '0:56:29', 'first_name': 'Saville', 'num': 4, 'last_name': 'Marier', 'sex': 'M'}
##>>> l[2]       
##>>> l1[2]
##{'performance': '1:21:23', 'first_name': 'Vincent', 'num': 3, 'last_name': 'Riquier', 'sex': 'M'}
##>>> l1[4]
##{'performance': '1:6:20', 'first_name': 'Namo', 'num': 5, 'last_name': 'Lereau', 'sex': 'M'}
##>>> l1[5]
##{'performance': '1:17:8', 'first_name': 'Romaine', 'num': 6, 'last_name': 'Hughes', 'sex': 'F'}
##>>> l1[6]
##{'performance': '0:46:31', 'first_name': 'Archard', 'num': 7, 'last_name': 'Rivard', 'sex': 'M'}
##>>> l1[7]
##{'performance': '0:48:10', 'first_name': 'Cheney', 'num': 8, 'last_name': 'Chassé', 'sex': 'M'}
##>>> l1[8]
##{'performance': None, 'first_name': 'Avelaine', 'num': 9, 'last_name': 'CinqMars', 'sex': 'F'}
##>>> l1[9]
##{'performance': '1:6:38', 'first_name': 'Sidney', 'num': 10, 'last_name': 'Charest', 'sex': 'M'}
##>>> 

def compare_name(n1,n2):
    plus_petit = min(len(n1),len(n2))
    for i in range (plus_petit):
        if n1[i]>n2[i]:
            return [n2, n1]
        elif n1[i]<n2[i]:
            return [n1,n2]
    n1_aux=list(n1)
    n2_aux=list(n2)
    if n1_aux[:plus_petit]==n2_aux[:plus_petit]:
        if len(n1)<=len(n2):
            return [n1,n2]
        elif len(n1)>len(n2):
            return [n2,n1]
        
def tri_alphabetique(l): ## Ne fonctionne pas
    liste=list()
    l_aux=l
    for i in range (len(l_aux)-1):
        for y in range (len(l)):
            print(l_aux[i],l[y])
            l2=compare_name(l_aux[i],l[y])
            if l_aux[i]!=l[y]:
                liste=liste+[l2[0]]
                print(liste)
    return liste
