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
    import matplotlib.pyplot as plt

    def atom_analysis(file_name,atoms):
        angles = []
        dists = []
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
                            dists.append(dist)
                            if dist < 1.2 or dist > 1.5:
                                print("distance outlier found in", file_name)
                                distance_outliers.append(dist)
                                distance_outliers_filename.append(file_name)
                            else:
                                print("expected distances returned")


                            for thi_atom in range(sec_atom+1, len(atoms)):
                                if "O" in atoms.symbols[thi_atom]:
                                    dist = atoms.get_distance(iatom, thi_atom, mic=True)
                                    if dist < 2.0:
                                        angle = atoms.get_angle(sec_atom,iatom,thi_atom,mic=True)
                                        angle_degrees = math.degrees(angle)
                                        print("%s %s %s are at an angle of %10.6f degrees" % (atoms.symbols[iatom],atoms.symbols[sec_atom],atoms.symbols[thi_atom],angle))
                                        angles.append(angle)
                                        if angle < 100 or angle > 140:
                                            print("angle outlier found in", file_name)
                                            angle_outliers.append(angle)
                                            angle_outliers_filename.append(file_name)
                                        else:
                                            print("expected angles returned")
        return angles, dists

#   view(atoms)
    geomfile = ["1_geometry_100_def1.in", "ZnO_110_6l_2b2_CO2.in", "2_geometry_100_def1.in", "3_geometry_100_def1.in", \
                "4_geometry_100_def1.in", "5_geometry_100_def1.in", "6_geometry_100_def1.in"]
    angle_outliers = []
    angle_outliers_filename = []
    distance_outliers = []
    distance_outliers_filename =[]
    total_distances = []
    total_angles = []

    for file in geomfile:
        atoms = read(file)
        angles,dists = atom_analysis(file,atoms)
        total_angles.append(angles)
        total_distances.append(dists)
        print ("volume of angle outliers = %d" % len(angles))
        print("angle outliers are", angle_outliers)
        print("angle outliers were found in", angle_outliers_filename)
        print("volume of distance outliers = %d" % len(dists))
        print("distance outliers are", distance_outliers)
        print("distance outliers were found in", distance_outliers_filename)

plt.subplot(2, 1, 1)
plt.hist(total_angles, bins=10)
plt.xlabel("Angle")
plt.ylabel("Frequency")
plt.title("Angles between carbon and two oxygen atoms")
plt.show()

plt.subplot(2, 1, 2)
plt.hist(total_distances, bins=10)
plt.xlabel("Distance")
plt.ylabel("Frequency")
plt.title("Distance between oxygen and carbon atoms")
plt.show()


