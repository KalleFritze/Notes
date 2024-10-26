# Lesson 2

[Lesson2, summary](vim_lesson_two_summary.md)


## 2.1 deleting commands
deleting a word:
- in normal mode, cursor at beginning of word
- type dw

delete everything to the end of the line:
-  in normal mode, cursor at the end of the correct line:
-  type d$
  
delete an entire line>
- in normal mode, curser on the line
- type dd

## 2.2 on operators and motions

Many commands that change text are made from an [operator](operator) and a [motion](navigation).
The format for a delete command with the [d](d) delete operator is as follows:

    d   motion

  Where:
    d      - is the delete operator.
    motion - is what the operator will operate on (listed below).

  A short list of motions:
    [w](w) - until the start of the next word, EXCLUDING its first character.
    [e](e) - to the end of the current word, INCLUDING the last character.
    $ - to the end of the line, INCLUDING the last character.
    0 to  move to the start of the line
    
  Thus typing `de` will delete from the cursor to the end of the word.

NOTE: Pressing just the motion while in Normal mode without an operator will move the cursor as specified.



## Lesson 2.7: The Undo command

press u to undo last command
press U to  undo the commands made o the entire line

press Ctrl+r to redo the changes




