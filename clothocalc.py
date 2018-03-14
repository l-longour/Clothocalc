#© Longour Lucas, 28/01/2018

# lucas.longour@protonmail.ch

#Ce logiciel est un programme informatique servant à calculer les éléments nécessaires à l'implantation des raccordements routiers de type clothoïde.

#Ce logiciel est régi par la licence CeCILL soumise au droit français et
#respectant les principes de diffusion des logiciels libres. Vous pouvez
#utiliser, modifier et/ou redistribuer ce programme sous les conditions
#de la licence CeCILL telle que diffusée par le CEA, le CNRS et l'INRIA
#sur le site "http://www.cecill.info".

#En contrepartie de l'accessibilité au code source et des droits de copie,
#de modification et de redistribution accordés par cette licence, il n'est
#offert aux utilisateurs qu'une garantie limitée.  Pour les mêmes raisons,
#seule une responsabilité restreinte pèse sur l'auteur du programme,  le
#titulaire des droits patrimoniaux et les concédants successifs.

#A cet égard  l'attention de l'utilisateur est attirée sur les risques
#associés au chargement,  à l'utilisation,  à la modification et/ou au
#développement et à la reproduction du logiciel par l'utilisateur étant
#donné sa spécificité de logiciel libre, qui peut le rendre complexe à
#manipuler et qui le réserve donc à des développeurs et des professionnels
#avertis possédant  des  connaissances  informatiques approfondies.  Les
#utilisateurs sont donc invités à charger  et  tester  l'adéquation  du
#logiciel à leurs besoins dans des conditions permettant d'assurer la
#sécurité de leurs systèmes et ou de leurs données et, plus généralement,
#à l'utiliser et l'exploiter dans les mêmes conditions de sécurité.

#Le fait que vous puissiez accéder à cet en-tête signifie que vous avez
#pris connaissance de la licence, et que vous en avez accepté les
#termes.

import math
projet = input("Nom du projet ? :")
cas = input("Cas du projet (1 pour symetriques, 2 pour symetrique-dissymetrique, 3 pour arcs de cercles) :")
cr = input("Entrer la catégorie de route :")
nv = input("Entrer le nombre de voies :")
r = input("Entrer le rayon du cercle projeté :")
aa = input("Entrer l'angle entre les raccordements (en gon) :")
p = input("Entrer la valeur du dévers en alignement (en %) :")
pma = float(p)/100
def vr(cr):
  if cr is 'R60':
    return 90
  if cr is 'R80':
    return 110
  if cr is 'T80':
    return 90
  if cr is 'T100':
    return 90
  if cr is 'L80':
    return 110
  if cr is 'L100':
    return 130
  if cr is 'L120':
    return 140
  if cr is 'A80':
    return 90
  if cr is 'A100':
    return 90
  if cr is 'U60':
    return 70
  if cr is 'U80':
    return 70

def rm(cr):
  if cr is 'R60':
    return 120
  if cr is 'R80':
    return 240
  if cr is 'T80':
    return 240
  if cr is 'T100':
    return 425
  if cr is 'L80':
    return 240
  if cr is 'L100':
    return 425
  if cr is 'L120':
    return 665
  if cr is 'A80':
    return 240
  if cr is 'A100':
    return 425
  if cr is 'U60':
    return 120
  if cr is 'U80':
    return 240

def rdm(cr):
  if cr is 'R60':
    return 450
  if cr is 'R80':
    return 650
  if cr is 'T80':
    return 650
  if cr is 'T100':
    return 900
  if cr is 'L80':
    return 650
  if cr is 'L100':
    return 900
  if cr is 'L120':
    return 1500
  if cr is 'A80':
    return 300
  if cr is 'A100':
    return 600
  if cr is 'U60':
    return 200
  if cr is 'U80':
    return 400

def rnd(cr):
  if cr is 'R60':
    return 600
  if cr is 'R80':
    return 900
  if cr is 'T80':
    return 900
  if cr is 'T100':
    return 1300
  if cr is 'L80':
    return 900
  if cr is 'L100':
    return 1300
  if cr is 'L120':
    return 1800
  if cr is 'A80':
    return 400
  if cr is 'A100':
    return 800
  if cr is 'U60':
    return 0
  if cr is 'U80':
    return 0
    
def rvm(cr):
  if cr is 'R60':
    return 1500
  if cr is 'R80':
    return 3000
  if cr is 'T80':
    return 3000
  if cr is 'T100':
    return 6000
  if cr is 'L80':
    return 3000
  if cr is 'L100':
    return 6000
  if cr is 'L120':
    return 10000
  if cr is 'A80':
    return 6000
  if cr is 'A100':
    return 10000
  if cr is 'U60':
    return 2500
  if cr is 'U80':
    return 6000

def pM ():
  if cr is 'R60' or cr is 'R80' or cr is 'T80' or cr is 'T100' or cr is 'L80' or cr is 'L100' or cr is 'L120':
    return round(0.07 + (float(pma)-0.07)*(float(r)-rm(cr))/(rdm(cr) - rm(cr)),3)
  if cr is 'A80' or cr is 'A100' or cr is 'U60' or cr is 'U80':
    return round(0.05 +(float(pma)-0.05)*(float(r)-rm(cr))/(rdm(cr) - rm(cr)),3)

def lr():
  if cr is 'L80' or cr is 'L100' or cr is 'L120' or cr is 'U60' or cr is 'U80' or 'A80' or cr is 'A100':
    if float(r)/9 < 14*(abs((float(pM())*100)-(-float(pma)*100))):
      return 14*(abs((float(pM())*100)-(-float(pma)*100)))
    if float(r)/9 > 14*(abs((float(pM())*100)-(-float(pma)*100))):
      print("Choix incorrect")
  if cr is 'R60' or cr is 'R80' or cr is 'T80' or cr is 'T100':
    if nv is '2':
      if 6*float(r)**0.4<67:
        return 6*float(r)**0.4
      if 6*float(r)**0.4>67:
        print("Calcul impossible: rayon trop grand")
    if nv is '3':
      if 9*float(r)**0.4<100:
        return 9*float(r)**0.4
      if 9*float(r)**0.4>100:
        print("Calcul impossible: rayon trop grand")
    if nv is '2x2' or nv is '2*2':
      if 12*float(r)**0.4<133:
        return 12*float(r)**0.4
      if 12*float(r)**0.4>133:
        print("Calcul impossible: rayon trop grand")
a = round(math.sqrt(float(r)*float(lr())),2)
if a > float(r)/10*math.sqrt((200-float(aa))*math.pi/2):
  print("! Condition d'existence non respectée !")
if a < float(r)/3:
  print("! Condition de visibilitée non respectée !")
L = lr()
print ("")
print("---RAPPEL DONNÉES CLOTHOÏDE---")
print("R :",r,"m")
print("L :",L,"m")
print("A :",a)
print("")
ch = input("Saisir o pour conserver, saisir n pour changer le paramètre :")
print("")
if ch is 'o':
  A = a
  R = r
  L = lr()
if ch is 'n':
  R = float(r)
  A = input("A :")
  L = float(A)**2/float(r)
  print("R :"),r,("m")
  print("L :"),L,("m")
print("")
print("---PARAMÈTRES DE LA CLOTHOÏDE---")
t = round(((float(L)**2)/(2*float(A)**2))/math.pi*200,4)
print("τ :"),t,("gon")
xF = round(float(L)*(1-(float(L)**4)/(40*(float(A)**4))+(float(L)**8)/(3456*(float(A)**8))+(float(L)**13)/(599040*(float(L)**13))),3)
print("xF :"),xF,("m")
yF = round((float(L)**3)/(6*(float(A)**2))*(1-(float(L)**4)/(56*(float(A)**4))+(float(L)**8)/(7040*(float(A)**8))),3)
print("yF :"),yF,("m")
rp = round(float(yF)-float(r)*(1-(math.cos(float(t)*math.pi/200))),3)
print("Ripage :"),rp,("m")
xC = round(float(xF)-float(R)*math.sin(float(t)*math.pi/200),3)
print("xC :"),xC,("m")
yC = round(float(R)+float(rp),3)
print("yC :"),yC,("m")
xS = round(float(xC)+(float(R)+float(rp))/math.tan(float(aa)*math.pi/400),3)
print("xS :"),xS,("m")
cOF = round(math.sqrt(float(xF)**2+float(yF)**2),3)
print("Corde OF :"),cOF,("m")
o = round(math.atan(float(yF)/float(xF))*200/math.pi,4)
print("ωF :"),o,("gon")
print("")
print("---PARAMÈTRES DE L'ARC RACCORDÉ---")
ac = 200-float(aa)
al = round(float(ac)-2*float(t),4)
print("α :"),al,("gon")
lar = round(float(R)*float(al)/200*math.pi,3)
print("Longueur :"),lar,("m")
cff = round(2*float(R)*math.sin(float(al)/400*math.pi),3)
print("Corde :"),cff,("m")
far = round(float(R)*(1-math.cos(float(al)*math.pi/400)),3)
print("Flèche :"),far,("m")
print("")
print("---IMPLANTATION PREMIERE CLOTHOÏDE---")
nbc1 = input("Entrer la distance entre chaques points :")
npa1 = round(float(L)/float(nbc1)+2,0)
print("Nombre de points à implanter :"),npa1
# IMPRESSION DES RESULTATS
rapport = open(projet+' - Rapport.txt','w')
rapport.write(' -----------------------------------------------------------------------------\n|                     Rapport de calcul des clothoides                        |\n -----------------------------------------------------------------------------\n   2018 - Clothocalc [Licence CeCILL_V2]      '+'github.com/llongour/Clothocalc'+'\n\nProjet: '+str(projet)+'\nVersion du logiciel: 2018.01.27\n ----------------------------------------------------------------------------- \n|                     D O N N E E S   E N   E N T R E E                       |\n -----------------------------------------------------------------------------\n  Categorie de route                 |  '+ cr + '\n  Nombre de voies                    |  '+ nv +'\n  Rayon du cercle projete (m)        |  '+ r + '\n  Angle entre les raccordements (gon)|  '+ aa +'\n  Devers en alignement (%)           |  '+ p +'\n\n\n\n================================================================================\n                           PARAMETRES DE LA CLOTHOIDE\n--------------------------------------------------------------------------------\n                 A                   |  '+ A +'\n                 R                   |  '+ r +'\n                 L                   |  '+str(L)+'\n================================================================================\n\n\n\n================================================================================\n|                                                                              |\n|                          ELEMENTS DE LA CLOTHOIDE                            |\n|                                                                              |\n|------------------------------------------------------------------------------|\n  PARAMETRES GENERAUX\n'+'    -τ (gon)               |  '+str(t)+'\n                             -------------------\n  DANS LE REPERE O,X,Y'+'\n    -oF (gon)              |  '+str(o)+'\n    -Ripage (m)            |  '+str(rp)+'\n                             -------------------\n  COORDONNEES DU CENTRE C\n    -X (m)                 |  '+str(xC)+'\n    -Y (m)                 |  '+str(yC)+'\n                             -------------------\n  ABSCISSE DU SOMMET S\n    -X (m)                 |  '+str(xS)+'\n================================================================================\n\n\n\n\n================================================================================\n|                                                                              |\n|                         ELEMENTS DE L ARC RACCORDE                           |\n|                                                                              |\n|------------------------------------------------------------------------------|\n  PARAMETRES GENERAUX\n    -a (gon)               |  '+str(al)+'\n    -Longueur (m)          |  '+str(lar)+'\n    -Corde (m)             |  '+str(cff)+'\n    -Fleche (m)            |  '+str(far)+'\n================================================================================\n\n\n\n\n\n\n       calculs effectues conformement aux directives du SETRA et du CERTU')
rapport.close()
# IMPRESSION IMPLANTATION
implantation = open(projet+' - Listing.txt','w')
implantation.write(' -----------------------------------------------------------------------------\n|                 Listing pour implantation de la clothoide 1                 |\n -----------------------------------------------------------------------------\n  2018 - Lucas Longour [Licence CeCILL_V2]     '+'github.com/llongour/Clothocalc'+'\n\nProjet: '+str(projet)+'\nVersion du logiciel: 2018.01.27\n -----------------------------------------------------------------------------\n|               I N F O R M A T I O N S   G E N E R A L E S                   |\n -----------------------------------------------------------------------------\n  Distance entre chaques points (m)  |  '+str(nbc1)+'\n  Nombre de points a implanter       |  '+str(npa1))
implantation.close()
