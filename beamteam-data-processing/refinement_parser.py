import csv
import re

def parse_refinement(refine_path):

    f = open(refine_path,"r").read()

    store_names = []
    store_frac = []
    phase_name = re.compile('Phase name:')
    weight_frac = re.compile('Weight fraction')
    for n in f:
        if phase_name.search(n) != None:
            store_names.append(n)
        elif weight_frac.search(n) != None:
            store_frac.append(n)
    f.close()

    info_store_names = []
    info_store_frac  = []
    for n in range(0,len(store_names)):
        info_store_names.append(store_names[n].split())

    for n in range(0,len(store_frac)):
        info_store_frac.append(store_frac[n].split())

    temp = []
    phase_frac_info = []
    for n in info_store_frac:
        hold = n
        phase_frac_info.append(hold[3])
        temp =[]

    m = 0
    outfile_path = refine_path.replace(".lst","_template.csv")
    outfile = open(outfile_path,"w")
    for ii in info_store_names:
        temp = ii
        outfile.write("Property " + temp[2] + "Phase Fraction,")
        outfile.write(phase_frac_info[m] + " ")
        m+=1
    outfile.close()

    return outfile_path
