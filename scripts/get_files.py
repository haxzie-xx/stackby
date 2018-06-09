from os.path import isfile, isdir, join
from os import listdir
  
""" Method to return all files in the given directory """
def getFiles(dir):
    #get all the contents of the dir
    #add valid file to the array
    files = [filename for filename in listdir(dir) if isfile(join(dir, filename))]
    return files