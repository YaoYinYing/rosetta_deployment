#!/usr/bin/env python # -*- coding: utf-8 -*-
# this script is adapted by Yao YinYing @ 2018.1.3
# Github: https://github.com/YaoYinYing/
import re
class phaserlog:
    def __init__(self):
        self.index=0
        self.resol_limit=[]
        self.observe=[]
        self.unique=[]
        self.possible=[]
        self.completeness=[]
        self.R_observed=[]
        self.R_expected=[]
        self.Compared=[]
        self.I_Sig=[]
        self.R_meas=[]
        self.CC_half=[]
        self.AnomalCorr=[]
        self.SigAno=[]
        self.Nano=[]
#print("Hello word")
logAll=open("buffer.log","r")
logRead=logAll.read().split("total")
logAll.close()

extractlog=logRead[logRead.__len__()-2]
#print(logRead)
#print(extractlog)
inLine=extractlog.split("\n")

inLine.pop(0)
inLine.pop(0)
inLine.pop(inLine.__len__()-1)

mylog=phaserlog()

# while i<inLine.__len__()+1:
for i in inLine:
    # print(i)
    inLineSplt=list()
    inLineSplt=i.split(" ")
    # inLineSplt= re.sub("[^\s]", " ",inLine[i]).split()
    while '' in inLineSplt:
        inLineSplt.remove('')
        pass

    j=0
    #print(i)
    #print(mylog.resol_limit.__len__())
    #print(inLineSplt)
    mylog.resol_limit.append(inLineSplt[j])
    j+=1
    mylog.observe.append(inLineSplt[j])
    j+=1
    mylog.unique.append(inLineSplt[j])
    j+=1
    mylog.possible.append(inLineSplt[j])
    j+=1
    mylog.completeness.append(inLineSplt[j])
    j+=1
    mylog.R_observed.append(inLineSplt[j])
    j+=1
    mylog.R_expected.append(inLineSplt[j])
    j+=1
    mylog.Compared.append(inLineSplt[j])
    j+=1
    mylog.I_Sig.append(inLineSplt[j])
    j+=1
    mylog.R_meas.append(inLineSplt[j])
    j+=1
    mylog.CC_half.append(inLineSplt[j])
    j+=1
    mylog.AnomalCorr.append(inLineSplt[j])
    j+=1
    mylog.SigAno.append(inLineSplt[j])
    j+=1
    mylog.Nano.append(inLineSplt[j])


mylog.index=mylog.I_Sig.__len__()

#print(mylog.index)
#print(mylog.resol_limit)
def output(input_log):
    i=0
    resol_sel=[]
    '''while i < int(input_log.index - 1):
        print("%s \t %f" % (input_log.CC_half[i], float(input_log.CC_half[i].split("*")[0])))
        i+=1
        pass'''
    while i < int(input_log.index-1):
        if (float(input_log.completeness[i].split("%")[0])>90.0
            and float(input_log.CC_half[i].split("*")[0])>50
            and float(input_log.R_expected[i].split("%")[0])<100
            and float(input_log.R_observed[i].split("%")[0])<100
            and float(input_log.I_Sig[i])>1.00
            and float(input_log.R_meas[i].split("%")[0])<100
            ):
            #print(input_log.resol_limit[i])
            resol_sel.append(input_log.resol_limit[i])
        i+=1
        pass
    return(resol_sel[resol_sel.__len__()-1])
    pass
#print("The best resolution is %s Angstron." % (output(mylog)))
print("%s" % (output(mylog)))


