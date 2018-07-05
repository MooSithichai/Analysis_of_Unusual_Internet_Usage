from __future__ import division
from pylab import plot, ylim, xlim, show, xlabel, ylabel, grid
from numpy import linspace, loadtxt, ones, convolve
import numpy as numpy
import matplotlib
import datetime 
import scipy
from scipy import signal
import numpy as np
import pandas as pd

#from movingaverage import movingaverage

def test_3():
    x =[7,8,9,10,11,12]
    y = [1,2,3,4,5,6]

    #x = [datetime.datetime.now() + datetime.timedelta(minutes=i) for i in range(6)]
    #print(x)

    # x   = ['16:39:27',
    # '16:39:41',
    # '16:41:41',
    # '16:43:41',
    # '16:43:54',
    # '16:45:38']
    # datetime_object = datetime.datetime.strptime(x, '%H:%M:%S')
    # print(datetime_object)
    # dates = ['Apr 12 2018 04:50:10','Apr 12 2018 05:50:21','Apr 12 2018 06:50:21','Apr 12 2018 07:50:51']
    # DATE = [datetime.datetime.strptime(x,'%b %d %Y %H:%M:%S') for x in dates]

    #dates = matplotlib.dates.date2num(DATE)
    #matplotlib.pyplot.plot_date(DATE, y)
    #print(dates)

    matplotlib.pyplot.plot(x, y,"k.")
    y_av = movingaverage(y, 6)
    print(y_av)
    y_av = fftconvolve_sma(y, 6)
    print(y_av)
    y_av = pandas_sma(y, 6)
    print(y_av)
    y_av = new_mov(y, 3)
    print(y_av)
    y_av = new_mov2(y, 3)
    print(y_av)
    plot(x, y_av,"r")
    myFmt = matplotlib.dates.DateFormatter('%H:%M')
    matplotlib.pyplot.gca().xaxis.set_major_formatter(myFmt)
    # # xlim(0,1000)
    # xlabel("Months since Jan 1749.")
    # ylabel("No. of Sun spots")
    # grid(True)
    show()

def fftconvolve_sma(array, period):    
    return scipy.signal.fftconvolve(
        array, np.ones((period,))/period, mode='same')   

def pandas_sma(array, period):
    myarray = np.asarray(array)
    return pd.rolling_mean(myarray, period)

def movingaverage(interval, window_size):

    window= numpy.ones(int(window_size))/float(window_size)
    return numpy.convolve(interval, window, 'same')

def new_mov(interval, window_size):
    cumsum, moving_aves = [0], []
    for i, x in enumerate(interval, 1):
        cumsum.append(cumsum[i-1] + x)
        if i>=window_size:
            moving_ave = (cumsum[i] - cumsum[i-window_size])/window_size
            moving_aves.append(moving_ave)
            print(moving_ave)
    return moving_aves
def new_mov2(interval, window_size):
    smoothed = np.convolve(interval, np.ones(window_size)/window_size)
    print(smoothed)
    return smoothed


def test_2():
    mylist = [1, 2, 3, 4, 5, 6, 7]
    N = 3
    cumsum, moving_aves = [0], []

    for i, x in enumerate(mylist, 1):
        cumsum.append(cumsum[i-1] + x)
        if i>=N:
            moving_ave = (cumsum[i] - cumsum[i-N])/N
            #can do stuff with moving_ave here
            moving_aves.append(moving_ave)
    x = mylist
    y = numpy.array([1,2,3])
    print(x)
    print(y)

    plot(x,y,"r")
    show()
    
    print(moving_aves)


if __name__ == '__main__':
    #raedfile()
    #test_2()
    test_3()