# Only needed for access to command line arguments
import sys

import random

from PyQt5 import QtCore

# We import the PyQt5 classes that we need for the application
# from the QtWidgets module
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
)


###############
# MAIN WINDOW #
###############
# This is a pre-made widget which provides a lot of standard window 
# features you’ll make use of in your apps, including toolbars, menus, 
# a statusbar, dockable widgets and more.
class MainWindow(QMainWindow):
    def __init__(self):
        """!
        @brief Init MainWindow.
        """
        # If you want to create a custom window, the best approach is 
        # to subclass QMainWindow and then include the setup for the 
        # window in this __init__ block.

        super(MainWindow, self).__init__()

        # title and geometry
        self.setWindowTitle("GUI")
        width = 300
        height = 250
        self.setMinimumSize(width, height)

        self.initUI()

    #####################
    # GRAPHIC INTERFACE #
    #####################
    def initUI(self):
        """!
        @brief Set up the graphical interface structure.
        """
        # ******* DEFINIZIONE BOTTONI **********
        self.plus_btn = QPushButton(
            text="+1",
            clicked=self.add_one # METODO 1 per COLLEGARE CLICK e SELF
                                 # clicked segnale che viene generato alla pressione del pulsante
                                 # add one è lo slot che tiene i dati generati dal segnale 
                                 # NB sintassi non richiede l'utilizzo delle parentesi tonde 
        )
        # METODO 2 per COLLEGARE CLICK e SELF
        # usato nel caso in cui abbiamo bisogno di passare anche dei dati
        # self.plus_btn.clicked.connect(self.add_one)
        self.minus_btn = QPushButton(
            text="-1",
            clicked=self.remove_one
        )
        # alternatively, signals can be connected in this way
        # self.plus_btn.clicked.connect(self.add_one)
        
        # ********* DEFINIZIONE ETICHETTA **********
        self.label_number = int(random.random()*100)
        self.display_label = QLabel(
            str(self.label_number), #testo da visualizzare, numero dato in precedenza 
            alignment=QtCore.Qt.AlignCenter
        )
        
        
        ############### ho creato gli oggetti ma non sono "da nessuna parte" -> diamo un layout all'applicazione

        # ****** DEFINIZIONE LAYOUT ******** 
        # funziona ad "inscatolamento" dei singoli elementi 
        
        button_hlay = QHBoxLayout() #horizontal box layout 
        button_hlay.addWidget(self.plus_btn) # da sinistra a destra 
        button_hlay.addWidget(self.minus_btn)
        vlay = QVBoxLayout() # vertical box layout
        vlay.addLayout(button_hlay) # ci aggiungo il layout orizzontale sopra con i due pulsanti 
        vlay.addWidget(self.display_label)
        widget = QWidget() # per sintassi di pyqp non è sufficiente, devo CREARE UN WIDGET VUOTO a cui ASSEGNARE il LAYOUT FINALE
        widget.setLayout(vlay)
        #.setCentralWidget is a QMainWindow specific function that 
        # allows you to set the widget that goes in the middle of the window.
        self.setCentralWidget(widget)  # metto il widget come CentralWidget 

    def add_one(self):
        """!
        @brief Add 1 to the number displayed in the label.
        """
        self.label_number = self.label_number+1
        self.display_label.setText(str(self.label_number))

    def remove_one(self):
        """!
        @brief Subtract 1 to the number displayed in the label.
        """
        self.label_number = self.label_number-1
        self.display_label.setText(str(self.label_number))


#############
#  RUN APP  #
#############
if __name__ == '__main__':
    # You need one (and only one) QApplication instance per application.
    # Pass in sys.argv to allow command line arguments for your app.
    # If you know you won't use command line arguments QApplication([])
    # works too.
    app = QApplication(sys.argv) #app è uniistanza della classe QApplication 
    # Create a Qt widget, which will be our window.
    w = MainWindow()
    w.show() # ******* IMPORTANT!!!!! Windows are hidden by default*******
    # show è definita in QMainWindow,q quindi ho già i suoi attriuti pche ho ereditato  
    # Start the event loop.
    sys.exit(app.exec_()) ## comando che "migliora" l'esecuzione dell'applicazione 

    # Your application won't reach here until you exit and the event
    # loop has stopped.