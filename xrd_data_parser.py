import csv
from bs4 import BeautifulSoup
from pypif.obj import *

def parse_csv(csv_path):

    with open(csv_path, 'r') as csv_file:

        angle = []
        intensity = []

        reader = csv.reader(csv_file)
        for index, row in enumerate(reader):
            if index >= 32:
                angle.append(row[0])
                intensity.append(row[1])


    outfile_path = csv_path.replace(".csv", "_template.csv")
    outfile = open(outfile_path, 'w')
    outfile.write("PROPERTY: Intensity, CONDITION: 2$\\theta$ ($\circ$)\n")
    outfile.write("\"["+",".join(intensity)+"]\""+","+"\"["+",".join(angle)+"]\"")
    outfile.close()

    return outfile


def parse_xrdml(xrdml_file):

    soup = BeautifulSoup(open(xrdml_file, 'r'), 'xml')

    intensity = soup.intensities.contents[0].split(" ")
    intensity = [str(x) for x in intensity]
    start_position = float(soup.startPosition.contents[0])
    end_position = float(soup.endPosition.contents[0])
    print(start_position, end_position)
    number_of_steps = len(intensity)-1
    step_size = (end_position-start_position)/number_of_steps
    theta_values = []
    angle = start_position
    while len(theta_values) < len(intensity):
        theta_values.append(str(round(angle, 8)))
        angle += step_size

    print(theta_values)
    print(start_position, end_position)
    print(step_size)

    outfile_path = xrdml_file.replace(".xrdml", "_xrdml_template.csv")
    outfile = open(outfile_path, 'w')
    outfile.write("PROPERTY: Intensity, CONDITION: 2$\\theta$ ($\circ$)\n")
    outfile.write("\"[" + ",".join(intensity) + "]\"" + "," + "\"[" + ",".join(theta_values) + "]\"")
    outfile.close()






    return