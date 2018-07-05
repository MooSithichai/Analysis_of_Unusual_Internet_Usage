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
import operator

PATH_WEB_LOG_FILE = '/media/moojokeubuntu/AA6259046258D6A3/AnotherDrive/Project/weblog/data/weblog-20180312_2/12/%s'
PATH_SAVE_LOG = '/home/moojokeubuntu/KU/4_2/RealProject/webpattern/Output_domain'

def readFile():


    list_folder_name = [
     "00%s",
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
    dict_domain = {}

    for folder in list_folder_name :
        for file_name in list_file_name :
            for minute in list_minute_name :
                for sub in list_sub_name :
                    #print(PATH_WEB_LOG_FILE%folder%file_name%folder%minute%sub)  

                    with open (PATH_WEB_LOG_FILE%(folder%(file_name%(folder%(minute%(sub))))),'r',encoding='utf-8', errors='ignore') as file:   
                        for line in file.readlines():
                            line_split = line.split(" ")
                            if len(line_split) >= 17 :
                                row_data = {}
                                request = line_split[15]
                                # time = file_name%(folder%(minute%(sub)))
                                # time_after = time[5:-4]
                                # realtime = time_after.split(".txt")[0]
                                # row_data['time'] = time_after
                                domain = get_domainname(line_split[16])
                                group = group_domain(domain)
                                # row_data['IP'] = line_split[10]
                                # print(time_after)
                                print(request)
                                if request == 'GET':
                                #if row_data['Request'] == 'GET' or row_data['Request'] == 'HTTPS' :
                                    if '.' in domain or domain == '-'  :
                                        pass
                                    else :
                                        if group not in dict_domain.keys():
                                            dict_domain[group] = 1
                                        else :
                                            dict_domain[group] += 1
                                        
    #group_domain(list_data)
    writett(dict_domain)

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