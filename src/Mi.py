#!/bin/python3
# -*- coding: UTF-8 -*-

import sys

from PySide6 import QtCore
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QApplication, QFileDialog, QTableWidget, QTableWidgetItem, QLabel
from PySide6.QtUiTools import QUiLoader
from ImageCvt import *
from enum import Enum


class IMG_OUT_TYPE(Enum):
    IMG_BMP = 0
    IMG_JPG = 1
    IMG_JPEG = 2
    IMG_PNG = 3
    IMG_TIFF = 4




class QtApp(QWidget):
    _TitleName = ""
    _width = 0
    _height = 0

    def __init__(self, app_title_name="default_name", width=800, height=480):
        super().__init__()
        _TitleName = app_title_name
        self._width = width
        self._height = height
        self.LoaderUi()

    def LoaderUi(self):
        self.ui = QUiLoader().load('../res/main_ui.ui')

        self.ui.lable_image_pre.setScaledContents(True)

        # 基本属性设置 : tableWidget
        self.ui.tableWidget.resizeColumnsToContents()           # 宽度自适应
        self.ui.tableWidget.resizeRowsToContents()              # 高度自适应
        self.ui.tableWidget.setAlternatingRowColors(True)       # 表格颜色纵横交错显示
        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)  # 最后一列填充

        # Connect slots
        self.ui.btn_src_path.clicked.connect(self.on_btn_src_path_clicked)
        self.ui.btn_dst_path.clicked.connect(self.on_btn_dst_path_clicked)
        self.ui.btn_startc.clicked.connect(self.on_btn_startc_clicked)
        self.ui.btn_quit.clicked.connect(self.on_btn_quit_clicked)
        self.ui.tableWidget.cellClicked.connect(self.on_tableWidget_cell_clicked)

        self.center()
        self.ui.setWindowTitle("PicIC")
        self.ui.show()

    def center(self):
        qr = self.frameGeometry()
        # cp = QDesktopWidget().availableGeometry().center()
        # qr.moveCenter(cp)
        self.move(qr.topLeft())

    def on_btn_src_path_clicked(self):
        dir_file_list = []
        directory_path = QFileDialog.getExistingDirectory(self, "请选择文件夹", "./")
        if len(directory_path) > 0:
            self.ui.label_src_path.setText(directory_path)
            dir_file_list = os.listdir(directory_path)

            self.ui.tableWidget.setRowCount(len(dir_file_list))
            self.ui.tableWidget.setColumnCount(2)

            for i in range(len(dir_file_list)):
                self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(dir_file_list[i]))
                self.ui.tableWidget.setItem(i, 1, QTableWidgetItem(directory_path + "/" + dir_file_list[i]))

    def on_btn_dst_path_clicked(self):
        directory_path = QFileDialog.getExistingDirectory(self, "请选择文件夹", "./")
        if len(directory_path) > 0:
            self.ui.label_dst_path.setText(directory_path)

    def on_btn_startc_clicked(self):
        if len(self.ui.label_src_path.text()) <= 0:
            self.ui.label_info.setText("Error: 原路径为空")
            return False

        if len(self.ui.label_dst_path.text()) <= 0:
            self.ui.label_info.setText("Error: 目标路径为空")
            return False

        info_index = self.ui.comboBox_targetType.currentIndex()

        imghanle = ImageCvt(self.ui.label_dst_path.text(), self.ui.label_src_path.text())

        if info_index == IMGCVT_OUT_TYPE.IMG_BMP.value:
            imghanle.toBmp()
        elif info_index == IMGCVT_OUT_TYPE.IMG_JPG.value:
            imghanle.toJPG()
        elif info_index == IMGCVT_OUT_TYPE.IMG_JPEG.value:
            imghanle.toJPEG()
        elif info_index == IMGCVT_OUT_TYPE.IMG_PNG.value:
            imghanle.toPNG()

        return True

    def on_btn_quit_clicked(self):
        pass

    def on_tableWidget_cell_clicked(self, row, column):

        item = self.ui.tableWidget.item(row, 1)
        pixmap = QPixmap()
        pixmap.load(item.text())

        if pixmap.isNull() == False:
            self.ui.lable_image_pre.setPixmap(pixmap)
            self.ui.lable_image_pre.show()
        else:
            print("pixmap is null")

        print("row: {0} column: {1} text: {2}" .format(row, column, item.text()))
