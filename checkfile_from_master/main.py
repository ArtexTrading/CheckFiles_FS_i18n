#!/usr/bin/python
# _*_ coding: utf-8 _*_

import json
import os
from glob import glob

#
# MAIN CLASS
#   Load the list of translation keys from the master file and generate
#   a new file for each language file with only the translation keys
#   existing in the master file
#


class Main(object):

    def __init__(self):
        filename = os.path.dirname(os.path.realpath(__file__)) + '/settings'
        self.config = self.get_json_file(filename)

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

    def loadkeys(self, filename):
        result = []
        data = self.get_json_file(filename)
        for key, value in data.iteritems():
            result.append(key)

        result.sort()
        return result

    def run(self):
        master_file = self.config['path'] + self.config['master']
        keys = self.loadkeys(master_file)
        files = self.get_json_list(self.config['path'])
        for item in files:
            if item == master_file:
                continue

            item_data = self.get_json_file(item)
            item_output = {}
            for masterkey in keys:
                item_value = item_data.get(masterkey)
                if item_value is not None:
                    item_output[masterkey] = item_value

            os.remove(item)
            self.set_json_file(item, item_output)
