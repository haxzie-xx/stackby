import fire, re
from os import listdir, getcwd, makedirs, rename, walk, sep
from os.path import isfile, isdir, join, splitext, abspath, pathsep, basename, dirname
from magic import from_file as what_format

class StackBy:
  """ Fire Class for StackBy Operations """
  def __init__(self):
    print("StackBy v0.01 Alpha")

  """ Method to return all files in the given directory """
  def listFiles(self, directory, recursion = False):
    # Print all the files of the directory
    for root, dirs, files in walk(directory):
        level = root.replace(directory, '').count(sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}|_{}'.format(subindent, f))
        # Print directory recursively if True
        if recursion is False:
          break

  """ Function to stack the given directory into filetypes based on extensions """
  def FileTypes(self, fromDirectory, toDirectory=getcwd()):
    # If the given directory is invalid, return
    if not isdir(fromDirectory):
      print('Invalid Directory')
      return

    print(abspath(fromDirectory))
    files =  listdir(fromDirectory)                                                      
    for File in files:
      # Full file path taken to overcome sym links error
      old_file_path = join(fromDirectory,File)
      # Directories are not moved
      if isdir(old_file_path):
        print("***{} is a Directory, Skipping.***".format(File))
      else:
        # Find the file extension 
        f, ext = splitext(File)
        extension = ext[1:]
        # Find file/application format dictated by the system
        fileFormat = what_format(old_file_path, mime=True)
       
        if extension == fileFormat.split("/")[1]:
          new_file_path = join(fileFormat, File)
        else:
          new_file_path = join(fileFormat, extension, File)
        print(" {} - Format:{}  Extension:{}  NewPath:{}".format(File, fileFormat, (extension if extension != '' else 'None'), new_file_path)) 
        #if the directory doesn't exist,
        dir_path = dirname(new_file_path)
        if not isdir(dir_path):
          print("Creating Directory: ", dir_path)
          #create the new directory
          makedirs(dir_path)
        #finally, move the file to the new extension directory
        print("Moving: ",old_file_path," -> ",new_file_path)
        rename(join(fromDirectory, old_file_path), join(toDirectory, new_file_path))
        
    
    #get all the filenames and validate based on extension
    #this will avoid dotfiles and files with no extensions
    # for filename in self.getFiles(dir):
    #   result = re.match(r'^[A-Za-z0-9_\-\\()\s,\.\'@\[\]]+\.([a-zA-Z0-9]+)$', filename)
    #   if not result:
    #     continue
      
    #   #get the file extension
    #   extention = result.groups()[0]
    #   #generate the new directory of the file
    #   file_dir = join(dir, extention)
    #   #if the directory doesn't exist,
    #   if not isdir(file_dir):
    #     print("Creating Directory: ", file_dir)
    #     #create the new directory
    #     makedirs(file_dir)
    #   #finally, move the file to the new extension directory
    #   print("Moving: ",filename," -> ",extention,"/",filename)
    #   rename(join(dir, filename), join(file_dir, filename))
    
    """ Function to stack files based on type of predetermined filetypes """
    def type(self, dir = getcwd()):
      print("Not yet implemented")

    """ Function to stack files based on created date """
    def created(self, dir = getcwd()):
      print("Not yet implemented")
      
if __name__ == '__main__':
  fire.Fire(StackBy)