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
#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
from pprint import pprint
import pandas as pd
from pandas.io.json import json_normalize
data = [
  {
    'name': {
      'first': 'vikash',
      'last': 'singh'
    },
    'age': 27
  },
  {
    'name': {
      'first': 'satyam',
      'last': 'singh'
    },
    'age': 14
  }
]

df = pd.DataFrame.from_dict(json_normalize(data), orient='columns')
print(df)
print(json_normalize(data))

jsondata = open('perceval.json').read()
json_object = json.loads(jsondata)
print(json_object)