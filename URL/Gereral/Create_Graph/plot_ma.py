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

    x = ['0-3','3-6','6-9','9-12','12-15','15-18','18-21','21-24']
    y = [38201,11608,34954,230826,186014,145945,132870,108993]

    plot_map(x,y)

def plot_map(x,y):
    xlen = []
    aver = sum(y) / float(len(y))
    #aver = 458.3256282806
    print(aver)
    print(y)
    for i in range(len(x)):
        xlen.append(i)
    #print(xlen)
    #plt.plot([0, len(x)], [aver, aver], lw=1 ,color = "red",label = "Average")
    plt.title('Unusual Web Log')
    plt.bar(xlen,y)
    plt.xticks(xlen, x,rotation=90,horizontalalignment='left')
    plt.xlabel('Time')
    plt.ylabel('Number of unusual log')
    matplotlib.rcParams.update({'font.size': 16})
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