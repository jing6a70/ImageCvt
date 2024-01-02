#!/bin/python3
# -*- coding: UTF-8 -*-

# PImageCvt Image Convert

import os
from PIL import Image

from PImageCvt import Image_convert

# 实现JPG转BMP
# 设置路径
class ImageJpg():
    src_type = ""       # Source Type
    dir_list = []       # File List

    _dst_dir = ""       # 目标路径
    _src_dir = ""       # JPG原路径

    def __init__(self) -> None:
        super().__init__()

    def __init__(self, path_dst, path_src):
        if len(path_dst) != 0 and len(path_src) != 0:
            self._dst_dir = path_dst
            self._src_dir = path_src

            print(self._dst_dir)
            print(self._src_dir)

    def toBmp(self):
        convert_count = 0
        if len(self._src_dir) != 0 and len(self._dst_dir) != 0:
            try:
                self.dir_list = os.listdir(self._src_dir)
            except Exception as re:
                print("Error : < %s > 此路径不存在!", self._src_dir)
                exit(-1)

            # 打开目标目标文件夹，不存在则创建
            try:
                os.mkdir(self._dst_dir)
            except Exception as re:
                print("%s 已经存在", self._dst_dir)

            # 开始转换
            for fileName in self.dir_list:
                if os.path.splitext(fileName)[1] == '.jpg' or os.path.splitext(fileName)[1] == '.JPG':
                    name = os.path.splitext(fileName)[0]
                    newFileName = name + ".bmp"

                    img = Image.open(self._src_dir + "/" + fileName)
                    img.save(self._dst_dir + "/" + newFileName)
                    convert_count += 1
                    print(f" {fileName} \t\t\t 转换为: {newFileName}")

            print("{0} 转为 {1} 文件总个数为: {2}" .format("JPG", "BMP", convert_count))
            return True
        else:
            print("路径设置为空, 转换失败")
            return False
