from UI.test import Ui_MainWindow
from UI.datachoose import Ui_Form
from PySide2 import QtWidgets
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys
import numpy as np


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.actionOpenFile.triggered.connect(self.opendatabase)

    def opendatabase(self):
        form = QtWidgets.QWidget()
        ui = Ui_Form()
        ui.setupUi(form)
        form.show()
        form.exec_()



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
