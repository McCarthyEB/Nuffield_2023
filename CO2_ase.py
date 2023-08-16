# This is a sample Python script.

from ase import Atoms
from ase.io import write
from ase.visualize import view

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ != '__main__':
    pass
# Press the green button in the gutter to run the script.
else:
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pychar
CO2 = Atoms('OCO', positions=[(0,0,0),(0,0,1.16),(0,0,2.32)])
write('CO2.in', CO2, format='aims')
d=CO2.get_distance(1,2)
print(f, "distance = %10.6f" % d)
#view(CO2)
