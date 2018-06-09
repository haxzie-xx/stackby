import time

""" Method to create backup log in .stackby file """
def backup(source, destination, filename):
  try:
    fh = open(source+'/.stackby','a+')
    fh.write(str(time.time())+" "+source+" "+destination+" "+filename+"\n")
    fh.close()
  except IOError:
    print("IO Error : Unable to write to backup file")
    fh.close()
  return