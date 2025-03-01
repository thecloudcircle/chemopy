"""
##############################################################################
The calculation of Kier and Hall's kappa indices based on its topological

structure. You can get 7 molecular kappa descriptors. You can 

freely use and distribute it. If you hava  any problem, you could contact 

with us timely!

Authors: Dongsheng Cao and Yizeng Liang.

Date: 2012.09.18

Email: oriental-cds@163.com
##############################################################################
"""

from rdkit import Chem
from rdkit.Chem import PeriodicTable
from rdkit.Chem.rdMolDescriptors import CalcHallKierAlpha as _HallKierAlpha
from rdkit.Chem import rdchem

periodicTable = rdchem.GetPeriodicTable()

Version = 1.0


################################################################

def CalculateKappa1(mol):
    """
    #################################################################
    Calculation of molecular shape index for one bonded fragment
    
    ---->kappa1
    
    Usage:
        
        result=CalculateKappa1(mol)
        
        Input: mol is a molecule object.
        
        Output: result is a numeric value.
    #################################################################
    """
    P1 = mol.GetNumBonds(onlyHeavy=1)
    A = mol.GetNumHeavyAtoms()
    denom = P1 + 0.0
    if denom:
        kappa = (A) * (A - 1) ** 2 / denom ** 2
    else:
        kappa = 0.0
    return round(kappa, 3)


def CalculateKappa2(mol):
    """
    #################################################################
    Calculation of molecular shape index for two bonded fragment
    
    ---->kappa2

    Usage:
        
        result=CalculateKappa2(mol)
        
        Input: mol is a molecule object.
        
        Output: result is a numeric value.
    #################################################################
    """
    P2 = len(Chem.FindAllPathsOfLengthN(mol, 2))
    A = mol.GetNumHeavyAtoms()

    denom = P2 + 0.0
    if denom:
        kappa = (A - 1) * (A - 2) ** 2 / denom ** 2
    else:
        kappa = 0.0
    return round(kappa, 3)


def CalculateKappa3(mol):
    """
    #################################################################
    Calculation of molecular shape index for three bonded fragment
    
    ---->kappa3
    
    Usage:
        
        result=CalculateKappa3(mol)
        
        Input: mol is a molecule object.
        
        Output: result is a numeric value.
    #################################################################
    """
    P3 = len(Chem.FindAllPathsOfLengthN(mol, 3))
    A = mol.GetNumHeavyAtoms()

    denom = P3 + 0.0
    if denom:
        if A % 2 == 1:
            kappa = (A - 1) * (A - 3) ** 2 / denom ** 2
        else:
            kappa = (A - 3) * (A - 2) ** 2 / denom ** 2
    else:
        kappa = 0.0
    return round(kappa, 3)


def CalculateKappaAlapha1(mol):
    """
    #################################################################
    Calculation of molecular shape index for one bonded fragment 
    
    with Alapha
    
    ---->kappam1
    
    Usage:
        
        result=CalculateKappaAlapha1(mol)
        
        Input: mol is a molecule object.
        
        Output: result is a numeric value.
    #################################################################
    """
    P1 = mol.GetNumBonds(onlyHeavy=1)
    A = mol.GetNumHeavyAtoms()
    alpha = _HallKierAlpha(mol)
    denom = P1 + alpha
    if denom:
        kappa = (A + alpha) * (A + alpha - 1) ** 2 / denom ** 2
    else:
        kappa = 0.0
    return round(kappa, 3)


def CalculateKappaAlapha2(mol):
    """
    #################################################################
    Calculation of molecular shape index for two bonded fragment 
    
    with Alapha
    
    ---->kappam2
    
    Usage:
        
        result=CalculateKappaAlapha2(mol)
        
        Input: mol is a molecule object.
        
        Output: result is a numeric value.
    #################################################################
    """
    P2 = len(Chem.FindAllPathsOfLengthN(mol, 2))
    A = mol.GetNumHeavyAtoms()
    alpha = _HallKierAlpha(mol)
    denom = P2 + alpha
    if denom:
        kappa = (A + alpha - 1) * (A + alpha - 2) ** 2 / denom ** 2
    else:
        kappa = 0.0
    return round(kappa, 3)


def CalculateKappaAlapha3(mol):
    """
    #################################################################
    Calculation of molecular shape index for three bonded fragment 
    
    with Alapha
    
    ---->kappam3
    
    Usage:
        
        result=CalculateKappaAlapha3(mol)
        
        Input: mol is a molecule object.
        
        Output: result is a numeric value.
    #################################################################
    """
    P3 = len(Chem.FindAllPathsOfLengthN(mol, 3))
    A = mol.GetNumHeavyAtoms()
    alpha = _HallKierAlpha(mol)
    denom = P3 + alpha
    if denom:
        if A % 2 == 1:
            kappa = (A + alpha - 1) * (A + alpha - 3) ** 2 / denom ** 2
        else:
            kappa = (A + alpha - 3) * (A + alpha - 2) ** 2 / denom ** 2
    else:
        kappa = 0.0
    return round(kappa, 3)


def CalculateFlexibility(mol):
    """
    #################################################################
    Calculation of Kier molecular flexibility index
    
    ---->phi
    
    Usage:
        
        result=CalculateFlexibility(mol)
        
        Input: mol is a molecule object.
        
        Output: result is a numeric value.
    #################################################################
    """
    kappa1 = CalculateKappaAlapha1(mol)
    kappa2 = CalculateKappaAlapha2(mol)
    A = mol.GetNumHeavyAtoms()
    phi = kappa1 * kappa2 / (A + 0.0)

    return round(phi, 3)


def GetKappa(mol):
    """
    #################################################################
    Calculation of all kappa values.
    
    Usage:
        
        result=GetKappa(mol)
        
        Input: mol is a molecule object.
        
        Output: result is a dcit form containing 6 kappa values.
    #################################################################
    """
    res = {}
    res['kappa1'] = CalculateKappa1(mol)
    res['kappa2'] = CalculateKappa2(mol)
    res['kappa3'] = CalculateKappa3(mol)
    res['kappam1'] = CalculateKappaAlapha1(mol)
    res['kappam2'] = CalculateKappaAlapha2(mol)
    res['kappam3'] = CalculateKappaAlapha3(mol)
    res['phi'] = CalculateFlexibility(mol)
    return res
