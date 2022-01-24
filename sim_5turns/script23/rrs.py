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

#from pycaret.regression import load_model


																																																

REFERENCE_SCRIPT_FILE_NAME = f'run_ansys_ref_N5.py'
    

def run_simul(version_idx_str):
    #0 Initialize random variables

    

    height = 34.2
    # airx = spacex*ratiox6*2.5
    # airy = spacey*ratio5*3
    # airz = 30

    # magx = spacex*ratiox5
    # magy = spacey*ratioy5

    N1 = 5


    freq = round(random.uniform(100, 500), 0)
    w1 = round(random.uniform(1.0, 5.0), 1)
    w2 = round(random.uniform(1.0, w1), 1)
    w3 = round(random.uniform(1.0, w2), 1)
    w4 = round(random.uniform(1.0, w3), 1)
    w5 = round(random.uniform(1.0, w4), 1)
    spacex = round(random.uniform(5, 30), 0)
    spacey = round(random.uniform(5, 30), 0)
    ratiox1p = round(random.uniform(0.5, 5.0), 2)
    ratiox1= ratiox1p
    ratiox2p = round(random.uniform(w1/spacex*1.500, 3.0), 2)
    ratiox2= ratiox1p+ratiox2p
    ratiox3p = round(random.uniform(w2/spacex*1.500, 2.0), 2)
    ratiox3= ratiox1p+ratiox2p+ratiox3p
    ratiox4p = round(random.uniform(w3/spacex*1.500, 1.0), 2)
    ratiox4= ratiox1p+ratiox2p+ratiox3p+ratiox4p
    ratiox5p = round(random.uniform(w4/spacex*1.500, 1.0), 2)
    ratiox5= ratiox1p+ratiox2p+ratiox3p+ratiox4p+ratiox5p
    ratiox6p = round(random.uniform(w5/spacex*1.500, 0.5), 2)
    ratiox6= ratiox1p+ratiox2p+ratiox3p+ratiox4p+ratiox5p+ratiox6p
    ratioy1p = round(random.uniform(0.5, 5.0), 2)
    ratioy1= ratioy1p
    ratioy2p = round(random.uniform(w1/spacey*1.500, 3.0), 2)
    ratioy2= ratioy1p+ratioy2p
    ratioy3p = round(random.uniform(w2/spacey*1.500, 2.0), 2)
    ratioy3= ratioy1p+ratioy2p+ratioy3p
    ratioy4p = round(random.uniform(w3/spacey*1.500, 1.0), 2)
    ratioy4= ratioy1p+ratioy2p+ratioy3p+ratioy4p
    ratioy5p = round(random.uniform(w4/spacey*1.500, 1.0), 2)
    ratioy5= ratioy1p+ratioy2p+ratioy3p+ratioy4p+ratioy5p

    X2freq = round(random.uniform(100, 500), 0)
    X2w1 = round(random.uniform(1.0, 5.0), 1)
    X2w2 = round(random.uniform(1.0, X2w1), 1)
    X2w3 = round(random.uniform(1.0, X2w2), 1)
    X2w4 = round(random.uniform(1.0, X2w3), 1)
    X2w5 = round(random.uniform(1.0, X2w4), 1)
    X2spacex = round(random.uniform(5, 30), 0)
    X2spacey = round(random.uniform(5, 30), 0)
    X2ratiox1p = round(random.uniform(0.5, 5.0), 2)
    X2ratiox1= X2ratiox1p
    X2ratiox2p = round(random.uniform(X2w1/X2spacex*1.500, 3.0), 2)
    X2ratiox2= X2ratiox1p+X2ratiox2p
    X2ratiox3p = round(random.uniform(X2w2/X2spacex*1.500, 2.0), 2)
    X2ratiox3= X2ratiox1p+X2ratiox2p+X2ratiox3p
    X2ratiox4p = round(random.uniform(X2w3/X2spacex*1.500, 1.0), 2)
    X2ratiox4= X2ratiox1p+X2ratiox2p+X2ratiox3p+X2ratiox4p
    X2ratiox5p = round(random.uniform(X2w4/X2spacex*1.500, 1.0), 2)
    X2ratiox5= X2ratiox1p+X2ratiox2p+X2ratiox3p+X2ratiox4p+X2ratiox5p
    X2ratiox6p = round(random.uniform(X2w5/X2spacex*1.500, 0.5), 2)
    X2ratiox6= X2ratiox1p+X2ratiox2p+X2ratiox3p+X2ratiox4p+X2ratiox5p+X2ratiox6p
    X2ratioy1p = round(random.uniform(0.5, 5.0), 2)
    X2ratioy1= X2ratioy1p
    X2ratioy2p = round(random.uniform(X2w1/X2spacey*1.500, 3.0), 2)
    X2ratioy2= X2ratioy1p+X2ratioy2p
    X2ratioy3p = round(random.uniform(X2w2/X2spacey*1.500, 2.0), 2)
    X2ratioy3= X2ratioy1p+X2ratioy2p+X2ratioy3p
    X2ratioy4p = round(random.uniform(X2w3/X2spacey*1.500, 1.0), 2)
    X2ratioy4= X2ratioy1p+X2ratioy2p+X2ratioy3p+X2ratioy4p
    X2ratioy5p = round(random.uniform(X2w4/X2spacey*1.500, 1.0), 2)
    X2ratioy5= X2ratioy1p+X2ratioy2p+X2ratioy3p+X2ratioy4p+X2ratioy5p


    X3freq = round(random.uniform(100, 500), 0)
    X3w1 = round(random.uniform(1.0, 5.0), 1)
    X3w2 = round(random.uniform(1.0, X3w1), 1)
    X3w3 = round(random.uniform(1.0, X3w2), 1)
    X3w4 = round(random.uniform(1.0, X3w3), 1)
    X3w5 = round(random.uniform(1.0, X3w4), 1)
    X3spacex = round(random.uniform(5, 30), 0)
    X3spacey = round(random.uniform(5, 30), 0)
    X3ratiox1p = round(random.uniform(0.5, 5.0), 2)
    X3ratiox1= X3ratiox1p
    X3ratiox2p = round(random.uniform(X3w1/X3spacex*1.500, 3.0), 2)
    X3ratiox2= X3ratiox1p+X3ratiox2p
    X3ratiox3p = round(random.uniform(X3w2/X3spacex*1.500, 2.0), 2)
    X3ratiox3= X3ratiox1p+X3ratiox2p+X3ratiox3p
    X3ratiox4p = round(random.uniform(X3w3/X3spacex*1.500, 1.0), 2)
    X3ratiox4= X3ratiox1p+X3ratiox2p+X3ratiox3p+X3ratiox4p
    X3ratiox5p = round(random.uniform(X3w4/X3spacex*1.500, 1.0), 2)
    X3ratiox5= X3ratiox1p+X3ratiox2p+X3ratiox3p+X3ratiox4p+X3ratiox5p
    X3ratiox6p = round(random.uniform(X3w5/X3spacex*1.500, 0.5), 2)
    X3ratiox6= X3ratiox1p+X3ratiox2p+X3ratiox3p+X3ratiox4p+X3ratiox5p+X3ratiox6p
    X3ratioy1p = round(random.uniform(0.5, 5.0), 2)
    X3ratioy1= X3ratioy1p
    X3ratioy2p = round(random.uniform(X3w1/X3spacey*1.500, 3.0), 2)
    X3ratioy2= X3ratioy1p+X3ratioy2p
    X3ratioy3p = round(random.uniform(X3w2/X3spacey*1.500, 2.0), 2)
    X3ratioy3= X3ratioy1p+X3ratioy2p+X3ratioy3p
    X3ratioy4p = round(random.uniform(X3w3/X3spacey*1.500, 1.0), 2)
    X3ratioy4= X3ratioy1p+X3ratioy2p+X3ratioy3p+X3ratioy4p
    X3ratioy5p = round(random.uniform(X3w4/X3spacey*1.500, 1.0), 2)
    X3ratioy5= X3ratioy1p+X3ratioy2p+X3ratioy3p+X3ratioy4p+X3ratioy5p


    X4freq = round(random.uniform(100, 500), 0)
    X4w1 = round(random.uniform(1.0, 5.0), 1)
    X4w2 = round(random.uniform(1.0, X4w1), 1)
    X4w3 = round(random.uniform(1.0, X4w2), 1)
    X4w4 = round(random.uniform(1.0, X4w3), 1)
    X4w5 = round(random.uniform(1.0, X4w4), 1)
    X4spacex = round(random.uniform(5, 30), 0)
    X4spacey = round(random.uniform(5, 30), 0)
    X4ratiox1p = round(random.uniform(0.5, 5.0), 2)
    X4ratiox1= X4ratiox1p
    X4ratiox2p = round(random.uniform(X4w1/X4spacex*1.500, 3.0), 2)
    X4ratiox2= X4ratiox1p+X4ratiox2p
    X4ratiox3p = round(random.uniform(X4w2/X4spacex*1.500, 2.0), 2)
    X4ratiox3= X4ratiox1p+X4ratiox2p+X4ratiox3p
    X4ratiox4p = round(random.uniform(X4w3/X4spacex*1.500, 1.0), 2)
    X4ratiox4= X4ratiox1p+X4ratiox2p+X4ratiox3p+X4ratiox4p
    X4ratiox5p = round(random.uniform(X4w4/X4spacex*1.500, 1.0), 2)
    X4ratiox5= X4ratiox1p+X4ratiox2p+X4ratiox3p+X4ratiox4p+X4ratiox5p
    X4ratiox6p = round(random.uniform(X4w5/X4spacex*1.500, 0.5), 2)
    X4ratiox6= X4ratiox1p+X4ratiox2p+X4ratiox3p+X4ratiox4p+X4ratiox5p+X4ratiox6p
    X4ratioy1p = round(random.uniform(0.5, 5.0), 2)
    X4ratioy1= X4ratioy1p
    X4ratioy2p = round(random.uniform(X4w1/X4spacey*1.500, 3.0), 2)
    X4ratioy2= X4ratioy1p+X4ratioy2p
    X4ratioy3p = round(random.uniform(X4w2/X4spacey*1.500, 2.0), 2)
    X4ratioy3= X4ratioy1p+X4ratioy2p+X4ratioy3p
    X4ratioy4p = round(random.uniform(X4w3/X4spacey*1.500, 1.0), 2)
    X4ratioy4= X4ratioy1p+X4ratioy2p+X4ratioy3p+X4ratioy4p
    X4ratioy5p = round(random.uniform(X4w4/X4spacey*1.500, 1.0), 2)
    X4ratioy5= X4ratioy1p+X4ratioy2p+X4ratioy3p+X4ratioy4p+X4ratioy5p


    #0.5 Config Identifier-Variable set.
    config = {
        "$VERSION_IDX_STR"  :   version_idx_str,
        "$N1"  :  N1,
        "$freq"  :  freq,
        "$height"  :  height,
        "$w1"  :  w1,
        "$w2"  :  w2,
        "$w3"  :  w3,
        "$w4"  :  w4,
        "$w5"  :  w5,
        "$spacex"  :  spacex,
        "$spacey"  :  spacey,
        "$ratiox1"  :  ratiox1,
        "$ratiox2"  :  ratiox2,
        "$ratiox3"  :  ratiox3,
        "$ratiox4"  :  ratiox4,
        "$ratiox5"  :  ratiox5,
        "$ratiox6"  :  ratiox6,
        "$ratioy1"  :  ratioy1,
        "$ratioy2"  :  ratioy2,
        "$ratioy3"  :  ratioy3,
        "$ratioy4"  :  ratioy4,
        "$ratioy5"  :  ratioy5,
        "$X2freq"  :  X2freq,
        "$X2w1"  :  X2w1,
        "$X2w2"  :  X2w2,
        "$X2w3"  :  X2w3,
        "$X2w4"  :  X2w4,
        "$X2w5"  :  X2w5,
        "$X2spacex"  :  X2spacex,
        "$X2spacey"  :  X2spacey,
        "$X2ratiox1"  :  X2ratiox1,
        "$X2ratiox2"  :  X2ratiox2,
        "$X2ratiox3"  :  X2ratiox3,
        "$X2ratiox4"  :  X2ratiox4,
        "$X2ratiox5"  :  X2ratiox5,
        "$X2ratiox6"  :  X2ratiox6,
        "$X2ratioy1"  :  X2ratioy1,
        "$X2ratioy2"  :  X2ratioy2,
        "$X2ratioy3"  :  X2ratioy3,
        "$X2ratioy4"  :  X2ratioy4,
        "$X2ratioy5"  :  X2ratioy5,
        "$X3freq"  :  X3freq,
        "$X3w1"  :  X3w1,
        "$X3w2"  :  X3w2,
        "$X3w3"  :  X3w3,
        "$X3w4"  :  X3w4,
        "$X3w5"  :  X3w5,
        "$X3spacex"  :  X3spacex,
        "$X3spacey"  :  X3spacey,
        "$X3ratiox1"  :  X3ratiox1,
        "$X3ratiox2"  :  X3ratiox2,
        "$X3ratiox3"  :  X3ratiox3,
        "$X3ratiox4"  :  X3ratiox4,
        "$X3ratiox5"  :  X3ratiox5,
        "$X3ratiox6"  :  X3ratiox6,
        "$X3ratioy1"  :  X3ratioy1,
        "$X3ratioy2"  :  X3ratioy2,
        "$X3ratioy3"  :  X3ratioy3,
        "$X3ratioy4"  :  X3ratioy4,
        "$X3ratioy5"  :  X3ratioy5,
        "$X4freq"  :  X4freq,
        "$X4w1"  :  X4w1,
        "$X4w2"  :  X4w2,
        "$X4w3"  :  X4w3,
        "$X4w4"  :  X4w4,
        "$X4w5"  :  X4w5,
        "$X4spacex"  :  X4spacex,
        "$X4spacey"  :  X4spacey,
        "$X4ratiox1"  :  X4ratiox1,
        "$X4ratiox2"  :  X4ratiox2,
        "$X4ratiox3"  :  X4ratiox3,
        "$X4ratiox4"  :  X4ratiox4,
        "$X4ratiox5"  :  X4ratiox5,
        "$X4ratiox6"  :  X4ratiox6,
        "$X4ratioy1"  :  X4ratioy1,
        "$X4ratioy2"  :  X4ratioy2,
        "$X4ratioy3"  :  X4ratioy3,
        "$X4ratioy4"  :  X4ratioy4,
        "$X4ratioy5"  :  X4ratioy5,


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
    ref_script_str = "\n".join(lines);

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

    # ==============================
    # ===== export field data =====
    # ==============================

    if os.path.isfile(".\\data_temp\\Hfield4.fld") == False :
        return

    # ==== post processing (field data) =====
                                                                                                                                                                                            
    text_file_path = [".\\data_temp\\Hfield1.fld",".\\data_temp\\Hfield2.fld",".\\data_temp\\Hfield3.fld",".\\data_temp\\Hfield4.fld"]

    for i in np.arange(4) :

        raw_data = pd.read_csv(text_file_path[i], sep=" ")
        raw_data = raw_data[1:].to_numpy()
        raw_data = raw_data[:,0:5]

        raw_data = pd.DataFrame(
                raw_data,
                columns =
                    ['X', 'Y', 'Z', 'NaN', 'field']
                )
        raw_data = raw_data.drop("NaN",axis=1)

        raw_data = raw_data.to_numpy()
        raw_data = raw_data[:,3].reshape(1,128,128,10)

        np.save(f'..\\data\\script23\\field\\data_field_{4*version_idx_str+i}.npy', raw_data.astype(np.float) )

        if i==0 :
            input = np.concatenate((4*version_idx_str+0,N1,freq,w1,w2,w3,w4,w5,spacex,spacey,ratiox1,ratiox2,ratiox3,ratiox4,ratiox5,ratiox6,ratioy1,ratioy2,ratioy3,ratioy4,ratioy5),axis=None)
        elif i==1 : 
            input = np.concatenate((4*version_idx_str+1,N1,X2freq,X2w1,X2w2,X2w3,X2w4,X2w5,X2spacex,X2spacey,X2ratiox1,X2ratiox2,X2ratiox3,X2ratiox4,X2ratiox5,X2ratiox6,X2ratioy1,X2ratioy2,X2ratioy3,X2ratioy4,X2ratioy5),axis=None)
        elif i==2 :
            input = np.concatenate((4*version_idx_str+2,N1,X3freq,X3w1,X3w2,X3w3,X3w4,X3w5,X3spacex,X3spacey,X3ratiox1,X3ratiox2,X3ratiox3,X3ratiox4,X3ratiox5,X3ratiox6,X3ratioy1,X3ratioy2,X3ratioy3,X3ratioy4,X3ratioy5),axis=None)     
        elif i==3 :
            input = np.concatenate((4*version_idx_str+3,N1,X4freq,X4w1,X4w2,X4w3,X4w4,X4w5,X4spacex,X4spacey,X4ratiox1,X4ratiox2,X4ratiox3,X4ratiox4,X4ratiox5,X4ratiox6,X4ratioy1,X4ratioy2,X4ratioy3,X4ratioy4,X4ratioy5),axis=None)
    
        np.save(f'..\\data\\script23\\input\\data_input_{4*version_idx_str+i}.npy', input.astype(np.float) )
    


    # ==============================
    # ===== RL data export =====
    # ==============================

    temp1 = pd.read_csv(f'.\\data_temp\\RLdata1.csv', sep=",")
    temp1 = temp1.to_numpy()
    temp2 = pd.read_csv(f'.\\data_temp\\RLdata2.csv', sep=",")
    temp2 = temp2.to_numpy()
    temp3 = pd.read_csv(f'.\\data_temp\\RLdata3.csv', sep=",")
    temp3 = temp3.to_numpy()
    temp4 = pd.read_csv(f'.\\data_temp\\RLdata4.csv', sep=",")
    temp4 = temp4.to_numpy()

    temp1 = np.concatenate((N1,freq,w1,w2,w3,w4,w5,spacex,spacey,ratiox1,ratiox2,ratiox3,ratiox4,ratiox5,ratiox6,ratioy1,ratioy2,ratioy3,ratioy4,ratioy5,temp1[0][1],temp1[0][2]),axis=None)
    print(temp1)
    temp2 = np.concatenate((N1,X2freq,X2w1,X2w2,X2w3,X2w4,X2w5,X2spacex,X2spacey,X2ratiox1,X2ratiox2,X2ratiox3,X2ratiox4,X2ratiox5,X2ratiox6,X2ratioy1,X2ratioy2,X2ratioy3,X2ratioy4,X2ratioy5,temp2[0][1],temp2[0][2]),axis=None)
    temp3 = np.concatenate((N1,X3freq,X3w1,X3w2,X3w3,X3w4,X3w5,X3spacex,X3spacey,X3ratiox1,X3ratiox2,X3ratiox3,X3ratiox4,X3ratiox5,X3ratiox6,X3ratioy1,X3ratioy2,X3ratioy3,X3ratioy4,X3ratioy5,temp3[0][1],temp3[0][2]),axis=None)
    temp4 = np.concatenate((N1,X4freq,X4w1,X4w2,X4w3,X4w4,X4w5,X4spacex,X4spacey,X4ratiox1,X4ratiox2,X4ratiox3,X4ratiox4,X4ratiox5,X4ratiox6,X4ratioy1,X4ratioy2,X4ratioy3,X4ratioy4,X4ratioy5,temp4[0][1],temp4[0][2]),axis=None)

    with open(f'.\\ML_data\\data_RL.csv',"a", encoding='utf-8', newline='') as f :
        wr = csv.writer(f)
        wr.writerow(temp1)
        wr.writerow(temp2)
        wr.writerow(temp3)
        wr.writerow(temp4)

    # ==============================
    # ==============================



for i in range(0, 10000): 

    #run_simul(i)
    #print("end")


    try :
        try:
            os.remove(f'.\data_temp\Hfield1.fld')
            os.remove(f'.\data_temp\Hfield2.fld')
            os.remove(f'.\data_temp\Hfield3.fld')
            os.remove(f'.\data_temp\Hfield4.fld')
            os.remove(f'.\data_temp\RLdata1.csv')
            os.remove(f'.\data_temp\RLdata2.csv')
            os.remove(f'.\data_temp\RLdata3.csv')
            os.remove(f'.\data_temp\RLdata4.csv')
        except:
            time.sleep(1)
        try:
            os.remove(f'.\ML_aedt\ML23.aedt.lock')
        except:
            time.sleep(1)
        if os.path.isfile(f'.\ML_aedt\ML23.aedt') :
            os.remove(f'.\ML_aedt\ML23.aedt')
        time.sleep(1)	

        shutil.copy(f'.\ML_aedt\ML_ref.aedt',f'.\ML_aedt\ML23.aedt')
        time.sleep(1)

        run_simul(i)

        if os.path.isfile(f'.\ML_aedt\ML23.aedt') :
            os.remove(f'.\ML_aedt\ML23.aedt')
        time.sleep(1)	

        shutil.rmtree(f'.\ML_aedt\ML23.aedtresults')
        try:
            os.remove(f'.\ML_aedt\ML23.aedt.lock')
        except:
            time.sleep(1)
    except :
        time.sleep(1)	


    
    time.sleep(1)


os.system("pause")
