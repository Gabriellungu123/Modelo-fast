import mysql.connector

database = mysql.connector.connect(
    host = "host.docker.internal",
    port = 3310,
    ssl_disabled = True,
    user = 'root',
    password = 'clase',
    database = 'Ordenadores'
)