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

from __future__ import print_function

import gtester.sgf as sgflib
from gtester.gtp import GTPMetaMachine, InvalidGTPResponse
from gtester.taskmaster import start_process
from gtester.parser import GnuGoParser


class GobanTester:
    def __init__(self, goban_1, goban_2, goban_1_parser=None,
                 goban_2_parser=None,
                 sgf_file=None,
                 sgf_str=None):
        self.meta = GTPMetaMachine()

        # start gobans and register to meta
        goban_1 = start_process(goban_1[0], goban_1[1])
        goban_2 = start_process(goban_2[0], goban_2[1])
        self.goban_1 = self.meta.register_goban(goban_1)
        self.goban_2 = self.meta.register_goban(goban_2)

        if goban_1_parser is not None:
            self.goban_1_parser = goban_1_parser
        else:
            self.goban_1_parser = GnuGoParser()

        if goban_2_parser is not None:
            self.goban_2_parser = goban_2_parser
        else:
            self.goban_2_parser = GnuGoParser()

        # ====
        if sgf_file is not None:
            self.games = [sgflib.parse_file(sgf_file)]
        elif sgf_str is not None:
            self.games = [sgflib.parse(sgf_str)]
        else:
            self.games = [
                sgflib.parse(f)
                for f in sgflib.sgf_download()
            ]

        self.games = [
            sgflib.sgf2gtp(sgf)
            for sgf in self.games
        ]

    def run(self):
        error_occured = False
        for reverse_color in [False, True]:
            for i, game in enumerate(self.games):
                for goban in [self.goban_1, self.goban_2]:
                    self.meta.send(goban, 'clear_board')

                print('Game {:-2d}/{}'.format(i + 1, len(self.games)))
                for j, cmd in enumerate(game):
                    print("{:3d}) {}".format(j + 1, cmd))

                    boards = [
                        self.meta.send(goban, 'showboard')
                        for goban in [self.goban_1, self.goban_2]
                    ]

                    responses = []

                    for goban in [self.goban_1, self.goban_2]:
                        try:
                            resp = self.meta.send(goban, cmd,
                                                  reverse_colors=reverse_color)
                            responses.append(resp)
                        except InvalidGTPResponse as e:
                            print("Command:")
                            print(cmd)
                            print("Response:")
                            print(resp)
                            print("  ", boards[0])
                            print("  ", boards[1])
                            self.kill_gobans()
                            exit(1)

                    prev_boards = boards

                    boards = [
                        self.meta.send(goban, 'showboard')
                        for goban in [self.goban_1, self.goban_2]
                    ]

                    result = self._compare_boards(boards[0], boards[1])
                    if len(result) > 0:
                        print('Oops!')
                        print(result)
                        print(responses)
                        print("Previous boards:")
                        print("  ", prev_boards[0])
                        print("  ", prev_boards[1])
                        print("Current boards:")
                        print("  ", boards[0])
                        print("  ", boards[1])
                        error_occured = True
                        self.kill_gobans()
                        exit(1)
                    else:
                        print('OK')

            if not error_occured:
                print('Reversing colors ..')

        if not error_occured:
            print('All tests passed.')

    def kill_gobans(self):
        for goban in [self.goban_1, self.goban_2]:
            self.meta.send(goban, 'quit')

    def _compare_boards(self, board_1, board_2):
        """
        Compares boards and returns different indexes
        :param board_1:
        :param board_2:
        :return:
        """
        board_1 = self.goban_1_parser.parse(board_1)
        board_2 = self.goban_2_parser.parse(board_2)

        if board_1 == board_2:
            return []
        else:
            return [(i, board_1[i], board_2[i]) for i in range(len(board_2)) if
                    board_1[i] != board_2[i]]
