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



PATH_TO_LOG = '/home/moojokeubuntu/KU/4_2/RealProject/webpattern/Output_IP'
PATH_TO_SAVE = '/home/moojokeubuntu/KU/4_2/RealProject/webpattern/Graph'


def raedfile():
    y = []
    y_temp = []
    x = []
    x_temp = []
    count = 0
    temp = 0
    list_map_building = []
    compath = os.path.join(PATH_TO_LOG, 'user3.csv')
    with open(compath,'r') as f:
        reader = csv.reader(f)
        for i in reader:
            if len(i[0]) == 12 :
                print(i[0][8:])
                if temp != int(i[0][10:-1]) :
                    x.append(i[0][8:-2]+":"+i[0][10:])
                    y.append(int(i[1]))
            else :
                if temp != int(i[0][10:-3]) :
                    x.append(i[0][8:-4]+":"+i[0][10:-2])
                    y.append(int(i[1]))
            
    print(x)
    plot_map(x,y)

def plot_map(x,y):
    xlen = []
    new_x = []
    print(y)
    for i in range(len(x)):
        xlen.append(i)
    plt.title('Number of unique users in 1 day')
    plt.plot(xlen,y)
    xlim(0,len(x))
    x_new = []
    for i in x :
        s = i.split(':')
        if s[1] == "50":
            new_x.append(s[0])
        else :
            new_x.append('')
    print(new_x)
    plt.xticks(xlen, new_x,horizontalalignment='left',fontsize = 13)
    plt.xlabel('Time', fontsize=11)
    plt.ylabel('Number of unique users',fontsize=11)
    plt.grid()
    #ylim(0,6000)
    plt.show()
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