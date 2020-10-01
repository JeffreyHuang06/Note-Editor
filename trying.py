import argparse
parser = argparse.ArgumentParser()
parser.add_argument("input", type=str)
parser.add_argument("-o", "--output", type=str)

args = parser.parse_args()
print(args)