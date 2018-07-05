import csv
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
import gc
import numpy as np
from sklearn import random_projection
from scipy.spatial.distance import mahalanobis
import scipy as sp
import pandas as pd

#test_3to6.csv skiprow = 2 , len = 168
#test_0to3.csv skiprow = 2 , len = 197
#test_6to9.csv skiprow = 2 , len = 198
#test_9to12.csv skiprow = 1 , len = 312
#test_12to15.csv skiprow = 2 , len = 386



# PATH_TO_INPUT = "/home/moojokeubuntu/KU/4_2/RealProject/webpattern/Detection/Input2"
PATH_TO_INPUT = "/home/moojoke34/Project/web/Detection/Input2"
PATH_TO_SAVE = "/home/moojoke34/Project/web/Detection/Output2"


def readfile():
    # compath = os.path.join(PATH_TO_INPUT, "test_3to6.csv")
    # ncols = 0
    # ncols_temp = 0
    # count = 0
    # with open(compath) as f:
    #     for line in f :
    #         line_split = line.split(",")
    #         ncols = len(line_split)
    #         count += 1
    #         # print(line_split)
    #         # print(len(line_split))
    #         if ncols == ncols_temp :
    #             break
    #         else :
    #             print(ncols)
    #             ncols_temp = ncols
    #             print('ooooooooooooooooooooooooooooooooooooo')
    #             print(ncols_temp)
    #         if count == 5 :
    #             break
        
    #     print('////////////////////////////////////////////')
    #     print(ncols_temp)
        
    # print(ncols)
    # print(count)

    # data = pd.read_csv(compath, nrows=2)
    # print(len(data))
    
    a = np.loadtxt(open(compath, "rb"), delimiter=",", skiprows=2,usecols=range(0,168))

    # print(a.shape)
    #print(a)
    #mahalano(a)
    # tranform(a)
    # del a

def tranform(matrix):
    transformer = random_projection.SparseRandomProjection(n_components=2,density=1/3)
    matrix_new = transformer.fit_transform(matrix)
    del matrix
    print(matrix_new.shape)
    mahalano(matrix_new)
    
    del matrix_new

def mahalano(X):
    print("come")
    mean = np.mean(X,axis=0)
    print("mean")
    x_con = np.cov(X,rowvar=False)
    print("x_con")
    invcovmx = sp.linalg.inv(x_con)
    #del x_con
    compath = os.path.join(PATH_TO_SAVE, '9.txt')
    count = 0
    for i in range(len(X)):
        mala = z = mahalanobis(X[i], mean, invcovmx)
        print(mala)
        with open(compath,'a') as f:
            f.writelines(str(mala)+'\n') 
        


if __name__ == '__main__':
    start = timeit.default_timer()
    readfile()
    stop = timeit.default_timer()
    print(stop - start)
