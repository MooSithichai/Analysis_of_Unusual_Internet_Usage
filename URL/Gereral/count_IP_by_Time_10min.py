import csv
import os.path
import collections
import tldextract
import itertools
from urllib.parse import urlsplit
from urllib.parse import urlparse
from datetime import datetime
import timeit
import math
import operator

PATH_WEB_LOG_FILE = '/media/moojokeubuntu/AA6259046258D6A3/AnotherDrive/Project/weblog/data/weblog-20180312_2/12/%s'
PATH_SAVE_LOG = '/home/moojokeubuntu/KU/4_2/RealProject/webpattern/Output_IP'

def readFile():

    list_folder_name = [
     "00%s",
     "01%s",
     "02%s",
     "03%s",
     "04%s",
     "05%s",
     "06%s",
     "07%s",
     "08%s",
     "09%s",
     "10%s",
     "11%s",
     "12%s",
     "13%s",
     "14%s",
     "15%s",
     "16%s",
     "17%s",
     "18%s",
     "19%s",
     "20%s",
     "21%s",
     "22%s",
     "23%s"]

    list_file_name =["/web-20180312%s"]

    list_minute_name = ["00%s",
    "01%s",
    "02%s",
    "03%s",
    "04%s",
    "05%s",
    "06%s",
    "07%s",
    "08%s",
    "09%s",
    "10%s",
    "11%s",
    "12%s",
    "13%s",
    "14%s",
    "15%s",
    "16%s",
    "17%s",
    "18%s",
    "19%s",
    "20%s",
    "21%s",
    "22%s",
    "23%s",
    "24%s",
    "25%s",
    "26%s",
    "27%s",
    "28%s",
    "29%s",
    "30%s",
    "31%s",
    "32%s",
    "33%s",
    "34%s",
    "35%s",
    "36%s",
    "37%s",
    "38%s",
    "39%s",
    "40%s",
    "41%s",
    "42%s",
    "43%s",
    "44%s",
    "45%s",
    "46%s",
    "47%s",
    "48%s",
    "49%s",
    "50%s",
    "51%s",
    "52%s",
    "53%s",
    "54%s",
    "55%s",
    "56%s",
    "57%s",
    "58%s",
    "59%s"]
    

    list_sub_name = [".0.txt",".1.txt",".2.txt",".3.txt",".4.txt",".5.txt"]

    dict_time_in = {}
    dict_time_out = {}
    dict_time_in_v4 = {}
    dict_time_in_v6 = {}
    dict_time_out_v4 = {}
    dict_time_out_v6 = {}
    

    for folder in list_folder_name :
        for file_name in list_file_name :
            for minute in list_minute_name :
                for sub in list_sub_name :
                    #print(PATH_WEB_LOG_FILE%folder%file_name%folder%minute%sub)  
                    with open (PATH_WEB_LOG_FILE%(folder%(file_name%(folder%(minute%(sub))))),'r',encoding='utf-8', errors='ignore') as file:
                        IP_list = []
                        IP_list_out = []   
                        for line in file.readlines():
                            line_split = line.split(" ")
                            IP_in = line_split[10]
                            IP_out = line_split[11]
                            time = file_name%(folder%(minute%(sub)))
                            time_after = time[5:-4]
                            realtime = str(time_after.split(".txt")[0])
                            print(realtime)
                            if IP_in not in IP_list :
                                if realtime not in dict_time_in.keys() :
                                    dict_time_in[realtime] = 1
                                    if '.' in IP_in :
                                        if realtime not in dict_time_in_v4.keys():
                                            dict_time_in_v4[realtime] = 1
                                        else :
                                            dict_time_in_v4[realtime] += 1
                                    elif ':' in IP_in :
                                        if realtime not in dict_time_in_v6.keys():
                                            dict_time_in_v6[realtime] = 1
                                        else :
                                            dict_time_in_v6[realtime] += 1
                                elif realtime in dict_time_in.keys() :
                                    dict_time_in[realtime] += 1
                                    if '.' in IP_in :
                                        if realtime not in dict_time_in_v4.keys():
                                            dict_time_in_v4[realtime] = 1
                                        else :
                                            dict_time_in_v4[realtime] += 1
                                    elif ':' in IP_in :
                                        if realtime not in dict_time_in_v6.keys():
                                            dict_time_in_v6[realtime] = 1
                                        else :
                                            dict_time_in_v6[realtime] += 1
                                IP_list.append(IP_in)
                            if IP_out not in IP_list_out :
                                if realtime not in dict_time_out.keys() :
                                    dict_time_out[realtime] = 1
                                    if '.' in IP_out :
                                        if realtime not in dict_time_out_v4.keys():
                                            dict_time_out_v4[realtime] = 1
                                        else :
                                            dict_time_out_v4[realtime] += 1
                                    elif ':' in IP_out :
                                        if realtime not in dict_time_out_v6.keys():
                                            dict_time_out_v6[realtime] = 1
                                        else :
                                            dict_time_out_v6[realtime] += 1
                                elif realtime in dict_time_out.keys() :
                                    dict_time_out[realtime] += 1
                                    if '.' in IP_out :
                                        if realtime not in dict_time_out_v4.keys():
                                            dict_time_out_v4[realtime] = 1
                                        else :
                                            dict_time_out_v4[realtime] += 1
                                    elif ':' in IP_out :
                                        if realtime not in dict_time_out_v6.keys():
                                            dict_time_out_v6[realtime] = 1
                                        else :
                                            dict_time_out_v6[realtime] += 1
                                IP_list_out.append(IP_out)
                        del IP_list
                        del IP_list_out
            
    writee1(dict_time_in)
    writee2(dict_time_in_v4)
    writee3(dict_time_in_v6)
    writee4(dict_time_out)
    writee5(dict_time_out_v4)
    writee6(dict_time_out_v6)

def writee1(dict_IP):
    od = collections.OrderedDict(sorted(dict_IP.items()))
    print(od)
    compath = os.path.join(PATH_SAVE_LOG,'dict_time_in.csv')
    with open(compath,'w',newline = '') as csvfile:
        writer=csv.writer(csvfile)
        for (key,value) in od.items():
            writer.writerow([key,value])

def writee2(dict_IP):
    od = collections.OrderedDict(sorted(dict_IP.items()))
    compath = os.path.join(PATH_SAVE_LOG,'dict_time_in_v4.csv')
    with open(compath,'w',newline = '') as csvfile:
        writer=csv.writer(csvfile)
        for (key,value) in od.items():
            writer.writerow([key,value])

def writee3(dict_IP):
    od = collections.OrderedDict(sorted(dict_IP.items()))
    compath = os.path.join(PATH_SAVE_LOG,'dict_time_in_v6.csv')
    with open(compath,'w',newline = '') as csvfile:
        writer=csv.writer(csvfile)
        for (key,value) in od.items():
            writer.writerow([key,value])
def writee4(dict_IP):
    od = collections.OrderedDict(sorted(dict_IP.items()))
    compath = os.path.join(PATH_SAVE_LOG,'dict_time_out.csv')
    with open(compath,'w',newline = '') as csvfile:
        writer=csv.writer(csvfile)
        for (key,value) in od.items():
            writer.writerow([key,value])
def writee5(dict_IP):
    od = collections.OrderedDict(sorted(dict_IP.items()))
    #od = sorted(dict_IP.items(), key=operator.itemgetter(1) ,reverse=True)
    compath = os.path.join(PATH_SAVE_LOG,'dict_time_out_v4.csv')
    with open(compath,'w',newline = '') as csvfile:
        writer=csv.writer(csvfile)
        for (key,value) in od.items():
            writer.writerow([key,value])
def writee6(dict_IP):
    od = collections.OrderedDict(sorted(dict_IP.items()))
    #od = sorted(dict_IP.items(), key=operator.itemgetter(1) ,reverse=True)
    compath = os.path.join(PATH_SAVE_LOG,'dict_time_out_v6.csv')
    with open(compath,'w',newline = '') as csvfile:
        writer=csv.writer(csvfile)
        for (key,value) in od.items():
            writer.writerow([key,value])

                                
if __name__ == '__main__':
    start = timeit.default_timer()
    readFile()
    stop = timeit.default_timer()
    print(stop - start)