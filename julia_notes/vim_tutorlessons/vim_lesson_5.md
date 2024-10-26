# Lesson 5

## Lesson 5.1: execute an external command

type :! in normal mode to execute any external shell command

## Lesson 5.2: writing files

:!dir to get a listing of the directory
:w filename to create a new file named filename

delete file: :!del filename

## Lesson 5.3 selecting text to write
press v ([visual selection]()) and move curser to highlight text
type :
        `:'<,'>` will appear

type w filename to create a new file with the highlighted lines


## Lesson 5  summary:
 1. [:!command](:!cmd) executes an external command.

     Some useful examples are:
     `:!dir`{vim}                   - shows a directory listing
     `:!del FILENAME`{vim}          - removes file FILENAME

 2. [:w](:w) FILENAME              writes the current Neovim file to disk with
                             name FILENAME.

 3. [v](v)  motion  :w FILENAME   saves the Visually selected lines in file
                             FILENAME.

 4. [:r](:r) FILENAME              retrieves disk file FILENAME and puts it
                             below the cursor position.

 5. [:r !dir](:r!)                  reads the output of the dir command and
                             puts it below the cursor position.