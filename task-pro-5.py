"""

Ru: скрипт удаления старых файлов и пустых директорий

Eng: script to delete old files and empty directories

"""

import os
import time

DAYS = 5
FOLDERS = ["C:\/testDelete\/12"]

print(FOLDERS)

TOTAL_DELETED_SIZE = 0
TOTAL_DELETED_FILE = 0
TOTAL_DELETED_DIRS = 0

nowTime = time.time() 
oldTime = nowTime - 60*60*24*DAYS 

def delete_old_files(folder):
    """Delete files older than X DAYS"""
    global TOTAL_DELETED_FILE
    global TOTAL_DELETED_SIZE
    for path, dirs, files in os.walk(folder):  
        for file in files:                     
            fileName = os.path.join(path, file)
            fileTime = os.path.getmtime(fileName)
            if fileTime < oldTime:
                sizeFile = os.path.getsize(fileName)
                TOTAL_DELETED_SIZE += sizeFile   
                TOTAL_DELETED_FILE += 1          
                print("Deleting file: " + str(fileName))
                os.remove(fileName)              

def delete_empty_dir(folder):
    global TOTAL_DELETED_DIRS
    empty_folders_in_this_run = 0
    for path, dirs, files in os.walk(folder):
        if (not dirs) and (not files):
            TOTAL_DELETED_DIRS += 1
            empty_folders_in_this_run += 1
            print("Deleting empty dir: " + str(path))
            os.rmdir(path)
    if empty_folders_in_this_run > 0:
        delete_empty_dir(folder)


starttime = time.asctime()          

for folder in FOLDERS:
    delete_old_files(folder)        
    delete_empty_dir(folder)        

finishtime = time.asctime()

print("--- --- --- --- --- --- --- --- --- --- ---")
print("Start time: " + str(starttime))
print("Total deleted size: " + str(int(TOTAL_DELETED_SIZE/1024/1024)) + "Mb")
print("Total deleted files: " + str(TOTAL_DELETED_FILE))
print("Total deleted empty folders: " + str(TOTAL_DELETED_DIRS))
print("Finish time: " + str(finishtime))
print("--- --- --- --- --- --- --- --- --- --- ---")