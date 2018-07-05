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

#avereage in = 458.3256282806
# IPv4 = 516.0503343281
# IPv6 = 317.7723566131



PATH_TO_LOG = '/home/moojokeubuntu/KU/4_2/RealProject/webpattern/Output_IP'
PATH_TO_SAVE = '/home/moojokeubuntu/KU/4_2/RealProject/webpattern/Graph'


def raedfile():
    y = []
    x = []
    count = 0
    list_map_building = []
    compath = os.path.join(PATH_TO_LOG, 'count_IP.csv')
    with open(compath,'r') as f:
        reader = csv.reader(f)
        for i in reader:
            if len(x) == 0:
                print("1")
                count = 1
                x.append(i[1])
            else :
                #print(x[-1])
                #print(i[1])
                if i[1] == x[-1]:
                    count += 1
                    print(count)
                else:
                    #print("aa")
                    y.append(count)
                    if len(y) != 1:
                        x.append(i[1])
                    count = 1
    print(x[-1])
    x.reverse()
    y.reverse()
    print(x[-1])
    y_cum = []
    for i in range(len(x)):
        if len(y_cum) == 0:
            y_cum.append(int(y[i]))
        else :
            out = y_cum[-1]+int(y[i])
            y_cum.append(out)
    #print(y_cum)
    plot_map(x,y_cum)

def plot_map(x,y):
    xlen = []
    aver = sum(y) / float(len(y))
    per = 95*y[-1]/100
    #aver = 458.3256282806
    #print(aver)
    #print(y)
    for i in range(len(x)):
        xlen.append(i)
    #print(xlen)
    plt.plot([0, 2300], [per, per], lw=2 ,color = "red",label='95%')
    plt.plot([2300,2300 ], [0, per], lw=2 ,color = "red")
    plt.title('Number of IPs at different usage frequency')
    plt.plot(xlen,y)
    x_new = []
    for i in x:
        if int(i)%1000 == 0:
            x_new.append(i)
        else :
            x_new.append("")
        
    plt.xticks(xlen, x_new,rotation=90,horizontalalignment='left')
    plt.xlabel('Usage frequency')
    plt.ylabel('Number of IPs')
    plt.text(2300,per+10000,"x = 2300",fontsize=22)
    matplotlib.rcParams.update({'font.size': 22})
    plt.legend()
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