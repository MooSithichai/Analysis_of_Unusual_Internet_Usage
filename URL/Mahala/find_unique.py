import csv
import pymongo
import os.path
import collections
import tldextract
import itertools
from urllib.parse import urlsplit
from urllib.parse import urlparse
from pymongo import MongoClient
from datetime import datetime
import timeit
import unicodedata
import gc


PATH_WEB_LOG_FILE = '/media/moojokeubuntu/AA6259046258D6A3/AnotherDrive/Project/weblog/data/weblog-20180312_2/12/%s'
PATH_WEB_LOG_FILE_2 = '/media/moojokeubuntu/AA6259046258D6A3/AnotherDrive/Project/weblog/data/weblog-20180319_2/19/%s'
PATH_SAVE_LOG = '/home/moojokeubuntu/KU/4_2/RealProject/webpattern/Detection/Input'
PATH_SAVE_LOG2 = '/home/moojokeubuntu/KU/4_2/RealProject/webpattern/Detection/Input/%s'

def readfile():

    list_folder_name = ["00%s",
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
    


    #list_folder_name = ["13%"s"%s","14%s","15%s"]
    #list_folder_name = ["20%s","21%s","22%s"]
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
    
    list_char = []
    count = 0
    list_sub_name = [".0.txt",".1.txt",".2.txt",".3.txt",".4.txt",".5.txt"]
    for folder in list_folder_name :
        for file_name in list_file_name :
            for minute in list_minute_name :
                for sub in list_sub_name :
                    with open (PATH_WEB_LOG_FILE%(folder%(file_name%(folder%(minute%(sub)))))) as file:  
                        for line in file.readlines():
                            #print(line)
                            line_split = line.split(" ")
                            #print(len(line_split))
                            if len(line_split) >= 17 :
                                if line_split[15] == 'GET':
                                    if line_split[4] != "-" :
                                        print(line_split[17])
                                        for j in line_split[17] :
                                            if j not in list_char:
                                                print(j)
                                                count += 1
                                                list_char.append(j)
    for folder in list_folder_name :
        for file_name in list_file_name :
            for minute in list_minute_name :
                for sub in list_sub_name :
                    with open (PATH_WEB_LOG_FILE_2%(folder%(file_name%(folder%(minute%(sub)))))) as file:  
                        for line in file.readlines():
                            #print(line)
                            line_split = line.split(" ")
                            #print(len(line_split))
                            if len(line_split) >= 17 :
                                if line_split[15] == 'GET':
                                    if line_split[4] != "-" :
                                        print(line_split[17])
                                        for j in line_split[17] :
                                            if j not in list_char:
                                                print(j)
                                                count += 1
                                                list_char.append(j)
    print(count)
    Write(list_char)
    

def Write(list_char):
    compath = os.path.join(PATH_SAVE_LOG, 'unique_all.txt')
    with open(compath,'a') as f:
        for key in list_char:
            f.writelines(key+'\n')    


if __name__ == '__main__':
    start = timeit.default_timer()
    readfile()
    #oopen()
    #test()
    stop = timeit.default_timer()
    print(stop - start)