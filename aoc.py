import argparse
import importlib
import sys

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
            if hasattr(problem, 'step1') and callable(getattr(problem, 'step1')):
                print("Step 1:", problem.step1())
            if hasattr(problem, 'step2') and callable(getattr(problem, 'step2')):
                print("Step 2:", problem.step2())
            print()
        except ImportError as e:
            print("Day", day, "is not implemented yet")
