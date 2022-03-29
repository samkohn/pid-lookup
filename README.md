PID Lookups
==========


Name to PID
---------

The script ``name_to_pid.py`` is an interactive script
which attempts to find the PersonID corresponding
to each in a list of names.

Run the script by simply executing it with Python.
The script will ask for a filename of a CSV.
The file should have columns "FullName" and "PersonID".
Any other columns will be ignored.

The script will also ask for a list of names.
These can be copied from a single column in a spreadsheet
and pasted directly into the command line.
An extra blank line will confirm the list is complete.

Then the script will loop through each name that was input,
and try to find the best match among the names in the CSV.
The top 5 matches will be presented, along with an option
to indicate no match was found.

After all names have been processed,
the script will give you the option to provide an output CSV filename
that saves the name and PersonID of each row,
or to simply press enter to have the PersonID results copied to the clipboard.
These copied results are in a format to be pasted directly
into a column of a spreadsheet,
are in the exact same order as the original input list of names,
and include blank lines / cells where no match was found,
so that the output can be pasted into the same spreadsheet
the input was taken from.

PID to Data
----------

The script pid_to_data.py is an interactive script
which looks up data columns from a spreadsheet,
given a list of PersonIDs.

The execution is almost identical to the ``name_to_pid.py`` script:
a master CSV file is requested,
followed by a list of column names to look up.
Then the results are either saved to a spreadsheet or copied to the clipboard,
again in a format that is pasteable directly into a spreadsheet.

