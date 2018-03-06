# Goban Tester
Tests your goban implementation by playing with both gnugo and your implementation.

Downloads 10 random games from [gokifu.com](http://gokifu.com/index.php) homepage as SGF and simulates games with implementations.

## Getting Started
### Requirements
 * Python 2.7+ (see `requirements.txt`)
 * gnugo (see [Utilities](#Utilities) for system-wide installer)
 * Goban implementation with GTP interface
 
#### GTP Requirements for Gobans
See also [Useful Resources](#Useful Resources) which also contains link to _GTP Command Reference_

 * You must obey GTP v2 specifications.
 * Implement those commands:
   * quit
   * boardsize
   * clear_board
   * play
   * showboard
 
### Installation
 * Fork and clone this repository
 * Install it from PyPI
    
        pip install gtester
        
   **Warning**: The name `gtester` conflicts with GLib unit test tool. You may want to run gtester with `python -m gtester`
 
### Usage
    usage: gtester [-h] [-v] [--goban-args GOBAN_ARGS] [--gnugo GNUGO] [--sgf SGF]
                   [--test-games TEST_GAMES]
                   goban-path
    
    Tests your goban implementation by playing with both gnugo and your
    implementation.
    
    positional arguments:
      goban-path            Path to executable of your implementation of goban
    
    optional arguments:
      -h, --help            show this help message and exit
      -v, --version         show program's version number and exit
      --goban-args GOBAN_ARGS
                            Goban arguments
      --gnugo GNUGO         Path to gnugo binary
      --sgf SGF             Test board with specific SGF file
      --test-games TEST_GAMES
                            Amount of games to test with

Test gnugo goban implementation against itself:

    python main.py gnugo --goban_args "--mode gtp" 

 
## Utilities
 * **gnugo installer**: you can find a bash script to install in project root, named as `install_gnugo.sh`. Script will install __gnugo__ system-wide, building from sources.

## Useful Resources
 * [GTP Command Reference](https://www.gnu.org/software/gnugo/gnugo_19.html#SEC200)
 * [SGF FF[4] Standard](https://www.red-bean.com/sgf/)

# Contributing
Anyone can send pull requests for any kind of improvements.

# License
See GNU Public License v3

# Changelog
 * 06/03/2018
    * Initial release.
