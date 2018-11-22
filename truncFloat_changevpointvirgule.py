# -*- coding: Latin-1 -*
def afficher_flottant(numf):
	print numf
	print type(numf)
	numfList = numf.split(".")
#	print numfList
	intPart = numfList[0]
	decimal = numfList[1]
	truncDec = decimal[0:3]
	newFloat = numfList[0]+","+truncDec
	print newFloat
	
#	if type(numf) is not float :
#		raise TypeError ("Le paramètre attendu doit etrê un flottant")

Ent_Num = raw_input("Tape un numero float avec point:")
try:
	float(Ent_Num)
except:
	print("Error: It is not a float number")
afficher_flottant(Ent_Num)
