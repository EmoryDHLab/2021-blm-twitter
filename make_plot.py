import sys
import csv
import matplotlib.pyplot as plt
import pandas as pd
import re
from scipy.signal import argrelextrema
import numpy as np


def days_since(og_date):
    year = int(og_date[0:4])
    month = int(og_date[5:7])
    day = int(og_date[8:10])
    daycount = 0
    daycount += day - 1

    #next, do the months
    while(month > 1):
        if month == 2:
            if(year == 2016 or year == 2020): daycount += 29
            else: daycount += 28
        elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            daycount += 31
        else: daycount += 30
        month -= 1

    while(year > 2014):
        if year == 2020 or year == 2016:
            daycount += 366
        else: daycount += 365
        year -= 1
    return(daycount)



def get_table(ogfile):
    with open(ogfile) as make_dates:
        make_dates_reader = make_dates.read() + "\n"
    match = re.findall("20\d\d-\d\d-\d\d", make_dates_reader)
    dates_lib = dict()
    for row in match:
        if dates_lib.get(days_since(row),0) == 0:
            dates_lib[days_since(row)] = 1
        else: dates_lib[days_since(row)] += 1
    
    data = pd.DataFrame.from_dict(list(dates_lib.items()))
    data.columns = ["days_since", "frequency"]
    for x in range(data.iloc[-1][0]):
        if dates_lib.get(days_since(x),0) == 0:
            data = 0
    data = data.sort_values(by = ['days_since'])

    
    return data

def make_bins(data, mode, use_bin_numbers = False, bintervals = 0):
    final_list = []


    if mode == "localmaxmin":
        to_append = data.iloc[argrelextrema(data.frequency.values, np.greater_equal,
                    order=80)[0]]['days_since']
        to_append = to_append.tolist()
        for row in to_append:
            final_list.append([row, -1])


    elif mode == "time":
        x = 159
        while x < data.iloc[-1][0]:
            final_list.append([x, -1])
            x += bintervals


    elif mode == "tweets":
        if use_bin_numbers:
            if bintervals == 0: raise Exception("Specify a number of bins please!")
            tweet_cap = int((data.sum()[1]) / bintervals)
            makebins(data, mode, bintervals = tweet_cap)

        else:
            x = 0
            exhaust = 0
            while x < len(data):
                if exhaust + data.iloc[x][1] > bintervals:
                    final_list.append([data.iloc[x][0], x])
                    exhaust = 0
                    x += 1
                else:
                    exhaust += data.iloc[x][1]
                    x += 1
            

    else: raise Exception("Please use 'time', 'tweets', or 'localmaxmin'")

    return final_list


def make_plot(data, bins = None):
    plt.plot(data['days_since'], data['frequency'])
    if bins is not None:
        for x in range(len(bins)):
            plt.axvline(x = bins[x][0], color = 'r', label = bins[x][0])
    if bins is not None:
        plt.savefig("plot_binned.jpg")
    else: plt.savefig("plot.jpg")
    print(bins)


