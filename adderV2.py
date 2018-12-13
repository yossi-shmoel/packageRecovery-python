import sys
import os.path
import string
from os import listdir
from os.path import isfile, join
import io


##########parameters


####input packageconfig
#PAPTH to package config file
pacFile = 'C:/00comp/04 python/013 package recovery/packages.config'
#PATH to packages folder
pacPath = 'C:/00comp/04 python/013 package recovery/packages/'


'''
pacFile = 'C:/docs/000comp/013 package recovery/packages.config'
pacPath = 'C:/docs/000comp/013 package recovery/packages'
'''


########## Class
class PackageData:
    def __init__(self, name, version):
        self.name = name
        self.version = version

########## Functions
def Open_file(pacFile):
    with open(pacFile) as f:
        read_data=[f.rstrip('\n') for f in open(pacFile)]
        f.closed
    return read_data

def Get_pacData(fileData):
    packageList=[]
    for data in fileData:
        if(data.find('package')>2):
            splitedData=data.split('"')
            packageList.append(PackageData(splitedData[1], splitedData[3]))
    return packageList

def GetNotExsists_pac(packageList):
    NotExsitsPackageList=[]
    for data in packageList:
        if(data.name.find('GRT')==0 or data.name.find('Grt')==0):
            fullPath=pacPath+data.name+'.'+data.version
            if(not os.path.exists(fullPath)):
                NotExsitsPackageList.append(PackageData(data.name, data.version))
    return NotExsitsPackageList

def Create_pac(missingPackage):
    for data in missingPackage:
        os.makedirs(pacPath+data.name+'.'+data.version+'/lib/net452')
        Create_files(pacPath+data.name+'.'+data.version+'/', data.name+'.'+data.version, "nupkg")
        Create_files(pacPath+data.name+'.'+data.version+'/lib/net452/', data.name, "dll")
        Create_files(pacPath+data.name+'.'+data.version+'/lib/net452/', data.name, "XML")

def Create_files(path,fileName,FileType): 
    f=open(path + fileName+"."+FileType,"w+")
    f.close()
    
def Printer(printData):
    for data in printData:
        print(data.name+'.'+data.version)



       
#Main
print('Started')
data = Open_file(pacFile)
packageData = Get_pacData(data)
notExsits = GetNotExsists_pac(packageData)
Printer(notExsits)
Create_pac(notExsits)
print()
print('Ended, created: ' +str(len(notExsits)))
