#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2018  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gnu.org>
# Maintainer: David Arroyo Menéndez <davidam@gnu.org>

# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.

# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with GNU Emacs; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

import csv
import requests
import json
from pprint import pprint

with open('partial.csv') as csvfile:
    namsorreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    next(namsorreader, None)
    namsorlist = []
    for row in namsorreader:
#        print(row)
        name = row[0]
        surname = row[2]
        name = name.replace('"', '')
        surname = surname.replace('"', '')
        r = requests.get('https://api.namsor.com/onomastics/api/json/gender/'+ name +'/' + surname)
        d = json.loads(r.text)
        namsorlist.append((d['firstName'], d['gender']))
        # pprint(d)
        # pprint(d['firstName'])
        # pprint(d['gender'])
#        print(d['firstName'])
        #namsorlist.append((r['firstname'],r['gender']))
print(namsorlist)
