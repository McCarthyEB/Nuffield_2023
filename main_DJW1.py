# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for clhasses, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


print("HI David")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    # See PyCharm help at https://www.jetbrains.com/help/pycharm/

    from ase import Atoms
    from ase.io import read, write, Trajectory
    from ase.visualize import view
    import math

    def atom_analysis(file_name,atoms):
        print(f"Analyzing atoms from {file_name}:")
        for iatom in range(0, len(atoms)):
            print(f"%d %s %10.6f %10.6f %10.6f" \
                  % (iatom, atoms.symbols[iatom], atoms.positions[iatom][0], \
                     atoms.positions[iatom][1], atoms.positions[iatom][2]))
        print("Looking for carbon:")
        for iatom in range(0, len(atoms)):
            if "C" in atoms.symbols[iatom]:
                print(f"%d %s %10.6f %10.6f %10.6f" \
                      % (iatom, atoms.symbols[iatom], atoms.positions[iatom][0], \
                         atoms.positions[iatom][1], atoms.positions[iatom][2]))
    # if Carbon to oxygen less than 2.0 A print this may be in the carbonate.
    #  loop over atoms again and find Oxygens
                for sec_atom in range(0, len(atoms)):
                    if "O" in atoms.symbols[sec_atom]:
                        dist = atoms.get_distance(iatom,sec_atom,mic=True)
                        if dist < 2.0:
                            print("%d %d are %10.6f apart" % ( iatom, sec_atom, dist))

                            for thi_atom in range(0, len(atoms)):
                                if "O" in atoms.symbols[thi_atom] and dist < 2.0:
                                    angle = atoms.get_angle(sec_atom,iatom,thi_atom,mic=True)
                                    angle_degrees = math.degrees(angle)
                                    print("%s %s %s are at an angle of %10.6f degrees" % (atoms.symbols[iatom],atoms.symbols[sec_atom],atoms.symbols[thi_atom],angle))
#   view(atoms)
    geomfile = ["1_geometry_100_def1.in", "ZnO_110_6l_2b2_CO2.in", "2_geometry_100_def1.in", "3_geometry_100_def1.in", \
                "4_geometry_100_def1.in", "5_geometry_100_def1.in", "6_geometry_100_def1.in"]

    for file in geomfile:
        atoms = read(file)
        atom_analysis(file,atoms)



