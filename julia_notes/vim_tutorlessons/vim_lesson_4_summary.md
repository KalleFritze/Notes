# Lesson 4 SUMMARY 1. `<C-g>`{normal}     displays your location and the file status. `G`{normal}         moves to the end of the file. number `G`{normal}  moves to that line number. `gg`{normal}        moves to the first line. 2. Typing `/`{normal} followed by a phrase searches FORWARD for the phrase. Typing `?`{normal} followed by a phrase searches BACKWARD for the phrase. After a search type `n`{normal} to find the next occurrence in the same
    direction or `N`{normal} to search in the opposite direction.
    `<C-o>`{normal} takes you back to older positions, `<C-i>`{normal} to
    newer positions.

 3. Typing `%`{normal} while the cursor is on a (, ), [, ], {, or } goes to its
    match.

 4. To substitute new for the first old in a line type
~~~ cmd
        :s/old/new
~~~
    To substitute new for all olds on a line type
~~~ cmd
        :s/old/new/g
~~~
    To substitute phrases between two line #'s type
~~~ cmd
        :#,#s/old/new/g
~~~
    To substitute all occurrences in the file type
~~~ cmd
        :%s/old/new/g
~~~
    To ask for confirmation each time add 'c'
~~~ cmd
        :%s/old/new/gc
