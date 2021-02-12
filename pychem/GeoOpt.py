"""
This module is used for optimizing molecular structures and getting ARC file
 
based on pybel and MOPAC!

Written by Dongsheng Cao

Date:2011.3.23
"""

import os
import string

from pychem import vector3d

Version = 1.1


################################################################################
class Atom:
    """
    #################################################################
    A atom class used for wrapping some properties of atoms.
    
    Note that Coordinates is the output of the function 
    
    (_ReadCoordinates).
    #################################################################
    """

    def __init__(self, Coordinates):

        self.pos = vector3d.Vector3d()
        self.radius = 0.0
        self.Coordinates = Coordinates
        self.Element = ''

    def SetCoordinates(self):

        temp = self.Coordinates
        self.pos.x = float(temp[1])
        self.pos.y = float(temp[2])
        self.pos.z = float(temp[3])

    def GetCoordinates(self):

        self.SetCoordinates()

        return self.pos

    def SetElement(self):

        temp = self.Coordinates

        self.Element = temp[0]

    def GetElement(self):

        self.SetElement()

        return self.Element

    def SetRadius(self):

        radii = {'H': 1.20, 'N': 1.55, 'Na': 2.27, 'Cu': 1.40, 'Cl': 1.75, 'C': 1.70,
                 'O': 1.52, 'I': 1.98, 'P': 1.80, 'B': 1.85, 'Br': 1.85, 'S': 1.80, 'Se': 1.90,
                 'F': 1.47, 'Fe': 1.80, 'K': 2.75, 'Mn': 1.73, 'Mg': 1.73, 'Zn': 1.39, 'Hg': 1.8,
                 'Li': 1.8, '.': 1.8}

        temp = self.GetElement()

        if temp in radii.keys():
            self.radius = radii[temp]
        else:
            self.radius = radii['.']

    def GetRadius(self):

        self.SetRadius()

        return self.radius


###########################################################################

def GetAtomClassList(Coordinates):
    """
    #################################################################
    Combine all atoms in a molecule into a list form.
    
    Note that Coordinates is the output of the function (_ReadCoordinates).
    #################################################################
    """
    Atoms = []
    for i in Coordinates:
        atom = Atom(i)
        atom.SetCoordinates()
        atom.SetElement()
        atom.SetRadius()
        Atoms.append(atom)
    return Atoms


###########################################################################    

def _ReadCoordinates(filename="temp"):
    """
    #################################################################
    Read the coordinates and charge of each atom in molecule from .arc file.
    #################################################################
    """
    res = []

    f = open(filename, 'r')
    templine = f.readlines()
    f.close()

    for line in range(len(templine)):
        if templine[line][-7:-1] == "CHARGE":
            k = line
            break

    for i in templine[k + 4:len(templine) - 1]:
        temp = i.split()
        ElementCoordinate = [string.strip(temp[0]), string.strip(temp[1]),
                             string.strip(temp[3]), string.strip(temp[5]),
                             string.strip(temp[10])]
        res.append(ElementCoordinate)

    return res


#############################################################################


def RunMOPAC(filename):
    """
    #################################################################
    Run the MOPAC using os.system
    #################################################################
    """

    itest = os.system("run_mopac7" + " " + filename)
    # time.sleep(1)
    return itest
