from sys import argv
script,file_name = argv

print("We will be deleting all the contails of the file please,")
print("Press Enter key to move forword else hit ctrl+C")
input('? ')

print("Openning the file...")
#'w' will erase the file befor Openning so its prefered to use truncate()
#if we want to append to the existing file we can use 'a' write command will
#automaticly add next to the line
txt = open(file_name,'r+')

print("Deleting all entries in the file")
#txt.truncate()

print("Please provide 3 lines about yourself")

line1 = input('Line1: ')
line2 = input('Line2: ')
line3 = input('Line3: ')

_nexLine = '\n'
txt.write(line1)
txt.write(_nexLine)
txt.write(line2)
txt.write(_nexLine)
txt.write(line3)
txt.write(_nexLine)

print("We are done writting into the file we are closing the file now!")
txt.close()
with open(file_name,'r') as tx_read:
    #tx_read.seek(0)
    print(file_name)
    print(tx_read.read())
tx_read.close
