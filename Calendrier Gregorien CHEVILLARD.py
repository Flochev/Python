#Florian Chevillard 

#import
import sys

#entrées
jours=int(input("Mettre le Jour : "))
mois=int(input("le Mois  : "))
an=int(input(" et l'Année : "))

#Hors Gregorien
if an<=1582:
    print("Nous ne somme pas dans le calendrier Gregorien à cette date")
    sys.exit()
    
#formule
else:
    mois<=2
    mois=mois+12
    an=an-1
    F=(jours+(13*(mois+1))//5+an+an//4-an//100+an//400)%7

#sortie
Jours=['samedi','dimanche','lundi','mardi','mercredi','jeudi','vendredi']
print("C'était un",Jours[F])


