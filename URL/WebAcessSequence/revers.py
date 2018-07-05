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

PATH_OUT_LOG = '/home/moojokeubuntu/KU/4_2/RealProject/webpattern/Output_group/%s'

PATH_OUT_LOG2 = '/home/moojokeubuntu/KU/4_2/RealProject/webpattern/Output_sequence'

PATH_OUT_LOG3 = '/home/moojokeubuntu/KU/4_2/RealProject/webpattern/Reverse2'





PATH_SAVE_LOG = '/home/moojokeubuntu/KU/4_2/RealProject/webpattern/Input_new/%s'


def readfile():
    l_1 = 0
    l_2 = 0
    list_file_name =["2_10.txt"]
    data = {}
    
    count = 0
    for file_name in list_file_name:
        l_1 = 0
        with open (PATH_OUT_LOG%(file_name),'r',encoding='utf-8', errors='ignore') as file:
            for line in file:
                l_1 += 1            
                temp = ""
                line_strip = line.split(" ")
                if len(line_strip) == 3:
                    group_sequence = line_strip[0]
                    sequence = line_strip[1]
                    num = line_strip[2]
                    sequence = sequence.replace('\n','')
                    web_access = sequence.split(',')
                else :
                    group_sequence = line_strip[0]
                    num = line_strip[1]
                    web_access = ""
                mark = False
                if count == 0 :
                    data.update({group_sequence:web_access})
                else :
                    for i in list(data) :
                        for j in range(len(web_access)) :
                            if i == web_access[j]:
                               # print(str(i)+" "+str(web_access[j])+" "+str(data[i]))
                                data.update({group_sequence:web_access})
                                #print("lost "+str(data[group_sequence]))
                                for k in data[i]:
                                    data[group_sequence].append(k)
                                temp = i
                                #print(data[group_sequence])
                                mark = True
                    if mark == False :
                        data.update({group_sequence:web_access}) 
                    else :
                        del data[temp]
        count += 1
        print(l_1)
    
    #print(data)
        

    first,last = [list_file_name[0], list_file_name[-1]]
    first = first.split("_")[0] 
    last = last.split("_")[-1]
    df = first+"_"+last

    compath = os.path.join(PATH_OUT_LOG2, df)
    temp_count = 0
    line_count = 0
    with open(compath,'a') as f:
        for key in data:
            line_count += 1
            temp_count = 0
            temp_2 = ''
            #print(len(data[key]))
            for value in range(len(data[key])):
                if data[key][value] == "":
                    temp_2 = ""
                else :
                    temp_2 += data[key][value]+','
                temp_count +=1
                # print(data[key][value])
                # print(temp_count)
            temp_2 = temp_2[:-1] 
            # print("print"+" "+(key+" "+temp_2+ " "+str(temp_count) +'\n'))
            # print(len(data[key]))
            f.writelines(key+" "+temp_2+ " "+str(temp_count) +'\n')
    print("aa"+" "+str(line_count))
    # ##sort
    # ##แกะ access point log ตัวใหม่
    # ##map กลับ 
    # ##สรุปผล
    reverse_map(df)
    

def reverse_map(file_name):
    uni = {}
    reverse = []
    with open (PATH_SAVE_LOG%('unicode_map_12.csv'),'r') as file:
        reader = csv.reader(file)
        for i in reader:
            uni.update({i[0]:i[1]})
    #print(uni)

    with open (PATH_OUT_LOG%(file_name),'r',encoding='utf-8', errors='ignore') as file:
        for line in file:
            temp_group = []
            temp_web_all = []
            line_strip = line.split(" ")
            if len(line_strip) == 3:
                group_sequence = line_strip[0]
                sequence = line_strip[1]
                num = line_strip[2]
                num = num.replace('\n','')
                sequence = sequence.replace('\n','')
                web_access = sequence.split(',')
                #print(num)
            else :
                group_sequence = line_strip[0]
                num = line_strip[1]
                web_access = ""
                # print("aha"+str(num))
                # print("yes"+len(line_strip))
            #print(group_sequence)
            for j in range(len(group_sequence)):
                for domain in uni :
                    if group_sequence[j] == uni[domain]:
                        temp_group.append(domain)
            my_list_group = ','.join(map(str, temp_group))
            #print(my_list_group)
            for i in range(len(web_access)):
                temp_web_1 = []
                for j in range(len(web_access[i])):
                    for domain in uni :
                        if web_access[i][j] == uni[domain]:
                            temp_web_1.append(domain)
                my_list_web_1 = ','.join(map(str, temp_web_1))
                temp_web_all.append(my_list_web_1)
            my_list_web_all = '|'.join(map(str, temp_web_all))
            c_count = len(my_list_web_all.split("|"))
            print(my_list_web_all)
            print(c_count)
            #print(num)
            #print(my_list_web_all)
            putin = my_list_group+" "+my_list_web_all+" "+str(c_count)
            reverse.append(putin)
    #print(reverse)
    # for i in  :
    #     print(i.split(" ")[2])


    sort = sorted(reverse, key=lambda x: int(x.split(" ")[2]),reverse=True)


    # sort = []
    # for i in reverse :
    #     if int(i.split(" ")[2]) <= 1:
    #         sort.append(i)

    # print(sort)

    for j in range(len(sort)-1) : 
        df = file_name+"_reverse_"+str(sort[j].split(" ")[2])
        compath = os.path.join(PATH_OUT_LOG3, df+'.txt')
        with open(compath,'a') as f:
            f.writelines(sort[j].split(" ")[0]+" :"'\n')
            spl = sort[j].split(" ")[1]
            se = spl.split("|")
            for i in se :
                f.writelines(i+'\n')
    
    # compath = os.path.join(PATH_OUT_LOG2, df+'.txt')
    # with open(compath,'a') as f:
    #     for i in sort:
    #         # line = i.split(" ")[1]
    #         # see = line.split("|")
    #         # print(see)
    #         # print(len(see))
    #         f.writelines(i+'\n')
 
            


    

if __name__ == '__main__':
    readfile()
    #reverse_map('2_32.txt')
