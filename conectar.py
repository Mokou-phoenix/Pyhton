import pymysql

class conect():
    def __init__(self):
        self.crearconect()
        self.abrirconect()
    def crearconect(self):
        self.db = pymysql.connect(
            host="localhost",  
            port=3306, 
            user="root",
            passwd="Gordazo1234", 
            db="prueba"
        )

    def abrirconect(self):
        self.cursor = self.db.cursor()
    
    def ejecutarsql(self,sql):
        self.cursor.execute(sql)

    def devolverdatos(self):
        return self.cursor.fetchall()

    def realizarcambios(self):
        self.db.commit()

    def deshacer(self):
        self.db.rollback()

    def cerrarbase(self):
        self.db.close()