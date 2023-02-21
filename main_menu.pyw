
import sys
from front.front_menu import *
from conexion.conexion import *
from PyQt5.QtWidgets import QTableWidgetItem
from os import startfile
from PyQt5.QtCore import QPropertyAnimation
from PyQt5 import QtCore
import re
from PyQt5.QtGui import QRegExpValidator, QValidator
from PyQt5.QtCore import QRegExp
from PyQt5 import QtGui, QtWidgets


class MiApp(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_MainWindow() 
		self.ui.setupUi(self)
		
		#conexion a bd
		self.datos = Registro_datos()

		#Configura la entrada de texto y numero
		self.ui.linea_buscar_individual.setValidator(QRegExpValidator(QRegExp("[0-9]+")))
		self.ui.linea_orden_actualizar.setValidator(QRegExpValidator(QRegExp("[0-9]+")))
		self.ui.linea_orden_eliminar.setValidator(QRegExpValidator(QRegExp("[0-9]+")))
		self.ui.linea_forma_actualizar.setValidator(QRegExpValidator(QRegExp(r"([P])-([0-9]{2,2})$")))
		
		#Escribe en los campos de entradas
		self.ui.linea_forma_actualizar.setText('P-00')
		self.ui.linea_vbox_actualizar.setSpecialValueText('00,00')
		self.ui.linea_hbox_actualizar.setSpecialValueText('00,00')
		self.ui.linea_puente_actualizar.setSpecialValueText('00,00')
		
		#Funcion del menu de opciones, paginas
		self.ui.btn_trazas.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_trazas))
		
		self.ui.btn_eliminar.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_eliminar))
		
		self.ui.btn_actualizar.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_actualizar))
		
		self.ui.btn_inicio.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_inicio))
		
		self.ui.btn_nueva_traza.clicked.connect(self.abrir_app)
		
		#configuracion de los botones
		self.ui.btn_menu.clicked.connect(self.mover_menu)
		self.ui.btn_buscar_actualizar.clicked.connect(self.buscar_por_orden_actualizar)
		self.ui.btn_refrescar.clicked.connect(self.limpiar)
		self.ui.btn_buscar_individual.clicked.connect(self.buscar_traza)
		self.ui.btn_actualizar2.clicked.connect(self.modificar_traza)
		self.ui.btn_buscar_eliminar.clicked.connect(self.bucar_por_orden_eliminar)
		self.ui.btn_borrar.clicked.connect(self.eliminar_traza)
		
		#Desactivar botones
		self.ui.btn_actualizar2.setEnabled(False)
		self.ui.linea_forma_actualizar.setEnabled(False)
		self.ui.linea_vbox_actualizar.setEnabled(False)
		self.ui.linea_hbox_actualizar.setEnabled(False)
		self.ui.linea_puente_actualizar.setEnabled(False)
		self.ui.linea_url_actualizar.setEnabled(False)
		
		
		#Configurar columnas de la tabla
		self.ui.tabla_trazas.setColumnWidth(0,98)
		self.ui.tabla_trazas.setColumnWidth(1,100)
		self.ui.tabla_trazas.setColumnWidth(2,98)
		self.ui.tabla_trazas.setColumnWidth(3,98)
		self.ui.tabla_trazas.setColumnWidth(4,98)
		self.ui.tabla_trazas.setColumnWidth(5,198)

		self.ui.tabla_borrar.setColumnWidth(0,98)
		self.ui.tabla_borrar.setColumnWidth(1,100)
		self.ui.tabla_borrar.setColumnWidth(2,98)
		self.ui.tabla_borrar.setColumnWidth(3,98)
		self.ui.tabla_borrar.setColumnWidth(4,98)
		self.ui.tabla_borrar.setColumnWidth(5,198)
			
			
	def limpiar(self):
		'''Resetea la tabla'''
		self.ui.tabla_trazas.clearContents()
		self.ui.tabla_trazas.setRowCount(0)
		self.mostrar_trazas()
		
		
	def abrir_app(self):
		'''Ejecuta archivo'''
		self.open = startfile("main_traza.pyw")
		#self.close()
	
	def mover_menu(self):
		'''Desplazamiento horizontal del menu'''
		if True:
			width = self.ui.frame_control.width()
			normal = 0
			if width == 0:
				extender = 140
			else:
				extender = normal
			self.animacion = QPropertyAnimation(self.ui.frame_control, b'minimumWidth')
			self.animacion.setDuration(300)
			self.animacion.setStartValue(width)
			self.animacion.setEndValue(extender)
			self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
			self.animacion.start()

	def buscar_traza(self):
		'''Muestra el registro por el numero de orden'''
		num_orden = self.ui.linea_buscar_individual.text()
		num_format = re.compile(r'^\-?[0-9][0-9]*$')
		valor = re.match(num_format, num_orden)
		
		if valor:

			if num_orden == (''):
				self.ui.btn_buscar_individual.setStyleSheet("color: red;")
				self.ui.signal_trazas.setStyleSheet("color: red;")
				self.ui.signal_trazas.setText('Número de Orden es Requerido')
			
			else:	
				self.ui.signal_trazas.setText('')
				self.ui.btn_buscar_individual.setStyleSheet("color: white;")
				self.ui.btn_buscar_individual.setStyleSheet("QPushButton:hover{color: black;}")
				self.ui.signal_trazas.setStyleSheet("color: rgb(0,128,120,90%);")
			
				num_orden = int(num_orden)	
				datosB = self.datos.busca_traza(num_orden)
				
				if len(datosB) == 0:
					self.ui.signal_trazas.setStyleSheet("color: red;")
					self.ui.signal_trazas.setText('No existe')
				else:
					self.ui.signal_trazas.setStyleSheet("color: rgb(0,128,120,90%);")
					self.ui.signal_trazas.setText('')
					self.ui.linea_buscar_individual.setText('')
					
				i = len(datosB)
				self.ui.tabla_trazas.setRowCount(i)
				tablerow = 0
				for row in datosB:
					self.ui.tabla_trazas.setItem(tablerow,0,QtWidgets.QTableWidgetItem(str(row[1])))
					self.ui.tabla_trazas.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[2]))
					self.ui.tabla_trazas.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[3]))
					self.ui.tabla_trazas.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[4]))
					self.ui.tabla_trazas.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[5]))
					self.ui.tabla_trazas.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row[6]))
					tablerow +=1
		
		else:
			self.ui.btn_buscar_individual.setStyleSheet("color: red;")
			self.ui.signal_trazas.setStyleSheet("color: red;")
			self.ui.signal_trazas.setText('Número de Orden es Requerido')
	
	def mostrar_trazas(self):
		'''Muestra todo los registros'''
		datos = self.datos.buscar_trazas()
		i = len(datos)
		self.ui.tabla_trazas.setRowCount(i)
		tablerow = 0
		
		for row in datos:
			self.Id = row [0]
			self.ui.tabla_trazas.setItem(tablerow,0,QtWidgets.QTableWidgetItem(str(row[1])))
			self.ui.tabla_trazas.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[2]))
			self.ui.tabla_trazas.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[3]))
			self.ui.tabla_trazas.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[4]))
			self.ui.tabla_trazas.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[5]))
			self.ui.tabla_trazas.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row[6]))
			tablerow +=1
		
		self.ui.signal_trazas.setText('')
		self.ui.btn_buscar_individual.setStyleSheet("color: white;")
		self.ui.btn_buscar_individual.setStyleSheet("QPushButton:hover{color: black;}")
		self.ui.signal_trazas.setStyleSheet("color: rgb(0,128,120,90%);")
		
	def buscar_por_orden_actualizar(self):
		'''Muestra el registro por el numero de orden'''
		num_orden = self.ui.linea_orden_actualizar.text()
		
		if num_orden == (''):
			self.ui.btn_actualizar2.setStyleSheet("color: red;")
			self.ui.btn_buscar_actualizar.setStyleSheet("color: red;")
			self.ui.signal_actualizar.setStyleSheet("color: red;")
			self.ui.signal_actualizar.setText('Número de Orden es Requerido')
			self.ui.btn_actualizar2.setEnabled(False)
		
		else:
			self.ui.btn_actualizar2.setEnabled(True)
			self.ui.signal_actualizar.setText('')
			self.ui.btn_actualizar2.setStyleSheet("color: white;")
			self.ui.btn_actualizar2.setStyleSheet("QPushButton:hover{color: black;}")
			self.ui.btn_buscar_actualizar.setStyleSheet("color: white;")
			self.ui.btn_buscar_actualizar.setStyleSheet("QPushButton:hover{color: black;}")
			self.ui.signal_actualizar.setStyleSheet("color: rgb(0,128,120,90%);")
			
			self.ui.linea_forma_actualizar.setEnabled(True)
			self.ui.linea_vbox_actualizar.setEnabled(True)
			self.ui.linea_hbox_actualizar.setEnabled(True)
			self.ui.linea_puente_actualizar.setEnabled(True)
			self.ui.linea_url_actualizar.setEnabled(True)
			
			num_orden = int(num_orden)
			self.producto = self.datos.busca_traza(num_orden)
			
			if len(self.producto) != 0:
				self.ui.Id = self.producto[0][0]
				self.ui.linea_orden_actualizar.setText(str(self.producto[0][1]))
				self.ui.linea_forma_actualizar.setText(self.producto[0][2])
				self.ui.linea_vbox_actualizar.setSpecialValueText(self.producto[0][3])
				self.ui.linea_hbox_actualizar.setSpecialValueText(self.producto[0][4])
				self.ui.linea_puente_actualizar.setSpecialValueText(self.producto[0][5])
				self.ui.linea_url_actualizar.setText(self.producto[0][6])
				
			else:
				self.ui.linea_forma_actualizar.setEnabled(False)
				self.ui.linea_vbox_actualizar.setEnabled(False)
				self.ui.linea_hbox_actualizar.setEnabled(False)
				self.ui.linea_puente_actualizar.setEnabled(False)
				self.ui.linea_url_actualizar.setEnabled(False)
				
				self.ui.btn_actualizar2.setStyleSheet("color: red;")
				self.ui.btn_buscar_actualizar.setStyleSheet("color: red;")
				self.ui.signal_actualizar.setStyleSheet("color: red;")
				self.ui.signal_actualizar.setText('No existe')
				self.ui.btn_actualizar2.setEnabled(False)
				
	
	def modificar_traza(self):
		'''Modifica el registo, mantiene constante el Id'''
		num_orden = self.ui.linea_orden_actualizar.text()
		if self.producto != '':
			
			num_orden = self.ui.linea_orden_actualizar.text()
			forma = self.ui.linea_forma_actualizar.text().upper()
			vbox = self.ui.linea_vbox_actualizar.text().upper()
			hbox = self.ui.linea_hbox_actualizar.text().upper()
			puente = self.ui.linea_puente_actualizar.text().upper()
			url = self.ui.linea_url_actualizar.text().upper()
			
			if num_orden != '' and forma != '' and vbox != '' and hbox != '' and puente != '':
				act = self.datos.actualiza_traza(self.ui.Id, num_orden, forma , vbox, hbox, puente, url)
				
				if act == 1:
					self.ui.signal_actualizar.setText("ACTUALIZADO")
					self.ui.btn_actualizar2.setEnabled(False)
					self.ui.linea_orden_actualizar.clear()
					self.ui.linea_forma_actualizar.setText('P-00')
					self.ui.linea_vbox_actualizar.setSpecialValueText('00,00')
					self.ui.linea_hbox_actualizar.setSpecialValueText('00,00')
					self.ui.linea_puente_actualizar.setSpecialValueText('00,00')
					self.ui.linea_url_actualizar.clear()
	
				elif act == 0:
					self.ui.signal_actualizar.setText("ERROR")
					
				else:
					self.ui.signal_actualizar.setText("INCORRECTO")
			
			else: 
				self.ui.signal_actualizar.setText('Hay espacios vacios')
			
	def bucar_por_orden_eliminar (self):
		'''Muestra el registro por el numero de orden'''
		self.num_orden = self.ui.linea_orden_eliminar.text()
		
		if self.num_orden == (''):
			self.ui.btn_borrar.setStyleSheet("color: red;")
			self.ui.signal_eliminar.setStyleSheet("color: red;")
			self.ui.btn_buscar_eliminar.setStyleSheet("color: red;")
			self.ui.signal_eliminar.setText('Número de Orden es Requerido')
			self.ui.btn_borrar.setEnabled(False)
			
		else:
			self.ui.btn_borrar.setEnabled(True)
			self.ui.signal_eliminar.setText('')
			self.ui.btn_borrar.setStyleSheet("color: white;")
			self.ui.btn_buscar_eliminar.setStyleSheet("color: white;")
			self.ui.btn_buscar_eliminar.setStyleSheet("QPushButton:hover{color: black;}")
			self.ui.btn_borrar.setStyleSheet("QPushButton:hover{color: black;}")
			self.ui.signal_eliminar.setStyleSheet("color: rgb(0,128,120,90%);")
			
			self.num_orden = int( self.num_orden )
			producto = self.datos.busca_traza(self.num_orden)
			
			self.ui.tabla_borrar.setRowCount(len(producto))
			
			if len(producto) == 0:
				self.ui.signal_eliminar.setText('No existe')
				self.ui.signal_eliminar.setStyleSheet("color: red;")
			else:
				self.ui.signal_eliminar.setStyleSheet("color: rgb(0,128,120,90%);")
				self.ui.signal_eliminar.setText('')
			
			tablerow = 0
			for row in producto:
				self.orden_a_eliminar = row[2]
				self.ui.tabla_borrar.setItem(tablerow,0,QtWidgets.QTableWidgetItem(str(row[1])))
				self.ui.tabla_borrar.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[2]))
				self.ui.tabla_borrar.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[3]))
				self.ui.tabla_borrar.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[4]))
				self.ui.tabla_borrar.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[5]))
				self.ui.tabla_borrar.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row[6]))
				tablerow +=1
		
	def eliminar_traza(self):
		'''Elimina el registro seleccionado'''
		self.row_flag = self.ui.tabla_borrar.currentRow()
		if self.row_flag == 0:
			self.ui.tabla_borrar.removeRow(0)
			self.datos.elimina_traza(self.num_orden)
			self.ui.linea_orden_eliminar.setText('')
			self.ui.signal_eliminar.setText('Orden eliminada')

if __name__ == "__main__":
     app = QtWidgets.QApplication(sys.argv)
     mi_app = MiApp()
     mi_app.show()
     sys.exit(app.exec_())		
