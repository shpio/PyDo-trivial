import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
                    help = "display a square of a given number")
parser.add_argument("-v", "--verbose", action="store_true",
                    help="increase output verbosity")
parser.add_argument("-V", "--version", action="store_true",
                    help= "displays version")
args = parser.parse_args()
answer = args.square**2
if args.verbose:
    print(f"the square of {args.square} equals {answer}")
elif args.version:
    print(f"the square of {args.square} equals {answer} and the version is 1.3.5")
else:
    print(answer)
