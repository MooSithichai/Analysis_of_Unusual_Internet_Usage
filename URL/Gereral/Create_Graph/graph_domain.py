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
from pylab import plot, ylim, xlim, show, xlabel, ylabel, grid
from numpy import linspace, loadtxt, ones, convolve
import numpy as numpy
import matplotlib
import pylab
import math
import scipy
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
import random
from itertools import cycle

PATH_WEB_LOG_FILE = '/home/moojokeubuntu/KU/4_2/RealProject/webpattern/Output_domain'
PATH_SAVE_LOG = '/home/moojokeubuntu/KU/4_2/RealProject/webpattern/Output_domain'

def readFile():
    li = []
    compath = os.path.join(PATH_WEB_LOG_FILE, 'count_domain_13.csv')
    with open(compath,'r') as csvfile:
        r = csv.reader(csvfile)
        for i in r:
            row_data = {}
            row_data['Domain'] = i[0]
            row_data['Count'] = int(i[1])
            li.append(row_data)
            print(i[0])
    cummu(li)

def cummu(list_use):
    y_cum  = []
    y_use = []
    temp = 0
    max_n = 47202807
    sort = sorted(list_use, key=lambda x:(x['Count'],x['Domain']) ,reverse = True)
    print(sort)
    for i in range(len(sort)):
        row_data = {}
        temp += int(sort[i]['Count'])
        row_data['Domain'] = sort[i]['Domain']
        row_data['Count'] = temp
        y_cum.append(row_data)
    print(y_cum[0])
    compath = os.path.join(PATH_SAVE_LOG, 'domain.txt')
    with open(compath,'a') as f:
        for i in y_cum:
            f.writelines(i['Domain']+" "+str(i['Count'])+'\n')
    
    per95 = int(95*max_n/100)
    per955 = int(95.5*max_n/100)
    per98 = int(98*max_n/100)
    per97 = int(97*max_n/100)
    per96 = int(96*max_n/100)
    per99 = int(99*max_n/100)
    print(per95)
    print(per98)
    print(per97)
    for i in range(len(y_cum)):
        if y_cum[i]['Count'] < per955 :
            #print('no98')
            pass
        else :
            print('yes97')
            print(y_cum[i]['Domain'])
            print(y_cum[i]['Count'])
            break
    for i in range(len(y_cum)):
        if y_cum[i]['Count'] == 44842974 :
            print(y_cum[i]['Domain'])
    p95 = 'tosbase' #2493
    p98 = 'gradjobs' 
    p97 = 'fjallraven'
    p96 = 'epp5online2' #3517
    p99 = 'performancecashsystem'
    p955 = 'ait'
    x = []
    y = []
    cc = 0
    for i in range(len(sort)):
        if sort[i]['Domain'] == p95:
            #print(i)
            #print(sort[i]['Domain'])
            for j in range(i,len(sort)):
                if sort[j]['Domain'] != p98:
                    x.append(sort[j]['Domain'])
                    y.append(sort[j]['Count'])
                else :
                    x.append(sort[j]['Domain'])
                    y.append(sort[j]['Count'])
                    break
    #print(x)
    print(len(x))

    plot_map(x,y)

def plot_map(x,y):
    xlen = []
    print(y)
    for i in range(len(x)):
        xlen.append(i)
    plt.title('Unusual Domain')
    plt.bar(xlen,y)
    plt.xticks([], x,rotation=90,horizontalalignment='left')
    plt.xlabel('Domain')
    plt.ylabel('Number of Domain uses')
    matplotlib.rcParams.update({'font.size': 16})
    plt.legend()
    plt.show()
        
    


        

def writett(dict_domain):
    od = sorted(dict_domain.items(), key=operator.itemgetter(1) ,reverse=True)
    compath = os.path.join(PATH_SAVE_LOG, 'count_domain_13.csv')
    with open(compath,'w',newline = '') as csvfile:
        writer=csv.writer(csvfile)
        for key,value in od:
            writer.writerow([key,value])

def get_domainname(domainname):
    if 'http://' not in domainname and  'https://' not in domainname and 'ftp://' not in domainname:
        domainname = 'http://' + domainname
    subdomain,domain,suf = tldextract.extract(domainname)
    if domain in 'edgesuite' :
        subdomain,domain,suf = tldextract.extract(subdomain)
    elif subdomain == 'ads' :
        domain = '-'
    elif domain in '':
        print('null')
    return domain
    

def group_domain(data) :
    dmain = {}
    dmain["facebook"] = [('fbcdn'),('facebook'),('fb')]
    dmain['apple'] = [('apple'),('mail')]
    dmain['ku'] = [('ku'),('kasetsart')]
    dmain["line"] = [('naver'),('line-apps'),('line'),('line-cdn'),('linetv')]
    dmain["baidu"] = [('baidu')]
    dmain['avast'] = [('avast')]
    dmain['microsoft'] = [('microsoft')]
    dmain["google"] = [('google'),('google'),('google-analytics')]
    dmain["steam"] = [('steamcontent'),('steamstatic'),('steampowered')] 
    dmain["youtube"] = [('googlevideo'),('youtube'),('youtu'),('youtube-nocookie')]
    dmain["garena"] = [('garenanow')]
    dmain['icould'] = [('icloud')]
    dmain["twitter"] = [('twimg'),('twitter')]
    dmain['instagram'] = [('instagram')]
    dmain['adobe'] = [('adobe')]
    dmain["wechat"] = [('wechat'),('qq')]
    dmain["sanook"] = [('isanook'),('fsanook'),('sanook')]
    dmain['kapook'] = [('kapook')]
    dmain['shopee'] = [('shopee')]
    dmain['videe'] = [('videe')]
    dmain['live'] = [('live')]
    dmain['outlook'] = [('outlook')]
    dmain['android'] = [('android')]
    dmain["pantip"] = [('pantip'),('ptcdn'),('mikelab')]
    dmain['teamviewer'] = [('teamviewer')]
    dmain["msn"] = [('msn'),('s-msn')]
    dmain["windowsupdate"] = [('windowsupdate')]
    dmain["springserve"] = [('springserve')]
    dmain["chula"] = [('chula')]
    dmain['lkqd'] = [('lkqd')]
    dmain['ptvcdn'] = [('ptvcdn')]
    dmain['gstatic'] = [('gstatic'),('gstatic')]
    dmain['googlesyndication'] = [('googlesyndication')]
    dmain['akami'] = [('akami')]
    dmain['manager'] = [('manager')]
    dmain['adobe'] = [('adobe'),('adobesc')]
    dmain['mozilla'] = [('mozilla'),('mozillamessaging')]
    dmain['firefox'] = [('firefoxplugin'),('firefoxusercontent'),('firefox')]
    dmain['aniview'] = [('aniview'),('ani-view')]
    dmain['addthis'] = [('addthis'),('addthisedge')]
    dmain['tapjoy'] = [('tapjoy'),('tapjoyads')]

    list_domain = []
    list_not_group = []
    list_save_cvs = []
    for d in dmain :
        for word in dmain[d] :
            if '.'+str(word)+'.' in '.'+data+'.' :
                data = d
    #list_data = sorted(list_data, key=getKey)
    return data
    print(list_data)

def getKey(item):
    return item['IP']

def count_domain(list_data):
    unique_domain = {}
    list_all = []
    for i in range(len(list_data)):
        list_all.append(list_data[i]["domain"])
    # for i in range(len(list_data)):
    #     if list_data[i]["domain"] not in unique_domain.keys():
    #         unique_domain.update({list_data[i]["domain"]:1})
    #     else :
    #         tempcount = unique_domain[list_data[i]["domain"]]
    #         count = int(tempcount)+1
    #         unique_domain.update({list_data[i]["domain"]:count})
    printtt(list_all)
def printtt(list_data):
    counter=collections.Counter(list_data)
    print(counter)
    sort = counter.most_common()
    compath = os.path.join(PATH_SAVE_LOG, 'domain_count.csv')
    with open(compath,'w',newline = '') as csvfile:
        fieldnames=['domain','count']
        writer=csv.writer(csvfile)
        writer.writerow(fieldnames)
        for key, value in sort:
            domain = key.split() 
            writer.writerow(domain+[value])

    

    
    

if __name__ == '__main__':
    start = timeit.default_timer()
    readFile()
    #check_user([{'time': '201803120900.2', 'IP': '1.0.213.87', 'Request': 'GET', 'domain': 'ku'},{'time': '201803121000.2', 'IP': '1.0.213.87', 'Request': 'GET', 'domain': 'ku'},{'time': '201803121000.5', 'IP': '1.0.213.87', 'Request': 'GET', 'domain': 'ku'},{'time': '201803121100.2', 'IP': '1.0.213.87', 'Request': 'GET', 'domain': 'ku'},{'time': '201803120900.3', 'IP': '1.0.213.87', 'Request': 'GET', 'domain': 'sa'}])
    #cal_time('201803120900.2')
    stop = timeit.default_timer()
    print(stop - start)
    #readAllurl()