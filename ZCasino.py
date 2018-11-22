# -*- coding: Latin-1 -*

#ZCasino Project 1 book Python le Goff
#Carolina FC 10-07-18
# E : num_mise/somme_mise
# D : num_gagnant
# S : somme_remet
import os
import math
from random import randrange

num_mise = raw_input("Choisi le numero mise entre [0,49]")
try :
	num_mise = int(num_mise)
except : 
	print("Erreur lors de la convertion du numero coisi")
while (num_mise<0) or (num_mise>49) :
	num_mise = input("Choisi un numero entre [0,49]")

somme_mise = raw_input("Choisi la somme de la mise ($):")
try :
	somme_mise = int(somme_mise)
except : 
	print("Erreur lors de la convertion de la somme mise")

# la tirage au sort

num_gagnant = randrange(3)
print("Le numero gagnant est:", num_gagnant)
os.system("pause")
if num_mise == num_gagnant:
	somme_remet = somme_mise + 3*somme_mise
	print ("Vous avez gagner! Votre somme remise est de %2d$") %(somme_remet)
elif num_mise%2 == num_gagnant%2 :
	somme_remet = somme_mise + math.ceil(0.5*somme_mise)
	print ("Vous avez frapper que la colleur. Votre somme remise est de %2d$") %(somme_remet)
else:
	print ("Vous avez toute perdu votre mise!")