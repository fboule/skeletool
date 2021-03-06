# skeletool - http://skeletool.googlecode.com/
#
# Copyright (C) 2010 Fabien Bouleau
#
# This file is part of skeletool.
#
# skeletool is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# skeletool is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with skeletool.  If not, see <http://www.gnu.org/licenses/>.


class Container(object):
    @staticmethod
    def __new__(cls):
        if cls is Container:
            raise TypeError('Cannot directly instanciate ' + repr(cls))

        if '_instance' not in dir(cls):
            cls._instance = super(Container, cls).__new__(cls)
            cls._instance._items = {}

        return cls._instance

    def get(self, cls):
        if cls in self._items:
            return self._items[cls]
        return None

    def set(self, item):
        self._items[item.__class__] = item

    def all(self):
        return self._items
