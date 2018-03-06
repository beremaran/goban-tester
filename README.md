# Goban Tester
![version-0-0-2](https://img.shields.io/badge/version-0.0.2-blue.svg)

Tests your goban implementation by playing with both gnugo and your implementation.

Downloads 10 random games from [gokifu.com](http://gokifu.com/index.php) homepage as SGF and simulates games with implementations.

## Getting Started
### Requirements
 * Python 2.7+ (see `requirements.txt`)
 * gnugo (see [Utilities](#Utilities) for system-wide installer)
 * Goban implementation with GTP interface
 
#### GTP Requirements for Gobans
See also __Useful Resources__ which also contains link to _GTP Command Reference_

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
 * Implement a board parser for your implementation by extending `gtester.parser.Parser` class.
    * If your output is compatible with gnugo output it is not required.
 * If you omit `goban_X_parser` parameter in `GobanTester` constructor, `GnuGoParser` will be used
 
 ```python
    from gtester import GNU_GO_COMMAND
    from gtester.parser import Parser
    from gtester.tester import GobanTester
    
    class ExampleParser(Parser):
        ...
        
    # GobanTester(goban_1, goban_2, goban_1_parser=None, goban_2_parser=None ...
    tester = GobanTester(["example_goban", ["--mode gtp"]], GNU_GO_COMMAND, ExampleParser())
```


Test gnugo goban implementation against itself:

```bash
    python main.py gnugo --goban_args "--mode gtp"
```

 
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
