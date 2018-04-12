def parse_refinement(refine_path,phase1,phase2,phase3):

    import re

    f = open(refine_path,"r").read()

    store_struc = []
    store_params = []

    """ Finding where the phase information for each phase is located in the refinement """
    """for line in f:
        if 'Phases' in line:
            store_struc.append(f.index(line))
        elif 'Phase:' in line:
            store_params.append(f.index(line))

    phaselist = []
    for iter in range(store_struc[1],store_params[1]):
        if 'Phase name:' in f[iter]:
            phase.append(f[iter])
        elif 'Unit cell' in f[iter]:
            phase.append(f[iter])

    phase = ''.join(phase)
    phase = phase.split()

    phasefrac = []
    for count in f:
        if 'Phase frac' in count:
            phasefrac.append(count)

    phasefrac = ''.join(phasefrac)
    phasefrac = phasefrac.split()"""

    store_names = []
    store_frac = []
    phase_name = re.compile('Phase name:')
    weight_frac = re.compile('Weight fraction')
    for n in f:
        if phase_name.search(n) != None:
            store_names.append(n)
        elif weight_frac.search(n) != None:
            store_frac.append(n)

    info_store_names = []
    info_store_frac  = []
    for n in range(0,len(store_names)):
        info_store_names.append(store_names[n].split())

    for n in range(0,len(store_frac)):
        info_store_frac.append(store_frac[n].split())

    temp = []
    phase1_info = []
    for n in info_store_frac:
        hold = n
        phase1_info.append(hold[3])
        temp =[]
