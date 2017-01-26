#! /usr/bin/python3

# Author: Maximilian Muth <mail@maxi-muth.de>
# https://github.com/mammuth/bing-wallpaper
# Version: 1.0
# License: GPL-2.0
# Description: Downloads the Bing picture of the Day and sets it as wallpaper (Linux / Windows).

import datetime
from urllib.request import urlopen, urlretrieve
from xml.dom import minidom
import os


#Variables:
idx = '0' #defines the day of the picture: 0 = today, 1 = yesterday, ... 20.
saveDir = './'

#Getting the XML File
usock = urlopen(
    'http://www.bing.com/HPImageArchive.aspx?format=xml&idx=' + idx + '&n=1&mkt=ru-RU') #ru-RU, because they always have 1920x1200 resolution pictures
xmldoc = minidom.parse(usock)
#Parsing the XML File
for element in xmldoc.getElementsByTagName('url'):
    url = 'http://www.bing.com' + element.firstChild.nodeValue

    #Get Current Date as fileName for the downloaded Picture
    now = datetime.datetime.now()
    picPath = saveDir + now.strftime('bing_wp_%d-%m-%Y') + '.jpg'

    #Download and Save the Picture
    #Get a higher resolution by replacing the file name
    #urlretrieve(url.replace('_1366x768', '_1920x1200'), picPath)

    urlretrieve(url, picPath)
    #Set Wallpaper:
    os.system("feh --bg-fill "+picPath)
