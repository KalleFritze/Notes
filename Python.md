#PYTHON	

####Index

[strings](##Strings)
    [printing only parts of the string](###printing parts of the string)
[tuples](##Tuples)
    [tuple unpacking](###Tuple unpacking)
[built in functions](##built in functions)
[File Input and Output](##File Input and Output)
    [writing text files](###writing files)
    [reading text files](###reading files)
    [appending to text files](###appending to files)
    [complicated folder structures](### complicated folder structures)
    [the os module](###the os module)
    [the glob module](###the glob module)
    [reading and writing CSV data](###CSV data)
    



##Strings

###printing parts of the string
line = "hello world"
lines_piece = line[1:3]

lines_piece="el"
========================
line = "hello world"
lines_piece = line[0:(len(line)-3)]
    -removes three characters from original line


##Tuples

### Tuple unpacking
list-of-tuples = [(a1, b1, b2), (a2, b2, b3), ......]

for (a, b, c) in list-of-tuples:
    print(a)
    print(b)
    print(c)
    
-splits every tuple in its components and returns them seperately


##built in functions
type(object)
    -returns type of an object:
    types:
        -str
        -int
        -type





## File Input and Output
open() function:
needs to arguments:	1. the file name
			2. whether to [read](###reading files) from the file or to [write](###writing files) in the file
bsp: 
myOutpuFile = open("hello.txt", "w")
 this creates a new file called hello.txt, unless specified otherwise it  is created in the same folder as the script
 
myOutputFile.close()
 this closes the function
 
 
opening a file stored somewhere else:
myInputFile = open(r"C:\path\to\file.txt")

[the os module](###the os module)
### writing files
# if an already existing file is opened in write mode its content is deleted
	to add lines see [append mode](###appending to files)

myOutputFile = open("hello.txt", "w")
myOutputFile.writelines("this is my first file.")
myOutpuFile.close()


writing several lines:
lines can be stored in a list, linebreaks need to be specified by \n:

linesToWrite = ["this is line1", "\n this is line2", "\n this is line3]
myOutputFile.writelines(linesTowrite)


reading from a file stored somewhere else:
myInputFile = open(r"C:\path\to\file.txt", "w")



### appending to files
linebreaks need to be specified even on the first line:
bsp
myOutputFile= open('file.txt', 'a')
linesToAdd = ["\nThis is an added line"]
myOutpuFile.writelines(linesToAdd)
myOutputFile.close()



### reading files]
myInputfile = open("hello.txt", "r")
print myInputfile.readlines()
myInputfile.close()

printing each line seperately:

myInputFile = open("Julia.md", "r")

for x in myInputFile.readlines():
    print(x,  end = "")
    
myInputFile.close()


the end = "" part has to be added, otherwise the print function adds extra linebreaks
anything can be added in the end section, python will print this at the start of each line starting with the second one

### complicated folder structures
import os

myPath = r"C:\Users\User\Desktop\Notes"
inputFileName = os.path.join(myPath, "Julia.md")
with open(inputFileName, "r")as myInputFile:
    for line in myInputFile.readlines():
        print(line, end="")

os.path.join() function combines to paths to create a single  valid path





### the os module
gives some of thesame basic functions as a terminal (bspw to make or delete directories)

functions:
os.path.join(path1, path2)
    -joins two path strings into a valid path
os.listdir(path/to/directory)
    -creates a list of every file and folder in the directory (but not the files in the folders)
os.rename(path/to/file_oldname, path/to/file_newname)
os.path.isfile(path/to/object)
    -checks if the object is a file, returns boolean
os.path.isdir(path/to/object)
    -checks if the object is a directory, returns boolean
os.path.exists(path/to/object)
    -checks if file exists, returns True if it exists
os.walk(path/to/directory)
    -returns list of tuples of the form: (directory, [subfolders], [files]) for each directory
    -for each subfolder of the directory the tuple contains: (path/to/directory, [list of subfolders in directory], [list of files in the directory(not in subfolders)])
    -this is reapeated for each subfolder, even those already listed in the subfolders category of previous tuples
os.path.getsize(path/to/file)
    -returns integer of the size of the file in bites
os.path.remove(path/to/file)
    -deletes file

    
modules:
filename.endswith(.extension)
    -returns boolean value:
    True if filename has .extension extension, False if not


example of functions:		(keyword: removing characters from a string)
rename every .gif file in a folder to be a.jpg file
import os

path = r"C:\Users\User\Desktop\aaron"

fileNameslist = os.listdir(path)
for file in fileNameslist:
    if file.endswith(".md"):
        new_filename = (file[0:len(file)-2] + "txt")
        os.rename(os.path.join(path, file), os.path.join(path, new_filename))


print(os.listdir(path))


###the glob module
functions:
glob.glob(path\to\directory\*.extension): creates a list: filters a directory for a given filetype (fileextension)
takes directory with * and an extension as the argument
* in this case stands for "any": the list should contain any file in the directory with the file extension .extension
creates a list of all files in the given directory with that extension
glob.glob(path\to\directory\*\*.extension)
looks for file extensions only in files that are in folders in the directory (one layer deeper)
the filtered files can be further specified: "image[0-9][0-9].gif" searches for any .gif file that is called "image" followed by to numbers in the range 0-9
        * is not used here as we are not filtering for any file but only files with a specific file name

    
   
   
###CSV data
-csv: comma seperated value

    
    
    
    
    
    
    -
