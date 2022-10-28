from tkinter import W
import yaml
import os
import subprocess
import random
import csv
import time
import csv
import numpy as np
import math
import pandas as pd
import shutil

#from pycaret.regression import load_model


																																																

REFERENCE_SCRIPT_FILE_NAME = f'run_ansys_ref.py'
f = open("../computer_name.txt", 'r')
COMPUTER_NAME = f.readline()

def random_choice(X) :
    return round(np.random.choice( np.arange( X[0] , X[1]+X[2] , X[2]) ),X[3])
    
def run_simul(version_idx_str):
    #0 Initialize random variables

    height0_range = [500, 4000, 10, 0]
    height1_range = [500, 4000, 10, 0]

    gap0_range = [5, 60, 1, 0]
    gap1_range = [5, 60, 1 ,0]

    width0_range = [150, 500, 10, 0]
    width1_range = [150, 500, 10, 0]

    ferrite_thick0_range = [5, 50, 1, 0]
    ferrite_thick1_range = [5, 50, 1, 0]

    ferrite_height0_range = [5, 50, 1, 0]
    ferrite_height1_range = [5, 50, 1, 0]

    ferrite_ex0_range = [5, 50, 1, 0]
    ferrite_ex1_range = [5, 50, 1, 0]

    ferrite_margin0_range = [5, 80, 1, 0]
    ferrite_margin1_range = [5, 80, 1, 0]

    airgap_range = [50, 250, 1, 0]




    # Design 1

    gap0 = random_choice(gap0_range)
    gap1 = random_choice(gap1_range)

    ferrite_thick0 = random_choice(ferrite_thick0_range) 
    ferrite_thick1 = random_choice(ferrite_thick1_range) 

    ferrite_height0 = random_choice(ferrite_height0_range) 
    ferrite_height1 = random_choice(ferrite_height1_range) 

    ferrite_ex0 = random_choice(ferrite_ex0_range) 
    ferrite_ex1 = random_choice(ferrite_ex1_range) 

    ferrite_margin0 = random_choice(ferrite_margin0_range) 
    ferrite_margin1 = random_choice(ferrite_margin1_range) 

    if width0_range[0] < round(2.5/10*(ferrite_margin0 + 2*gap0))*10 :
        width0_range = [round(2.5/10*(ferrite_margin0 + 2*gap0))*10, 500, 10, 0]
    if width1_range[0] < round(2.5/10*(ferrite_margin1 + 2*gap1))*10 :
        width1_range = [round(2.5/10*(ferrite_margin1 + 2*gap1))*10, 500, 10, 0]

    width0 = random_choice(width0_range)
    width1 = random_choice(width1_range)

    if height0_range[0] < round(2.5/10*(ferrite_margin0 + 2*gap0))*10 :
        height0_range = [round(2.5/10*(ferrite_margin0 + 2*gap0))*10, 4000, 10, 0]
    if height0_range[1] < round(2.5/10*(ferrite_margin1 + 2*gap1))*10 :
        height1_range = [round(2.5/10*(ferrite_margin1 + 2*gap1))*10, 4000, 10, 0]

    height0 = random_choice(height0_range)
    height1 = random_choice(height1_range)

    airgap = random_choice(airgap_range)

    

    


    #FIXME : add some variables


    #0.5 Config Identifier-Variable set.
    config = {
        "$VERSION_IDX_STR"  :   version_idx_str,
        "$height0"  :  height0,
        "$height1"  :  height1,
        "$gap0"  :  gap0,
        "$gap1"  :  gap1,
        "$width0"  :  width0,
        "$width1"  :  width1,
        "$ferrite_thick0" : ferrite_thick0,
        "$ferrite_thick1" : ferrite_thick1,
        "$ferrite_height0" : ferrite_height0,
        "$ferrite_height1" : ferrite_height1,
        "$ferrite_ex0" : ferrite_ex0,
        "$ferrite_ex1" : ferrite_ex1,
        "$ferrite_margin0" : ferrite_margin0,
        "$ferrite_margin1" : ferrite_margin1,
        "$airgap" : airgap
    
        #FIXME : add some idt : variables
    }


    #1 Make Folder
    folder_name = f'SIMUL_{version_idx_str}'
    os.mkdir(f'.\ML\SIMUL_{version_idx_str}')


    #2 Make Variable info file
    with open(f'.\ML\SIMUL_{version_idx_str}\info.yaml', "w") as info_file:
        yaml.dump(config,info_file)


    #3 Make python script file
    #Load file string
    ref_script_str = ""
    with open(REFERENCE_SCRIPT_FILE_NAME) as f :
        lines = f.readlines()
    ref_script_str = "\n".join(lines)

    #Change Identifiers
    for idt, var in config.items() :
        ref_script_str = ref_script_str.replace(idt, str(var))

    #Save file
    with open(f'.\\ML\\SIMUL_{version_idx_str}\\run_ansys_{version_idx_str}.py',"w") as f :
        f.write(ref_script_str)


    #4 make batch file.
    filepath2 = os.path.join('ML',folder_name,f'run_bat_{version_idx_str}.bat')
    with open(f'.\\ML\\SIMUL_{version_idx_str}\\run_bat_{version_idx_str}.bat',"w") as f :
        f.write(f'"C:\\Program Files\\AnsysEM\\AnsysEM21.1\\Win64\\ansysedt.exe" -iconic -runscriptandexit ".\\ML\SIMUL_{version_idx_str}\\run_ansys_{version_idx_str}.py"')


    workingDir = f'.\\ML\\SIMUL_{version_idx_str}'
    executeFile = f'.\\ML\\SIMUL_{version_idx_str}\\run_bat_{version_idx_str}.bat'
    #os.chdir(workingDir)
    try :
        os.system(executeFile)
    except :
        time.sleep(1)


    temp1 = pd.read_csv(f'.\ML_data\inductance{version_idx_str}_dat.csv', sep=",")
    temp1 = temp1.to_numpy()
    temp2 = pd.read_csv(f'.\ML_data\coupling{version_idx_str}_dat.csv', sep=",")
    temp2 = temp2.to_numpy()
    temp3 = pd.read_csv(f'.\ML_data\loss{version_idx_str}_dat.csv', sep=",")
    temp3 = temp3.to_numpy()

    parameter = np.array([width0,width1,height0,height1,airgap,gap0,gap1,ferrite_thick0,ferrite_thick1,ferrite_height0,ferrite_height1,ferrite_ex0,ferrite_ex1,ferrite_margin0,ferrite_margin1])

    temp1 = np.append(parameter,temp1)
    temp2 = np.append(parameter,temp2)
    temp3 = np.append(parameter,temp3)


    print(temp1)
    print(temp2)
    print(temp3)


    data1 = np.loadtxt(f'Z:\Autosimul_data\LRT\simple_model_turn22_v6\{COMPUTER_NAME}\script26\inductance.csv', delimiter=",")
    new_data1 = np.vstack((data1, temp1))
    np.savetxt(f'Z:\Autosimul_data\LRT\simple_model_turn22_v6\{COMPUTER_NAME}\script26\inductance.csv',new_data1,delimiter=",")

    data2 = np.loadtxt(f'Z:\Autosimul_data\LRT\simple_model_turn22_v6\{COMPUTER_NAME}\script26\coupling.csv', delimiter=",")
    new_data2 = np.vstack((data2, temp2))
    np.savetxt(f'Z:\Autosimul_data\LRT\simple_model_turn22_v6\{COMPUTER_NAME}\script26\coupling.csv',new_data2,delimiter=",")

    data3 = np.loadtxt(f'Z:\Autosimul_data\LRT\simple_model_turn22_v6\{COMPUTER_NAME}\script26\loss.csv', delimiter=",")
    new_data3 = np.vstack((data3, temp3))
    np.savetxt(f'Z:\Autosimul_data\LRT\simple_model_turn22_v6\{COMPUTER_NAME}\script26\loss.csv',new_data3,delimiter=",")




for i in range(0, 10000): 

    #run_simul(i)
    #print("end")


    try :
        try:
            os.remove(f'.\ML_aedt\ML26.aedt.lock')
        except:
            time.sleep(1)
        if os.path.isfile(f'.\ML_aedt\ML26.aedt') :
            os.remove(f'.\ML_aedt\ML26.aedt')
        time.sleep(1)	

        shutil.copy(f'.\ML_aedt\ML_ref.aedt',f'.\ML_aedt\ML26.aedt')
        time.sleep(1)

        try:
            run_simul(i)
        except Exception as e: 
            print(f'error number {i}')
            print(e)

        if os.path.isfile(f'.\ML_aedt\ML26.aedt') :
            os.remove(f'.\ML_aedt\ML26.aedt')
        time.sleep(1)	

        shutil.rmtree(f'.\ML_aedt\ML26.aedtresults')
        try:
            os.remove(f'.\ML_aedt\ML26.aedt.lock')
        except:
            time.sleep(1)
    except :
        time.sleep(1)	


    
    time.sleep(1)


os.system("pause")
