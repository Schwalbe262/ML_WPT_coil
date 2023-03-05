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

    coil_width_range = [10, 40, 0.1, 1]
    length_range = [1000, 5000, 1, 0]
    width_range = [250, 800, 1, 0]
    coil_offset_range = [1, 30, 0.1, 1]
    turn_length_gap_range = [5, 100, 1, 0]
    turn_width_gap_range = [5, 60, 1, 0]
    ferrite_thick_range = [5, 50, 1, 0]
    ferrite_length_margin_range = [5, 200, 1, 0]
    ferrite_width_margin_range = [5, 100, 1, 0]
    ferrite_side_height_range = [10, 100, 1, 0]
    ferrite_side_thick_range = [5, 80, 1, 0]
    air_gap_range = [50, 300, 0.1, 1]
    current_range = [0, 700, 1, 0]




    # Design 1



    coil_width0 = random_choice(coil_width_range)
    coil_width1 = random_choice(coil_width_range)

    length0 = random_choice(length_range)
    length1 = random_choice(length_range)

    coil_offset0 = random_choice(coil_offset_range)
    coil_offset1 = random_choice(coil_offset_range)

    turn_length_gap0 = random_choice(turn_length_gap_range)
    turn_length_gap1 = random_choice(turn_length_gap_range)

    turn_width_gap0 = random_choice(turn_width_gap_range)
    turn_width_gap1 = random_choice(turn_width_gap_range)

    ferrite_thick0 = random_choice(ferrite_thick_range)
    ferrite_thick1 = random_choice(ferrite_thick_range)

    ferrite_length_margin0 = random_choice(ferrite_length_margin_range)
    ferrite_length_margin1 = random_choice(ferrite_length_margin_range)

    ferrite_width_margin0 = random_choice(ferrite_width_margin_range)
    ferrite_width_margin1 = random_choice(ferrite_width_margin_range)

    
    ferrite_side_height1 = random_choice(ferrite_side_height_range)

    ferrite_side_thick0 = random_choice(ferrite_side_thick_range)
    ferrite_side_thick1 = random_choice(ferrite_side_thick_range)

    Itx = random_choice(current_range)
    Irx = random_choice(current_range)


    if ferrite_side_height_range[0] > coil_width0 + coil_offset0 :
        ferrite_side_height0 = random_choice(ferrite_side_height_range)
    else :
        ferrite_side_height_range_temp = [coil_width0 + coil_offset0, 100, 1, 0]
        ferrite_side_height0 = random_choice(ferrite_side_height_range_temp)

    if ferrite_side_height_range[0] > coil_width1 + coil_offset1 :
        ferrite_side_height1 = random_choice(ferrite_side_height_range)
    else :
        ferrite_side_height_range_temp = [coil_width0 + coil_offset1, 100, 1, 0]
        ferrite_side_height1 = random_choice(ferrite_side_height_range_temp)



    if width_range[0] - 5*coil_width0 - 4*turn_width_gap0 > 2*coil_width0 :
        width0 = random_choice(width_range)
    else :
        width_range_temp = [round(5*coil_width0 - 4*turn_width_gap0) + 2*coil_width0, width_range[1], width_range[2], width_range[3]]
        width0 = random_choice(width_range_temp)

    if width_range[0] - 5*coil_width1 - 4*turn_width_gap1 > 2*coil_width1 :
        width1 = random_choice(width_range)
    else :
        width_range_temp = [round(5*coil_width1 - 4*turn_width_gap1) + 2*coil_width1, width_range[1], width_range[2], width_range[3]]
        width1 = random_choice(width_range_temp)

    
    if air_gap_range[0] + ferrite_side_height0 + ferrite_side_height1 > coil_offset0 + coil_offset1 + 2.5*(coil_width0 + coil_width1) + 5 : 
        air_gap = random_choice(air_gap_range)
    else :
        air_gap_range = [10*(coil_offset0 + coil_offset1 + 2.5*(coil_width0 + coil_width1) + 5 - ferrite_side_height0 - ferrite_side_height1)/10, air_gap_range[1], air_gap_range[2], air_gap_range[3]]
        air_gap = random_choice(air_gap_range)




    
    


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


    parameter = np.array([Itx, Irx, air_gap, coil_width0, coil_width1, length0, length1, width0, width1, coil_offset0, coil_offset1, turn_length_gap0, turn_length_gap1, + \
                          turn_width_gap0, turn_width_gap1, ferrite_thick0, ferrite_thick1, ferrite_length_margin0, ferrite_length_margin1, ferrite_width_margin0, ferrite_width_margin1, + \
                            ferrite_side_height0, ferrite_side_height1, ferrite_side_thick0, ferrite_side_thick1]) # 25 parameter
    
    #temp = np.append(parameter,temp1[0][1])
    #temp = np.append(temp,temp1[0][2])
    #temp = np.append(temp,temp1[0][3])
    #temp = np.append(temp,temp2[0][2])
    #temp = np.append(temp,temp2[0][3])
    temp = np.concatenate((parameter,temp1[0][1],temp1[0][2],temp1[0][3],temp2[0][2],temp2[0][3]), axis=None)

    print(temp)


    data1 = np.loadtxt(f'Z:\\Autosimul_data\\LRT\HFSS_model_turn33_v1\\{COMPUTER_NAME}\\script10\\result_data.csv', delimiter=",")
    new_data1 = np.vstack((data1, temp))
    np.savetxt(f'Z:\\Autosimul_data\\LRT\\HFSS_model_turn33_v1\\{COMPUTER_NAME}\\script10\\result_data.csv',new_data1,delimiter=",")
    #np.savetxt(f'temp.csv',[temp],delimiter=",")





for i in range(0, 10000): 

    #run_simul(i)
    #print("end")


    try :
        try:
            os.remove(f'.\ML_aedt\ML10.aedt.lock')
        except:
            time.sleep(1)
        if os.path.isfile(f'.\ML_aedt\ML10.aedt') :
            os.remove(f'.\ML_aedt\ML10.aedt')
        time.sleep(1)	

        shutil.copy(f'.\ML_aedt\ML_ref.aedt',f'.\ML_aedt\ML10.aedt')
        time.sleep(1)

        try:
            run_simul(i)
        except Exception as e: 
            print(f'error number {i}')
            print(e)

        if os.path.isfile(f'.\ML_aedt\ML10.aedt') :
            os.remove(f'.\ML_aedt\ML10.aedt')
        time.sleep(1)	

        shutil.rmtree(f'.\ML_aedt\ML10.aedtresults')
        try:
            os.remove(f'.\ML_aedt\ML10.aedt.lock')
        except:
            time.sleep(1)
    except :
        time.sleep(1)	


    
    time.sleep(1)


os.system("pause")
