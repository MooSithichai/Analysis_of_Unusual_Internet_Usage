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
PATH_SAVE_LOG = '/home/moojokeubuntu/KU/4_2/RealProject/webpattern/Input_new'



def readFile():

    list_folder_name = ["09%s",
    "10%s",
    "11%s"]
    #list_folder_name = ["12%s"]
    #list_folder_name = ["13%s","14%s","15%s"]
    #list_folder_name = ["00%s","01%s","02%s","03%s","04%s","05%s"]



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
                            line_split = line.split(" ")
                            if len(line_split) >= 16 :
                                print(line_split)
                                row_data = {}
                                row_data['Request'] = line_split[15]
                                time = file_name%(folder%(minute%(sub)))
                                time_after = time[5:-4]
                                realtime = time_after.split(".txt")[0]
                                row_data['time'] = time_after
                                row_data['domain'] = get_domainname(line_split[16])
                                if line_split[4] != "-" :
                                    row_data['user'] = line_split[4]
                                    if len(row_data['user']) == 32:
                                        if row_data['Request'] == 'GET':
                                            if '.' in row_data['domain'] or row_data['domain'] == '-'  :
                                                pass
                                            else :
                                                list_data.append(row_data)
                           
    group_domain(list_data)

def get_domainname(domainname):
    if 'http://' not in domainname and  'https://' not in domainname and 'ftp://' not in domainname:
        domainname = 'http://' + domainname
    subdomain,domain,suf = tldextract.extract(domainname)
    if domain in 'edgesuite' :
        subdomain,domain,suf = tldextract.extract(subdomain)
    elif subdomain == 'ads' :
        domain = '-'
    elif domain == '':
        domain = '-'
    return domain
    

def group_domain(list_data) :
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
    for i in range(len(list_data)) :
        for d in dmain :
            for word in dmain[d] :
                if '.'+str(word)+'.' in '.'+list_data[i]['domain']+'.' :
                    list_data[i]['domain'] = d
    list_data = sorted(list_data, key=getKey)
    print(list_data)
    check_user(list_data)

# check ว่า user มีการใช้งานเกิน 30 นาทีรึเปล่า ถ้ามี ก็แยกออกเป็น อีก sequence
def check_user(list_data):
    list_new_IP = []
    list_link2 = sorted(list_data, key=lambda x:(x['user'],x['time'],x['domain']))

   
    link = [list_link2[0]]
    for i in range(len(list_link2)) :
        if '_' in link[-1]['user'] :
            IP = link[-1]['user'].split("_")[0]
            print(IP)
            if IP == list_link2[i]['user']:
                list_link2[i]['user'] = link[-1]['user']
                if math.fabs(cal_time(link[-1]['time'])-cal_time(list_link2[i]['time']))  > 1800:
                    list_link2[i]["user"] = list_link2[i]["user"]+"_"+str(i)
                    link.append(list_link2[i])
                else :
                    link.append(list_link2[i])
            else :
                link.append(list_link2[i])
        else :
            if link[-1]['user'] == list_link2[i]['user']:
                if math.fabs(cal_time(link[-1]['time'])-cal_time(list_link2[i]['time']))  > 1800:
                    list_link2[i]["user"] = list_link2[i]["user"]+"_"+str(i)
                    link.append(list_link2[i])
                else :
                    link.append(list_link2[i])
            else :
                link.append(list_link2[i])
    #print(link)
    sequence_gather(link)
    

def getKey(item):
    return item['user']

def cal_time(data):
    time_split = data.split(".")
    hour = time_split[0][-4:-2]
    minute = time_split[0][-2:]
    second = time_split[1]
    time = (int(hour)*3600)+(int(minute)*60)+(int(second)*10)
    return time

def sequence_gather(list_data):
    list_IP = []
    list_sequence = {}
    list_link2 = sorted(list_data, key=lambda x:(x['user'],x['time'],x['domain']))
    list_link = sorted(list_data, key=lambda x:(x['user'],x['domain'],x['time']))
    print(list_link)
    link = [list_link[0]]
    for i in range(1,len(list_link)):
        if link[-1]['domain'] == list_link[i]['domain']:
            if math.fabs(cal_time(link[-1]['time'])-cal_time(list_link[i]['time']))  > 60:
                link.append(list_link[i])
        else:
            link.append(list_link[i])
    link = sorted(link, key=lambda x:(x['user'],x['time'],x['domain']))
    
    list_link2=[]
    list_link=[]
    print("///////////////////////////////////////////")
   
    for i in range(len(link)-1) :
        print(i)
        print(link[i]['domain'])
        if(link[i]['user'] == link[i+1]['user']):
            print(link[i]['user'])
            
            if(link[i]['domain'] != link[i+1]['domain']):
                tempIP = str(link[i]['user'])
                tempdomain = link[i]['domain']
                if tempIP not in list_sequence.keys():
                    list_sequence.update({tempIP:[tempdomain]})
                else :
                    list_sequence[tempIP].append(tempdomain)
        
    print(len(list_sequence))

    # เขียนลง file  
    compath = os.path.join(PATH_SAVE_LOG, 'input_user_cut_00to06.txt')
    count = 0
    with open(compath,'a') as f:
        for key in list_sequence:
            temp = ''
            for value in range(len(list_sequence[key])):
                temp += list_sequence[key][value]+','
                count +=1
            temp = temp[:-1] 
            print(count)
            f.writelines(key+" "+temp+'\n')
            

    

if __name__ == '__main__':
    start = timeit.default_timer()
    readFile()
    #check_user([{'time': '201803120900.2', 'IP': '1.0.213.87', 'Request': 'GET', 'domain': 'ku'},{'time': '201803121000.2', 'IP': '1.0.213.87', 'Request': 'GET', 'domain': 'ku'},{'time': '201803121000.5', 'IP': '1.0.213.87', 'Request': 'GET', 'domain': 'ku'},{'time': '201803121100.2', 'IP': '1.0.213.87', 'Request': 'GET', 'domain': 'ku'},{'time': '201803120900.3', 'IP': '1.0.213.87', 'Request': 'GET', 'domain': 'sa'}])
    #cal_time('201803120900.2')
    stop = timeit.default_timer()
    print(stop - start)
    #readAllurl()