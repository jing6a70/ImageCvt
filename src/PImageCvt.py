#!/bin/python3
# -*- coding: UTF-8 -*-

# PImageCvt Image Convert

import os
import abc

# 抽象类
class asbImager(metaclass=abc.ABCMeta):
    all_type = 'file'

    @abc.abstractmethod  # 定义抽象方法
    def image_convert(self):
        pass

# 图片转换父类实现复用接口类
class Image_convert(asbImager):
    convert_src_path = ""
    convert_dst_path = ""

    src_type = ""
    dst_type = ""

    convert_count = 0
    dir_list = []

    def __init__(self) -> None:
        super().__init__()

    def __init__(self, dst_type, src_type):
        if dst_type != "" and src_type != "":
            self.src_type = src_type
            self.dst_type = dst_type

    def __del__(self):
        pass


    def set_src_path(self, src_path):
        if src_path != "":
            self.convert_src_path = src_path

    def set_dst_path(self, dst_path):
        if dst_path != "":
            self.convert_dst_path = dst_path

    def get_src_path(self):
        return self.convert_src_path

    def get_dst_path(self):
        return self.convert_dst_path

    def get_src_type(self):
        return self.src_type

    def get_dst_type(self):
        return self.dst_type

    def image_convert(self):
        pass

