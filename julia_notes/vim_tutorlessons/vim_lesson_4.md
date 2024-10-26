# Lesson 4
[Lesson4, sumary](vim_lesson_four_summary.md)

## Lesson 4.1: Cursor location and file status, navigating the file

Ctrl+g to show filename and position in the file

G to move to the bottom of the file
gg to move to the start of the file

type the number of a fileline and G to jump to that line



## Lesson 4.2: the search command
type / and search for a word


## Lesson 4.3
with the cursor on a type of parenthesis like (), [], {}, ...
type % to highlight the corresopnding parenthesis


## Lesson 4.4: the substitute command
substitute words in one line:
subtitute one word in that line: :s/woord/word
- changes one instance of "woord" into "word"
substitute all instances of that word in that line: :s/old_word/new_word/g

change every occurrence of one word in the entire file into a new word:

:%s/old_word/new_word/g



