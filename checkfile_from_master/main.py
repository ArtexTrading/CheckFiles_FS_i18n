#!/usr/bin/python
# _*_ coding: utf-8 _*_

import os
from baseutils.utils import Utils


#
# MAIN CLASS
#   Load the list of translation keys from the master file and generate
#   a new file for each language file with only the translation keys
#   existing in the master file
#


class Main(object):

    def __init__(self):
        filename = os.path.dirname(os.path.realpath(__file__)) + '/settings'
        self.config = Utils.get_json_file(filename)

    def run(self):
        master_file = self.config['path'] + self.config['master']
        keys = Utils.loadkeys(master_file)
        files = Utils.get_json_list(self.config['path'])
        for item in files:
            if item == master_file:
                continue

            item_data = Utils.get_json_file(item)
            item_output = {}
            for masterkey in keys:
                item_value = item_data.get(masterkey)
                if item_value is not None:
                    item_output[masterkey] = item_value

            os.remove(item)
            Utils.set_json_file(item, item_output)
