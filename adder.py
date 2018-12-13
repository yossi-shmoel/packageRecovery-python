import sys
import os.path
import string
from os import listdir
from os.path import isfile, join
import serial
import io
import time
from time import mktime
import requests

##########parameters


#input packageconfig
'''
pacFile = 'C:/docs/000comp/012 package recovery/packages.config'
pacPath = 'C:/docs/000comp/012 package recovery/packages'
'''

pacFile = 'C:/00comp/04 python/013 package recovery/packages.config'
pacPath = 'C:/00comp/04 python/013 package recovery/packages/'




def Open_file(pacFile):
#GET data from input CSV file
    with open(pacFile) as f:
        read_data=[f.rstrip('\n') for f in open(pacFile)]
        f.closed
    return read_data
# END Open_csv


def Get_pacData(fileData):
    packageList=[]
    for data in fileData:
        if(data.find('package')>2):
            splitedData=data.split('"')
            packageList.append(splitedData[1]+'.'+splitedData[3])
    return packageList

def GetNotExsists_pac(packageList):
    NotExsitsPackageList=[]
    for data in packageList:
        if(data.find('GRT')==0 or data.find('Grt')==0):
            if(not os.path.exists(pacPath+data)):
                NotExsitsPackageList.append(data)
    #print(NotExsitsPackageList)
    return(NotExsitsPackageList)


def Create_pac(missingPackage):
    for data in missingPackage:
        os.makedirs(pacPath+data+'/lib/net452')
        Create_files(pacPath+data+'/', data, "nupkg")
        Create_files(pacPath+data+'/lib/net452/', data, "dll")
        Create_files(pacPath+data+'/lib/net452/', data, "XML")


def Create_files(path,fileName,FileType):
    #pacPath + 'Grt.Framework.Protocol.Services.2.201806.2124449.1-CI.nupkg'
    #pacPath + /lib/net452/
    #   Grt.Framework.Protocol.Services.dll
    #   Grt.Framework.Protocol.Services.XML
    # open("guru99.txt","w+")
    #print(path + data+".dll")
    
    f=open(path + fileName+"."+FileType,"w+")
    f.close()
    


data = Open_file(pacFile)
packageData = Get_pacData(data)
notExsits = GetNotExsists_pac(packageData)
Create_pac(notExsits)
print('END')


'''
#input CSV
#ParamFile='C:/00comp/04 python/012 video rqst/eventDatamini.csv'
ParamFile='/root/yossi/video/eventData.csv'

#log output
ParamLogFile='/root/yossi/video/failedRqst1.log'


#Testing Template
URL_TEMPLATE = 'http://il-qa-core-1:8090/CloudBackupAPI/GetVideoClip?DeviceType=50&Address=%s&Port=37777&LoginName=admin&Password=admin&Channel=%s&SensorAddress=%s&SensorPort=37777&SensorChannel=0&DeviceName=%s&VideoChannelName=%s&SensorChannelName=%sBehavior&AlarmTriggerTime=%s&PreRecordTime=10&PostRecordTime=10'




def Send_rqst(rqst):
	try:
		response = requests.get(rqst)
		print(response.text)
		if(response.text=='FAILED'):
			print(rqst)
	except:
		f=open(ParamLogFile,"a")
		f.write(rqst+"\n")
		print("except: "+rqst)
		f.close()
	#time.sleep(0.4)


def Convert_time(time):
    #print(time)
    hh=time[11:13]
    mm=time[14:16]
    ss=time[17:19]
    d=time[8:10]
    m=time[5:7]
    y=time[0:4]
    t=(int(y), int(m), int(d), int(hh), int(mm), int(ss), 0, 0, 0)
    unix_secs = mktime(t)+7200
    #print(unix_secs)
    return int(unix_secs)


def Genrate_rqst(data):
    #print(data[2])
    for i in range(0,int(data[2])):
        eventTime=Convert_time(data[4])
        rqstUrl=URL_TEMPLATE %( data[1], i,data[1],data[3],data[3],data[0], eventTime)
        #print(rqstUrl)
	Send_rqst(rqstUrl)
        




def Data_scan():
    CsvData=Open_csv(ParamFile)    
    for data in CsvData:
        data=data.split(",")
        data[1]=data[1].split(":")[0]
        #print(data[1])
        Genrate_rqst(data)


#Main
#f=open(ParamLogFile,"a")
#f.close()
#Data_scan()
'''
