#!/bin/python3
# -*- coding: UTF-8 -*-

# PImageCvt Image Convert

import os
from PIL import Image
from enum import Enum

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
                            ".png" :IMGCVT_OUT_TYPE.IMG_PNG,
                          }


    def __init__(self) -> None:
        super().__init__()

    def __init__(self, path_dst, path_src):
        if len(path_dst) != 0 and len(path_src) != 0:
            self.init_gen()
            self._dst_dir = path_dst
            self._src_dir = path_src
            self._out_type = IMGCVT_OUT_TYPE.IMG_BMP

    def set_dst_dir(self, dst_dir):
        self._dst_dir = dst_dir

    def set_src_dir(self, src_dir):
        self._src_dir = src_dir

    def get_src_file_type(self, src_path):
        pass

    def is_map_pic(self, val):
        res = None
        # res = list(self._type_map.keys())[list(self._type_map.values()).index(val)]
        for map_str, map_key in self._type_map.items():
            print("str = ", map_str)
            print("key = ", map_key)
            if map_key == val:
                res = map_str
                print("str ok = ", map_str)
                print("key ok = ", map_key)
                break
            print("\n")
        return res

    def get_str_output_type_name(self):
        return self.is_map_pic(self._out_type)

    def toBmp(self):
        self._out_type = IMGCVT_OUT_TYPE.IMG_BMP
        self.cvt(self._out_type, 0)

    def toJPG(self):
        self._out_type = IMGCVT_OUT_TYPE.IMG_JPG
        self.cvt(self._out_type, 0)

    def toJPEG(self):
        self._out_type = IMGCVT_OUT_TYPE.IMG_JPEG
        self.cvt(self._out_type, 0)

    def toPNG(self):
        self._out_type = IMGCVT_OUT_TYPE.IMG_PNG
        self.cvt(self._out_type, 0)



    def cvt(self, dst_type, src_type):
        convert_count = 0
        # 查询类型是否于列表
        print("is_map_pic para: ", dst_type)
        if self.is_map_pic(dst_type) is None:
            print("ImageCvt() : 转换类型错误!!!")
            return
        # 判断源文件夹与目标文件夹是否为空
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
                res = file_name_ex.lower()
                if res not in self._type_map:
                    print("Error: 文件扩展名错误 :", fileName)
                    continue
                else:
                    name = os.path.splitext(fileName)[0]
                    newFileName = name + self.get_str_output_type_name()
                    img = Image.open(self._src_dir + "/" + fileName)
                    img.save(self._dst_dir + "/" + newFileName)
                    convert_count += 1
                    # print(f" {fileName} \t\t\t 转换为: {newFileName}")
            return True
        else:
            return False
