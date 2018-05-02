#!/usr/bin/env python

"""
    Goban Tester
    Copyright (C) 2018 Berke Emrecan Arslan

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import re


class Parser:
    """
    Base class for goban parser.
    """

    def __init__(self):
        pass

    def parse(self, state):
        raise NotImplementedError


class GnuGoParser(Parser):
    """
    Parser for gnugo
    """

    def __init__(self):
        Parser.__init__(self)

    def parse(self, state):
        """
        Parses GnuGo board representation
        :param state:
        :return:
        """
        b = ''.join(state.splitlines()[1:-1])
        b = re.sub(
            r'\s*(WHITE|BLACK)\s+[(][OX][)]\s+has\s+captured\s+\d+\s+stones',
            '', b
        )
        b = re.sub(r'\d+', '', b)
        b = re.sub(r'\s+', '', b)
        b = b.replace('X', 'W').replace('O', 'B').replace('+', '.')

        return ''.join(b).strip()
