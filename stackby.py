import mimetypes
import fire, re
from os import listdir, getcwd, makedirs, rename
from os.path import isfile, isdir, join
""" Function to list known extension for filetype"""
def get_extensions_for_type(general_type):
  for ext in mimetypes.types_map:
      if mimetypes.types_map[ext].split('/')[0] == general_type:
          yield ext
class StackBy:
  """ Fire Class for StackBy Operations """
  def __init__(self):
    print("Welcome to stackby")

  """ Method to return all files in the given directory """
  def getFiles(self, dir):
    #get all the contents of the dir
    #add valid file to the array
    files = [filename for filename in listdir(dir) if isfile(join(dir, filename))]
    return files

  """ Function to stack the given directory based on extensions"""
  def ext(self, dir = getcwd()):
    #if the given directory is invalid, return
    if not isdir(dir):
      print('Invalid Directory')
      return

    #get all the filenames and validate based on extension
    #this will avoid dotfiles and files with no extensions
    for filename in self.getFiles(dir):
      result = re.match(r'^[A-Za-z0-9_\-\\()\s,\.\'@\[\]]+\.([a-zA-Z0-9]+)$', filename)
      if not result:
        continue
      
      #get the file extension
      extention = result.groups()[0]
      #generate the new directory of the file
      file_dir = join(dir, extention)
      #if the directory doesn't exist,
      if not isdir(file_dir):
        print("Creating Directory: ", file_dir)
        #create the new directory
        makedirs(file_dir)
      #finally, move the file to the new extension directory
      print("Moving: ",filename," -> ",extention,"/",filename)
      rename(join(dir, filename), join(file_dir, filename))
    
  """ Function to stack files based on type of predetermined filetypes """
  def type(self, dir = getcwd()):
      list = ['image','video','audio']
      for type in list:
        ext = tuple(get_extensions_for_type(type))
        for current_ext in ext:
          for filename in self.getFiles(dir):
            if filename.endswith(current_ext):
              #generate the new directory of the file
              file_dir = join(dir, type)
              #if the directory doesn't exist,
              if not isdir(file_dir):
                print("Creating Directory: ", file_dir)
                #create the new directory
                makedirs(file_dir)
              #finally, move the file to the new extension directory
              print("Moving: ",filename," -> ",type,"/",filename)
              rename(join(dir, filename), join(file_dir, filename))
            else:
              continue

  """ Function to stack files based on created date """
  def created(self, dir = getcwd()):
      print("Not yet implemented")
      
if __name__ == '__main__':
  fire.Fire(StackBy)