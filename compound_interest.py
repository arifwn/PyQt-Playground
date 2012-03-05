'''
Created on Mar 2, 2012

@author: arif

Calculate compound interest
'''

import sys

from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QDialog, QLabel, QSpinBox, QDoubleSpinBox, QGridLayout
from PyQt4.QtGui import QApplication


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        
        self.label_amount = QLabel('Amount')
        self.spin_amount = QDoubleSpinBox()
        self.spin_amount.setRange(0, 10000000000)
        self.spin_amount.setPrefix('Rp. ')
        self.spin_amount.setSingleStep(100000)
        
        self.label_rate = QLabel('Rate')
        self.spin_rate = QDoubleSpinBox()
        self.spin_rate.setSuffix(' %')
        self.spin_rate.setSingleStep(0.1)
        self.spin_rate.setRange(0, 100)
        
        self.label_year = QLabel('Years')
        self.spin_year = QSpinBox()
        self.spin_year.setSuffix(' year')
        self.spin_year.setSingleStep(1)
        self.spin_year.setRange(0, 1000)
        self.spin_year.setValue(1)
        
        
        self.label_total_ = QLabel('Total')
        self.label_total = QLabel('Rp. 0.00')
        
        grid = QGridLayout()
        grid.addWidget(self.label_amount, 0, 0)
        grid.addWidget(self.spin_amount, 0, 1)
        grid.addWidget(self.label_rate, 1, 0)
        grid.addWidget(self.spin_rate, 1, 1)
        grid.addWidget(self.label_year, 2, 0)
        grid.addWidget(self.spin_year, 2, 1)
        grid.addWidget(self.label_total_, 3, 0)
        grid.addWidget(self.label_total, 3, 1)
        self.setLayout(grid)
        
        self.connect(self.spin_amount, SIGNAL('valueChanged(double)'), self.update_ui)
        self.connect(self.spin_rate, SIGNAL('valueChanged(double)'), self.update_ui)
        self.connect(self.spin_year, SIGNAL('valueChanged(int)'), self.update_ui)
        self.setWindowTitle('Interest')
    
    def update_ui(self):        
        amount = self.spin_amount.value()
        rate = self.spin_rate.value()
        year = self.spin_year.value()
        total = amount * (1 + rate / 100.0) ** year
        
        self.label_total.setText('Rp. %.2f' % total)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()
    