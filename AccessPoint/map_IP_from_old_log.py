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


PATH_ACCESS_LOG_FILE = '/home/moojokeubuntu/KU/Year4_1/Prep/AccesspointLog/Project/AccessPointLogs/%s'
PATH_OUT_LOG = '/home/moojokeubuntu/KU/4_2/RealProject/accesspoint/Data'

def readfile():
    list_file_name = ["accesspoint.log-20161118",
    "accesspoint.log-20161119", 
    "accesspoint.log-20161120", 
    "accesspoint.log-20161121", 
    "accesspoint.log-20161122", 
    "accesspoint.log-20161123", 
    "accesspoint.log-20161124", 
    "accesspoint.log-20161125", 
    "accesspoint.log-20161126", 
    "accesspoint.log-20161127", 
    "accesspoint.log-20161128", 
    "accesspoint.log-20161129", 
    "accesspoint.log-20161130", 
    "accesspoint.log-20161201", 
    "accesspoint.log-20161202", 
    "accesspoint.log-20161203", 
    "accesspoint.log-20161204", 
    "accesspoint.log-20161205", 
    "accesspoint.log-20161206", 
    "accesspoint.log-20161207", 
    "accesspoint.log-20161208", 
    "accesspoint.log-20161209", 
    "accesspoint.log-20161210", 
    "accesspoint.log-20161211", 
    "accesspoint.log-20161212", 
    "accesspoint.log-20161213", 
    "accesspoint.log-20161214", 
    "accesspoint.log-20161215", 
    "accesspoint.log-20161216", 
    "accesspoint.log-20161217", 
    "accesspoint.log-20161218", 
    "accesspoint.log-20161219", 
    "accesspoint.log-20161220", 
    "accesspoint.log-20161221", 
    "accesspoint.log-20161222", 
    "accesspoint.log-20161223", 
    "accesspoint.log-20161224", 
    "accesspoint.log-20161225", 
    "accesspoint.log-20161226", 
    "accesspoint.log-20161227", 
    "accesspoint.log-20161228", 
    "accesspoint.log-20161229", 
    "accesspoint.log-20161230", 
    "accesspoint.log-20161231", 
    "accesspoint.log-20170101", 
    "accesspoint.log-20170102", 
    "accesspoint.log-20170103", 
    "accesspoint.log-20170104", 
    "accesspoint.log-20170105", 
    "accesspoint.log-20170106", 
    "accesspoint.log-20170107", 
    "accesspoint.log-20170108", 
    "accesspoint.log-20170109", 
    "accesspoint.log-20170110", 
    "accesspoint.log-20170111", 
    "accesspoint.log-20170112", 
    "accesspoint.log-20170113", 
    "accesspoint.log-20170114", 
    "accesspoint.log-20170115", 
    "accesspoint.log-20170116", 
    "accesspoint.log-20170117", 
    "accesspoint.log-20170118", 
    "accesspoint.log-20170119", 
    "accesspoint.log-20170120", 
    "accesspoint.log-20170121", 
    "accesspoint.log-20170122", 
    "accesspoint.log-20170123", 
    "accesspoint.log-20170124", 
    "accesspoint.log-20170125", 
    "accesspoint.log-20170126", 
    "accesspoint.log-20170127", 
    "accesspoint.log-20170128", 
    "accesspoint.log-20170129", 
    "accesspoint.log-20170130", 
    "accesspoint.log-20170131", 
    "accesspoint.log-20170201", 
    "accesspoint.log-20170202", 
    "accesspoint.log-20170203", 
    "accesspoint.log-20170204", 
    "accesspoint.log-20170205", 
    "accesspoint.log-20170206", 
    "accesspoint.log-20170207", 
    "accesspoint.log-20170208", 
    "accesspoint.log-20170209", 
    "accesspoint.log-20170210", 
    "accesspoint.log-20170211", 
    "accesspoint.log-20170212", 
    "accesspoint.log-20170213", 
    "accesspoint.log-20170214", 
    "accesspoint.log-20170215"]

    list_access = {}
    for file_name in list_file_name:
        with open (PATH_ACCESS_LOG_FILE%(file_name),'r',encoding='utf-8', errors='ignore') as file:
            for line in file:
                line_split = line.split(",")
                if len(line_split)  == 6 :
                    first_extract = line_split[0].split(" ")
                    AP_Name = first_extract[7]
                    if AP_Name not in list_access.keys() :
                        print(AP_Name)
                        second_extract = line_split[1].split(" ")
                        MAC = second_extract[4]
                        list_access.update({AP_Name:MAC})
                #print(row_data)
    write_out(list_access)

def write_out(list_access):
    compath = os.path.join(PATH_OUT_LOG, 'map_MAC.txt')
    with open(compath,'a') as f:
        for i in list_access.keys():
            f.writelines(str(i)+" "+str(list_access[i])+'\n')

if __name__ == '__main__':
    readfile()