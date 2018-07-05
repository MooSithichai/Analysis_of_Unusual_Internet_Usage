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

PATH_OUT_LOG = '/home/moojokeubuntu/KU/4_2/RealProject/webpattern/Reverse/%s'
PATH_OUT_LOG3 = '/home/moojokeubuntu/KU/4_2/RealProject/webpattern/Input_new/%s'
PATH_SAVE_LOG4 = '/home/moojokeubuntu/KU/4_2/RealProject/webpattern/Count_sub'

def readfile():
    list_file_name = ["5_13.txt_reverse_1.txt"
    , "5_13.txt_reverse_2.txt"
    , "5_13.txt_reverse_3.txt"
    , "5_13.txt_reverse_4.txt"
    , "5_13.txt_reverse_5.txt"
    , "5_13.txt_reverse_6.txt"
    , "5_13.txt_reverse_7.txt"
    , "5_13.txt_reverse_8.txt"
    , "5_13.txt_reverse_9.txt"
    , "5_13.txt_reverse_10.txt"
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
    , "5_13.txt_reverse_57.txt"
    , "5_13.txt_reverse_64.txt"
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
    , "5_13.txt_reverse_465.txt"
    ]
    uni = {}
    reverse = []
    with open (PATH_OUT_LOG3%('unicode_map_12.csv'),'r') as file:
        reader = csv.reader(file)
        for i in reader:
            uni.update({i[0]:i[1]})

    for file_name in list_file_name:
        with open (PATH_OUT_LOG%(file_name),'r',encoding='utf-8', errors='ignore') as file:
            list_use = []
            for line in file:
                temp_group = []
                temp_web_all = []
                if " :" in line :
                    line = line.replace(" :","")
                elif line == "\n" :
                    line = ""
                line = line.replace("\n","")
                web_access = line.split(",")
                print(web_access)
                
                for k in range(len(web_access)):
                    for j in uni :
                        if web_access[k] == j: 
                            print(web_access[k])
                            web_access[k] = uni[j]
                            
                my_list_str = ''.join(map(str, web_access))
                list_use.append(my_list_str)
        find_count(list_use,uni,file_name)

    

def find_count(list_use,uni,file_name):
    soor = sorted(list_use , key = len ,reverse=True)
    temp_anomaly = {}
    list_for_count = []
    for i in range(len(soor)) :
        for j in range(len(soor)):
            #if len(soor[i]) > max_length and len(soor[j]) > max_length:
            if soor[i] != soor[j] :
                if (soor[i],soor[j]) not in temp_anomaly and (soor[j],soor[i]) not in temp_anomaly:
                    GA = pairwise2.align.globalxx(soor[i], soor[j])
                    LA = pairwise2.align.localxx(soor[i], soor[j])
                    glob = GA[0][2]
                    start = 0
                    last =0
                    if len(LA) ==  0:
                        loc = 0 
                    else :
                        loc = LA[0][2]
                    list_temp_an = []
                    for a, b in zip(GA[0][0],GA[0][1]):
                        if a == b:
                            list_temp_an.append(a)
                            if start == 0:
                                start = len(list_temp_an)
                            last = len(list_temp_an)
                        else:
                            list_temp_an.append('-')
                    
                    new_temp = list_temp_an[start-1:last]
                    my_list_str = ''.join(map(str, new_temp)) 

                    temp_anomaly[(soor[i],soor[j])]=my_list_str
                    list_for_count.append(my_list_str)
                   
                        
                        
    
    print("finish_1")
    


    # with open("1.txt",'a') as f:
    #     for key in temp_anomaly:
    #         temp = ''
    #         for value in range(len(temp_anomaly[key])):
    #             if temp_anomaly[key][value] == "":
    #                 temp = ""
    #             else :
    #                 temp += temp_anomaly[key][value]+','
    #         temp = temp[:-1] 
    #         f.writelines(str(key)+" "+str(temp)+'\n')

    
    list_b = []

    # for k in range(len(list_for_count)):
    #     for i in list_for_count[k]:
    #         if len(list_for_count[k]) > 1:
    #             if i != '-':
    #                 for j in uni :
    #                     if i == uni[j]: 
    #                         list_a.append(j)
    #             else :
    #                 list_a.append('-')
    #     my_list_1 = ','.join(map(str, list_a))
    #     list_b.append(my_list_1)


    # with open("count_re.txt",'a') as f:
    #     counter=collections.Counter(list_b)
    #     for key in counter :
    #         f.writelines(str(key)+":"+str(counter[key])+'\n')

    compath = os.path.join(PATH_SAVE_LOG4, file_name+"_count_in.txt")
        
    with open(compath,'a') as f:
        zz = [(k, len(list(v))) for k, v in itertools.groupby(sorted(temp_anomaly.values()))]
        zz = sorted(zz,key=lambda x:x[1])
        for k in zz:
            list_a = []
            for i in k[0]:
                if i != '-':
                    for j in uni :
                        if i == uni[j]: 
                            list_a.append(j)
                else :
                    list_a.append('-')
            if len(k[0]) > 1:
                my_list_1 = ','.join(map(str, list_a))
                f.writelines(str(my_list_1)+":"+str(k[1])+'\n')

        
        
        # cc=collections.Counter(temp_anomaly)
        # print(dict( cc.items() ))

        # for i in cc :
        #     f.writelines(str(temp_anomaly[i])+" "+str(count)+'\n')
            



    # with open("compath.txt",'a') as f:
    #     for i in list_use:
    #         f.writelines(i+'\n')
            


if __name__ == '__main__':
    readfile()