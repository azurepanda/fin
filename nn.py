from pybrain.tools.shortcuts import buildNetwork;
import math
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams["savefig.dpi"] = 100
import numpy as np
import os
from os import path
#Date,Open,High,Low,Close,Volume,OpenInt

print;
def readFiles():
    pairs = [[], []]
    for f in os.listdir('./pairs/'):
        pairs[0].append(f[:-4]);
        data = [];
        lineno = 0;
        dayno = 0;
        for line in open('./pairs/' + f, 'r').read().split('\r\n'):
            i = 0;
            linedata = line.split(',');
            if not lineno == 0:
                for s in linedata:
                    if len(linedata) == 8:
                        if len(data) <= len(linedata):
                            data.append([]);
                        if not i == 0 and not i == 1:
                            data[i].append(float(s));
                        else:
                            data[i].append(dayno);
                        i = i + 1;
                dayno = dayno + 1;
            lineno = lineno + 1;
        pairs[1].append(data);
    return pairs

pairs = readFiles();

def plotPair(n=-1, name=''):
    if name == '':
        i = n;
    if n == -1:
        try:
            i = pairs[0].index(name);
        except:
            print 'Error: plotPair: Item not in list';
    if i == -1:
        print 'Error: plotPair: No index found';
        return;
    plt.plot(pairs[1][i][1], pairs[1][i][4]);
    plt.title(pairs[0][i].upper());
    plt.xlabel('time [hours]');
    plt.ylabel('price [close]');
    plt.show();

plotPair(name='eurusd');

def logPctChange(x1, x2):
    return (math.log10(x1)-math.log10(x2))/math.log10(x2);


#data.append([])
#for n in range(0, len(data[0])):
    #if n == 0:
        #data[7].append(0.0);
    #else:
        #data[7].append(logPctChange(data[4][n], data[4][n-1]));
#plt.plot(data[7], data[8]);
#plt.show();
