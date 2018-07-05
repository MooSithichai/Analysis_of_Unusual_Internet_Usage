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

PATH_WEB_LOG_FILE = '/media/moojokeubuntu/AA6259046258D6A3/AnotherDrive/Project/weblog/data/weblog-20180312_2/12/%s'
PATH_SAVE_LOG = '/home/moojokeubuntu/KU/4_2/RealProject/webpattern/Output_robot'

def readFile():

    # list_folder_name = ["09%s",
    # "10%s",
    # "11%s"]

    #list_folder_name = ["12%s"]

    list_folder_name = ["13%s","14%s","15%s"]

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
    

    list_sub_name = [".0.txt",".1.txt",".2.txt",".3.txt",".4.txt",".5.txt"]

    list_data = []
    list_save = []
    list_unique_len = []

    for folder in list_folder_name :
        for file_name in list_file_name :
            for minute in list_minute_name :
                for sub in list_sub_name :
                    #print(PATH_WEB_LOG_FILE%folder%file_name%folder%minute%sub)  

                    with open (PATH_WEB_LOG_FILE%(folder%(file_name%(folder%(minute%(sub))))),'r',encoding='utf-8', errors='ignore') as file:   
                        for line in file:
                            if 'robots.txt' in line :
                                list_data.append(line)
                           
    write_file(list_data)

def write_file(list_data):
    compath = os.path.join(PATH_SAVE_LOG, 'robots_13to16.txt')
    count = 0
    with open(compath,'a') as f:
        for i in range(len(list_data)):
            f.writelines(list_data[i]+'\n')


    

if __name__ == '__main__':
    start = timeit.default_timer()
    readFile()
    #check_user([{'time': '201803120900.2', 'IP': '1.0.213.87', 'Request': 'GET', 'domain': 'ku'},{'time': '201803121000.2', 'IP': '1.0.213.87', 'Request': 'GET', 'domain': 'ku'},{'time': '201803121000.5', 'IP': '1.0.213.87', 'Request': 'GET', 'domain': 'ku'},{'time': '201803121100.2', 'IP': '1.0.213.87', 'Request': 'GET', 'domain': 'ku'},{'time': '201803120900.3', 'IP': '1.0.213.87', 'Request': 'GET', 'domain': 'sa'}])
    #cal_time('201803120900.2')
    stop = timeit.default_timer()
    print(stop - start)
    #readAllurl()