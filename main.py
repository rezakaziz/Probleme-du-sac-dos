#imports
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from fenetre import Ui_MainWindow
from Objet import Objet
from random import randint
from functions import *

def clear():
	"""
		remettre a blanc tout les champs
	"""
	global objets
	objets=[]
	ensObjets=ui.ensObjets
	while ensObjets.rowCount() > 0:
	    ensObjets.removeRow(0)
	ensResults=ui.tableWidget
	while ensResults.rowCount() > 0:
	    ensResults.removeRow(0)
	ui.poidMax.setText('')
	ui.PoidMin.setText('')
	ui.GainMin.setText('')
	ui.GainMax.setText('')
	ui.PoidText.setText('')
	ui.gainText.setText('')
	ui.NbreObjets.setText('')
	ui.PoidMax.setText('')

def ajouter():
	"""
		ajouter l'objet(poid,gain) a la liste des objets
		et afficher dans la table des objets 
	"""
	global objets
	try:
		#recuperer les valeurs de poid et gain
		poid=int(ui.PoidText.toPlainText())
		gain=int(ui.gainText.toPlainText())
		#creer l'objet correspondant
		objet = Objet(poid,gain)
		#verifier que l'objet n'existe pas deja
		if objet not in objets:
			#ajouter l'objet a la liste des objets
			objets.append(Objet(poid,gain))
			#manipuler l'interface graphique
			rowPosition = ui.ensObjets.rowCount()
			ui.ensObjets.insertRow(rowPosition)
			ui.ensObjets.setItem(rowPosition,0, QtWidgets.QTableWidgetItem(str(poid)))
			ui.ensObjets.setItem(rowPosition,1, QtWidgets.QTableWidgetItem(str(gain)))
	except ValueError:
		print("Verifer les valeurs entrées")
	except:
		print("erreur non connu")
	


def supprimer():
	"""
		supprimer l'objet selectionné de la lise des objets
		et le supprimer de la table 
	"""
	global objets
	try:
		#recuperer la position de la ligne a supprimer
		rowPosition=ui.ensObjets.currentRow()
		if rowPosition>-1:
			#construire l'objet a supprimer 
			objet=Objet(int(ui.ensObjets.item(rowPosition,0).text()),int(ui.ensObjets.item(rowPosition,1).text()))
			ui.ensObjets.removeRow(rowPosition)
			objets.remove(objet)
	except ValueError as e:
		raise
	else:
		pass
	finally:
		pass
	

def aleatoire():
	"""
		generer une liste d'objets aleatoires tels que 
		le poid d'un objet est entre poid min et poid max 
		et le gain d'un objet entre gain min et gain max
	"""
	global objets
	try:
		poidMin=int(ui.PoidMin.toPlainText())
		poidMax=int(ui.PoidMax.toPlainText())+1
		gainMin=int(ui.GainMin.toPlainText())
		gainMax=int(ui.GainMax.toPlainText())+1
		nbreObjet=int(ui.NbreObjets.toPlainText())
		i=0
		nbObjetMax=(poidMax-poidMin)*(gainMax-gainMin)
		if nbObjetMax<nbreObjet:
			raise ValueError
		while i < nbreObjet:
			poid=randint(poidMin,poidMax)
			gain=randint(gainMin,gainMax)
			objet = Objet(poid,gain)
			if objet not in objets:
				i+=1
				objets.append(Objet(poid,gain))
				rowPosition = ui.ensObjets.rowCount()
				ui.ensObjets.insertRow(rowPosition)
				ui.ensObjets.setItem(rowPosition,0, QtWidgets.QTableWidgetItem(str(poid)))
				ui.ensObjets.setItem(rowPosition,1, QtWidgets.QTableWidgetItem(str(gain)))
	except ValueError:
		print("Verifer les valeurs entrées")
	else:
		pass
	finally:
		pass
	
	

def genererSolution():
	"""
		generer la solution optimale et l'afficher
	"""
	global objets
	try:
		W=int(ui.poidMax.toPlainText())
		nbreObjet=len(objets)
		table=P(nbreObjet,W,objets)
		misDansSac=trouverObjet(table,nbreObjet,W)
		sommepoid= sommePoid(misDansSac) 
		for o in misDansSac:
			rowPosition = ui.tableWidget.rowCount()
			ui.tableWidget.insertRow(rowPosition)
			ui.tableWidget.setItem(rowPosition,0, QtWidgets.QTableWidgetItem(str(o.poid)))
			ui.tableWidget.setItem(rowPosition,1, QtWidgets.QTableWidgetItem(str(o.gain)))
		ui.gainMaxText.setText(str(table[nbreObjet][W]))
		ui.poidMaxText.setText(str(sommepoid))	
	except ValueError as e:
		print('la valeur de poid max de sac a dos est manquante')
	else:
		pass
	finally:
		pass

def trouverObjet(table,N,W):
	"""
		Trouver un chemin de longueur m tq les noeud sont des poids et les arc sont des gains
		on utilise le principe de djikstra avec une condition d'arret sur le gain max
	"""
	global objets
	objetsAretenir=[]
	gain=table[N][W]
	while gain>0:
		if W>=objets[N-1].poid:
			if table[N][W]==table[N-1][W-objets[N-1].poid]+objets[N-1].gain and table[N][W]!=table[N-1][W]:
				objetsAretenir.append(objets[N-1])
				gain=gain-objets[N-1].gain
				N=N-1
				W=W-objets[N].poid
			else:
				N=N-1
		else:
			N=N-1
	return objetsAretenir

def sommePoid(ob):
	sum=0
	for o in ob:
		sum+=o.poid
	return sum

	

if __name__ == "__main__":
    #initialisation
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()

	#liste des objets
	objets=[]

	#connection
	ui.ajouterBtn.clicked.connect(ajouter)
	ui.suppBtn.clicked.connect(supprimer)
	ui.solution.clicked.connect(genererSolution)
	ui.aleatoire.clicked.connect(aleatoire)
	ui.clear.clicked.connect(clear)


	#exit
	sys.exit(app.exec_())