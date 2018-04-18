import csv
import re

def parse_refinement(refine_path):

    lines = open(refine_path, "r").readlines()

    phases = []
    weights = []

    for line in lines:

        if "Phase name:" in line:
            phase = line.split("Phase name: ")[-1].strip("\n")
            phases.append(phase)

        if "Weight fraction" in line:
            all_num = re.findall("\d+\.\d+", line)
            weight = all_num[0]+"$\pm$"+all_num[1]
            weights.append(weight)

    outfile_path = refine_path.replace(".lst", "_template.csv")
    outfile = open(outfile_path, "w")
    outfile.write("PROPERTY: Phase, PROPERTY: Phase fraction (%)\n")

    for p, w in zip(phases, weights):
        outfile.write(p+", "+w)

    outfile.close()

    return outfile_path
