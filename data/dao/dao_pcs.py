from data.modelo.pcs import pcs

class DaoPcs :#Creao una clase
    #Hacer un select

    def get_all(self, db) -> list[pcs]: #defino un metodo llamado get_all que recibe un la conexion a la base de dato (db) y el -> list[pcs]: es que me lo devuelve en una lista de objetos
        cursor = db.cursor() #En esta linea creo un cursor que me permite ejecutar consultas de codigo y recorrer los resultados
        cursor.execute("SELECT * FROM pcs") #Aqui ejecuto la consulta (seleccionar todos los objetos de la tabla pcs)
        pcs_en_db = cursor.fetchall() #Recupera los datos es decir que lo que salga de la consulta de arriba y lo almacena en la variables pcs_en_db
        lista_pcs : list[pcs]=[] #Lista vacia donde se almacenaran los objetos de pcs
        for pc in pcs_en_db : #Este bucle recorre cada fila obtenida de la base de datos
            obj = pcs(pc[0],pc[1],pc[2],pc[3],) #Se crea un objeto  utilizando los datos de la fila
            lista_pcs.append(obj) # luego se agregan a la lista vacia 
        cursor.close() #Cerramos el cursor 
        return lista_pcs #- Se devuelve la lista lista_pcs, que contiene todos los objetos pcs creados a partir de los registros de la base de datos.

    #Hacer el Añadir
    
    def insert(self, db, marca:str, tipo:int, sistema:str, procesador:str): # define un metodo insert que recibe los siguientes parametros (db : conexion a la base de datos), marca , tipo, sistema, procesador
        cursor = db.cursor() #Esto permite ejecutar consultas SQL a la base de datos
        sql = "INSERT INTO pcs (marca, tipo, sistema, procesador) VALUES (%s,%s,%s,%s)" #- Se define una consulta SQL para insertar un nuevo registro en la tabla pcs. Los valores (%s, %s, %s, %s) son placeholders que serán reemplazados con los datos reales.
        data = (marca, tipo, sistema, procesador) #en data es donde se insertaran en la base de datos
        cursor.execute(sql, data) #Seria sql= INSERT INTO pcs (marca, tipo, sistema, procesador) VALUES (marca, tipo, sistema, procesador)
        db.commit() #Se guardan los cambios
        cursor.close() #Cierro cursor

    #Hacer el borrar 