import pyodbc
server = 'smro-arcgis-server.database.windows.net'
database = 'smro-arcgis-dev'
username = 'smro-admin@smro-arcgis-server'
password = 'Smith0722%'
driver= '{ODBC Driver 17 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute("SELECT * FROM [smro-arcgis-dev].[smro_mse_temp]  ")
row = cursor.fetchone()
while row:
    print (str(row[0]) + " " + str(row[1]))
    row = cursor.fetchone()