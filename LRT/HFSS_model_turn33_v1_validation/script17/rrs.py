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

    raw_data = pd.read_csv("../result.csv",delimiter=",")
    raw_data = raw_data[raw_data["Num"]==version_idx_str]


    Num = version_idx_str
    Itx = raw_data["Itx"].values[0]
    Irx = raw_data["Irx"].values[0]
    air_gap = raw_data["air_gap"].values[0]
    coil_width0 = raw_data["coil_width0"].values[0]
    coil_width1 = raw_data["coil_width1"].values[0]
    length0 = raw_data["length0"].values[0]
    length1 = raw_data["length1"].values[0]
    width0 = raw_data["width0"].values[0]
    width1 = raw_data["width1"].values[0]
    coil_offset0 = raw_data["coil_offset0"].values[0]
    coil_offset1 = raw_data["coil_offset1"].values[0]
    turn_length_gap0 = raw_data["turn_length_gap0"].values[0]
    turn_length_gap1 = raw_data["turn_length_gap1"].values[0]
    turn_width_gap0 = raw_data["turn_width_gap0"].values[0]
    turn_width_gap1 = raw_data["turn_width_gap1"].values[0]
    ferrite_thick0 = raw_data["ferrite_thick0"].values[0]
    ferrite_thick1 = raw_data["ferrite_thick1"].values[0]
    ferrite_length_margin0 = raw_data["ferrite_length_margin0"].values[0]
    ferrite_length_margin1 = raw_data["ferrite_length_margin1"].values[0]
    ferrite_width_margin0 = raw_data["ferrite_width_margin0"].values[0]
    ferrite_width_margin1 = raw_data["ferrite_width_margin1"].values[0]
    ferrite_side_height0 = raw_data["ferrite_side_height0"].values[0]
    ferrite_side_height1 = raw_data["ferrite_side_height1"].values[0]
    ferrite_side_thick0 = raw_data["ferrite_side_thick0"].values[0]
    ferrite_side_thick1 = raw_data["ferrite_side_thick1"].values[0]
 

    #FIXME : add some variables


    #0.5 Config Identifier-Variable set.
    config = {
        "$VERSION_IDX_STR"  :   version_idx_str,
        "$coil_width0"  :  coil_width0,
        "$coil_width1"  :  coil_width1,
        "$length0"  :  length0,
        "$length1"  :  length1,
        "$width0"  :  width0,
        "$width1"  :  width1,
        "$coil_offset0"  :  coil_offset0,
        "$coil_offset1"  :  coil_offset1,
        "$turn_length_gap0"  :  turn_length_gap0,
        "$turn_length_gap1"  :  turn_length_gap1,
        "$turn_width_gap0"  :  turn_width_gap0,
        "$turn_width_gap1"  :  turn_width_gap1,
        "$ferrite_thick0"  :  ferrite_thick0,
        "$ferrite_thick1"  :  ferrite_thick1,
        "$ferrite_length_margin0"  :  ferrite_length_margin0,
        "$ferrite_length_margin1"  :  ferrite_length_margin1,
        "$ferrite_width_margin0"  :  ferrite_width_margin0,
        "$ferrite_width_margin1"  :  ferrite_width_margin1,
        "$ferrite_side_height0"  :  ferrite_side_height0,
        "$ferrite_side_height1"  :  ferrite_side_height1,
        "$ferrite_side_thick0"  :  ferrite_side_thick0,
        "$ferrite_side_thick1"  :  ferrite_side_thick1,
        "$Itx"  :  Itx,
        "$Irx"  :  Irx,
        "$air_gap" : air_gap
    
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


    temp1 = pd.read_csv(f'.\\ML_data\\inductance{version_idx_str}_dat.csv', sep=",")
    temp1 = temp1.to_numpy()
    temp2 = pd.read_csv(f'.\\ML_data\\loss{version_idx_str}_dat.csv', sep=",")
    temp2 = temp2.to_numpy()


    parameter = np.array([Num, Itx, Irx, air_gap, coil_width0, coil_width1, length0, length1, width0, width1, coil_offset0, coil_offset1, turn_length_gap0, turn_length_gap1, + \
                          turn_width_gap0, turn_width_gap1, ferrite_thick0, ferrite_thick1, ferrite_length_margin0, ferrite_length_margin1, ferrite_width_margin0, ferrite_width_margin1, + \
                            ferrite_side_height0, ferrite_side_height1, ferrite_side_thick0, ferrite_side_thick1, +\
                            raw_data["Lt"].values[0],raw_data["Lr"].values[0],raw_data["k"].values[0],raw_data["loss_tx"].values[0],raw_data["loss_rx"].values[0]]) # 25 parameter
    
    #temp = np.append(parameter,temp1[0][1])
    #temp = np.append(temp,temp1[0][2])
    #temp = np.append(temp,temp1[0][3])
    #temp = np.append(temp,temp2[0][2])
    #temp = np.append(temp,temp2[0][3])
    temp = np.concatenate((parameter,temp1[0][1],temp1[0][2],temp1[0][3],temp2[0][2],temp2[0][3]), axis=None)

    print(temp)


    data1 = np.loadtxt(f'Z:\\Autosimul_data\\LRT\HFSS_model_turn33_v1\\valid_data.csv', delimiter=",")
    new_data1 = np.vstack((data1, temp))
    np.savetxt(f'Z:\\Autosimul_data\\LRT\HFSS_model_turn33_v1\\valid_data.csv',new_data1,delimiter=",")
    #np.savetxt(f'temp.csv',[temp],delimiter=",")





for i in range(0, 101): 

    #run_simul(i)
    #print("end")


    try :
        try:
            os.remove(f'.\ML_aedt\ML17.aedt.lock')
        except:
            time.sleep(1)
        if os.path.isfile(f'.\ML_aedt\ML17.aedt') :
            os.remove(f'.\ML_aedt\ML17.aedt')
        time.sleep(1)	

        shutil.copy(f'.\ML_aedt\ML_ref.aedt',f'.\ML_aedt\ML17.aedt')
        time.sleep(1)

        try:
            run_simul(i)
        except Exception as e: 
            print(f'error number {i}')
            print(e)

        if os.path.isfile(f'.\ML_aedt\ML17.aedt') :
            os.remove(f'.\ML_aedt\ML17.aedt')
        time.sleep(1)	

        shutil.rmtree(f'.\ML_aedt\ML17.aedtresults')
        try:
            os.remove(f'.\ML_aedt\ML17.aedt.lock')
        except:
            time.sleep(1)
    except :
        time.sleep(1)	


    
    time.sleep(1)


os.system("pause")
