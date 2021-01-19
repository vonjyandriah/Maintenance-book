import datetime
import sqlite3

conn = sqlite3.connect ('entretient.sq3')

now = datetime.datetime.now()
lieux = input ("Stations :")
odo = input ("Kilometrage au tableau :")
prix_litre = 4100
Litre =0
Ar =0
prix = float(input ("prix d'achat carburant :"))
if prix == 0 :
	Litre = float(input("quantite carburant :"))
	prix = Litre * prix_litre
	print ("Date :" + now.strftime("%c"))
	print ("Lieux :" + lieux)
	print ("Odo :" + odo)
	print ( prix)
	print ( Litre )
else :
	Litre = prix / prix_litre
	print ("Date :" + now.strftime("%c"))
	print ("Lieux :" + lieux)
	print ("Odo :" + odo)
	print ( prix)
	print ( Litre )

cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS carburant(
     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     now DATE,
     Lieux TEXT,
     ODO FLOAT,
     Litre FLOAT,
     PRIX INTEGER,
     ECART FLOAT
)
""")
ECART = 0
now = now.strftime("%c")
params = (now , lieux,odo,Litre,prix,ECART)
cursor.execute("INSERT INTO carburant(id,now,Lieux,ODO,Litre,PRIX,ECART) VALUES (NULL, ?, ?, ?, ?, ?, ?)", params)
conn.commit()
