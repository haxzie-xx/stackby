import mimetypes
from os import listdir, getcwd, makedirs, rename
from os.path import isfile, isdir, join, basename
from scripts.sb_backup import backup
from scripts.get_files import getFiles

""" Function to list known extension for filetype"""
def get_extensions_for_type(general_type):
  for ext in mimetypes.types_map:
      if mimetypes.types_map[ext].split('/')[0] == general_type:
          yield ext

def stackby_type(dir):
    extensions = ['image','video','audio']
    count = 0
    for type in extensions:
        ext = tuple(get_extensions_for_type(type))
        for current_ext in ext:
            for filename in getFiles(dir):
                if filename.endswith(current_ext):
                    #generate the new directory of the file
                    file_dir = join(dir, type)
                    #if the directory doesn't exist,
                    if not isdir(file_dir):
                        print("Creating Directory: ", file_dir)
                        #create the new directory
                        try:
                            makedirs(file_dir)
                        except IOError:
                            print("ERROR: Unable to create directory:")
                            print(file_dir)
                            return
                    #finally, move the file to the new extension directory
                    #print("Moving: ",filename," -> ",type,"/",filename)
                    rename(join(dir, filename), join(file_dir, filename))
                    backup(dir, file_dir, filename)
                    count += 1
                else:
                    continue
    
    print("Moved ", count, " files successfully");