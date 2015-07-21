from pybrain.tools.shortcuts import buildNetwork;
import math
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams["savefig.dpi"] = 100
import numpy as np
import os
from os import path
#Date,Open,High,Low,Close,Volume,OpenInt
data = [];
lineno = 0;
dayno = 0;
for line in open('./pairs/eurusd.txt', 'r').read().split('\r\n'):
    i = 0;
    linedata = line.split(',');
    if len(linedata) == 7 and int(linedata[0]) > 20100104 and int(linedata[0]) <= 20150715:
        for s in linedata:
            if len(data) <= i:
                data.append([]);
            data[i].append(float(s));
            i = i + 1;
        if len(data) <= 7:
            data.append([]);
        data[7].append(dayno);
        dayno = dayno + 1;
    lineno = lineno + 1;
#plt.plot(data[7], data[4]);
#plt.show();

def logPctChange(x1, x2):
    return (math.log10(x1)-math.log10(x2))/math.log10(x2);

data.append([])
for n in range(0, len(data[0])):
    if n == 0:
        data[8].append(0.0);
    else:
        data[8].append(logPctChange(data[4][n], data[4][n-1]));

plt.plot(data[7], data[8]);
plt.show();
