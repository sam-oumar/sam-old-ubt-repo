import os, openpyxl, csv

os.chdir('/home/samabaly/Bureau/Fichiers/Etats')

for file in os.listdir():
	if file.endswith(".xlsx"):
		filename = os.path.join(file)
		csv_file, ext = os.path.splitext(file)
		xlsfile = openpyxl.load_workbook(filename)
		title = xlsfile.sheetnames
		sheet = xlsfile[title[0]]

		columns = [2, 4, 5, 6, 7, 15]

		HEADER = ("Montant", "No", "Annee", "Prenom", "Nom", "No_dossier")
		csv_filename = csv_file+'.csv'
		with open(csv_filename, "w", newline="") as csvfile:
			etat = csv.writer(csvfile)
			etat.writerow(HEADER)
			rows = iter(sheet.rows)
			next(rows)
			next(rows)

			while True:
				try:
					row = next(rows)				
					DATA = [row[i].value for i in columns]
					# print(DATA)
					# os.chdir('/home/samabaly/Bureau/Fichiers/Etats/Csv')
					etat.writerow(DATA)
				except StopIteration:
					break