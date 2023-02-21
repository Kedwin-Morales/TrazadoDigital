
import mysql.connector
from PyQt5 import QtCore

class Registro_datos(): 
    #Iniciamos la conexion a la bd
    def __init__(self): 
        self.conexion = mysql.connector.connect( host='localhost', database ='bd_traza_remota', user = 'root', password ='123456')
        
    #Busca el usuario y retorna todo de la fila                                        
    def busca_users(self, users):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM tb_usuarios WHERE USERS = {}".format(users)
        cur.execute(sql)
        
        #Devuelve una lista de tuplas restantes de la última declaración ejecutada de una tabla
        usersx = cur.fetchall()
        
        cur.close()     
        return usersx 
    
    #Busca la contrasena y retorna todo de la fila
    def busca_password(self, password):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM tb_usuarios WHERE PASSWORD = {}".format(password)
        cur.execute(sql)
        
        #Devuelve una lista de tuplas restantes de la última declaración ejecutada de una tabla
        passwordx = cur.fetchall()
        
        cur.close()     
        return passwordx 
    
    
    def inserta_datos(self, num_orden, forma_tipo, valor_vbox, valor_hbox, valor_puente, url):
        cur = self.conexion.cursor()
        sql='''INSERT INTO tb_trazas (NUM_ORDEN, FORMA_TIPO, VBOX, HBOX, PUENTE, RUTA_ARCHIVO) 
        VALUES('{}','{}','{}','{}','{}','{}')'''.format(num_orden, forma_tipo, valor_vbox, valor_hbox, valor_puente, url)
        cur.execute(sql)
        ordenx = cur.fetchall()
        self.conexion.commit()
        cur.close()
        return ordenx

        
    def buscar_orden(self, num_orden):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM tb_trazas WHERE NUM_ORDEN = {}".format(num_orden)
        cur.execute(sql)
        #Devuelve una lista de tuplas restantes de la última declaración ejecutada de una tabla
        ordenx = cur.fetchall()
        cur.close()
        return ordenx
        
    def buscar_trazas(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM tb_trazas "
        QtCore.QTimer.singleShot(2000, self.buscar_trazas)
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def busca_traza(self, num_orden):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM tb_trazas WHERE NUM_ORDEN = {}".format(num_orden)
        cur.execute(sql)
        nombreX = cur.fetchall()
        cur.close()
        return nombreX

    def elimina_traza(self, num_orden):
        cur = self.conexion.cursor()
        sql = '''DELETE FROM tb_trazas WHERE NUM_ORDEN = {}'''.format(num_orden)
        cur.execute(sql)
        a = cur.rowcount
        self.conexion.commit()
        cur.close()
        return a

    def actualiza_traza(self, Id, num_orden, forma_tipo, vbox, hbox, puente, url):
        cur = self.conexion.cursor()
        sql = ''' UPDATE tb_trazas SET NUM_ORDEN = '{}', FORMA_TIPO = '{}', VBOX = '{}', HBOX = '{}', PUENTE = '{}', RUTA_ARCHIVO = '{}' WHERE Id = '{}' '''.format(num_orden, forma_tipo, vbox, hbox, puente, url, Id)
        cur.execute(sql)
        a = cur.rowcount
        self.conexion.commit()
        cur.close()
        return a
        
    
        