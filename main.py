#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import json
import urllib
import time

from clases.Player import Player

if __name__ == '__main__':

    """ load configuration """
    if os.path.isfile(os.path.join('config.json')):
        try:
            json_data = open(os.path.join('config.json'))
            game_config = json.load(json_data)
            json_data.close()
        except:
            print("The file 'config.json' can not be loaded.")
            exit(2)
    else:
        print("The file 'config.json' can not be find.")
        exit(1)

    """ load languges """
    if os.path.isfile(os.path.join(game_config['default_language_file'])):
        try:
            json_data = open(os.path.join(game_config['default_language_file']))
            game_config['lang'] = json.load(json_data)
            json_data.close()
            print(game_config['lang']['string_01'])
        except:
            print("The file '"+game_config['default_language_file']+"' can not be loaded.")
            exit(3)
    else:
        print("The file '"+game_config['default_language_file']+"' can not be find.")
        exit(4)

    p1 = Player(game_config)
