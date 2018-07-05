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
import unicodedata

PATH_SAVE_LOG = '/home/moojokeubuntu/KU/4_2/RealProject/webpattern/Input_new/%s'
PATH_SAVE_LOG2 = '/home/moojokeubuntu/KU/4_2/RealProject/webpattern/Input_new'


def readfile():
    list_file_name = ["input_user_uncut_9to12.txt", "input_user_uncut_12to13.txt", "input_user_uncut_13to16.txt", "input_user_uncut_20to23.txt"]
    
    max_length = 0
    unique_domain = []
    for file_name in list_file_name:
        with open (PATH_SAVE_LOG%(file_name),'r') as file:
            for i in file:
                line_strip = i.split(' ')
                IP = line_strip[0]
                sequence = line_strip[1]
                sequence = sequence.replace('\n','')
                #print(sequence)
                web_access = sequence.split(',')
                if max_length < len(web_access):
                    max_length = len(web_access)
                #print(sequence+" "+str(len(web_access)))
                for j in web_access :
                    if j not in unique_domain:
                        unique_domain.append(j)
                #print(line_strip[0])
    unicode_map(unique_domain)

def unicode_map(list_domain):
    compath = os.path.join(PATH_SAVE_LOG2, 'unicode_map_12.csv')
    dict_unicode = {}
    for i in range(len(list_domain)) :
        dict_unicode.update({list_domain[i]:chr(i+192)})

    co =0
    with open(compath, 'w', newline='') as f:
        writer = csv.writer(f)
        for key in dict_unicode:
            co += 1
            print(co)
            writer.writerow([key,dict_unicode[key]])
    

        


if __name__ == '__main__':
    readfile()