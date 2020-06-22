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

class Listener:
     def __init__(self, name, subject):
         self.name = name
         subject.register(self)

     def notify(self, event):
         print(self.name + " received event " + event)


class Subject:
     def __init__(self):
         self.listeners = []
 
     def register(self, listener):
         self.listeners.append(listener)
 
     def unregister(self, listener):
         self.listeners.remove(listener)
 
     def notify_listeners(self, event):
         for listener in self.listeners:
             listener.notify(event)


subject = Subject()
listenerA = Listener("<listener A>", subject)
listenerA = Listener("<listener AA>", subject)
listenerB = Listener("<listener B>", subject)
# El objeto Subject ahora tiene dos "escuchadores" registrados
subject.notify_listeners("<events>")