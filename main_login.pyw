
import sys
from front.front_login import *
from os import startfile
from conexion.conexion import *
import time
from PyQt5.QtGui import QRegExpValidator, QValidator
from PyQt5.QtCore import QRegExp


class MiApp(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_MainWindow() 
		self.ui.setupUi(self)
		
		#Configura la entrada de texto y numero
		self.ui.users.setValidator(QRegExpValidator(QRegExp(r"^([a-z,\.,0-9]{3,25})@([a-z]{4,12}).com$")))
			    
		#eliminar barra de window
		self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
		self.setWindowOpacity(1)
		
		#Colocar transparente frame de Qt
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
     	
     	#Conexion a bd 
		self.datos = Registro_datos()
		
		#Funcion del boton
		self.ui.bt_ingresar.clicked.connect(self.verificar)
	
	
	def verificar(self):
		'''Verifica el texto ingresado en los campos'''
		usuario = self.ui.users.text()
		clave  = self.ui.password.text()
		
		if usuario != '' and clave != '':
			self.ui.usuario_incorrecto.setText('')
			self.ui.contrasena_incorrecta.setText('')
		
			if '@' in usuario:                                  #Chequear que @ esté presente
					ubicacionArroba = usuario.find('@')         # Identificar la posición de @
					
					if usuario[len(usuario)-4:] == '.com':      # Chequear que los últimos 4 caracteres sean '.com'
						usuario[0:ubicacionArroba]              # Extraer la cadena a la izquierda de @
						
						if usuario.islower():                   #cadena de alfabeto en minuscula
							self.iniciar_sesion()
							
						else:
							self.ui.usuario_incorrecto.setText('SOLO MINUSCULAS')
						
					else:
						self.ui.usuario_incorrecto.setText('DOMINIO INCORRECTO')
				
			else:
				self.ui.usuario_incorrecto.setText('USUARIO INCOMPLETO')
				
		else:
			self.ui.usuario_incorrecto.setText('CAMPO OBLIGATORIO')
			self.ui.contrasena_incorrecta.setText('CAMPO OBLIGATORIO')
			
	
	def iniciar_sesion(self):
		'''Verificar datos ingresados'''
		#Verfica que no hay nada escrito en el label de las signals, usuario y contrasena incorrecta
		self.ui.contrasena_incorrecta.setText('')
		self.ui.usuario_incorrecto.setText('')
		
		#Obtenemos los valores ingresados de los input.
		users_entry = self.ui.users.text()
		password_entry = self.ui.password.text()
		
		#Asignamos comillas para realizar la busqueda en el metodo de conexion, formato string
		users_entry = str("'" + users_entry + "'")
		password_entry = str("'" + password_entry + "'")
		
		#Obtenemos datos con el objeto datos(base de datos).
		dato1 = self.datos.busca_users(users_entry)
		dato2 = self.datos.busca_password(password_entry)

		fila1 = dato1
		fila2 = dato2
		
		#Compara los datos del input, ambos campos vacios retorna el mensaje
		if dato1 == [] and dato2 ==[]:
			self.ui.contrasena_incorrecta.setText('CONTRASEÑA INCORRECTA')
			self.ui.usuario_incorrecto.setText('USUARIO INCORRECTO')
		else:
			
			#Compara los datos del input ingresados
			if dato1 ==[]:
				self.ui.usuario_incorrecto.setText('USUARIO INCORRECTO')
			else:
				dato1 = dato1[0][1]
			
			#Compara los datos del input ingresados
			if dato2 ==[]:
				self.ui.contrasena_incorrecta.setText('CONTRASEÑA INCORRECTA')
			else:
				dato2 = dato2[0][2]
			
			#Compara los datos del input ingresados
			if dato1 != [] and dato2 != []:
				
				self.abrir = self.abrir_menu()
				
				#Para activar la barra de progreso
				for i in range(0, 99):
					time.sleep(0.02)
					self.ui.progressBar.setValue(i)
					self.ui.cargando.setText('CARGANDO...')
				
				#Oculta y cierra la pestana del login
				self.hide()
				self.close()
			
	def abrir_menu(self):
		'''Ejecutar archivo'''
		self.abrir = startfile("main_menu.pyw")


if __name__ == "__main__":
     app = QtWidgets.QApplication(sys.argv)
     mi_app = MiApp()
     mi_app.show()
     sys.exit(app.exec_())	