#!/usr/bin/python
# _*_ coding: utf-8 _*_

from os.path import dirname
from os.path import realpath
from baseutils.utils import Utils


#
# MAIN CLASS
#   Load the list of translation keys from the master file and scan source
#   files to check if keys it's used
#


class Main(object):

    def __init__(self):
        filename = dirname(realpath(__file__)) + '/settings'
        self.config = Utils.get_json_file(filename)

    def run(self):
        keys = Utils.loadkeys(self.config['master'])
        for source in self.config['sources']:
            for path in source['paths']:
                files = Utils.get_file_list(path, source['extension'])
                for item in files:
                    if len(keys) == 0:
                        break

                    data = Utils.loadfile(item)
                    for masterkey in keys:
                        if masterkey in data:
                            keys.remove(masterkey)
                            if len(keys) == 0:
                                break
        Utils.set_json_file(self.config['master'] + '.not_used.json', keys)
