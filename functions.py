def P(i,j,objets):
	"""
		resoudre le probleme de sac a dos 
		retourne la table utiliser pour la solution
		la table a en colonne le poid de 0 a j (inclu)est en ligne
	"""
	table=[]
	for ligne in range(len(objets)+1):
		#len(objets)+1 pour inclure le cas ou on inlut aucun objet 
		#ligne correspond a i dans l'enoncé
		row=[]
		for colonne in range(j+1):
			#j+1 pour inclure la valeur de j
			#colonne correspont a j dans l'enoncé
			if ligne==0 or colonne==0:
				row.append(0)
			elif colonne<objets[ligne-1].poid:
				row.append(table[ligne-1][colonne])
			else:
				row.append(max(table[ligne-1][colonne],table[ligne-1][colonne-objets[ligne-1].poid]+objets[ligne-1].gain))
		table.append(row)
	return table


if __name__ == "__main__":
	pass