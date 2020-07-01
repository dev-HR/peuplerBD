#!/usr/bin/python3


src = open( 'noms/noms.txt' , 'r' )

#entete = src.readline()
#print( entete )

#nbLignes = 0
#for ligne in src :
	#nbLignes += 1
	#print( '[' + ligne + ']' )
	
	#print( ligne.split( '\t' )[0] )
	
	

#print( nbLignes )

entete = src.readline()

ligne = src.readline()

while ligne.split()[0] != 'AUTRES' :
	print( ligne.split()[0] )
	
	ligne = src.readline()



src.close()
