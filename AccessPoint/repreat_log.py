from __future__ import division
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

PATH_MAP = '/home/moojokeubuntu/KU/4_2/RealProject/accesspoint/Data/'
PATH_TO_LOG = '/media/moojokeubuntu/AA6259046258D6A3/AnotherDrive/Project/accesslog/%s'
PATH_TO_SAVE = '/home/moojokeubuntu/KU/4_2/RealProject/accesspoint/Log_per_build/LWAPP-3-REPLAY_ERR'

def raedfile():
    list_map_building = []
    compath = os.path.join(PATH_MAP, 'map_MAC.txt')
    with open(compath,'r') as f:
        for line in f :
            row_data = {}
            line_split = line.split(' ')
            print(len(line_split))
            AP_name = line_split[1]
            row_data['AP'] = AP_name
            row_data['ENG'] = line_split[0]
            list_map_building.append(row_data)

    readAP(list_map_building)

def readAP(list_map_building):
    list_AP = []
    list_ap_u = {}
    count = 0
    list_name = ['aplog-20180420'
    ,'aplog-20180421','aplog-20180422','aplog-20180423','aplog-20180424']
    for filename in list_name :
        with open (PATH_TO_LOG%(filename),'r') as file:
            for line in file:
                if 'count' in line :
                    print(line)
                    line_split = line.split(" ")
                    print(len(line_split))
                    if len(line_split) == 28 :
                        row_data = {}
                        row_data['Month'] = line_split[0]
                        row_data['Day'] = line_split[1]
                        row_data['Time'] = line_split[2]
                        row_data['Count'] = line_split[24]
                        row_data['AP'] = line_split[27]
                        print(row_data['Count'])
                        print(row_data['AP'])
                        list_AP.append(row_data)
    
    mac_to_ap(list_map_building,list_AP)

def mac_to_ap(list_map_building,list_AP):
    for i in range(len(list_AP)):
        for j in range(len(list_map_building)):
            if list_AP[i]["AP"] == list_map_building[j]["AP"]:
                list_AP[i]["AP"] = list_map_building[j]["ENG"]
                print(list_AP[i]["AP"])

    save_to(list_AP)
            

def save_to(list_AP):
    compath = os.path.join(PATH_TO_SAVE, '20to24.txt')
    with open(compath,'a') as f:
        for i in range(len(list_AP)):
            f.writelines(str(list_AP[i]["Month"])+" "
            +str(list_AP[i]["Day"])+
            " "+str(list_AP[i]["Time"])+" "+str(list_AP[i]["AP"])+
            " "+str(list_AP[i]["Count"])+'\n')




def movingaverage(interval, window_size):

    window= numpy.ones(int(window_size))/float(window_size)
    return numpy.convolve(interval, window, 'same')


    
    
            
    #             print(row_data['Month'])
    #             #print(line_split)
    #             print(len(line_split))
    #             if len(line_split) not in list_ap_u.keys():
    #                 list_ap_u.update({len(line_split):line})
    #             if len(line_split) == 28 :
    #                 count += 1
    # # with open ("aa.txt",'a') as f:
    # #     for a in list_ap_u.keys():
    # #         f.writelines(str(a)+" "+list_ap_u[a]+'\n')
    # # print(list_ap_u)
    # print(count)

if __name__ == '__main__':
    raedfile()
    #readAP()    