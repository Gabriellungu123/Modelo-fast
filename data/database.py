import mysql.connector

database = mysql.connector.connect(
    host = "mysql",
    port = 3310,
    ssl_disabled = False,
    user = 'root',
    password = 'clase',
    database = 'Ordenadores'
)