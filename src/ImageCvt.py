#!/bin/python3
# -*- coding: UTF-8 -*-

# PImageCvt Image Convert

import os
from PIL import Image
from enum import Enum
from PImageCvt import Image_convert

class IMGCVT_OUT_TYPE(Enum):
    IMG_BMP = 0
    IMG_JPG = 1
    IMG_JPEG = 2
    IMG_PNG = 3
    IMG_TIFF = 4

class ImageCvt():
    src_type = ""       # Source Type
    dir_list = []       # File List

    _dst_dir = ""       # 目标路径
    _src_dir = ""       # JPG原路径

    def init_gen(self):
        self._type_map = {
                            ".bmp" :IMGCVT_OUT_TYPE.IMG_BMP,
                            ".jpg" :IMGCVT_OUT_TYPE.IMG_JPG,
                            ".jpeg":IMGCVT_OUT_TYPE.IMG_JPEG,
                            ".jpg" :IMGCVT_OUT_TYPE.IMG_PNG,
                          }

    def __init__(self) -> None:
        super().__init__()

    def __init__(self, path_dst, path_src):
        if len(path_dst) != 0 and len(path_src) != 0:
            self.init_gen()
            self._dst_dir = path_dst
            self._src_dir = path_src
            self._out_type = IMGCVT_OUT_TYPE.IMG_BMP

    def __init__(self, path_dst, path_src, out_type):
        if len(path_dst) != 0 and len(path_src) != 0:
            self.init_gen()
            self._dst_dir = path_dst
            self._src_dir = path_src
            self._out_type = out_type
            self._output_w = output_w = 0
            self._output_h = output_h = 0

    def __init__(self, path_dst, path_src, out_type, output_w, output_h):
        if len(path_dst) != 0 and len(path_src) != 0:
            self.init_gen()
            self._dst_dir = path_dst
            self._src_dir = path_src
            self._out_type = out_type
            self._output_w = output_w
            self._output_h = output_h

    def get_src_file_type(self, src_path):
        pass

    def get_str_output_type_name(self):
        res = ""
        if self._out_type == IMGCVT_OUT_TYPE.IMG_BMP:
            res = ".bmp"
        elif self._out_type == IMGCVT_OUT_TYPE.IMG_JPG:
            res = ".jpg"
        elif self._out_type == IMGCVT_OUT_TYPE.IMG_JPEG:
            res = ".jpeg"
        elif self._out_type == IMGCVT_OUT_TYPE.IMG_PNG:
            res = ".png"

    def toBmp(self):
        self._out_type = IMGCVT_OUT_TYPE.IMG_BMP
        pass
    def toJPG(self):
        self._out_type = IMGCVT_OUT_TYPE.IMG_JPG
        pass
    def toJPEG(self):
        self._out_type = IMGCVT_OUT_TYPE.IMG_JPEG
        pass
    def toPNG(self):
        self._out_type = IMGCVT_OUT_TYPE.IMG_PNG
        pass

    def cvt(self, dst_type, src_type):
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
                # 获取文件扩展名
                file_name_ex = os.path.splitext(fileName)[1]
                # 获取文件扩展名类型
                res = self._type_map(file_name_ex)

                if not res:
                    print("self._type_map[file_name_ex] ERROR")
                    continue
                else:
                    name = os.path.splitext(fileName)[0]
                    newFileName = name + self.get_str_output_type_name()

                    img = Image.open(self._src_dir + "/" + fileName)
                    img.save(self._dst_dir + "/" + newFileName)
                    convert_count += 1
                    print(f" {fileName} \t\t\t 转换为: {newFileName}")
            return True
        else:
            return False
