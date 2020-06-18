#!/usr/bin/env python3

import os
import re
from colorama import Fore, Back, Style

mp4_file_regex = re.compile (r'[12][0-9]{3}\-[01][0-9]\-[0-3][0-9]\-[a-z]+[0-9]+(.*)(\.mp4)$')
def isCorrectMP4(s):
    return mp4_file_regex.match (s)


def unpack_file (file):
    return file[0:4], file[5:7], file[8:10], file[11: file.find ('-', 11)]
    
PATH_105 = '/'
PATH_106 = '/Users/amohamdy/Documents/projects/lina-academic-deletion-automation/106/'

def file_is_missing (file):
    path = ''
    year, month, day, course = unpack_file (file)
    formatted_date = year[2:] + month + day

    if os.path.exists (PATH_106 + course):
        path = PATH_106
    elif os.path.exists (PATH_105 + course):
        path = PATH_105
    else: # Not in either server -- file is missing!
        return True
    
    date_folder_regex = re.compile ('{}.*'.format (formatted_date))
    date_folders = list (filter (date_folder_regex.match, os.listdir (path + course)))
    if not len (date_folders): # Folder does not exist
        return True
    
    video_regex = re.compile ('{}-{}.*\.mp4'.format (formatted_date, course))
    # If multiple folders look through all of them
    for folder in date_folders:
        print ("PATH:", path)
        print ("COURSE:", course)
        print ("FOLDER:", folder)
        for file in os.listdir (path + course + '/' + folder):
            if (video_regex.match (file)) and os.stat (path + course + '/' + folder + '/' + file).st_size > 0:
                return False

    return True

def check_dir (path, checked, dups, missing, unchecked):
    if (os.path.isfile (path)): # base case
        file = path[path.rfind ('/') + 1:]
        if not isCorrectMP4 (file): # incorrect video format -- cannot process
            unchecked.append (path)
            return
        
        if path in checked: # duplicate file 
            print ("Duplicate file:", path)
            return

        checked.add (path) # avoids double checking duplicates
        if file_is_missing (file):
            missing.append (path )
        else:
            dups.append (path)

    else: # recursive case
        orig_dir = os.getcwd ()
        print ("Entering", path)
        os.chdir (path)
        
        for entry in os.listdir ():
            check_dir (path + entry, checked, dups, missing, unchecked)
        
        print ("Exiting", path)
        os.chdir (orig_dir)
        
        
AM_PATH = "/Users/amohamdy/Documents/projects/lina-academic-deletion-automation/academic-simulator/" 
def main():
    checked = set([])
    dups = []
    missing = []
    unchecked = []
    check_dir (AM_PATH, checked, dups, missing, unchecked)
    print()

    # Printing
    print (Style.BRIGHT + Fore.RED + '----------------------- MISSING -----------------------')
    for video in missing:
        print (video)
    print(Style.RESET_ALL)

    print (Style.BRIGHT + Fore.GREEN + '----------------------- DUPLICATES -----------------------')
    for video in dups:
        print (video)
    print(Style.RESET_ALL)
    
    print (Style.BRIGHT + Fore.YELLOW + '----------------------- UNCHECKED -----------------------')
    for video in unchecked:
        print (video)
    print(Style.RESET_ALL)

if __name__ == '__main__':
    main()


# def isMP4(name):
#     return name[-4:] == '.mp4'

# def removeNonMP4(lst):
#     print(lst)
#     for file in lst:
#         if isMP4(file):
#             mp4_files.append(file)
#     return mp4_files
