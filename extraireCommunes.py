#!/usr/bin/python3

src = open( 'communes/communes.csv' )



entete = src.readline()

for ligne in src :
	donnees = ligne.split( ';' )
	
	if donnees[0][:2].isdigit() and int( donnees[0][:2] ) <= 95 :
		print( ':'.join( donnees[:3] ) )


src.close()
