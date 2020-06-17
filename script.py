#!/usr/bin/env python3

import os
import re

mp4_file_regex = re.compile(r'[12][0-9]{3}\-[01][0-9]\-[0-3][0-9]\-[a-z]+[0-9]+(.*)(\.mp4)$')
# [12][0-9]{3}\-[01][0-9]\-[03][0-9]\-[a-z]+[0-9]+(.*)(\.mp4)
def getCorrectMP4(lst):
    return list(filter(mp4_file_regex.match, lst))

def isMP4(name):
    return name[-4:] == '.mp4'

def removeNonMP4(lst):
    print(lst)
    mp4_files = []
    for file in lst:
        if isMP4(file):
            mp4_files.append(file)
    return mp4_files

def check_dir (dir):
    

AM_PATH = "/Users/amohamdy/Documents/projects/lina-academic-deletion-automation/academic-simulator/" 
def main():
    os.chdir (AM_PATH)
    all_files = os.listdir ()
    print ("all files:", all_files)
    mp4_files = getCorrectMP4 (all_files)
    print ("mp4's:", mp4_files)


if __name__ == '__main__':
    main()
