
import matplotlib
matplotlib.use('Agg')
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
import pylab
import math
import matplotlib.pyplot as plt



PATH_TO_LOG = '/home/moojokeubuntu/KU/4_2/RealProject/webpattern/Output2/%s'
# PATH_TO_SAVE = '/home/moojokeubuntu/KU/4_2/RealProject/webpattern/Graph'

# PATH_TO_LOG = "/home/moojoke34/Project/web/Detection/Output2/%s"
PATH_TO_SAVE = "/home/moojoke34/Project/web/Detection/Output2"


def raedfile():
    y = []
    x = []
    count = 0
    
    list_file_name =[
    #     '21to224.txt', '22to234.txt', '23to244.txt',
    # "9to12.txt", 
    #     "9to12_2.txt",
    #     "9to123.txt",
    #     "9to124.txt",
    #     "9to125.txt",
    #     "9to126.txt",
    #     "9to127.txt",
    #     "9to128.txt",
    #     "9to129.txt", 
    #     "9to1210.txt", 
    #     "9to1211.txt", 
    #     "9to1212.txt", 
    #     "9to1213.txt", 
    #     "9to1214.txt", 
    #     "9to1215.txt", 
    #     "9to1216.txt", 
    #     "9to1217.txt", 
    # "9to1218.txt", 
    # "9to1219.txt", 
    # "9to1220.txt", 
    # "9to1221.txt", 
    # "9to1222.txt", 
    # "9to1223.txt", 
    # "9to1224.txt", 
    # "9to1225.txt", 
    # "9to1226.txt", 
    # "9to1227.txt", 
    # "9to1228.txt", 
    # "9to1229.txt", 
    # "9to1230.txt", 
    # "9to1231.txt", 
    # "9to1232.txt", 
    # "9to1233.txt", 
    # "9to1234.txt", 
    # "9to1235.txt", 
    # "9to1236.txt", 
    # "9to1237.txt",
    # "12to134.txt", "13to144.txt", "14to154.txt"]
    # "15to18_4.txt",
    # "15to18_5.txt"
    # ,"15to18_6.txt"
    # ,"15to18_7.txt"
    # ,"15to18_8.txt"
    # ,"15to18_9.txt"
    # ,"15to18_10.txt"
    # ,"15to18_11.txt"
    # ,"15to18_12.txt"
    # ,"15to18_13.txt"
    # ,"15to18_14.txt"
    # ,"15to18_15.txt"
    # ,"15to18_16.txt"
    # ,"15to18_17.txt"
    # ,"15to18_18.txt"
    # ,"15to18_19.txt"
    # ,"15to18_20.txt"
    # ,"15to18_21.txt"
    # ,"15to18_22.txt"
    # ,"15to18_23.txt"
    # ,"15to18_24.txt"
    # ,"15to18_25.txt"
    # ,"15to18_26.txt"
    # ,"15to18_27.txt"
    # ,"15to18_28.txt"
    # ,"15to18_29.txt"
    # ,"15to18_30.txt"
    # ,"15to18_31.txt"
    # ,"15to18_32.txt"
    # ,"15to18_33.txt"
    # ,"15to18_34.txt"
    # ,"15to18_35.txt"
    # ,"15to18_36.txt"
    # ,"15to18_37.txt"
    # ,"15to18_38.txt"
    # ,"15to18_39.txt"
    # ,"15to18_40.txt"
    # ,"15to18_41.txt"
    # ,"15to18_42.txt"
    # ,"15to18_43.txt"
    "18to194.txt", "19to204.txt", "20to214.txt"]
    # ,"0to3.txt","3to6.txt","6to9.txt"]


    for file_name in list_file_name:
        with open (PATH_TO_LOG%(file_name),'r') as f:
            reader = csv.reader(f)
            for i in reader:
                y.append(float(i[0]))
                print(i[0])
                count += 1
                # if count == 10000 :
                #     break
    m = max(y)
    print("average")
    aver = sum(y)/float(len(y))
    sd = numpy.std(y)
    print(aver)
    print(m)
    print(sd)
    print("////////////////")
    print(len(y))
    y_new = []
    cc = 0
    for i in y:
        if i > aver+(3*sd):
            cc += 1
    print(cc)
 
    # print(y)
    # plot_map(y)

def plot_map(y):
    xlen = []
    print(len(y))
    for i in range(len(y)):
       xlen.append(i)
    print(xlen)
    x_new = []
    for i in range(len(xlen)):
        if i%1000 == 0:
            x_new.append(i)
        else :
            x_new.append("")
    plt.title('Distance')
    plt.bar(xlen,y)
    plt.xticks(xlen, x_new,rotation = 90 ,horizontalalignment='center',fontsize = 7)
    plt.xlabel('Log', fontsize=11)
    #plt.xscale('log')
    plt.xticks([])
    plt.ylabel('Mahalanobis distance',fontsize=11)
    plt.show()
    plt.savefig("0to3_1.png")
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