import yaml
import os
import subprocess
import random
import csv
import time
import numpy as np
import math
import shutil
import pandas as pd


import matplotlib.pyplot as plt



version_idx_str = "0"


# 1 Set Variable

#N1 = round(random.uniform(2.5, 12.5)) # 3~12
N1 = 5
freq = 30e+3
height = 34.2

w01 = 1
w02 = 1
w03 = 1
w04 = 1
w05 = 1

spacex = 10
spacey = 10

ratiox01 = 1
ratiox02 = 2
ratiox03 = 3
ratiox04 = 4
ratiox05 = 5
ratiox06 = 6

ratioy01 = 1
ratioy02 = 2
ratioy03 = 3
ratioy04 = 4
ratioy05 = 5


# 2 Config Identifier-Variable set.

config = {
    "$VERSION_IDX_STR"  :   version_idx_str,
    "$N1"  :  N1,
    "$freq" : freq,
    "$height" : height,
    "$spacex" : spacex,
    "$spacey" : spacey,
    "$w01" : w01,
    "$w02" : w02,
    "$w03" : w03,
    "$w04" : w04,
    "$w05" : w05,
    "$ratiox01" : ratiox01,
    "$ratiox02" : ratiox02,
    "$ratiox03" : ratiox03,
    "$ratiox04" : ratiox04,
    "$ratiox05" : ratiox05,
    "$ratiox06" : ratiox06,
    "$ratioy01" : ratioy01,
    "$ratioy02" : ratioy02,
    "$ratioy03" : ratioy03,
    "$ratioy04" : ratioy04,
    "$ratioy05" : ratioy05,

    #FIXME : add some idt : variables
}


#3 Make Folder

folder_name = f'SIMUL_{version_idx_str}'
os.mkdir(f'.\ML\SIMUL_{version_idx_str}')


#4 Make Variable info file

with open(f'.\ML\SIMUL_{version_idx_str}\info.yaml', "w") as info_file:
    yaml.dump(config,info_file)


#5 Make python script file
#Load file string

REF_N001 = f'../script_ref/func_ref/N001_initial.py'
REF_N002 = f'../script_ref/func_ref/N002_variable_N{str(N1).zfill(2)}.py'
REF_N003 = f'../script_ref/func_ref/N003_make_model_N{str(N1).zfill(2)}.py'

ref_script_str = ""
with open(REF_N001) as f :
    lines1 = f.readlines()
with open(REF_N002) as f :
    lines2 = f.readlines()
with open(REF_N003) as f :
    lines3 = f.readlines()

lines = lines1 + lines2 + lines3
    
ref_script_str = "".join(lines)

#Change Identifiers
for idt, var in config.items() :
    ref_script_str = ref_script_str.replace(idt, str(var))

#Save file
with open(f'.\\ML\\SIMUL_{version_idx_str}\\run_ansys_{version_idx_str}.py',"w") as f :
    f.write(ref_script_str)