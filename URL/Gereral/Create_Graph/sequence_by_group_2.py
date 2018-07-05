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
import numpy as numpy
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
    count = 0
    temp = 0 
    temp_value = 0
    list_map_building = []
    compath = os.path.join(PATH_TO_LOG, 'count_group_in_group.csv')
    with open(compath,'r') as f:
        reader = csv.reader(f)
        for i in reader:
            if len(y) == 0:
                y.append(int(i[1]))
                x.append(i[0])
            else :
                out = int(y[-1])
                y.append(int(i[1])+out)
                x.append(i[0])



    #plot_map(x_new,y_new)
    plot_map(x,y)

def plot_map(x,y):
    xlen = []
    print(y)
    for i in range(len(x)):
        xlen.append(i)
    #print(xlen)
    per = 95*y[-1]/100
    plt.title('Member in group')
    plt.plot(xlen,y)
    plt.xticks(xlen, x,rotation = 90 ,horizontalalignment='center',fontsize = 10)
    plt.plot([0, 58], [per, per], lw=2 ,color = "red",label='95%')
    c = 0
    for i in x :
        if i == '91':
            break
        else :
            c += 1
    print(c)
    plt.plot([58, 58], [0, per], lw=2 ,color = "red")
    plt.xlabel('Number of member in group', fontsize=11)
    plt.ylabel('Number of Group',fontsize=11)
    plt.legend()
    plt.show()
    grid(True)
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