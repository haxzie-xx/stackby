import fire, random, string
from os import listdir, getcwd, makedirs, rename, urandom
from os.path import isfile, isdir, join

rand_files = ['jpg', 'png', 'gif', 'txt', 'pdf', 'mov', 'avi', 'mp4', 'doc', 'docx', 'html', 'css', 'exe']

""" Method to create random file """
def create_rand_file(dir):
    filename = "".join( [random.choice(string.ascii_lowercase) for i in range(random.randint(3, 15))])
    filename = filename + "."+random.choice(rand_files)
    with open(join(dir, filename), 'wb') as fout:
        fout.write(urandom(random.randint(1024, 10240)))

class Files:
    """ Class to generate random files and drop it in the given directory"""
    def __init__ (self):
        print("Current dir: ",getcwd())
    
    

    """ Function to generate random files in the given directory 
        By default, it'll create in files sub-directory in cwd """
    def random(self, dir = getcwd(), count = 100):
        #if the destination is current directory
        #create a subdirectory with name files
        if dir is getcwd():
            self.destination = join(dir, "test_files")
            if not isdir(self.destination):
                makedirs(self.destination)
        else:
            self.destination = join(dir, "test_files")
            if not isdir(self.destination):
                makedirs(self.destination)
        
        for i in range(count):
            create_rand_file(self.destination)

if __name__ == '__main__':
  fire.Fire(Files)

