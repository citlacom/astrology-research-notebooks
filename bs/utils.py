import subprocess
import os
import sys
import inspect
import re

import shutil



currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

path = '/path/*'

def cleanup():
    j = 'rm -fr ' + path
    print(j)
    # j = 'del /S C:\\sweph\\csv\\*.csv'
    p = subprocess.Popen(j,
    shell=True,
    stdin=None,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE )
    lines = p.communicate()[0].decode('utf-8').splitlines()
    print(lines)

def archive(year):
    if not os.path.exists(path + 'archive/' + str(year)):
        os.makedirs(path + 'archive/' + str(year))
    j = 'cp -r ' + path + 'p/' + str(year) + '.csv' + ' ' + path + 'archive/' + str(year)
    p = subprocess.Popen(j,
    shell=True,
    stdin=None,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE )
    lines = p.communicate()[0].decode('utf-8').splitlines()
    print(lines)

    k = 'cp -r ' + path + '/csv ' + path + 'archive/' + str(year)
    p = subprocess.Popen(k,
    shell=True,
    stdin=None,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE )
    lines = p.communicate()[0].decode('utf-8').splitlines()
    print(lines)

def isLeap(year):
    # Python program to check if year is a leap year or not
    # To get year (integer input) from the user
    # year = int(input("Enter a year: "))
    # To print
    # print("{0} is a leap year".format(year))

    if (year % 4) == 0:
       if (year % 100) == 0:
           if (year % 400) == 0:
               return True
           else:
               return False
       else:
           return True
    else:
       return False

def checkLeap(year):
    if isLeap(year) == True:
        year_len = '366'
    else:
        year_len = '365'
    return year_len

def updateCommand(command,body,year,days,center,key=None):
        if center == 'helio':
            command = re.sub('g,', 'g, -hel', command)
        if key:
            command = re.sub('key', str(key), command)

        command = re.sub('body', str(body), command)
        command = re.sub('year', str(year), command)
        command = re.sub('days', str(days), command)

        return command

def changeZodiac(line):
    line1 = line
    line2 = line

    line2 = re.sub('[ ]+', '', line2)
    line2 = re.sub('[a-zA-Z]+', '.', line2)

    line1 = re.sub('[ ]+', '', line1)
    line1 = re.sub('[0-9]+', '', line1)

    line1 = re.sub('ar',  '1'   , line1)
    line1 = re.sub('ta',  '2'   , line1)
    line1 = re.sub('ge',  '3'   , line1)
    line1 = re.sub('cn',  '4'   , line1)
    line1 = re.sub('le',  '5'   , line1)
    line1 = re.sub('vi',  '6'   , line1)
    line1 = re.sub('li',  '7'   , line1)
    line1 = re.sub('sc',  '8'   , line1)
    line1 = re.sub('sa',  '9'   , line1)
    line1 = re.sub('cp',  '10'  , line1)
    line1 = re.sub('aq',  '11'  , line1)
    line1 = re.sub('pi',  '12'  , line1)

    line3 = line1 + ',' + line2
    return line3

def coorZodiac(line):
    line1 = line

    line = re.sub('[ ]+', '', line)
    line = re.sub('[a-zA-Z]+', '.', line)

    return line

def cleanLine(line):
        line = re.sub('[ ]+', '', line)
        line = re.sub('[a-zA-Z]+', ':', line)
        return line
