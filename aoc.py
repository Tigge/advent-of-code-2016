#!/usr/bin/env python3

import argparse
import importlib
import sys
import time

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Advent of Code 2016")
    parser.add_argument("--day", type=int, dest="days", nargs="+", default=range(1, 25))
    parser.add_argument("--stdin", dest='stdin', action='store_true', default=False)
    args = parser.parse_args()

    print("Advent of Code 2016")
    print("===================")
    print()

    for day in args.days:
        try:
            problem_module = importlib.import_module("day_{}".format(day))
            input_file = open("day_{}.txt".format(day)) if not args.stdin else sys.stdin
            problem = problem_module.Problem(input_file)
            print("Day", day)
            print("------")

            for step in range(1, 3):
                function = "step{}".format(step)
                if hasattr(problem, function) and callable(getattr(problem, function)):
                    start_time = time.perf_counter()
                    result = getattr(problem, function)()
                    end_time = time.perf_counter()
                    print("Step {}: {} (took {:.2f} µs)".format(step, result, (end_time - start_time) * 1000000))
            print()
        except ImportError as e:
            print("Day", day, "is not implemented yet")
