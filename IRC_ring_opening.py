# use psi4conda environment
import psi4
import numpy as np

psi4.core.clean_options()

output_file = "cyclobutene_opening_IRC.log"

psi4.set_memory("4GB")
psi4.set_output_file(output_file, append=False)
psi4.core.set_num_threads(4)

data = """
       0 1
 C    1.040389109196    0.254964976384   -0.647674881834
 C    0.689591079928    0.000000000000    0.708001346062
 C   -0.689591079928    0.000000000000    0.708001346062
 C   -1.040389109196   -0.254964976384   -0.647674881834
 H    1.923694934595   -0.185448301950   -1.124148093391
 H    0.711123863746    1.180002035639   -1.108938410294
 H    1.381683913454   -0.238567611354    1.514789629143
 H   -1.381683913454    0.238567611354    1.514789629143
 H   -1.923694934595    0.185448301950   -1.124148093391
 H   -0.711123863746   -1.180002035639   -1.108938410294

       units angstrom
       """ 
mol = psi4.geometry(data)             # Create Molecule object from data string

psi4.set_options({
     "geom_maxiter":500,
     "full_hess_every":1,                # Tried -1 and 0
     "opt_type":"irc",
     "irc_step_size":0.15,               # Also tried 0.20 and 0.25
     "ensure_bt_convergence":True,       # Tried False
     "irc_direction": "forward",         # Tried 'backward'
     "reference": "rhf",                 # Also tried "uhf"
     "g_convergence": "GAU_VERYTIGHT",   # Also tried GAU_TIGHT and QCHEM
     "IRC_POINTS": 5                     # Tried 20 and 25
     })
print("start")
E, history = psi4.optimize('b3pw91/6-31+G(d)',molecule=mol, return_history=True)
print("done")