from PySide6.QtWidgets import QMainWindow,QApplication
import sys, os
from output import Ui_MainWindow

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.lineEdit.returnPressed.connect(self.my_slot)
        
        
        self.show()
        
    def my_slot(self):
        text = self.lineEdit.text()
        self.label.setText(text)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mwd = MyWindow()
    sys.exit(app.exec())
    