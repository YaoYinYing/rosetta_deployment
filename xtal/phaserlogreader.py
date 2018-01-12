#!/usr/bin/env python # -*- coding: utf-8 -*-
# this script is adapted by Yao YinYing @ 2018.1.3
# Github: https://github.com/YaoYinYing/
import re


# sed -n '/SUBSET OF INTENSITY DATA WITH SIGNAL.*/,/NUMBER OF REFLECTIONS IN SELECTED SUBSET OF IMAGES.*/p'
# ./CORRECT.LP |sed -n '/^\ *[0-9].*[0-9]$/p' > buffer.log


class phaserlog:
    def __init__(self):
        self.index = 0
        self.resol_limit = []
        self.observe = []
        self.unique = []
        self.possible = []
        self.completeness = []
        self.R_observed = []
        self.R_expected = []
        self.Compared = []
        self.I_Sig = []
        self.R_meas = []
        self.CC_half = []
        self.AnomalCorr = []
        self.SigAno = []
        self.Nano = []


# create a log object
mylog = phaserlog()
# read the log file split it into several parts
logAll = open("buffer.log", "r")
logRead = logAll.read().split("total")
logAll.close()
# read the final parts and spit it by \n
extractlog = logRead[logRead.__len__() - 2]
# print(logRead)
# print(extractlog)
inLine = extractlog.split("\n")

# remove the first two lines
inLine.pop(0)
inLine.pop(0)
inLine.pop(inLine.__len__() - 1)

# while i<inLine.__len__()+1:
for i in inLine:
    # split each line by space and remove the empty elements of list
    inLineSplt = i.split(" ")
    while '' in inLineSplt:
        inLineSplt.remove('')
        pass
    j = 0
    # print(i)
    # print(mylog.resol_limit.__len__())
    # print(inLineSplt)
    # add the formatted value to each list
    mylog.resol_limit.append(float(inLineSplt[j]))
    j += 1
    mylog.observe.append(int(inLineSplt[j]))
    j += 1
    mylog.unique.append(int(inLineSplt[j]))
    j += 1
    mylog.possible.append(int(inLineSplt[j]))
    j += 1
    mylog.completeness.append(float(inLineSplt[j].split("%")[0]))
    j += 1
    mylog.R_observed.append(float(inLineSplt[j].split("%")[0]))
    j += 1
    mylog.R_expected.append(float(inLineSplt[j].split("%")[0]))
    j += 1
    mylog.Compared.append(int(inLineSplt[j]))
    j += 1
    mylog.I_Sig.append(float(inLineSplt[j]))
    j += 1
    mylog.R_meas.append(float(inLineSplt[j].split("%")[0]))
    j += 1
    mylog.CC_half.append(float(inLineSplt[j].split("*")[0]))
    j += 1
    mylog.AnomalCorr.append(int(inLineSplt[j]))
    j += 1
    mylog.SigAno.append(float(inLineSplt[j]))
    j += 1
    mylog.Nano.append(int(inLineSplt[j]))
    pass
mylog.index = mylog.I_Sig.__len__()


def output(input_log):
    i = 0
    resol_sel = []
    # select the resolution limits value by the following factors
    while i < int(input_log.index - 1):
        if (input_log.completeness[i] > 90.0
            and input_log.CC_half[i] > 50
            and input_log.R_expected[i] < 100
            and input_log.R_observed[i] < 100
            and input_log.I_Sig[i] > 1.00
            and input_log.R_meas[i] < 100
            ):
            # print(input_log.resol_limit[i])
            resol_sel.append(input_log.resol_limit[i])
        i += 1
        pass
    # return the best of selected resolution limit values
    return (resol_sel[resol_sel.__len__() - 1])
    pass


# print("The best resolution is %s Angstron." % (output(mylog)))
# print the best resolution of data in console, this value will be given to another linux command to
# continue the data processing.
print("%s" % (output(mylog)))
