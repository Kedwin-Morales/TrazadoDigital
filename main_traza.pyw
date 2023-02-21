
import sys
import numpy as np
import matplotlib.pyplot as plt
from conexion.conexion import *  # importar archivo de conexion.
from front.front_traza import *                #importar la GUI de traza.
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator, QValidator
from PyQt5 import QtCore, QtGui, QtWidgets, QtPrintSupport
from os import startfile
from PyQt5.QtGui import *

class MiApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        #conexion a bd
        self.datos = Registro_datos()
        
        #Configura la entrada de texto y numero
        self.ui.linea_num_orden.setValidator(QRegExpValidator(QRegExp("[0-9]+")))
        
        #self.open = startfile("main_menu.pyw")
        
        #Permite el llenado del vertical_layout 
        self.grafica1  = Canvas_grafica()
        self.grafica2  = Canvas_grafica()
        self.grafica3  = Canvas_grafica()
        self.grafica4  = Canvas_grafica()
        self.grafica5  = Canvas_grafica()
        self.grafica6  = Canvas_grafica()
        self.grafica7  = Canvas_grafica()
        self.grafica8  = Canvas_grafica()
        self.grafica9  = Canvas_grafica()
        self.grafica10 = Canvas_grafica()
        self.grafica11 = Canvas_grafica()
        self.grafica12 = Canvas_grafica()
        self.grafica13 = Canvas_grafica()
        self.grafica14 = Canvas_grafica()
        self.grafica15 = Canvas_grafica()
        self.grafica16 = Canvas_grafica()
        
        # Permite colocar dentro del vertical_layout (P-1)
        self.ui.contenedor_grafica1.addWidget(self.grafica1)
        self.ui.contenedor_grafica2.addWidget(self.grafica2)
        
        # Permite colocar dentro del vertical_layout (P-2)
        self.ui.contenedor_grafica3.addWidget(self.grafica3)
        self.ui.contenedor_grafica4.addWidget(self.grafica4)
        
        # Permite colocar dentro del vertical_layout (P-3)
        self.ui.contenedor_grafica5.addWidget(self.grafica5)
        self.ui.contenedor_grafica6.addWidget(self.grafica6)
        
        # Permite colocar dentro del vertical_layout (P-4)
        self.ui.contenedor_grafica7.addWidget(self.grafica7)
        self.ui.contenedor_grafica8.addWidget(self.grafica8)
        
        # Permite colocar dentro del vertical_layout (P-5)
        self.ui.contenedor_grafica9.addWidget(self.grafica9)
        self.ui.contenedor_grafica10.addWidget(self.grafica10)
        
        # Permite colocar dentro del vertical_layout (P-6)
        self.ui.contenedor_grafica11.addWidget(self.grafica11)
        self.ui.contenedor_grafica12.addWidget(self.grafica12)
        
        # Permite colocar dentro del vertical_layout (P-7)
        self.ui.contenedor_grafica13.addWidget(self.grafica13)
        self.ui.contenedor_grafica14.addWidget(self.grafica14)
        
        # Permite colocar dentro del vertical_layout (P-8)
        self.ui.contenedor_grafica15.addWidget(self.grafica15)
        self.ui.contenedor_grafica16.addWidget(self.grafica16)
        
        # Permite evaluar el cambio de valor 
        self.ui.VBOX.valueChanged.connect(self.valor_vertical)
        self.ui.HBOX.valueChanged.connect(self.valor_horizontal)
        
        #Configurar botones
        self.ui.btn_enviar.clicked.connect(self.enviar)
        
        self.P_1 = self.ui.btn_uno.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_uno))
        
        self.P_2 = self.ui.btn_dos.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_dos))
        
        self.P_3 = self.ui.btn_tres.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_tres))
        
        self.P_4 = self.ui.btn_cuatro.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_cuatro))
        
        self.P_5 = self.ui.btn_cinco.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_cinco))
        
        self.P_6 = self.ui.btn_seis.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_seis))
        
        self.P_7 = self.ui.btn_siete.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_siete))
        
        self.P_8 = self.ui.btn_ocho.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_ocho))
        
        #Escribir el tipo de forma_tipo
        self.ui.btn_uno.clicked.connect(lambda: self.ui.linea_forma_tipo.setText('P-01'))
        self.ui.btn_dos.clicked.connect(lambda: self.ui.linea_forma_tipo.setText('P-02'))
        self.ui.btn_tres.clicked.connect(lambda: self.ui.linea_forma_tipo.setText('P-03'))
        self.ui.btn_cuatro.clicked.connect(lambda: self.ui.linea_forma_tipo.setText('P-04'))
        self.ui.btn_cinco.clicked.connect(lambda: self.ui.linea_forma_tipo.setText('P-05'))
        self.ui.btn_seis.clicked.connect(lambda: self.ui.linea_forma_tipo.setText('P-06'))
        self.ui.btn_siete.clicked.connect(lambda: self.ui.linea_forma_tipo.setText('P-07'))
        self.ui.btn_ocho.clicked.connect(lambda: self.ui.linea_forma_tipo.setText('P-08'))
    
    def enviar(self):
        """Envia datos"""
        self.ui.vacio.setText('')
        num_orden = self.ui.linea_num_orden.text()
        
        if num_orden == (''):
            self.ui.vacio.setText('N° ORDEN REQUERIDO')
            self.ui.btn_enviar.setStyleSheet("color: red;")
        
        else:
    
            dato = self.datos.buscar_orden(num_orden)
                
            if dato != []:
                self.ui.vacio.setText('LA ORDEN EXISTE')
                self.ui.btn_enviar.setStyleSheet("color: red;")
            
            else :
                
                self.guardarPDF()
                url = self.ruta
                valor_vbox = self.ui.VBOX.text()
                valor_hbox = self.ui.HBOX.text()
                valor_puente = self.ui.puente.text()
                forma_tipo = self.ui.linea_forma_tipo.text()
               
                self.datos.inserta_datos(num_orden, forma_tipo, valor_vbox, valor_hbox, valor_puente, url)
                self.ui.signal_enviado.setText('ENVIADO')
                self.ui.btn_enviar.setStyleSheet("color: black;")
                self.ui.vacio.setText('')
                self.ui.stackedWidget.setCurrentWidget(self.ui.INICIO)
                self.ui.linea_num_orden.setText('')
                self.ui.linea_num_orden.setEnabled(False)
			
    def guardar_widget(self, widget, filename):
        """Escribe dentro del PDF"""
        
        escribir = self.ui.linea_num_orden.text()
        vbox = self.ui.VBOX.text()
        hbox = self.ui.HBOX.text()
        puente = self.ui.puente.text()
        
        printer = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.HighResolution)
        printer.setOutputFormat(QtPrintSupport.QPrinter.PdfFormat)
        printer.setOutputFileName(filename)
        
        painter = QtGui.QPainter(printer)
        painter.setFont(QFont("Arial", 14));
        painter.drawText(250, 250, "NUMERO DE ORDEN: " + escribir)
        painter.drawText(250, 550, "HBOX: " + hbox)
        painter.drawText(250, 850, "VBOX: " + vbox)
        painter.drawText(250, 1150, "PUENTE: " + puente)
        
        # inicio de escala
        xscale = printer.pageRect().width() * 1.0 / widget.width()
        yscale = printer.pageRect().height() * 1.0 / widget.height()
        scale = min(xscale, yscale)
        painter.translate(printer.paperRect().center())
        painter.scale(scale, scale)
        painter.translate(-widget.width() / 2, -widget.height() / 2)
        
        # fin de escala
        widget.render(painter)
        painter.end()
        
    def guardarPDF(self):
        """Guardar PDF, abre dialogo"""
        numero = self.ui.linea_num_orden.text()
        fn, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Export PDF","pdfs/" + numero,"PDF files (.pdf);;All Files()")
        
        if fn:
            if QtCore.QFileInfo(fn).suffix() == "":
                fn += ".pdf"
            self.guardar_widget(self.ui.stackedWidget, fn)
        
        self.ruta = fn
		    
    def valor_vertical(self, event):
        """Actualiza valor de VBOX"""
        
        self.grafica1.datos1(event)
        self.grafica2.datos1(event)
        self.grafica3.datos1(event)
        self.grafica4.datos1(event)
        self.grafica5.datos1(event)
        self.grafica6.datos1(event)
        self.grafica7.datos1(event)
        self.grafica8.datos1(event)
        self.grafica9.datos1(event)
        self.grafica10.datos1(event)
        self.grafica11.datos1(event)
        self.grafica12.datos1(event)
        self.grafica13.datos1(event)
        self.grafica14.datos1(event)
        self.grafica15.datos1(event)
        self.grafica16.datos1(event)
        self.actualizar_plot()

    def valor_horizontal(self, event):
        """Actualiza valor de HBOX"""
        
        self.grafica1.datos2(event)
        self.grafica2.datos2(event)
        self.grafica3.datos2(event)
        self.grafica4.datos2(event)
        self.grafica5.datos2(event)
        self.grafica6.datos2(event)
        self.grafica7.datos2(event)
        self.grafica8.datos2(event)
        self.grafica9.datos2(event)
        self.grafica10.datos2(event)
        self.grafica11.datos2(event)
        self.grafica12.datos2(event)
        self.grafica13.datos2(event)
        self.grafica14.datos2(event)
        self.grafica15.datos2(event)
        self.grafica16.datos2(event)
        self.actualizar_plot()

    def actualizar_plot(self):         
        """Actualiza las graficas"""
        
        self.grafica1.grafica_P1()
        self.grafica2.grafica_P1()
        
        self.grafica3.grafica_P2()
        self.grafica4.grafica_P2()
        
        self.grafica5.grafica_P3_izquierdo()
        self.grafica6.grafica_P3_derecho()
        
        self.grafica7.grafica_P4_izquierdo()
        self.grafica8.grafica_P4_derecho()
        
        self.grafica9.grafica_P5_izquierdo()
        self.grafica10.grafica_P5_derecho()
        
        self.grafica11.grafica_P6_izquierdo()
        self.grafica12.grafica_P6_derecho()
        
        self.grafica13.grafica_P7_izquierdo()
        self.grafica14.grafica_P7_derecho()
        
        self.grafica15.grafica_P8()
        self.grafica16.grafica_P8()
        
    
class Canvas_grafica(FigureCanvas):
    """Permite graficar"""
    def __init__(self):
        """Configuracion de inicio"""
        self.fig, self.ax = plt.subplots(facecolor='white')

        super().__init__(self.fig)
        self.ax.margins(x=0)

        '''Para dibujar el plano cartesiano (tipo cruz)'''
        self.ax = plt.gca()  #gca significa 'obtener eje actual'
        
        #Oculta la linea de la caja.
        self.ax.spines['right'].set_color('none')
        self.ax.spines['top'].set_color('none')
        
        # Establece la posición del eje.
        self.ax.xaxis.set_ticks_position('bottom')
        self.ax.yaxis.set_ticks_position('left')
        
        # Establece la posición del eje.
        self.ax.spines['bottom'].set_position(('data', 0))
        self.ax.spines['left'].set_position(('data', 0))
        
        # Color del eje.
        self.ax.spines['bottom'].set_color('gray')
        self.ax.spines['left'].set_color('gray')
        
        # Oculta los valores en los ejes
        self.ax.get_xaxis().set_visible(False) 
        self.ax.get_yaxis().set_visible(False) 
        
        # Valores fijos a los ejes
        self.ax.set_xlim(-10, 10)               
        self.ax.set_ylim(-10, 10)
    
        # Valor inicial.
        self.nivel1 = 4
        self.nivel2 = 4
    
    '''Actualiza el valor a escala (milimetro)'''
    def datos1(self, valor1):
        self.nivel1 = valor1 * 0.1
        
    def datos2(self, valor2):
        self.nivel2 = valor2 * 0.1

    def grafica_P1(self):
        '''Graficar P-01'''
        # self.ax.set_title('Circular = P-1') colocar algun titulo sobre la grafica
        
        angulo = np.linspace(0, 2*np.pi)
        x = self.nivel2 * np.cos(angulo)
        y = self.nivel2 * np.sin(angulo)

        line, = self.ax.plot(x, y, color="red")
        
        self.draw()
        line.set_ydata(np.sin(y) + 24)

    def grafica_P2(self):
        '''Graficar P-02'''
        
        angulo = np.linspace(0, 2*np.pi)
        x = self.nivel2 * np.cos(angulo)
        y = self.nivel1 * np.sin(angulo)

        line, = self.ax.plot(x, y, color="red")

        self.draw()
        line.set_ydata(np.sin(y) + 24)

    def grafica_P3_izquierdo(self):
        '''Graficar P-03'''
        #Valor de x
        x = np.linspace(-1, 1, 1000)

        # Ecuación de la curva superior
        y1 = np.ceil(x**2)*(x/8) + np.tan(1/10-x**12)
        #Ecuación de la curva inferior
        y2 = np.ceil(x**2) - np.cbrt(1 - x**4)

        a = (self.nivel2 * 0.75)
        b = (self.nivel2 * 0.87)

        x1 = self.nivel1 * x
        y3 = a * y1 + b
        y4 = self.nivel2 * y2 - self.nivel2

        #Dibujamos las curvas para cada valor de x, con el color c y anchura lw
        line,  = self.ax.plot(y3, x1, c='red',  lw=1.5)
        line1, = self.ax.plot(y4, x1, c='red', lw=1.5)

        self.draw()

        #Limpia las lineas 
        line.set_ydata(np.sin(y1) + 24)
        line1.set_ydata(np.sin(y1) + 24)

    def grafica_P3_derecho(self):
        '''Graficar P-03'''
        #Valor de x
        x = np.linspace(-1, 1, 1000)

        # Ecuación de la curva superior
        y1 = np.ceil(x**2)*(x/8) + np.tan(1/10-x**12)
        #Ecuación de la curva inferior
        y2 = np.ceil(x**2) - np.cbrt(1 - x**4)

        a = (self.nivel2 * 0.75)
        b = (self.nivel2 * 0.87)

        x1 = self.nivel1 * x
        y3 = a * y1 + b
        y4 = self.nivel2 * y2 - self.nivel2

        #Dibujamos las curvas para cada valor de x, con el color c y anchura lw
        line,  = self.ax.plot(-y3, x1, c='red',  lw=1.5)
        line1, = self.ax.plot(-y4, x1, c='red', lw=1.5)

        self.draw()

        #Limpia las lineas 
        line.set_ydata(np.sin(y1) + 24)
        line1.set_ydata(np.sin(y1) + 24)

    def grafica_P4_izquierdo(self):
        '''Graficar P-04'''
        #Valor de x
        x = np.linspace(-1, 1, 1000)

        # Ecuación de la curva superior
        y1 = np.sqrt(np.sqrt(1-x**2))
        #Ecuación de la curva inferior
        y2 = np.sqrt((np.sin(1-x**7))**2) * (np.sqrt(np.arccos(x**2))) + np.sqrt(1-x**4)
        
        p = self.nivel1*0.49    
        x1 = self.nivel2 * x
        y3 = p * y1 + p
        y4 = (self.nivel1*0.75) * y2 - p
        
        #Dibujamos las curvas para cada valor de x, con el color c y anchura lw
        line,  = self.ax.plot(x1, y3, c='red', lw=1.5)
        line1, = self.ax.plot(x1, -y4, c='red', lw=1.5) 
        self.draw() 
        
        #Limpia las lineas 
        line.set_ydata(np.sin(y1) + 24)
        line1.set_ydata(np.sin(y1) + 24)

    def grafica_P4_derecho(self):
        '''Graficar P-04'''
        #Valor de x
        x = np.linspace(-1, 1, 1000) 
        
        # Ecuación de la curva superior
        y1 = np.sqrt(np.sqrt(1-x**2))  # + np.sqrt(1 - x **4)
        #Ecuación de la curva inferior
        y2 = np.sqrt((np.sin(1-x**7))**2) * (np.sqrt(np.arccos(x**2))) + np.sqrt(1-x**4)   
        
        p = self.nivel1*0.49    
        x1 = self.nivel2 * x
        y3 = p * y1 + p
        y4 = (self.nivel1*0.75) * y2 - p
        
        #Dibujamos las curvas para cada valor de x, con el color c y anchura lw
        line,  = self.ax.plot(x1, y3, c='red', lw=1.5)
        line1, = self.ax.plot(-x1, -y4, c='red', lw=1.5)    
        self.draw() 
        
        #Limpia las lineas 
        line.set_ydata(np.sin(y1) + 24)
        line1.set_ydata(np.sin(y1) + 24)

    def grafica_P5_izquierdo(self):
        '''Graficar P-05'''
        #Valor de x
        x = np.linspace(-1, 1, 1000)    
        
        # Ecuación de la curva superior
        y = np.sqrt(np.sqrt(1-x**2))
        
        # Ecuación de la curva superior
        y1 = np.sqrt((np.sin(1-x**2)))*(np.arccos(x)/4) + 1.15*np.sqrt(1-x**2) 
        
        amplitud = self.nivel1 * 0.5    
        x1 = self.nivel2 * x
        y2 = amplitud * y + amplitud
        y3 = self.nivel1 * y1 - amplitud    
        
        #Dibujamos las curvas para cada valor de x, con el color c y anchura lw
        line,  = self.ax.plot(-x1, y2, c='red', lw=1.5)
        line1, = self.ax.plot(-x1, -y3, c='red', lw=1.5)    
        self.draw() 
        
        #Limpia las lineas 
        line.set_ydata(np.sin(y2) + 24)
        line1.set_ydata(np.sin(y3) + 24)

    def grafica_P5_derecho(self):
        '''Graficar P-05'''
        #Valor de x
        x = np.linspace(-1, 1, 1000)
        
        # Ecuaciones
        y = np.sqrt(np.sqrt(1-x**2))
        y1 = np.sqrt((np.sin(1-x**2)))*(np.arccos(x)/4) + 1.15*np.sqrt(1-x**2)

        amplitud = self.nivel1 * 0.5
        x1 = self.nivel2 * x
        y2 = amplitud * y + amplitud
        y3 = self.nivel1 * y1 - amplitud

        #Dibujamos las curvas para cada valor de x, con el color c y anchura lw
        line,  = self.ax.plot(x1, y2, c='red', lw=1.5)
        line1, = self.ax.plot(x1, -y3, c='red', lw=1.5)

        self.draw()

        #Limpia las lineas 
        line.set_ydata(np.sin(y2) + 24)
        line1.set_ydata(np.sin(y3) + 24)
        
    def grafica_P6_izquierdo(self):
        '''Graficar P-06'''
        #Valor de x
        x = np.linspace(-1, 1, 1000)
        
        # Ecuación de la curva superior
        y = np.sin(1-x**3)*(x/3) + np.sqrt(5/4*np.tan(1-x**12))
        #Ecuación de la curva inferior
        y1 = np.sqrt(np.cbrt(1-x**4))

        a = self.nivel2 * 0.5
        b = self.nivel2 + a
        c = self.nivel2 * 0.33
        

        x1 = self.nivel1 * x
        y2 = c * y + a
        y3 = b * y1 - a

        #Dibujamos las curvas para cada valor de x, con el color c y anchura lw
        line,  = self.ax.plot(y2, x1, c='red', lw=1.5)
        line1, = self.ax.plot(-y3, x1, c='red', lw=1.5)

        self.draw()

        #Limpia las lineas 
        line.set_ydata(np.sin(y2) + 24)
        line1.set_ydata(np.sin(y3) + 24)
        
    def grafica_P6_derecho(self):
        '''Graficar P-06'''
        #Valor de x
        x = np.linspace(-1, 1, 1000)
        
        # Ecuación de la curva superior
        y = np.sin(1-x**3)*(x/3) + np.sqrt(5/4*np.tan(1-x**12))
        #Ecuación de la curva inferior
        y1 = np.sqrt(np.cbrt(1-x**4))

        a = self.nivel2 * 0.5
        b = self.nivel2 + a
        c = self.nivel2 * 0.33

        x1 = self.nivel1 * x
        y2 = c * y + a
        y3 = b * y1 - a

        #Dibujamos las curvas para cada valor de x, con el color c y anchura lw
        line,  = self.ax.plot(-y2, x1, c='red', lw=1.5)
        line1, = self.ax.plot(y3, x1, c='red', lw=1.5)

        self.draw()

        #Limpia las lineas 
        line.set_ydata(np.sin(y2) + 24)
        line1.set_ydata(np.sin(y3) + 24)
        
    def grafica_P7_izquierdo(self):
        '''Graficar P-07'''
        #Valor de x
        x = np.linspace(-1, 1, 1000)
        
        # Ecuaciones
        y = np.sqrt(np.sin(1-x**2))        
        y1 = (np.sqrt(1-x**2))*(np.arccos(x/2))/5 + np.sqrt(1-x**2)*(2/3)
        
        a = self.nivel1 * 0.825
        b = self.nivel1 * 0.25
        c = self.nivel1 + b

        x1 = self.nivel2 * x
        y2 = a * y + b
        y3 = c * y1 - b

        #Dibujamos las curvas para cada valor de x, con el color c y anchura lw
        line,  = self.ax.plot(x1,y2, c='red', lw=1.5)
        line1, = self.ax.plot(x1,-y3, c='red', lw=1.5)

        self.draw()

        #Limpia las lineas 
        line.set_ydata(np.sin(y2) + 24)
        line1.set_ydata(np.sin(y3) + 24)
        
    def grafica_P7_derecho(self):
        '''Graficar P-07'''
        #Valor de x
        x = np.linspace(-1, 1, 1000)
        
        # Ecuaciones
        y = np.sqrt(np.sin(1-x**2))
        y1 = (np.sqrt(1-x**2))*(np.arccos(x/2))/5 + np.sqrt(1-x**2)*(2/3)

        a = self.nivel1 * 0.825
        b = self.nivel1 * 0.25
        c = self.nivel1 + b

        x1 = self.nivel2 * x
        y2 = a * y + b
        y3 = c * y1 - b

        #Dibujamos las curvas para cada valor de x, con el color c y anchura lw
        line,  = self.ax.plot(-x1, y2, c='red', lw=1.5)
        line1, = self.ax.plot(-x1, -y3, c='red', lw=1.5)

        self.draw()

        #Limpia las lineas 
        line.set_ydata(np.sin(y2) + 24)
        line1.set_ydata(np.sin(y3) + 24)
        
    def grafica_P8(self):
        '''Graficar P-08'''
        
        #Valor de x
        x = np.linspace(-1, 1, 1000)
        
        #Ecuaciones
        y = np.sqrt(4/3*np.sin(1-x**2))
        y1 = (np.sqrt(1-x**2))*(np.arccos(x**2)/5) + np.sqrt(1-x**2)*(2/3)
        
        a = self.nivel1 * 0.50
        b = self.nivel1 + a

        x1 = self.nivel2 * x
        y2 = a * y + a
        y3 = b * y1 - a

        #Dibujamos las curvas para cada valor de x, con el color c y anchura lw
        line,  = self.ax.plot(x1, y2, c='red', lw=1.5)
        line1, = self.ax.plot(x1, -y3, c='red', lw=1.5)

        self.draw()

        #Limpia las lineas.
        line.set_ydata(np.sin(y2) + 24)
        line1.set_ydata(np.sin(y3) + 24)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # Creo mi aplicación
    mi_app = MiApp()
    # mi_app.resize(800, 600)               #Dimensiona la venta.
    mi_app.show()
    sys.exit(app.exec_())  # Ejecuto mi aplicación.
