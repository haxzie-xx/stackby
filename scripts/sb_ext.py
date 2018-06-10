import re
from os import listdir, getcwd, makedirs, rename
from os.path import isfile, isdir, join
from scripts.get_files import getFiles
from scripts.sb_backup import backup

def stackby_extension(dir):
     #if the given directory is invalid, return
    if not isdir(dir):
      print('Invalid Directory')
      return

    #get all the filenames and validate based on extension
    #this will avoid dotfiles and files with no extensions
    files = getFiles(dir);
    for filename in files:
      result = re.match(r'^[A-Za-z0-9_\-\\()\s,\.\'@\[\]]+\.([a-zA-Z0-9]+)$', filename)
      if not result:
        continue
      #get the file extension
      extension = result.groups()[0]
      #generate the new directory of the file
      file_dir = join(dir, extension)
      #if the directory doesn't exist,
      if not isdir(file_dir):
        print("Creating Directory: "+ file_dir)
        #create the new directory
        try:
          makedirs(file_dir)
        except IOError:
          print("ERROR: Unable to create directory:")
          print(file_dir)
          return
      #finally, move the file to the new extension directory
      #print("Moving: "+filename+" -> "+extension+"/"+filename)
      rename(join(dir, filename), join(file_dir, filename))
      backup(dir, file_dir, filename)
    
    print("Moved ", len(files)," Successfully")