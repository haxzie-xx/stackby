import fire
from os import getcwd
from scripts import sb_date, sb_type, sb_ext, sb_undo

class StackBy:
  """ Fire Class for StackBy Operations """
  def __init__(self):
    print("StackBy v0.01 Alpha")


  """ Method to revert stacking of files """
  def undo(self, dir = getcwd()):
    sb_undo.undo(dir)

  """ Function to stack the given directory based on extensions"""
  def ext(self, dir = getcwd()):
   sb_ext.stackby_extension(dir)
    
  """ Function to stack files based on type of predetermined filetypes """
  def type(self, dir = getcwd()):
    sb_type.stackby_type(dir)
            
  """ Function to stack files based on created date """
  def date(self, dir = getcwd()):
    sb_date.stackby_date(dir)

if __name__ == '__main__':
  fire.Fire(StackBy)
