import sys
from tkinter import *

from PyQt5.QtWidgets import QStyleFactory, QApplication
from PyQt5 import QtWidgets

from main import *

l_odb=3;
l_dos=3;

class Table_odbiorcy:

    def __init__(self, root, txt):

        lst = [("Odbiorca", 'Popyt', 'Cena')]

        total_rows = l_odb+1
        total_columns = 3

        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(root, width=10, fg='blue',
                               font=('Arial', 16, 'bold'))

                self.e.grid(row=i, column=j)
                if (i == 0):
                    self.e.insert(END, lst[i][j])
                elif (j==0):
                    self.e.insert(END, "O"+str(i))
                else:
                    txt.append(self.e)

class Table_dostawcy:

    def __init__(self, root, txt):

        lst = [("Dostawca", 'Podaż', 'Koszt')]

        total_rows = l_dos+1
        total_columns = 3

        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(root, width=10, fg='blue',
                               font=('Arial', 16, 'bold'))

                self.e.grid(row=i+l_odb+2, column=j)
                if (i == 0):
                    self.e.insert(END, lst[i][j])
                elif (j==0):
                    self.e.insert(END, "D"+str(i))
                else:
                    txt.append(self.e)

class Table_koszty_transportu:

    def __init__(self, root, txt):

        total_rows = l_dos+1
        total_columns = l_odb+1

        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(root, width=10, fg='blue',
                               font=('Arial', 16, 'bold'))

                self.e.grid(row=i+3, column=j+6)
                if (i == 0 and j>0):
                    self.e.insert(END, "O"+str(j))
                elif (j == 0):
                    self.e.insert(END, "D"+str(i))
                else:
                    txt.append(self.e)

def get_data():
    txt_odbiorcy=[]
    txt_dostawcy=[]
    txt_transport=[]
    root=Tk()
    t1=Table_odbiorcy(root,txt_odbiorcy)
    t2=Table_dostawcy(root,txt_dostawcy)
    t3=Table_koszty_transportu(root,txt_transport)

    def clicked():
        sellers = []
        buyers = []
        earnings = []
        valid=1
        err=''
        i=0
        j=0
        if valid==1:
            #odbiorcy
            popyt=0
            while (i < len(txt_odbiorcy)):
                buyers[i]=int(txt_odbiorcy[i].get())
                popyt+=buyers[i]
                i+=2
            buyers[i]=popyt

            #dostawcy
            podaz=0
            while (i < len(txt_dostawcy)):
                sellers[i] = int(txt_dostawcy[i].get())
                podaz+=sellers[i]
                i+=2
            sellers[i]=podaz

            #transport
            i=0
            temp=[]
            while (i < len(txt_dostawcy)):
                while (j < len(txt_odbiorcy)):
                    temp[j]=int(txt_odbiorcy[i+1])-int(txt_transport[j+i*len(txt_odbiorcy)].get())-int(txt_dostawcy[j+1])
                    j+=2
                earnings[i]=temp
                temp=[]
                i+=2




            app = QApplication(sys.argv)
            app.aboutToQuit.connect(app.deleteLater)
            app.setStyle(QStyleFactory.create("gtk"))
            #screen = PrettyWidget(events, activities)
            #screen.show()
            app.exec_()
        else:
            app = QApplication([])
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage(err)
            app.exec_()

    btn = Button(root, text="Zatwierdź", command=clicked)
    btn.grid(column=8, row=l_odb+l_dos+2)
    root.mainloop()

#get_data()