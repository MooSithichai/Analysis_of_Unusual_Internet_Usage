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







PATH_MAP = '/home/moojokeubuntu/KU/4_2/RealProject/accesspoint/Data'
PATH_TO_LOG = '/media/moojokeubuntu/AA6259046258D6A3/AnotherDrive/Project/accesslog/%s'
PATH_TO_ERR = '/home/moojokeubuntu/KU/4_2/RealProject/accesspoint/Log_per_build/LWAPP-3-REPLAY_ERR/%s'
PATH_TO_SAVE1 = '/home/moojokeubuntu/KU/4_2/RealProject/accesspoint/Moving_each_ap/20-24/small'
PATH_TO_SAVE2 = '/home/moojokeubuntu/KU/4_2/RealProject/accesspoint/Moving_each_ap/20-24/middle'
PATH_TO_SAVE3 = '/home/moojokeubuntu/KU/4_2/RealProject/accesspoint/Moving_each_ap/20-24/large'


def raedfile():
    list_map_building = []
    compath = os.path.join(PATH_MAP, 'map.txt')
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
            list_map_building.append(row_data)
            print(Thai_name)
    readAP(list_map_building)

def readAP(list_map_building):
    list_use = []
    with open (PATH_TO_ERR%('20to24.txt'),'r') as file:
        for line in file:
            line_split = line.split(" ")
            
            print(line_split)
            if len(line_split) == 5 :
                time = "Apr 12 2018"+" "+line_split[2] 
                AP = line_split[3]
                count = line_split[4].replace('\n','')
                row_data = {}
                row_data["Time"] = time
                row_data["Count"] = count
                for i in range(len(list_map_building)):
                    if AP == list_map_building[i]["AP"]:
                        AP = list_map_building[i]["ENG"]
                row_data["Build"] = AP
                if row_data["Build"] ==  '':
                    print('aaaa')
                list_use.append(row_data)
    pllot(list_use)

def movingaverage(interval, window_size):
    window= numpy.ones(int(window_size))/float(window_size)
    return numpy.convolve(interval, window, 'same')

def fftconvolve_sma(array, period):    
    return scipy.signal.fftconvolve(
        array, np.ones((period,))/period, mode='valid')    

def pllot(list_use):
    list_new = []
    sort = sorted(list_use, key=lambda x:(x['Build'],x['Time'],x['Count']))
    #print(sort)
    for i in range(len(sort)-1):
        # print(sort[i]["Build"])
        # print(i)
        if sort[i]["Build"] == '':
            pass
        else :
            if sort[i]["Build"] == sort[i+1]["Build"] :
                list_new.append(sort[i])
            else :
                list_new.append(sort[i])
                #t = find_window(list_new)
                t = find_window_by_length(list_new)
                plot_per_build_5_day(list_new,t)
                del list_new
                list_new = []
                print(list_new)
    
    find_window(list_new)
    #t = find_window(list_new)
    t = find_window_by_length(list_new)
    plot_per_build_5_day(list_new,t)
    del list_new
    list_new = []

            
        

def plot_per_build_5_day(sort,t):
    x = []
    y = []
    count = 0
    sort1 = sorted(sort, key=lambda x:(x['Time'],x['Count']))
    #print(sort1)
    for i in range(len(sort1)):
        if ' 12 ' in sort1[i]['Time']:
            # print(len(sort1))
            count += 1
            x.append(sort1[i]['Time'])
            y.append(int(sort1[i]['Count']))
            # print(sort1[i]['Time'])
            # print(sort1[i]['Build'])
    #print(sort1)
    #print(x)
    DATE = [datetime.strptime(i,'%b %d %Y %H:%M:%S') for i in x]
    #print(DATE)
    #print(sort1[0]["Build"])
    a = find_window(sort1)
    #o = check_noise(y)
    #print("///////////////////////////////")
    #print(o)
    new_y = movingaverage(y,a)
    #print(new_y)
    #print(len(new_y))
    #print(y)
    #print(len(y))
    #new_y = fftconvolve_sma(y,o)
    #print(new_y)
    plot(DATE, y,"k.")
    plot(DATE,new_y,"r")
    xlim(datetime(2018, 4, 12, 0, 0, 0),datetime(2018, 4, 12, 23, 59, 59))
    ylim(0,300,10)
    xlabel("Time")
    ylabel("Number of Errors(Count)")
    # # grid(True)
    pylab.title(sort1[0]["Build"])
    compath3 = os.path.join(PATH_TO_SAVE1,'cc.txt')
    with open(compath3,'a') as f:
        f.writelines(str(sort1[0]["Build"])+" "+str(count)+'\n')
    if count <= 10 :      
        compath = os.path.join(PATH_TO_SAVE1, 'testplot_'+sort1[0]["Build"]+'.png')
        pylab.savefig(compath)
        plt.clf()
    elif count > 10 and count <= 100:
        compath = os.path.join(PATH_TO_SAVE2, 'testplot_'+sort1[0]["Build"]+'.png')
        pylab.savefig(compath)
        plt.clf()
    else :
        compath = os.path.join(PATH_TO_SAVE3, 'testplot_'+sort1[0]["Build"]+'.png')
        pylab.savefig(compath)
        plt.clf()
    #show()
    


def find_window(list_new):
    print(list_new)
    temp = 0
    list_av = []
    count = 1
    for i in range(len(list_new)-1):
        line = list_new[i]["Time"]
        line_spilt = line.split(" ")
        time = line_spilt[3]
        time_split = time.split(':')
        hour = time_split[0]
        # print(hour)
        # print("/////////////////////////////////////")
        # print(count)
        if temp == 0 :
            temp = hour
        else :
            if hour != temp :
                temp = hour
                list_av.append(count)
                count = 1
            else :
                count += 1
    list_av.append(count)
    a = int(sum(list_av)/len(list_av))

    #print(a)
    return a

def find_window_by_length(list_new):
    print(len(list_new))                
    if len(list_new) <= 3 :
        a = len(list_new)
    elif len(list_new) > 3 and len(list_new) > 20 :
        a = int(len(list_new)/2)
    elif len(list_new) > 20 and len(list_new) > 50 :
        a = 5
    else :
        a = 10
    return a

def check_noise(y):
    list_save = []
    
    min_x = 999999999
    max_x = 0
    temp = 0
    temp_2 = 0
    for i in range(len(y)):
        dict_save = {}
        new_y = movingaverage(y,i+1)
        st = numpy.std(new_y)
        noise = st/math.sqrt(len(y))
        if noise < min_x :
            min_x = noise
            temp = i+1
        if noise > max_x :
            max_x = noise
            temp_2 = i+1
        dict_save["num"] = i+1
        dict_save["noise"] = noise
        list_save.append(dict_save)
        print(i+1)
        print(noise)
    sort = sorted(list_save, key=lambda x:(x['noise'],x['num']))
    print(sort)
    med = int(len(sort)/2)
    print(med)
    print(len(sort))
    a = sort[med]
    print(a)
    t = sort[med]["num"]
    
    return t


if __name__ == '__main__':
    raedfile()
    #readAP()    