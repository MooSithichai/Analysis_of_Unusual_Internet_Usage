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


PATH_MAP = '/home/moojokeubuntu/KU/4_2/RealProject/accesspoint/Data'
PATH_TO_LOG = '/media/moojokeubuntu/AA6259046258D6A3/AnotherDrive/Project/accesslog/%s'
PATH_TO_ERR = '/home/moojokeubuntu/KU/4_2/RealProject/accesspoint/Log_per_build/LWAPP-3-REPLAY_ERR/%s'
PATH_TO_SAVE = '/home/moojokeubuntu/KU/4_2/RealProject/accesspoint/Moving_each_ap/20-24'

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
                time = line_split[0]+" "+line_split[1]+ ' 2018'+" "+line_split[2] 
                AP = line_split[3]
                count = line_split[4].replace('\n','')
                row_data = {}
                row_data["Time"] = time
                row_data["Count"] = count
                for i in range(len(list_map_building)):
                    if AP == list_map_building[i]["AP"]:
                        AP = list_map_building[i]["ENG"]
                row_data["Build"] = AP
                list_use.append(row_data)
    pllot(list_use)

def movingaverage(interval, window_size):
    window= numpy.ones(int(window_size))/float(window_size)
    return numpy.convolve(interval, window, 'same')

def pllot(list_use):
    list_new = []
    sort = sorted(list_use, key=lambda x:(x['Build'],x['Time'],x['Count']))
    #print(sort)
    for i in range(len(sort)-1):
        print(sort[i]["Build"])
        print(i)
        if sort[i]["Build"] == sort[i+1]["Build"] :
            list_new.append(sort[i])
        else :
            list_new.append(sort[i])
            plot_per_build_3_day(list_new)
            del list_new
            list_new = []
    plot_per_build_3_day(list_new)
    del list_new
    list_new = []    
            
        

def plot_per_build_3_day(sort):
    x = []
    y = []
    count = 0
    sort1 = sorted(sort, key=lambda x:(x['Time'],x['Count']))
    print(len(sort1))
    #print(sort1)
    for i in range(len(sort1)):
        if ' 12 ' in sort1[i]['Time']:
            count += 1
            x.append(sort1[i]['Time'])
            y.append(int(sort1[i]['Count']))
            print(sort1[i]['Time'])
            print(sort1[i]['Build'])
    
    DATE = [datetime.strptime(i,'%b %d %Y %H:%M:%S') for i in x]
    print(DATE)
    #new_y = movingaverage(y,30)
    
    plot(DATE, y,"k.")
    #plot(DATE, new_y,"r")
    # myFmt = matplotlib.dates.DateFormatter('%H:%M')
    # matplotlib.pyplot.gca().xaxis.set_major_formatter(myFmt)
    xlim(datetime(2018, 4, 12, 0, 0, 0),datetime(2018, 4, 12, 23, 59, 59))
    #ax.set_xlim([datetime.date(2014, 1, 26), datetime.date(2014, 2, 1)])
    # xlabel("Months since Jan 1749.")
    # ylabel("No. of Sun spots")
    # grid(True)
    compath = os.path.join(PATH_TO_SAVE, 'testplot'+sort1[0]["Build"]+'.png')
    pylab.savefig(compath)
    show()


    


if __name__ == '__main__':
    raedfile()
    #readAP()    