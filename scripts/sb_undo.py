from os import listdir, getcwd, makedirs, rename, rmdir, remove, stat
from os.path import isfile, isdir, join, basename


""" Method to revert stacking of files """
def undo(dir):
    try:
      # Open the backup file
      backup_file = join(dir,'.stackby')
      fh = open(backup_file,'r')
      content = fh.readlines()
      fh.close()
      undoList = [] #create a list to store files to undo
      created_dirs = [] #list of script generated directories

      for data in content:
        undoList.append(data.split())
      for data in undoList:
            if isfile(join(data[2], data[3])) and isdir(data[1]):
              #print("Moving back: ",join(data[2], data[3])," -> ",join(data[1], data[3]))
              rename(join(data[2], data[3]), join(data[1], data[3]))
              #if the directory moved to doesn't exist in created_dirs list
              #add the dir to it
              if isdir(data[2]) and (data[2] not in created_dirs):
                created_dirs.append(data[2])
      
      #delete all the script generated directories if its not empty
      if len(created_dirs) != 0:
        for dirname in created_dirs:
          try:
            rmdir(dirname)
          except OSError:
            print("cannot delete ",dirname,", not an empty directory")

      #finally delete the backup file
      if isfile(backup_file):
        try:
          remove(backup_file)
          print('Backup file removed.')
        except OSError:
          print('ERROR: Unable to delete backup file.')

      print("Restored ", len(undoList)," files successfully.")
    except IOError:
      print("ERROR: No backup files found in ",dir)
      fh.close()
    return