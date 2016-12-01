# Advent of Code 2016

Here are my solutions built in Python 3. The structure is as follows:

* `aoc.py` - The CLI for the project. Read below how to use it.
* `day_X.py` - The soluion to day X
* `day_X.txt` - The input to day X

## How to use the CLI

* Run `./aoc.py --help` for help
  * The flag `--day X [Y [Z ...]]` selects which day(s) to run. Default is 
    day 1 to 24.
  * The flag `--stdin` reads problem input from stdin instead of the default
    `day_X.txt`.

### Example usage

`./aoc.py --day 1 2 3`
