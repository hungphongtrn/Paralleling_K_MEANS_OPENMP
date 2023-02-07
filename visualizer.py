import pandas as pd
import os
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

#/home/yuufongg/PARALLEL_PROGRAMMING_LTSS/datasets/dataset_50000_4.txt
#out_50000.txt


def delete_1st_line(dataset_path: str):
    with open(dataset_path, 'r+') as fp:
        # read an store all lines into list
        lines = fp.readlines()
        # move file pointer to the beginning of a file
        fp.seek(0)
        # truncate the file
        fp.truncate()

        # start writing lines except the first line
        # lines[1:] from line 2 to last line
        fp.writelines(lines[1:])

def visualize_dataset(dataset_path: str):
    #visualize the initial dataset
    if os.path.exists(dataset_path):
        # delete the first element of the dataset file
        delete_1st_line(dataset_path)
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

def visualize_output(output: str):
    if os.path.exists(dataset_path):
        # delete the first element of the dataset file
        delete_1st_line(dataset_path)
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
