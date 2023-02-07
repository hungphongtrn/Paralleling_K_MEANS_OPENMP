"""
    Purpose: Python script to visualize comparison of execution time.
    Author: Tran Hung Phong
"""
import subprocess
import matplotlib.pyplot as plt
import shlex

sizes = [50000, 100000, 200000, 400000, 800000, 1000000]
threads = [1, 2, 4, 8, 16]

try:
    subprocess.call('rm ./time_seq.txt', shell=True)
except:
    print("exception")

for size in sizes:
    syntax = 'sh run_sequential.sh 10 datasets/dataset_' + str(size)+'_4.txt out_'+str(size)+'.txt cent_'+str(size)+'.txt'
    print("syntax:", syntax)
    subprocess.call(shlex.split(syntax))

try:
    subprocess.call('rm ./time_openmp.txt', shell=True)
except:
    print("exception")

for size in sizes:
    for thread in threads:
        syntax = 'sh run_omp.sh 10 '+str(thread)+' datasets/dataset_' + str(size)+'_4.txt out_'+str(size)+'.txt cent_'+str(size)+'.txt'
        print("syntax:", syntax)
        subprocess.call(shlex.split(syntax))

file_seq = "time_seq.txt"
file_openmp = "time_openmp.txt"
with open(file_seq) as f:
    sequential = f.readlines()
sequential = [x.strip() for x in sequential]
sequential = list(map(float, sequential))
print('sequential times:', sequential)

with open(file_openmp) as f:
    openmp = f.readlines()
openmp = [x.strip() for x in openmp]
openmp = list(map(float, openmp))
print('Openmp times:', openmp)
i = 0
num_proc = len(threads)
for t_s in sequential:
    print("size:", sizes[i])
    currentlist = openmp[i*num_proc:(i+1)*num_proc]
    print("current:", currentlist)
    speedup = [t_s/x for x in currentlist]
    eff = []
    for j in range(len(speedup)):
        eff.append(speedup[j]/threads[j])
    plt.plot(threads, eff, label='N='+str(sizes[i]))
    plt.scatter(threads, eff)
    print("speedup:", speedup)
    i += 1
plt.title("Efficiency versus Number of threads at varying N")

plt.legend(loc='upper right')
plt.xlabel("Number of threads")
plt.ylabel("Efficiency")
plt.savefig("TIMING")
