# Open a file:

with open ("Module13/save_new.txt", "w") as my_file:
    my_file.write("This is a test")

# (Above code) Creates a new file called "save_new.txt" and writes ("w") "This is a test" inside.
# Using "w" will overwrite anything already written in the target file.
# Using "Module13/" allows the file to be created within a certain folder, just name the folder and then a slash.

# If we use "a" (append), it will add to the file rather than overwrite:
with open ("Module13/save_new.txt", "a") as my_file:
    my_file.write (" \nThis should add a new line of text")

# We can use "r" to read (print) lines of codes, in the example, I use "read()" as a way to read all the lines in the entire
# file, however using "readlines()" I can choose which lines to have printed out into the terminal.
with open ("Module13/save_new.txt", "r") as my_file:
    file_data = my_file.read()
    print(file_data)
