import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = 'BDNF_Concentrations_all_07.19.csv'
data = pd.read_csv(file_path)
print(data.head())
# Replace 'P' with 'A' in the 'Timepoint' column
data['Timepoint'] = data['Timepoint'].replace('P', 'A')
print(data.head())
# Find the number of individuals who have measurements for the acute response (PICU or other)
numE = data[data['Timepoint'] == 'A'].shape[0]
numSix =  data[data['Timepoint'] == '6M'].shape[0]
numTwelve = data[data['Timepoint'] == '12M'].shape[0]
print(numE,numSix,numTwelve)

# Results = 86 individuals most likely have measurements for all 3 timepoints - These individuals should be singled out for data analysis



 