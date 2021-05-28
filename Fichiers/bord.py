import openpyxl, csv

xlsfile = openpyxl.load_workbook("Rente_Caisse_CI.xlsx")
sheet = xlsfile["DossierPaiePension1"]
HEADER = ("Montant", "No", "Annee", "Prenom", "Nom", "No_dossier")
with open("etat2.csv", "w", newline="") as csvfile:
	etat = csv.writer(csvfile)
	etat.writerow(HEADER)
	for row in sheet.rows:
		DATA = [row[2].value, row[4].value, row[5].value, row[6].value, row[7].value, row[15].value]
		print(DATA)
		# etat.writerow(DATA)

