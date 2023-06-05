#!/usr/bin/env python

import os
import sys
import getopt
from MolKit import Read
from AutoDockTools.MoleculePreparation import AD4ReceptorPreparation


def usage():
    "Print helpful, accurate usage statement to stdout."
    print "Usage: prepare_receptor4.py -r filename"
    print
    print "    Description of command..."
    # Resto do código de ajuda


def prepare_receptor4(receptor_filename, outputfilename=None, repairs='', charges_to_add='Kollman',
                      preserve_charge_types=None, cleanup="nphs_lps_waters_nonstdres",
                      mode='automatic', delete_single_nonstd_residues=None, dictionary=None,
                      unique_atom_names=False, verbose=False):
    mols = Read(receptor_filename)
    # Resto do código de preparação do receptor

    RPO = AD4ReceptorPreparation(mol, mode, repairs, charges_to_add,
                                 cleanup, outputfilename=outputfilename,
                                 preserved=preserved,
                                 delete_single_nonstd_residues=delete_single_nonstd_residues,
                                 dict=dictionary)

    # Resto do código


if __name__ == '__main__':
    # Resto do código para processar os argumentos da linha de comando
    # ...

    if not receptor_filename:
        print 'prepare_receptor4: receptor filename must be specified.'
        usage()
        sys.exit()

    prepare_receptor4(receptor_filename, outputfilename, repairs, charges_to_add,
                      preserve_charge_types, cleanup, mode, delete_single_nonstd_residues,
                      dictionary, unique_atom_names, verbose)
