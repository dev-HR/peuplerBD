#!/usr/bin/python3

src = open( 'prenoms/prenoms.txt' , 'r' )

entete = src.readline()

prenom = ''

for ligne in src :
	
	prenomCourant = ligne.split( ';' )[1]
	
	if prenomCourant[0] != '_' :
		
		if 1 < len( prenomCourant ) :
			if prenomCourant != prenom :
				prenom = prenomCourant
				print( prenom.title() )
				
src.close()
