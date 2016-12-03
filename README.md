# Advent of Code 2016

Here are my solutions built in Python 3. The structure is as follows:

* `aoc.py` - The CLI for the project. Read below how to use it.
* `day_X.py` - The solution to day `X`
* `day_X.txt` - The input to day `X`

## How to use the CLI

```
usage: aoc.py [-h] [--day DAY [DAY ...]] [--perf] [--stdin]

Advent of Code 2016

optional arguments:
  -h, --help           show this help message and exit
  --day DAY [DAY ...]  select days (default: 1-25)
  --perf               enable performance measuring (default: off)
  --stdin              read input from stdin (default: off)
```

### Example usage

`./aoc.py --day 1 2 3`
