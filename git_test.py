from ase.io import read
from ase import Atoms
atoms=read("1_geometry_100_def1.in")
for iatom in range(0, len(atoms)):
    print(f"%d %s %10.6f %10.6f %10.6f" \
          % (iatom, atoms.symbols[iatom], atoms.positions[iatom][0], \
             atoms.positions[iatom][1], atoms.positions[iatom][2]))
print("This is a change made locally for test purposes of push.")
print("This is a change made in the repository for test purposes of pull.")
