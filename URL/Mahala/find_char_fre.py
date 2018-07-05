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
PATH_SAVE_LOG = '/home/moojokeubuntu/KU/4_2/RealProject/webpattern/Detection/Input2'
PATH_SAVE_LOG2 = '/home/moojokeubuntu/KU/4_2/RealProject/webpattern/Detection/Input2/%s'
PATH_TO_UNIQUE = '/home/moojokeubuntu/KU/4_2/RealProject/webpattern/Detection/Input'

def readfile():

    #list_folder_name = ["09%s"]


    #list_folder_name = ["13%s","14%s","15%s"]
    #list_folder_name = ["20%s","21%s","22%s"]
    list_folder_name = [
    # "00%s",
    #  "01%s",
    #  "02%s"]
    #  "03%s",
    #  "04%s",
    #  "05%s"]
    #  "06%s",
    #  "07%s",
    #  "08%s"]
    #  "09%s",
    #  "10%s",
    #  "11%s"]
    #  "12%s"]
    #  "13%s",
    #  "14%s"]
    #  "15%s",
     "16%s"]
    #  "17%s"]
    #  "18%s"]
    # "19%s"]
    # "20%s"]
    #  "21%s"]
    #  "22%s"]
    # "23%s"]

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
    
    list_string = []
    list_sub_name = [".0.txt",".1.txt",".2.txt",".3.txt",".4.txt",".5.txt"]
    for folder in list_folder_name :
        for file_name in list_file_name :
            for minute in list_minute_name :
                for sub in list_sub_name :
                    with open (PATH_WEB_LOG_FILE%(folder%(file_name%(folder%(minute%(sub))))),encoding='utf-8', errors='ignore') as file:  
                        count = 0 
                        for line in file.readlines():
                            count += 1
                            log_number_temp = file_name%(folder%(minute%(sub)))
                            log_number = log_number_temp[1:]+":"+str(count)
                            line_split = line.split(" ")
                            if len(line_split) >= 17 :
                                row_data = {}
                                if line_split[15] == 'GET':
                                    if line_split[4] != "-" :
                                        row_data['Log'] = log_number
                                        row_data['HTTP_request'] = line_split[17]
                                        list_string.append(row_data)
    write_be(list_string)
    unique_char_find(list_string)

def write_be(list_string):
    compath = os.path.join(PATH_SAVE_LOG, 'web_log_15to16_fix.txt')
    count = 0
    with open(compath,'a') as f:
        for i in range(len(list_string)):
            f.writelines(list_string[i]["Log"]+" "+list_string[i]["HTTP_request"]+'\n') 



def unique_char_find(list_string):

    list_unique = []
    # compath = os.path.join(PATH_TO_UNIQUE, 'unique.txt')
    # with open (compath , 'r') as f:
    #     for line in f :
    #         j = line.replace('\n','')
    #         list_unique.append(j)
    for i in range(len(list_string)):
        for j in list_string[i]['HTTP_request']:
            if j not in list_unique :
                list_unique.append(j)

    print(list_unique)
    print(len(list_unique))

    frequency_find(list_string,list_unique)


def test():
    list_m = []
    row_data = {}
    row_data['HTTP_request'] = 'abcdefg'
    list_m.append(row_data)
    row_data = {}
    row_data['HTTP_request'] = 'ab'
    list_m.append(row_data)
    row_data = {}
    row_data['HTTP_request'] = 'efg'
    list_m.append(row_data)
    row_data = {}
    list_n = ['a','b','c','d','e','f','g']
    frequency_find(list_m,list_n)

def frequency_find(list_string,list_unique):    
    co = 0
    for i in range(len(list_string)):
        
        row_data = {}
        #row_data["Log"] = list_string[i]["Log"]
        for k in list_unique:
            row_data[k] = 0
        print(len(row_data))
        print(list_string[i])
        for j in list_string[i]['HTTP_request']:
            for k in row_data :
                if j == k :
                    row_data[k] += 1
                    # print(k)
                    # print(row_data[k])
        #row_data["Log"] = list_string[i]["Log"]
        temp_char = sorted(row_data, key=len, reverse=True)
        temp_value = [ row_data[k] for k in temp_char ]
        compath = os.path.join(PATH_SAVE_LOG, 'test_15to16_fix.csv')
        with open(compath, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(temp_value)
        del temp_char 
        del temp_value
        del row_data


def oopen():
    count = 1
    with open(PATH_SAVE_LOG2%('test_9.csv'),'r') as f:
        reader = csv.reader(f)
        for i in reader:
            if count <= 3 :
                print(i)
                count += 1

if __name__ == '__main__':
    start = timeit.default_timer()
    readfile()
    #oopen()
    #test()
    stop = timeit.default_timer()
    print(stop - start)