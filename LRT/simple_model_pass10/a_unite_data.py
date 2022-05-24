import os
import subprocess
import random
import csv
import time
import csv
import numpy as np
import math
import pandas

with open(f'.\inductance.csv',"a", encoding='utf-8', newline='') as f :
    for k in range (1,201) :
        with open(f'.\script{k}\ML_data\inductance.csv', "r") as infile:
            temp = infile.read()
            temp = temp.strip("0,0,0,0,0,0,0,0,0,0,0,0,0")
            temp = temp.strip(".000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00")
            f.write(temp)

with open(f'.\coupling.csv',"a", encoding='utf-8', newline='') as f :
    for k in range (1,201) :
        with open(f'.\script{k}\ML_data\coupling.csv', "r") as infile:
            temp = infile.read()
            temp = temp.strip("0,0,0,0,0,0,0,0,0,0,0,0,0")
            temp = temp.strip(".000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00")
            f.write(temp)

with open(f'.\loss.csv',"a", encoding='utf-8', newline='') as f :
    for k in range (1,201) :
        with open(f'.\script{k}\ML_data\loss.csv', "r") as infile:
            temp = infile.read()
            temp = temp.strip(".000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00")
            temp = temp.strip("0,0,0,0,0,0,0,0,0,0,0,0,0")
            f.write(temp)