import pandas as pd
import os
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


output = "/home/yuufongg/PARALLEL_PROGRAMMING_LTSS/out_50000.txt"
if os.path.exists(output):
    print("The file exists")
    dataset = pd.read_csv(output, sep=" ")
    dataset.columns = ['X', 'Y', 'Z', 'label']

s