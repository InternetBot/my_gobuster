"""
Just trying to make my own gobuster in python
:3
"""
print ("Specify Targets IP or Url :3 :  ")
target = input()

#reading the file 
#sigh for some reason having issues with leading zeros and decimal literal reading into a file (will fix later)
def read_file(filename):
    with open('filename', 'r') as f:
        commondir = f.readlines()
    return commondir
 
filename = 'wordweblist.txt'
commondir = read_file(filename)
print(commondir)