#Python script to copy from one txt file to another

from sys import argv
from os.path import exists

script,from_fileName,to_fileName = argv

#open a file copy the contains of the file to a variable
in_file = open(from_fileName,'r').read()
print(in_file)

#find if new file exists
#print(f"Does the new file existx? {exists(to_fileName)}")

#write the contain to the new file or create one if not present
print("Do you want to continue?")
input('> ')
open(to_fileName,'w').write(in_file)

with open(to_fileName,'r') as txt:
    print(to_fileName,':')
    print(txt.read())
    txt.close()
