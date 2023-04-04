import sys
import re
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox


class PatternChecker(QWidget):
    def __init__(self):
        super().__init__()

        # creăm interfața grafică
        self.initUI()

    def initUI(self):
        # creăm etichetele pentru introducerea modelului și șirului
        self.patternLabel = QLabel('Model:', self)
        self.patternLabel.move(20, 20)
        self.stringLabel = QLabel('Șir:', self)
        self.stringLabel.move(20, 60)

        # creăm câmpurile de introducere pentru model și șir
        self.patternEdit = QLineEdit(self)
        self.patternEdit.move(80, 20)
        self.stringEdit = QLineEdit(self)
        self.stringEdit.move(80, 60)

        # creăm butonul de verificare
        self.checkButton = QPushButton('Verifică', self)
        self.checkButton.move(20, 100)
        self.checkButton.clicked.connect(self.checkPattern)

        # setăm dimensiunile ferestrei și titlul
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Verificare Model')
        self.show()

    def checkPattern(self):
        # obținem modelul și șirul introduse de utilizator
        pattern = self.patternEdit.text()
        string = self.stringEdit.text()

        # verificăm dacă modelul și șirul sunt goale
        if not pattern or not string:
            QMessageBox.warning(self, 'Eroare', 'Introduceți un model și un șir pentru a verifica')
            return

        # verificăm dacă modelul este valid
        try:
            re.compile(pattern)
        except re.error:
            QMessageBox.warning(self, 'Eroare', 'Modelul introdus este invalid')
            return

        # verificăm dacă șirul respectă modelul
        if re.match(pattern, string):
            QMessageBox.information(self, 'Rezultat', 'Șirul respectă modelul')
        else:
            QMessageBox.information(self, 'Rezultat', 'Șirul nu respectă modelul')


if __name__ == '__main__':
    # creăm o aplicație PyQt5
    app = QApplication(sys.argv)

    # creăm o instanță a clasei noastre de verificare a modelului
    patternChecker = PatternChecker()

    # rulăm aplicația
    sys.exit(app.exec_())