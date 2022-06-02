import sys
from tkinter import *

from PyQt5.QtWidgets import QStyleFactory, QApplication
from PyQt5 import QtWidgets

from main import *

class Table_odbiorcy:

    def __init__(self, root, txt,l_dos,l_odb):

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

    def __init__(self, root, txt,l_dos,l_odb):

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

    def __init__(self, root, txt,l_dos,l_odb):

        total_rows = l_dos+1
        total_columns = l_odb+1

        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(root, width=10, fg='blue',
                               font=('Arial', 16, 'bold'))

                self.e.grid(row=i+3, column=j+6)
                if (i == 0 and j>0):
                    self.e.insert(END, "O"+str(j))
                elif (j == 0 and i>0):
                    self.e.insert(END, "D"+str(i))
                elif (i!=0 and j!=0):
                    txt.append(self.e)

def get_data(l_dos,l_odb):
    txt_odbiorcy=[]
    txt_dostawcy=[]
    txt_transport=[]
    root=Tk()
    t1=Table_odbiorcy(root,txt_odbiorcy,l_dos,l_odb)
    t2=Table_dostawcy(root,txt_dostawcy,l_dos,l_odb)
    t3=Table_koszty_transportu(root,txt_transport,l_dos,l_odb)

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
            while (i < len(txt_odbiorcy)/2):
                buyers.append(int(txt_odbiorcy[i*2].get()))
                popyt+=buyers[i]
                i+=1

            i=0
            #dostawcy
            podaz=0
            while (i < len(txt_dostawcy)/2):
                sellers.append(int(txt_dostawcy[i*2].get()))
                podaz+=sellers[i]
                i+=1
            sellers.append(popyt)
            buyers.append(podaz)

            #transport
            i=0
            while (i < len(txt_dostawcy)/2):
                temp = []
                while (j < len(txt_odbiorcy)/2):
                    temp.append(int(txt_odbiorcy[j*2+1].get())-int(txt_transport[j+i*l_odb].get())-int(txt_dostawcy[i*2+1].get()))
                    j+=1
                    #print(len(txt_odbiorcy), j, i, temp)
                temp.append(0)
                #print(temp)
                earnings.append(temp)
                j=0
                i+=1
            j=0
            temp = []
            while (j < len(txt_odbiorcy)+2):
                temp.append(0)
                j+=2
            earnings.append(temp)







            #app = QApplication(sys.argv)
            #app.aboutToQuit.connect(app.deleteLater)
            #app.setStyle(QStyleFactory.create("gtk"))
            #screen = PrettyWidget(events, activities)
            #screen.show()
            #app.exec_()
            e = np.copy(earnings)
            tab = calculate_total(sellers, buyers, earnings, e)
            print('wynik:')
            print("====================================")
            print(np.transpose(np.matrix(tab)))
            #(tab)
        else:
            app = QApplication([])
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage(err)
            app.exec_()

    btn = Button(root, text="Zatwierdź", command=clicked)
    btn.grid(column=8, row=l_odb+l_dos+2)
    root.mainloop()


def step1():
    root=Tk()

    def clicked():
        l_odb=int(txt_odb.get("1.0", "end-1c"))
        l_dos=int(txt_dos.get("1.0", "end-1c"))
        print(l_dos,l_odb)

        #app = QApplication(sys.argv)
        #app.aboutToQuit.connect(app.deleteLater)
        #app.setStyle(QStyleFactory.create("gtk"))
        #app.exec_()
        get_data(l_dos,l_odb)

    label1 = Label(text="Liczba odbiorców =")
    txt_odb = Text(root, width=5, height=1)
    label2 = Label(text="Liczba dostawców =")
    txt_dos = Text(root, width=5, height=1)
    btn = Button(root, text="Zatwierdź", command=clicked)

    label1.grid(column=1, row=1)
    txt_odb.grid(column=2, row=1)
    label2.grid(column=1, row=2)
    txt_dos.grid(column=2, row=2)
    btn.grid(column=1, row=3)
    root.mainloop()

#get_data()
step1()