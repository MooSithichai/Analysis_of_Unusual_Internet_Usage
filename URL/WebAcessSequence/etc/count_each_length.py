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
from Bio import pairwise2
from Bio.pairwise2 import format_alignment

PATH_SAVE_LOG = '/home/moojokeubuntu/KU/4_2/RealProject/webpattern/Reverse/%s'
PATH_OUT = '/home/moojokeubuntu/KU/4_2/RealProject/webpattern/Out_table'



def readfile():
    list_group = []
    list_file_name = [
    "5_13.txt_reverse_1.txt","5_13.txt_reverse_2.txt",
     "5_13.txt_reverse_3.txt",
     "5_13.txt_reverse_4.txt",
     "5_13.txt_reverse_5.txt",
     "5_13.txt_reverse_6.txt",
     "5_13.txt_reverse_7.txt",
     "5_13.txt_reverse_8.txt",
     "5_13.txt_reverse_9.txt",
     "5_13.txt_reverse_10.txt"
    , "5_13.txt_reverse_11.txt"
    , "5_13.txt_reverse_12.txt"
    , "5_13.txt_reverse_13.txt"
    , "5_13.txt_reverse_14.txt"
    , "5_13.txt_reverse_15.txt"
    , "5_13.txt_reverse_16.txt"
    , "5_13.txt_reverse_17.txt"
    , "5_13.txt_reverse_18.txt"
    , "5_13.txt_reverse_19.txt"
    , "5_13.txt_reverse_20.txt"
    , "5_13.txt_reverse_21.txt"
    , "5_13.txt_reverse_22.txt"
    , "5_13.txt_reverse_23.txt"
    , "5_13.txt_reverse_24.txt"
    , "5_13.txt_reverse_25.txt"
    , "5_13.txt_reverse_26.txt"
    , "5_13.txt_reverse_27.txt"
    , "5_13.txt_reverse_30.txt"
    , "5_13.txt_reverse_33.txt"
    , "5_13.txt_reverse_35.txt"
    , "5_13.txt_reverse_36.txt"
    , "5_13.txt_reverse_39.txt"
    , "5_13.txt_reverse_43.txt"
    , "5_13.txt_reverse_45.txt"
    , "5_13.txt_reverse_48.txt"
    , "5_13.txt_reverse_51.txt"
    , "5_13.txt_reverse_57.txt",
    "5_13.txt_reverse_64.txt"
    , "5_13.txt_reverse_66.txt"
    , "5_13.txt_reverse_67.txt"
    , "5_13.txt_reverse_69.txt"
    , "5_13.txt_reverse_74.txt"
    , "5_13.txt_reverse_86.txt"
    , "5_13.txt_reverse_90.txt"
    , "5_13.txt_reverse_95.txt"
    , "5_13.txt_reverse_102.txt"
    , "5_13.txt_reverse_110.txt"
    , "5_13.txt_reverse_133.txt"
    , "5_13.txt_reverse_202.txt"
    , "5_13.txt_reverse_231.txt"
    , "5_13.txt_reverse_410.txt"
    , "5_13.txt_reverse_465.txt"]

    temp = ""
    
    for file_name in list_file_name:
       
        with open (PATH_SAVE_LOG%(file_name),'r',encoding='utf-8', errors='ignore') as file:
            row_data = {} 
            print(file_name)
            for line in file :
                if ":" in line :
                    if list_group != []:
                        counter=collections.Counter(list_group)
                        sort = counter.most_common()
                        compath = os.path.join(PATH_OUT,temp+".txt")
                        with open(compath,'a') as f:
                            f.writelines(temp+'\n')
                            for key, value in sort:
                                f.writelines(str(key)+":"+str(value)+'\n')
                        list_group = []
                        line_split = line.split(" :")
                        temp = line_split[0]
                    else :
                        line_split = line.split(" :")
                        temp = line_split[0]
                elif line != '\n' :
                    line_split = line.split(",")
                    length  = len(line_split)
                    list_group.append(length)
                    
    counter=collections.Counter(list_group)
    sort = counter.most_common()
    compath = os.path.join(PATH_OUT,temp+".txt")
    with open(compath,'a') as f:
        f.writelines(temp+'\n')
        for key, value in sort:
            f.writelines(str(key)+":"+str(value)+'\n')
               
                    

if __name__ == '__main__':
    start = timeit.default_timer()
    readfile()
    stop = timeit.default_timer()
    print(stop - start)
        