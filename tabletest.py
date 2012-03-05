'''
Created on Mar 4, 2012

@author: arif
'''

import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle('Table Test')
        self.main_widget = QWidget(self)
        
        layout = QVBoxLayout(self.main_widget)
        
        self.table = QTableWidget(1, 2, parent=self.main_widget)
        self.table.setHorizontalHeaderLabels(['Direction', 'Speed'])
        h = self.table.horizontalHeader()
        h.setResizeMode(QHeaderView.Stretch)
        
        self.btn_process = QPushButton('process', self.main_widget)
        self.btn_add_row = QPushButton('add row', self.main_widget)
        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.btn_add_row)
        btn_layout.addWidget(self.btn_process)
        
        self.connect(self.btn_process, SIGNAL('clicked()'), self.process_table)
        self.connect(self.btn_add_row, SIGNAL('clicked()'), self.add_row)
        
        layout.addWidget(self.table)
        layout.addLayout(btn_layout)
        
        # set the focus on the main widget
        self.main_widget.setFocus()
        
        # set the central widget of MainWindow to main_widget
        self.setCentralWidget(self.main_widget)

    def process_table(self):
        rows = self.table.rowCount()
        columns = self.table.columnCount()
        print 'row:', rows
        print 'column:', columns
        for row in xrange(rows):
            for column in xrange(columns):
                item = self.table.item(row, column)
                textdata = None
                if item is not None:
                    textdata = item.text()
                print row, column, ':', textdata
        
    def add_row(self):
        print 'add row'
        self.table.setRowCount(self.table.rowCount() + 1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
    