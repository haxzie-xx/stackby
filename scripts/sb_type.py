import mimetypes
from os import listdir, getcwd, makedirs, rename
from os.path import isfile, isdir, join, basename, abspath, splitext, dirname
from scripts.sb_backup import backup
from scripts.get_files import getFiles
from magic import from_file as what_type


""" Function to list known extension for filetype"""
def stackby_type(dir):
    # If the given directory is invalid, return
    if not isdir(dir):
      print('Invalid Directory')
      return

    files =  listdir(dir)                                                      
    for filename in files:
      # Full file path taken to overcome sym links error
      old_file_path = join(dir,filename)
      # Directories are not moved
      if isdir(old_file_path):
        pass
      else:
        # Find the file extension 
        f, ext = splitext(filename)
        extension = ext[1:]
        # Find file/application format dictated by the system
        fileFormat = what_type(old_file_path, mime=True)
       
       # To handle files without extensions
        if extension == fileFormat.split("/")[1]: # "/" is not from path just a string 
          new_file_path = join(fileFormat, filename)
        else:
          new_file_path = join(fileFormat, extension, filename)
        # print(" {} - Format:{}  Extension:{}  NewPath:{}".format(filename, fileFormat, (extension if extension != '' else 'None'), new_file_path)) 
        
        dir_path = join(dir, dirname(new_file_path))
		    #if the directory doesn't exist,
        if not isdir(dir_path):
          print("Creating Directory: "+ dir_path)
        #create the new directory
        try:
          makedirs(dir_path)
        except IOError:
          pass

        file_dir = join(dir, new_file_path)
    
        #finally, move the file to the new extension directory
        rename(old_file_path, file_dir)
        backup(dir, dir_path, filename)
    print("Moved ", len(files)," Successfully")
