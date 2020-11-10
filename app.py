import argparse


def main(args):
    result = args.base**args.exponent
    print(f"{args.base}**{args.exponent} = {result}")


parser = argparse.ArgumentParser()
parser.add_argument('--base', type=float, help='base')
parser.add_argument('--exponent', type=float, help='exponent')
args = parser.parse_args()

if __name__ == "__main__":
    main(args)
