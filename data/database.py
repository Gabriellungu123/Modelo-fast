import mysql.connector

database = mysql.connector.connect(
    host = "localhost",
    port = 3310,
    ssl_disabled = True,
    user = 'root',
    password = 'clase',
    database = 'Ordenadores'
)