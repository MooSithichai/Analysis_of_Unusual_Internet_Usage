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

PATH_SAVE_LOG = '/home/moojokeubuntu/KU/4_2/RealProject/webpattern/Input_new/%s'
#PATH_SAVE_LOG = '/home/sithichai_t/real_project/weblog/Input_new/%s'

PATH_SAVE_LOG4 = '/home/moojokeubuntu/KU/4_2/RealProject/webpattern/Output_group'
#PATH_SAVE_LOG4 = '/home/sithichai_t/real_project/weblog/Output_group_12'



pair = {}


length_max = 50
length_min = 2

interval = 2
max_length = 50

def readfile():
    data = {}
    uni = {}
    sq = []
    G = []
    count = 0
    with open (PATH_SAVE_LOG%('unicode_map_12.csv'),'r') as file:
        reader = csv.reader(file)
        for i in reader:
            if i[0] == "":
                pass
            else:
                uni.update({i[0]:i[1]})

    with open (PATH_SAVE_LOG%('input_user_cut_9to12.txt'),'r') as file:
        for i in file:
            line_strip = i.split(' ')
            IP = line_strip[0]
            sequence = line_strip[1]
            sequence = sequence.replace('\n','')
            web_access = sequence.split(',')
            if len(web_access) >= length_min and len(web_access) <= length_max :
                # if len(web_access) == length_max :
                #     count += 1
                #     for k in range(len(web_access)):
                #         for j in uni :
                #             if web_access[k] == j: 
                #                 web_access[k]=uni[j]
                #     my_list_str = ''.join(map(str, web_access))
                #     G.append(my_list_str)
                # else :
                #     for k in range(len(web_access)):
                #         for j in uni :
                #             if web_access[k] == j: 
                #                 web_access[k]=uni[j]
                #     #data.update({IP:web_access})
                #     my_list_str = ''.join(map(str, web_access))
                #     sq.append(my_list_str)
                for k in range(len(web_access)):
                    if web_access[k] == "":
                        pass
                    else:
                        for j in uni :
                            if web_access[k] == j: 
                                web_access[k]=uni[j]  
                my_list_str = ''.join(map(str, web_access))
                sq.append(my_list_str)


    #print(G)
    #G1 = find_align(G)
    #print(G1)
    #print(sq)       
    #print(data)
    start = 5
    now = 7
    for i in range(length_min,length_max+1,interval):
        start = 5
        now = i + interval
        if now > max_length :
            now = max_length
        use = []
        for j in sq :
            if len(j) >= start and len(j) <= now:
                use.append(j)
        print(str(start)+" "+str(now))
        find_align(use,start,now)
        


def find_num_group(G):
    group = []
    min_len = 0
    max_len = 0
    group_remove = []
    pair = {}
    sort = sorted(G,key=len,reverse = True) 
    for i in sort:
        for j in sort :
            if sort[i] != sort[j] :
                if (sort[i],sort[j]) not in pair and (sort[j],sort[i]) not in pair:
                    GA = pairwise2.align.globalxx(sort[i], sort[j])
                    LA = pairwise2.align.localxx(sort[i], sort[j])
                    glob = GA[0][2]
                    if len(LA) ==  0:
                        loc = 0 
                    else :
                        loc = LA[0][2]
                    
                    if len(sort[i]) >= len(sort[j]):
                        p = len(sort[j])/len(sort[i])
                    else:
                        p = len(sort[i])/len(sort[j])
                    align = ((1-p)*loc)+(p*glob)
                    pair[(sort[i],sort[j])] = align



def find_align(sequence,start,now):
    sort = sorted(sequence,key=len,reverse = True)
    #print(sort)
    for i in range(len(sort)) :
        for j in range(len(sort)):
            if sort[i] != sort[j] :
                if (sort[i],sort[j]) not in pair and (sort[j],sort[i]) not in pair:
                    GA = pairwise2.align.globalxx(sort[i], sort[j])
                    LA = pairwise2.align.localxx(sort[i], sort[j])
                    glob = GA[0][2]
                    if len(LA) ==  0:
                        loc = 0 
                    else :
                        loc = LA[0][2]
                    
                    if len(sort[i]) >= len(sort[j]):
                        p = len(sort[j])/len(sort[i])
                    else:
                        p = len(sort[i])/len(sort[j])
                    align = ((1-p)*loc)+(p*glob)
                    print(sort[i]+" "+sort[j]+" "+str(align)+" "+"find_align")
                    pair[(sort[i],sort[j])] = align
    #print(pair)
    #return pair
    
    find_G_max(pair,sort,start,now)

def find_G_max(pair,sort,start,now):
    group = []
    min_len = 0
    max_len = 0
    group_remove = []

    for i in sort :
        for j in sort :
            if (i,j) in pair:
                if len(i) == now and len(j) == now:
                    if j not in group_remove :
                        if len(i) < len(j) :
                            min_len = len(i)
                            max_len = len(j)
                        else :
                            min_len = len(j)
                            max_len = len(i)
                        if i not in group and j not in group:
                            if pair[(i,j)] < min_len/2 :
                                group.append(i)
                                group.append(j)
                        elif j not in group :
                            if pair[(i,j)] < min_len/2 :
                                group.append(j)
                        else :
                            if pair[(i,j)] > min_len/2 :
                                group.remove(j)
                                group_remove.append(j)
                    print(str(i)+" "+str(j)+" "+"find_G_max")
    #print(group)
    group_sequence(pair,group,sort,start,now)

def group_sequence(pair,group,sort,start,now):
    after = {}
    num = 0
    for i in group :
        after.update({i:[""]})

    for i in sort :
        max_alignval = 0
        temp_i = ""
        temp_k = ""
        for k in group :
            if i not in group :
                if (k,i) in pair:
                    if len(k) >= len(i):
                        p = len(i)/len(k)
                    else:
                        p = len(k)/len(i)
                    ALIGNVAL = pair[(k,i)]*p
                    if ALIGNVAL > max_alignval :
                        max_alignval = ALIGNVAL
                        temp_i = i
                        temp_k = k
                    print(max_alignval)
        if temp_k not in after :
            after.update({temp_k:[temp_i]})
        else :
            after[temp_k].append(temp_i)
        print(num)
        num += 1
   
    print(after)

    now = now
    df = str(start)+"_"+str(now)

    compath = os.path.join(PATH_SAVE_LOG4, df+'.txt')
    
    with open(compath,'a') as f:
        for key in after:
            count = -1
            temp = ''
            for value in range(len(after[key])):
                if after[key][value] == "":
                    temp = ""
                else :
                    temp += after[key][value]+','
                count +=1
            temp = temp[:-1] 
            print("AA"+" "+(key+" "+temp+ " "+str(count) +'\n'))
            f.writelines(key+" "+temp+ " "+str(count) +'\n')


if __name__ == '__main__':
    start = timeit.default_timer()
    readfile()
    stop = timeit.default_timer()
    print(stop - start)