#!/bin/python3
# -*- coding: UTF-8 -*-

import os
from ImageJpg import *
from Mi import *

def jpg2bmp():
    target_dir = os.getcwd() + "/Bmp"
    source_dir = os.getcwd() + "/Src"
    jpg = ImageJpg(target_dir, source_dir)
    jpg.toBmp()

def qt():
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(800, 600)
    w.move(300, 300)
    w.setWindowTitle('图像转换工具')
    w.show()

    sys.exit(app.exec())


def main():
    app = QApplication(sys.argv)
    ex = QtApp()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()

