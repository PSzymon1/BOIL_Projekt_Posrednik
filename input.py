import sys

from PyQt5.QtCore import pyqtSlot, QSize
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets

from main import *


class Table_odbiorcy(QTableWidget):

    def __init__(self,l_dos,l_odb):


        lst = [("Odbiorca", 'Popyt', 'Cena')]

        total_rows = l_odb+1
        total_columns = 3
        QTableWidget.__init__(self, total_rows, total_columns)
        self.setMinimumSize(QSize(350, 200))
        self.setWindowTitle("Odbiorcy")
        self.table=[]

        for i in range(total_rows):
            temp=[]
            for j in range(total_columns):
                self.e = QLineEdit()
                self.e.resize(100,32)
                if (i == 0):
                    self.e.setText(lst[i][j])
                    self.setCellWidget(i,j,self.e)
                elif (j==0):
                    self.e.setText("O"+str(i))
                    self.setCellWidget(i, j, self.e)
                elif (i != 0 and j != 0):
                    self.setCellWidget(i,j,self.e)
                    temp.append(self.e)
            self.table.append(temp)


class Table_dostawcy(QTableWidget):

    def __init__(self,l_dos,l_odb):


        lst = [("Dostawca", 'Podaż', 'Koszt')]

        total_rows = l_dos+1
        total_columns = 3
        QTableWidget.__init__(self, total_rows, total_columns)
        self.setMinimumSize(QSize(350, 200))
        self.setWindowTitle("Dostawcy")
        self.table = []

        for i in range(total_rows):
            temp=[]
            for j in range(total_columns):
                self.e = QLineEdit()
                self.e.resize(100,32)
                if (i == 0):
                    self.e.setText(lst[i][j])
                    self.setCellWidget(i,j,self.e)
                elif (j==0):
                    self.e.setText("D"+str(i))
                    self.setCellWidget(i, j, self.e)
                elif (i != 0 and j != 0):
                    self.setCellWidget(i,j,self.e)
                    temp.append(self.e)
            self.table.append(temp)

class Table_koszty_transportu(QTableWidget):

    def __init__(self, l_dos, l_odb):

        total_rows = l_dos + 1
        total_columns = l_odb + 1
        QTableWidget.__init__(self, total_rows, total_columns)
        self.setMinimumSize(QSize(500, 500))
        self.setWindowTitle("Transport")
        self.table = []

        for i in range(total_rows):
            temp = []
            for j in range(total_columns):
                self.e = QLineEdit()
                self.e.resize(100, 32)
                if (i == 0 and j > 0):
                    self.e.setText("O" + str(j))
                    self.setCellWidget(i, j, self.e)
                elif (j == 0 and i > 0):
                    self.e.setText("D" + str(i))
                    self.setCellWidget(i, j, self.e)
                elif (i != 0 and j != 0):
                    self.setCellWidget(i,j,self.e)
                    temp.append(self.e)
            self.table.append(temp)

class GetData(QWidget):

    def __init__(self,l_odb,l_dos):
        super().__init__()
        self.setMinimumSize(QSize(620, 440))
        self.setWindowTitle("Podaj dane")
        self.l_odb=l_odb
        self.l_dos=l_dos

        tab1hbox = QHBoxLayout()
        tab1hbox.setContentsMargins(5, 5, 5, 5)

        self.table_odbiorcy= Table_odbiorcy(l_dos,l_odb)
        tab1hbox.addWidget(self.table_odbiorcy)
        self.table_dostawcy = Table_dostawcy(l_dos, l_odb)
        tab1hbox.addWidget(self.table_dostawcy)
        self.table_transport = Table_koszty_transportu(l_dos, l_odb)
        tab1hbox.addWidget(self.table_transport)

        self.pybutton = QPushButton('Zatwierdź', self)
        self.pybutton.clicked.connect(self.on_click)
        self.pybutton.resize(200, 32)

        mainLayout = QGridLayout()
        mainLayout.addLayout(tab1hbox,0,0)
        mainLayout.addWidget(self.pybutton,1,0)
        self.setLayout(mainLayout)

    def on_click(self):
        sellers = []
        buyers = []
        earnings = []
        valid = 1
        i = 1
        j = 0
        if valid == 1:
            print(buyers)
            print(sellers)
            print(earnings)
            # odbiorcy
            popyt = 0
            while i<self.l_odb+1:
                buyers.append(int(self.table_odbiorcy.table[i][0].text()))
                popyt+=buyers[i-1]
                i+=1
            i = 1
            print(buyers)
            print(sellers)
            print(earnings)
            # dostawcy
            podaz = 0
            while(i<self.l_dos+1):
                sellers.append(int(self.table_dostawcy.table[i][0].text()))
                podaz += sellers[i-1]
                i += 1

            sellers.append(popyt)
            buyers.append(podaz)
            print(buyers)
            print(sellers)
            print(earnings)
            # transport
            i=1
            while (j < self.l_odb):
                temp=[]
                while(i < self.l_dos+1):
                    temp.append(int(self.table_odbiorcy.table[j+1][1].text())-int(self.table_transport.table[i][j].text())-int(self.table_dostawcy.table[i][1].text()))
                    i+=1
                temp.append(0)
                earnings.append(temp)
                i=1
                j+=1
            j=0
            temp=[]
            while(j<self.l_dos+1):
                temp.append(0)
                j+=1
            earnings.append(temp)

            print(buyers)
            print(sellers)
            print(earnings)

            e = np.copy(earnings)
            tab = calculate_total(sellers, buyers, earnings, e)
            print('wynik:')
            print("====================================")
            print(np.transpose(np.matrix(tab)))
            data = np.transpose(np.matrix(tab))
            self.w = MainWindow(data, e)
            self.w.show()
        else:
            QMessageBox.about(self, "Error", "Niepoprawne wartości!")




class Step1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w = None
        self.setMinimumSize(QSize(320, 140))
        self.setWindowTitle("Podaj dane")

        self.Label1 = QLabel(self)
        self.Label1.setText('Liczba odbiorców =')
        self.line1 = QLineEdit(self)

        self.line1.move(150, 20)
        self.line1.resize(50, 32)
        self.Label1.move(20, 20)

        self.Label2 = QLabel(self)
        self.Label2.setText('Liczba dostawców =')
        self.line2 = QLineEdit(self)

        self.line2.move(150, 60)
        self.line2.resize(50, 32)
        self.Label2.move(20, 60)

        pybutton = QPushButton('Zatwierdź', self)
        pybutton.clicked.connect(self.on_click)
        pybutton.resize(200, 32)
        pybutton.move(60, 100)

        self.show()


    def on_click(self):
        l_odb = int(self.line1.text())
        l_dos = int(self.line2.text())
        print(l_odb, l_dos)
        if (l_odb > 0 and l_dos > 0 and l_odb < 10 and l_dos < 10):
            self.w = GetData(l_odb, l_dos)
            self.w.show()
        else:
            QMessageBox.about(self, "Error", "Niepoprawne wartości!")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    screen = Step1()
    app.exec_()
