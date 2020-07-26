from Analysis_Table import Ui_MainWindow
import sys
import os
import pandas as pd
from PySide2 import *
from PySide2.QtWidgets import QMainWindow, QApplication, QFileDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.input_data = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionLoadFile.triggered.connect(self.open_file)

    def open_file(self):
        try:
            open_file_name, open_file_type = QFileDialog.getOpenFileName(self, '选取文件',  './EXCEL/',
                                                                         "All Files(*);;Text Files(*.txt)")
            self.input_data = pd.read_csv(open_file_name)
            print(open_file_name, open_file_type, self.input_data)
        except FileNotFoundError:
            print(FileNotFoundError)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
