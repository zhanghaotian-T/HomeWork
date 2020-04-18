from PySide2 import QtWidgets
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys
import numpy as np
import pandas as pd
from HomeWork.UI.test import Ui_MainWindow
from HomeWork.UI.datachoose import Ui_Dialog
from HomeWork.sql_functiom import SqliteFunction
import sqlite3
from sqlalchemy import create_engine


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.actionOpenFile.triggered.connect(self.opendatabase)
        self.actionReadData.triggered.connect(self.add_data)
        self.con = sqlite3.connect('foods.db')
        self.engine = create_engine('sqlite:///foods.db')

    def opendatabase(self):
        form = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(form)
        form.show()
        form.exec_()
        get_dataframe = pd.read_sql('foods', con=self.engine, )
        print(get_dataframe)

    def add_data(self):
        filename, filetype = QFileDialog.getOpenFileName(self, "选择文件", "/", "All Files (*);;Text Files (*.txt)")
        add_data = pd.read_csv(filename, ',')
        # con = sqlite3.connect('foods.db')
        # add_data.to_sql(name='foods', con=con, if_exists='append', index=False)
        sqlit_data = SqliteFunction()
        sqlit_data.database_write(sqlit_data)

    def datatransfer(self, input_dataframe, edit_table_weight):
        input_dataframe_rows = input_dataframe.shape[0]
        input_dataframe_colunms = input_dataframe.shape[1]
        input_dataframe_headers = input_dataframe.columns.values.tolist
        edit_table_weight.setHorizontalHeaderLabels(input_dataframe_headers)
        for i in range(input_dataframe_rows):
            input_dataframe_rows_value = input_dataframe.iloc[[i]]
            input_dataframe_rows_value_array = np.array(input_dataframe_rows_value)
            input_dataframe_rows_value_list = input_dataframe_rows_value_array.tolist()[0]
            for j in range(input_dataframe_colunms):
                input_dataframe_items_list = input_dataframe_rows_value_list[j]
                input_dataframe_items_list = str(input_dataframe_items_list)
                new_item = QTableWidgetItem(input_dataframe_items_list)
                new_item.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
                edit_table_weight.setItem(i, j, new_item)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    sys.exit(app.exec_())
