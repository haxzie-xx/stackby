import fire, re
from os import listdir, getcwd, makedirs, rename
from os.path import isfile, isdir, join

class StackBy:
  """ Fire Class for StackBy Operations """
  def __init__(self):
    print("StackBy v0.01 Alpha")

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
      extension = result.groups()[0]
      #generate the new directory of the file
      file_dir = join(dir, extension)
      #if the directory doesn't exist,
      if not isdir(file_dir):
        print("Creating Directory: "+ file_dir)
        #create the new directory
        makedirs(file_dir)
      #finally, move the file to the new extension directory
      print("Moving: "+filename+" -> "+extension+"/"+filename)
      rename(join(dir, filename), join(file_dir, filename))
    
    """ Function to stack files based on type of predetermined filetypes """
    def type(self, dir = getcwd()):
      print("Not yet implemented")

    """ Function to stack files based on created date """
  def created(self, dir = getcwd()):
      #check if the directory is valid
      if not isdir(dir):
          print('Invalid Directory')
          return
      #Fetching and Sorting of the files
      entries = (os.path.join(dir, fn) for fn in os.listdir(dir))
      entries = ((os.stat(path), path) for path in entries)
      entries = ((stat[ST_CTIME], path)
                for stat, path in entries if S_ISREG(stat[ST_MODE])) 
      for cdate, path in sorted(entries):
            date=time.ctime(cdate)
            fp=os.path.basename(path)
            #String Manipulation included to extract only Date, Month and Year from the 'Time'
            date=date[:8]+date[9]+date[19:]
            print date, fp
            file_dir=join(dir,date)
            #Replace all the spaces with underscores in the foldername
            file_dir=file_dir.replace(" ","_")
            #check if the folder by the name of Date Created exists, if not, make a new folder
            if not isdir(file_dir):
                print("Creating Directory : ",file_dir)
                makedirs(file_dir)
            fp=os.path.basename(path)
            #Move files to the respective directory
            print("Moving : ",fp,"->",file_dir)
            rename(join(dir,fp),join(file_dir,fp))
      
if __name__ == '__main__':
  fire.Fire(StackBy)
