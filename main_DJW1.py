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

    atoms = read("ZnO_110_6l_2b2_CO2.in")
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
#   view(atoms)


