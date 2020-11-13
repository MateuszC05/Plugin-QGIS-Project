
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget,QLineEdit,\
    QPushButton, QHBoxLayout,QLabel, QGridLayout, QTableWidget,QListWidgetItem
from PyQt5.QtGui import QIcon
import psycopg2
import sys
import functools 
import operator
import re 




class database_finder(QWidget):
    
    
    def __init__(self, parent=None):
        super().__init__(parent)

        self.interfejs()
        
        self.SERVER_NAME = '*****';
        self.DATABASE_NAME = '******';
        self.USERNAME = '*****';
        self.PASSWORD = '*****';
    
    
    
    def create_connection(self):
        self.conn = psycopg2.connect(
    dbname = self.DATABASE_NAME,
    user= self.USERNAME,
    host = self.SERVER_NAME,
    password = self.PASSWORD
    )
        self.tables = []
        self.cur = self.conn.cursor()
    
    
    
    
    def odczytaj_wart(self):
        self.input_cit = self.miastoEdt.displayText()
        self.input_ul = self.ulicaEdt.displayText()
        self.input_nmbr = self.nrdomuEdt.displayText() 
        self.szukaj_wart() 
 
    
    def szukaj_wart(self):
        
        if self.wynikEdt.count() > 0:
            self.wynikEdt.clear()
              
        
        self.create_connection()
        self.cur.execute("SELECT *******"  
                     .format(self.input_cit, self.input_ul, self.input_nmbr))
        dane = self.cur.fetchall()
        print(dane) 
        for rekord in dane:
            wynik = "{} {} {} {}".format(rekord[0], rekord[1], rekord[2], rekord[3])
            self.tables.append(wynik)
            print(wynik)
        
        self.conn.close()
        self.wynikEdt.addItems(self.tables)
        
        
    
    def convert_tuple(tup):
        str = functools.reduce(operator.add, (tup))
        return str
    
    
    
    def interfejs(self):
        
        self.resize(630, 300)
         #etykiety
        self.et1 = QLabel("Miasto:", self)
        self.et2 = QLabel("Ulica:", self)
        self.et3 = QLabel('Numer Domu:', self)
        self.et4 = QLabel('Wynik', self)

        
#        przypisanie do ukld tbl
        ukladT = QGridLayout()
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(4)
        self.et1.move(12,55)
        self.et1.adjustSize()
        self.et2.move(135, 55)
        self.et2.adjustSize()
        self.et3.move(258, 55)
        self.et3.adjustSize()
        self.et4.move(485,180)
        self.et4.adjustSize()

        #widzety
        
        #linowe pola edycyjne
        
        self.miastoEdt = QLineEdit()
        self.ulicaEdt = QLineEdit()
        self.nrdomuEdt = QLineEdit()
        self.wynikEdt =QListWidget()
        self.wynikEdt.readonly = True
        self.wynikEdt.setToolTip('Wpisz <b>dane</b> i wybierz szukaj')
        ukladT.addWidget(self.miastoEdt, 1,0)
        ukladT.addWidget(self.ulicaEdt, 1, 1)
        ukladT.addWidget(self.nrdomuEdt, 1, 2)
        ukladT.addWidget(self.wynikEdt, 1, 3)        
        #przycisk def
        szukajBtn = QPushButton("&Szukaj", self)
        koniecBtn = QPushButton("&Koniec", self)
        pokazBtn = QPushButton('&Pokaż na mapie', self)
        koniecBtn.resize(koniecBtn.sizeHint())
        

        #przyciskadd
        ukladBtn = QHBoxLayout()
        ukladBtn.addWidget(szukajBtn)
        ukladT.addLayout(ukladBtn, 2,1,6,1)
        ukladT.addWidget(koniecBtn, 2,1,22,1) 
        ukladT.addWidget(pokazBtn, 2,1,14,1)
        #przypis do okna
        self.setLayout(ukladT)
        koniecBtn.clicked.connect(self.koniec)
        szukajBtn.clicked.connect(self.odczytaj_wart)
        pokazBtn.clicked.connect(self.selected)
        self.setWindowIcon(QIcon('finder.png'))
        self.setWindowTitle('Data_base_finder')
        width = 630
        height = 300
        self.setFixedSize(width,height)
        self.show()
                
    def koniec(self):
        self.close()
        
    
    def selected(self):
        wybrane = self.wynikEdt.selectedItems()
        item_id = wybrane[0]
        xx = item_id.text()
        r1 = re.findall(r"\d*\b",xx)
        print(r1[0])

okno = database_finder()
#if __name__ == '__main__':

   # app = QApplication(sys.argv)



        





    



