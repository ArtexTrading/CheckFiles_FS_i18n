#!/usr/bin/python
# _*_ coding: utf-8 _*_

import fnmatch
import io
import json
import os

from glob import glob

#
# UTILS CLASS
#   Common utilities
#


class Utils(object):

    def __init__(self):
        pass

    @staticmethod
    def get_json_file(filename):
        with open(filename) as data:
            return json.load(data)

    @staticmethod
    def set_json_file(filename, data):
        with open(filename, 'w') as json_file:
            json.dump(data, json_file, indent=4)

    @staticmethod
    def get_json_list(path):
        return glob(path + '*.json')

    @staticmethod
    def get_file_list(path, extension):
        result = []
        for root, dirnames, filenames in os.walk(path):
            for filename in fnmatch.filter(filenames, '*.' + extension):
                result.append(os.path.join(root, filename))

        return result

    @staticmethod
    def loadkeys(filename):
        result = []
        data = Utils.get_json_file(filename)
        for key, value in data.iteritems():
            result.append(key)

        result.sort()
        return result

    @staticmethod
    def loadfile(filename):
        file_object = io.open(filename, mode="r", encoding="utf-8")
        result = file_object.read()
        file_object.close()
        return result
