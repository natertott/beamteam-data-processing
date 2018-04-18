import argparse
from xrd_data_parser import parse_csv, parse_xrdml
from refinement_parser import parse_refinement
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('csv', nargs='*', help='path to input files')

    args = parser.parse_args()

    for f in args.csv:

        print("PARSING: ", f)

        extension = f.split(".")[-1]

        if extension == "csv":
            system = parse_csv(f)

        elif extension == "xrdml":
            system = parse_xrdml(f)

        elif extension == "lst":
            print(f)
            system = parse_refinement(f)
