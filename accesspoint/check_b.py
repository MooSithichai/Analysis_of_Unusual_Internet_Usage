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
import scipy
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
import random
from itertools import cycle



PATH_MAP = '/home/moojokeubuntu/KU/4_2/RealProject/accesspoint/Data'
PATH_MAP2 = '/home/moojokeubuntu/KU/4_2/RealProject/accesspoint/Moving_each_ap/20-24/small'

def raedfile():
    p = []
    x = []
    y = []
    compath = os.path.join(PATH_MAP2, 'cc.txt')
    with open(compath,'r') as f:
        for line in f :
            row_data = {}
            line_split = line.split(' ')
            row_data['Building'] = line_split[0]
            row_data['Count'] = int(line_split[1])
            p.append(row_data)
    sort = sorted(p, key=lambda x:(x['Count'],x['Building']) ,reverse = True)
    print(sort)
    for i in range(len(sort)):
        x.append(sort[i]['Building'])
        y.append(int(sort[i]['Count']))
    xlen = []
    for i in range(len(x)):
        xlen.append(i)
    plt.title('Error Logs Count in Each Building')
    plt.bar(xlen,y, color = numpy.random.rand(3,1))
    plt.xticks(xlen, x,rotation=90,horizontalalignment='left')
    plt.xlabel('Building')
    plt.ylabel('Number of Error Logs')
    matplotlib.rcParams.update({'font.size': 12})
    cycol = cycle('bgrcmk')
    plt.legend()
    plt.show()


def random_color():
    rgbl=[255,0,0]
    random.shuffle(rgbl)
    print(tuple(rgbl))
    return tuple(rgbl)

def raedfile2():
    list_map_building = []
    unique = []
    compath = os.path.join(PATH_MAP2, 'map.txt')
    with open(compath,'r') as f:
        for line in f :
            row_data = {}
            line_split = line.split(',')
            AP_name = line_split[0].strip("'")
            AP_name = AP_name.strip("('")
            Eng_name = line_split[2].strip("'")
            Eng_name = Eng_name.strip(" '")
            Thai_name = line_split[3].split("'")
            if Thai_name[0] != ' ':
                Thai_name = Thai_name[0]
            else :
                Thai_name = Thai_name[1]
            row_data['AP'] = AP_name
            row_data['ENG'] = Eng_name
            row_data['Thai'] = Thai_name
            if Eng_name not in unique :
                unique.append(Eng_name)
            list_map_building.append(row_data)
    print(unique)
    print(len(unique))

if __name__ == '__main__':
    raedfile()
    #raedfile2()
    #random_color()  