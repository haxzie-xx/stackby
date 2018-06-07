import fire, re, time
from os import listdir, getcwd, makedirs, rename, rmdir, stat
from os.path import isfile, isdir, join

""" Method to create backup log in .stackby file """
def backup(source, destination, filename):
  try:
    fh = open(source+'/.stackby','a+')
    fh.write(str(time.time())+" "+source+" "+destination+" "+filename+"\n")
    fh.close()
  except IOError:
    print("IO Error")
    fh.close()
  return

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

  """ Method to revert stacking of files """
  def undo(self, dir = getcwd(), n = 1):
    n = int(n)
    if n > 0:
      try:
        fh = open(dir+'/.stackby','r')
        content = fh.readlines()
        print(content)
        fh.close()
        fh = open(dir+'/.stackby','w+')
        undoList = [] #create a list to store files to undo
        for data in content[-n:]:
          undoList.append(data.split())
        for data in undoList:
              if isfile(join(data[2], data[3])) and isdir(data[1]):
                print("Moving back: ",join(data[2], data[3])," -> ",join(data[1], data[3]))
                rename(join(data[2], data[3]), join(data[1], data[3]))
                try:
                  rmdir(data[2])
                except OSError:
                  print("cannot delete",data[2],",not an empty directory")
        fh.writelines(content[:-n])
        fh.close()
      except IOError:
        print("IO Error")
        fh.close()
      return
    else:
      print("number of files to undo must be greater than 0")
      return

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
      backup(dir, file_dir, filename)
    
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
      entries = (join(dir, fn) for fn in listdir(dir))
      entries = ((stat(path), path) for path in entries)
      entries = ((stat[ST_CTIME], path)
                for stat, path in entries if S_ISREG(stat[ST_MODE])) 
      for cdate, path in sorted(entries):
            date=time.ctime(cdate)
            fp=basename(path)
            #String Manipulation included to extract only Date, Month and Year from the 'Time'
            date=date[:8]+date[9]+date[19:]
            print(date, fp)
            file_dir=join(dir,date)
            #Replace all the spaces with underscores in the foldername
            file_dir=file_dir.replace(" ","_")
            #check if the folder by the name of Date Created exists, if not, make a new folder
            if not isdir(file_dir):
                print("Creating Directory : ",file_dir)
                makedirs(file_dir)
            fp=basename(path)
            #Move files to the respective directory
            print("Moving : ",fp,"->",file_dir)
            rename(join(dir,fp),join(file_dir,fp))
      
if __name__ == '__main__':
  fire.Fire(StackBy)
