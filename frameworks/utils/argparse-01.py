import argparse

print(argparse.__version__)


parser = argparse.ArgumentParser(description="Math equation")


# add arguments with method add_argument()
parser.add_argument('-v1', '--value1', type=int,
                    help="The first value of equation")
parser.add_argument('-v2', '--value2', type=int,
                    help="Second value of equation")

parser.add_argument('-w', '--word', type=str, help="Digit a simple word")
parser.add_argument('-f', '--number', type=float, help="Float number")

# parsing arguments
args = parser.parse_args()


def equation(value1, value2):
    calc = value1 * value2
    return calc


if __name__ == "__main__":
    print('The result is: {}'.format(equation(args.value1, args.value2)))
    print('\n')
    print("The word is: {}".format(args.word))
    print("Float number: {}".format(args.number))
