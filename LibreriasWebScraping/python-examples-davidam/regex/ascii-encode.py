#!/usr/bin/env python
# -*- coding: latin-1 -*-


a="aaa�������"
print(type(a))
print(a.encode('ascii','ignore'))
print(a.encode('ascii','replace'))
