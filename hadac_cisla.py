# nápad na projekt z tohoto webu: https://www.itnetwork.cz/python/formulare/resene-ulohy-pyqt-zakladni-ovladaci-prvky-obsluha-udalosti
# (Pouze inspirace grafickou stránkou projektu)
from PyQt5 import QtCore, QtGui, QtWidgets
import random
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        # Deklarace proměnných
        self.maximum = 0
        self.hadaneCislo = 0
        self.pocetPokusu = 0
        self.mojeTipy = []

        # Kód vytvořený designerem (program na vytváření GUI)
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(632, 217)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setWindowIcon(QtGui.QIcon("icon.png"))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 91, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 41, 31))
        self.label_2.setObjectName("label_2")
        self.rozsah_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.rozsah_comboBox.setGeometry(QtCore.QRect(50, 50, 271, 31))
        self.rozsah_comboBox.setToolTipDuration(-3)
        self.rozsah_comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.rozsah_comboBox.setEditable(False)
        self.rozsah_comboBox.setMaxVisibleItems(10)
        self.rozsah_comboBox.setMaxCount(100)
        self.rozsah_comboBox.setObjectName("rozsah_comboBox")
        self.zacit_button = QtWidgets.QPushButton(self.centralwidget)
        self.zacit_button.setGeometry(QtCore.QRect(340, 50, 281, 31))
        self.zacit_button.setObjectName("zacit_button")
        self.tipnout_button = QtWidgets.QPushButton(self.centralwidget)
        self.tipnout_button.setGeometry(QtCore.QRect(340, 90, 281, 31))
        self.tipnout_button.setObjectName("tipnout_button")
        self.zadaneCislo_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.zadaneCislo_spinBox.setGeometry(QtCore.QRect(30, 90, 291, 31))
        self.zadaneCislo_spinBox.setMaximum(100)
        self.zadaneCislo_spinBox.setObjectName("zadaneCislo_spinBox")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 140, 611, 21))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 632, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Vypnutí komponent, aby uživatel nemohl tipovat bez zadání rozmezí
        self.tipnout_button.setEnabled(False)
        self.zadaneCislo_spinBox.setEnabled(False)

        # Naplnění ComboBoxu čísly
        for i in range(100):
            i += 1
            if i % 10 == 0:
                self.rozsah_comboBox.addItem(str(i))

        # Přidání ikon a přidělení funkcí k tlačítkům
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.zacit_button.clicked.connect(self.zacit)
        self.tipnout_button.clicked.connect(self.hadani)
        self.zacit_button.setIcon(QtGui.QIcon("start.png"))
        self.zacit_button.setIconSize(QtCore.QSize(32,32))
        self.tipnout_button.setIcon(QtGui.QIcon("guess.png"))
        self.tipnout_button.setIconSize(QtCore.QSize(28, 28))

    # Funkce která zahájí program, a vybere náhodné číslo v daném rozmezí
    def zacit(self):
        self.maximum = int(self.rozsah_comboBox.currentText())
        self.hadaneCislo = random.randint(1, self.maximum)
        self.label_3.setText("Bylo vybráno číslo, zkus ho tipnout!")
        # Aktivace komponent, aby uživatel mohl začít hádat
        self.tipnout_button.setEnabled(True)
        self.zadaneCislo_spinBox.setEnabled(True)

    # Funkce, která sleduje počet pokusů, všechny předchozí tipy uživatele a vyhodnocení výsledku
    def hadani(self):
        self.pocetPokusu += 1
        self.mojeTipy.append(self.zadaneCislo_spinBox.value())
        # Pokud uživatel trefí číslo, otevře se dialog s výsledkem
        if self.zadaneCislo_spinBox.value() == self.hadaneCislo:
            self.konecDialog()
        # Pokud uživatel zadá větší hodnotu
        elif self.zadaneCislo_spinBox.value() > self.hadaneCislo:
            self.label_3.setText("Hledané číslo je menší!")
        # Pokud uživatel zadá menší hodnotu
        else:
            self.label_3.setText("Hledané číslo je větší!")

    # Dialog, který se objeví, pokud uživatel uhádne číslo
    def konecDialog(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("UHODL JSI!\n"
                       "Číslo: " + str(self.hadaneCislo) + " jsi uhodl na " + str(self.pocetPokusu)+ ". pokus\n"
                        "Tvé tipy: " + str(self.mojeTipy))
        msgBox.setWindowTitle("Gratuluji")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Close)

        returnValue = msgBox.exec()
        # Pokud uživatel zmáčkne OK, program se restartuje a můžeme hádat znovu
        if returnValue == QMessageBox.Ok:
            self.tipnout_button.setEnabled(False)
            self.zadaneCislo_spinBox.setEnabled(False)
            self.maximum = 0
            self.hadaneCislo = 0
            self.pocetPokusu = 0
            self.label_3.setText("Zadej rozsah a klikni na začít")
            self.zadaneCislo_spinBox.setValue(0)
            self.mojeTipy.clear()

        # pokud uživatel znáčkne CLOSE, program se ukončí
        if returnValue == QMessageBox.Close:
            sys.exit(app.exec_())

    # Kód vytvořený designerem
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hadej cislo"))
        self.label.setText(_translate("MainWindow", "Rozsah:"))
        self.label_2.setText(_translate("MainWindow", "0  -"))
        self.rozsah_comboBox.setCurrentText(_translate("MainWindow", "10"))
        self.zacit_button.setText(_translate("MainWindow", "Začít"))
        self.tipnout_button.setText(_translate("MainWindow", "Tipnout"))
        self.label_3.setText(_translate("MainWindow", "Zadej rozsah a klikni na začít"))

# Kód vytvořený designerem, spouští grafickou část programu
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
