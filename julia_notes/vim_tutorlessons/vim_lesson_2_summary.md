# Lesson 2 SUMMARY



 1. To delete from the cursor up to the next word type:    `dw`

 2. To delete from the cursor to the end of a line type:   `d$`

 3. To delete a whole line type:                           dd{normal}

 4. To repeat a motion prepend it with a number:           `2w`

 5. The format for a change command is:

    operator   [number]   motion

    where:

    operator -   is what to do, such as [d](d) for delete
    [number] -   is an optional count to repeat the motion
    motion   -   moves over the text to operate on, such as:
                    [w](w) (word),
                    $ (to the end of line), etc.

 6. To move to the start of the line use a zero: [0](0)

 7. To undo previous actions, type:            `u`{normal}  (lowercase u)
    To undo all the changes on a line, type:   `U`{normal}  (capital U)
    To redo the undos, type:                   `<C-r>`

