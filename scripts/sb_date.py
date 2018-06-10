import time
from os import listdir, getcwd, makedirs, rename, rmdir, remove, stat
from os.path import isfile, isdir, join, basename
from stat import S_ISREG, ST_MODE, ST_CTIME
from scripts.sb_backup import backup

def stackby_date(dir):
    #check if the directory is valid
    if not isdir(dir):
        print('Invalid Directory')
        return
    #Fetching and Sorting of the files
    entries = (join(dir, fn) for fn in listdir(dir))
    entries = ((stat(path), path) for path in entries)
    entries = ((stat[ST_CTIME], path) for stat, path in entries if S_ISREG(stat[ST_MODE])) 

    count = 0

    for cdate, path in sorted(entries):
      date=time.ctime(cdate)
      filename=basename(path)
      #String Manipulation included to extract only Date, Month and Year from the 'Time'
      if date[8]==' ':
        date=date[:8]+date[9]+date[19:]
      else:
        date=date[:10]+date[19:]
      file_dir=join(dir,date)
      #Replace all the spaces with underscores in the foldername
      file_dir=file_dir.replace(" ","_")
      #check if the folder by the name of Date Created exists, if not, make a new folder
      if not isdir(file_dir):
        print("Creating Directory : "+file_dir)
        try:
          makedirs(file_dir)
        except IOError:
          print("ERROR: Unable to create directory:")
          print(file_dir)
          return
      #Move files to the respective directory
      #print("Moving : "+filename+" -> "+file_dir)
      rename(join(dir,filename),join(file_dir,filename))
      backup(dir, file_dir, filename)
      count += 1


    print("Moved ",count," files successfully")