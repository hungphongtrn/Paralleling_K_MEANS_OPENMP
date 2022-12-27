import pandas as pd
import os
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

dataset_path = input('Enter a file path: ')
#/home/yuufongg/PARALLEL_PROGRAMMING_LTSS/dataset_50000_4.txt
#/home/yuufongg/PARALLEL_PROGRAMMING_LTSS/datasets/dataset_100000_4.txt

if os.path.exists(dataset_path):
    print("The file exists")

    dataset = pd.read_csv(dataset_path, sep=" ", header=None, on_bad_lines='skip')
    dataset.columns = ['X', 'Y', 'Z']
    print(dataset)
    fig = plt.figure(figsize=(10, 10))
    ax = plt.axes(projection='3d')
    ax.scatter3D(dataset['X'], dataset['Y'], dataset['Z'])
    plt.savefig("VISUALIZER")

else:
    raise FileNotFoundError('No such file or directory')
