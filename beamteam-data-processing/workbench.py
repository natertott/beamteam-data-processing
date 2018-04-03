import argparse
import xrd_data_parser

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('csv', nargs='*', help='path to input files')

    args = parser.parse_args()

    for f in args.csv:

        extension = f.split(".")[-1]

        if extension == "csv":
            print(f)
            system = xrd_data_parser.parse_csv(f)

        elif extension == "xrdml":
            print(f)
            system = xrd_data_parser.parse_xrdml(f)
