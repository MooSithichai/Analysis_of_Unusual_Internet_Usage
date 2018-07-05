import csv
import os.path
import collections
import tldextract
import itertools
from urllib.parse import urlsplit
from urllib.parse import urlparse
from datetime import datetime
import json
import timeit
from pylab import plot, ylim, xlim, show, xlabel, ylabel, grid
from numpy import linspace, loadtxt, ones, convolve
import numpy as ny
import matplotlib
import pylab
import math
import matplotlib.pyplot as plt



PATH_TO_LOG = '/home/moojokeubuntu/KU/4_2/RealProject/webpattern/Count_sequence'
PATH_TO_SAVE = '/home/moojokeubuntu/KU/4_2/RealProject/webpattern/Graph'


def raedfile():
    y = []
    x = []
    z = 0
    y_temp = 0
    count = 0
    temp = 0 
    temp_value = 0
    list_map_building = []
    compath = os.path.join(PATH_TO_LOG, 'count_group_in_group.csv')
    with open(compath,'r') as f:
        reader = csv.reader(f)
        for i in reader:


            if int(i[0]) < 10 :
                y_temp += int(i[1])
            elif int(i[0]) == 10:
                y_temp += int(i[1])
                y.append(y_temp) 
                x.append('small')
            elif int(i[0]) > 10 and int(i[0]) < 100:
                y_temp += int(i[1])
            elif int(i[0]) == 100 :
                y_temp += int(i[1])
                y.append(y_temp) 
                x.append('medium')
            elif int(i[0]) > 100 and int(i[0]) < 1275:
                y_temp += int(i[1])
            elif int(i[0]) == 1275 :
                y_temp += int(i[1])
                y.append(y_temp) 
                x.append('large')



                


    print(x)
    print(y)
    x.reverse()
    y.reverse()
    x = ['Large','Medium','Small']
    y = [17,149,374]
    print(len(y))

    #plot_map(x_new,y_new)
    plot_map(x,y)

def plot_map(x,y):
    xlen = []
    print(y)
    print(len(x))
    per = y[-1]*95/100
    for i in range(len(x)):
        xlen.append(i)
    #print(xlen)
    plt.title('Number of members in group')
    plt.plot(xlen,y)
    plt.xticks(xlen, x,rotation = 90 ,horizontalalignment='center')
    plt.plot([0, 1.92], [per, per], lw=2 ,color = "red" ,label='95%')
    # y = ax+n
    n = per*3/374
    print(n)
    plt.plot([1.92, 1.92], [0, per], lw=2 ,color = "red")


    plt.xlabel('Group size')
    plt.ylabel('Number of members in group')
    matplotlib.rcParams.update({'font.size': 22})
    plt.legend()
    plt.show()
    plt.grid()
    # compath = os.path.join(PATH_TO_SAVE,'IP_in_day.png')
    # plt.savefig(compath)

#      #Replace default x-ticks with xs, then replace xs with labels
#     plt.yticks(ys)  
#     plt.xticks(xs, labels) #Replace default x-ticks with xs, then replace xs with labels
# plt.yticks(ys)


if __name__ == '__main__':
    start = timeit.default_timer()
    raedfile()
    stop = timeit.default_timer()
    print(stop - start)