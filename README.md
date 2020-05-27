# ProcessHackerTrimmer

This python script was written very quickly and is not tested. It does seem to do what I was expecting, with some exceptions. 

You will need to delete the top three lines that are at the top of the file by default. It should look something like this:

      Process Hacker 2.39.124
      Windows NT 6.1 Service Pack 1 (64-bit)
      5/15/2020 2:52:48 PM
      
For the command to run the program, there are no flags and it only expects one command line argument.

## What it is supposed to do

This was made to help clean up process hacker memory string text files. It goes through the text file and removes  
the memory address and string length from the beginning of the lines. So it would take a line like:

      0x22a3b10 (9): example string
      
And make it:
      
      example string
      
I made this to be able to use the Process Hacker string dump with the rank_strings command that is in the FlareVM for FireEye.

## Issues:

- Does not trim the first lines if it is the first line in the file.
