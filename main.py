#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
#
#       Copyright 2017 Niflheim-Gate
#
#       This program is free software: you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation, either version 3 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program.  If not, see <http://www.gnu.org/licenses/>.

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
