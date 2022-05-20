import yaml
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
    with open(f'.\script1\ML_data\inductance.csv', "r") as infile:
        f.write(infile.read())
    with open(f'.\script2\ML_data\inductance.csv', "r") as infile:
        f.write(infile.read())
    with open(f'.\script3\ML_data\inductance.csv', "r") as infile:
        f.write(infile.read())
    with open(f'.\script4\ML_data\inductance.csv', "r") as infile:
        f.write(infile.read())
    with open(f'.\script5\ML_data\inductance.csv', "r") as infile:
        f.write(infile.read())
    with open(f'.\script6\ML_data\inductance.csv', "r") as infile:
        f.write(infile.read())
    with open(f'.\script7\ML_data\inductance.csv', "r") as infile:
        f.write(infile.read())
    with open(f'.\script8\ML_data\inductance.csv', "r") as infile:
        f.write(infile.read())
    with open(f'.\script9\ML_data\inductance.csv', "r") as infile:
        f.write(infile.read())
    with open(f'.\script10\ML_data\inductance.csv', "r") as infile:
        f.write(infile.read())
    with open(f'.\script11\ML_data\inductance.csv', "r") as infile:
        f.write(infile.read())
    with open(f'.\script12\ML_data\inductance.csv', "r") as infile:
        f.write(infile.read())
    with open(f'.\script13\ML_data\inductance.csv', "r") as infile:
        f.write(infile.read())
    with open(f'.\script14\ML_data\inductance.csv', "r") as infile:
        f.write(infile.read())
    with open(f'.\script15\ML_data\inductance.csv', "r") as infile:
        f.write(infile.read())

with open(f'.\coupling.csv',"a", encoding='utf-8', newline='') as f :
    with open(f'.\script1\ML_data\coupling.csv', "r") as infile:
        f.write(infile.read())
    with open(f'.\script2\ML_data\coupling.csv', "r") as infile:
        f.write(infile.read())
    with open(f'.\script3\ML_data\coupling.csv', "r") as infile:
        f.write(infile.read())
    with open(f'.\script4\ML_data\coupling.csv', "r") as infile:
        f.write(infile.read())
    with open(f'.\script5\ML_data\coupling.csv', "r") as infile:
        f.write(infile.read())
    with open(f'.\script6\ML_data\coupling.csv', "r") as infile:
        f.write(infile.read())
    with open(f'.\script7\ML_data\coupling.csv', "r") as infile:
        f.write(infile.read())
    with open(f'.\script8\ML_data\coupling.csv', "r") as infile:
        f.write(infile.read())
    with open(f'.\script9\ML_data\coupling.csv', "r") as infile:
        f.write(infile.read())
    with open(f'.\script10\ML_data\coupling.csv', "r") as infile:
        f.write(infile.read())
    with open(f'.\script11\ML_data\coupling.csv', "r") as infile:
        f.write(infile.read())
    with open(f'.\script12\ML_data\coupling.csv', "r") as infile:
        f.write(infile.read())
    with open(f'.\script13\ML_data\coupling.csv', "r") as infile:
        f.write(infile.read())
    with open(f'.\script14\ML_data\coupling.csv', "r") as infile:
        f.write(infile.read())
    with open(f'.\script15\ML_data\coupling.csv', "r") as infile:
        f.write(infile.read())

with open(f'.\loss.csv',"a", encoding='utf-8', newline='') as f :
    with open(f'.\script1\ML_data\loss.csv', "r") as infile:
        f.write(infile.read())
    with open(f'.\script2\ML_data\loss.csv', "r") as infile:
        f.write(infile.read())
    with open(f'.\script3\ML_data\loss.csv', "r") as infile:
        f.write(infile.read())
    with open(f'.\script4\ML_data\loss.csv', "r") as infile:
        f.write(infile.read())
    with open(f'.\script5\ML_data\loss.csv', "r") as infile:
        f.write(infile.read())
    with open(f'.\script6\ML_data\loss.csv', "r") as infile:
        f.write(infile.read())
    with open(f'.\script7\ML_data\loss.csv', "r") as infile:
        f.write(infile.read())
    with open(f'.\script8\ML_data\loss.csv', "r") as infile:
        f.write(infile.read())
    with open(f'.\script9\ML_data\loss.csv', "r") as infile:
        f.write(infile.read())
    with open(f'.\script10\ML_data\loss.csv', "r") as infile:
        f.write(infile.read())
    with open(f'.\script11\ML_data\loss.csv', "r") as infile:
        f.write(infile.read())
    with open(f'.\script12\ML_data\loss.csv', "r") as infile:
        f.write(infile.read())
    with open(f'.\script13\ML_data\loss.csv', "r") as infile:
        f.write(infile.read())
    with open(f'.\script14\ML_data\loss.csv', "r") as infile:
        f.write(infile.read())
    with open(f'.\script15\ML_data\loss.csv', "r") as infile:
        f.write(infile.read())





