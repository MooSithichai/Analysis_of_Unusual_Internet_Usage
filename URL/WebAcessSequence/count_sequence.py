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

PATH_SAVE_LOG = '/home/moojokeubuntu/KU/4_2/RealProject/webpattern/Input_new/%s'
PATH_SAVE_LOG2 = '/home/moojokeubuntu/KU/4_2/RealProject/webpattern/Input_new'

def readfile():
    count = {}
    max_length = 0
    temp = ""
    temp_length = 0
    temp_rea = []
    
    with open (PATH_SAVE_LOG%('input_user_cut_20to23.txt'),'r') as file:
        for i in file:
            line_strip = i.split(' ')
            IP = line_strip[0]
            sequence = line_strip[1]
            sequence = sequence.replace('\n','')
            web_access = sequence.split(',')
            if len(web_access) not in count :
                count.update({len(web_access):1})
            else :
                count[len(web_access)] += 1
            if len(web_access) > max_length:
                max_length = len(web_access)
                temp = IP
            if int(len(web_access)) > 159 :
                print(len(web_access))
                print(IP)
                row_rea = {}
                row_rea["IP"] = IP
                row_rea["C"] = len(web_access)
                temp_rea.append(row_rea)
    od = collections.OrderedDict(sorted(count.items()))
    # print(od)
    # print(max_length)
    # print(temp)
    # print(temp_rea)

    compath = os.path.join(PATH_SAVE_LOG2, 'count_sequence_20to23.csv')
    
    with open(compath,'w',newline = '') as csvfile:
        writer=csv.writer(csvfile)
        for key in od:
            writer.writerow([key,od[key]])
    sort = sorted(temp_rea,key=lambda x:(x['C'],x['IP']))
    compath = os.path.join(PATH_SAVE_LOG2, 'count_sequence_more_20to23.txt')
    with open(compath,'a') as f:
        for i in sort:
            f.writelines(str(i)+'\n')

if __name__ == '__main__':
    readfile()