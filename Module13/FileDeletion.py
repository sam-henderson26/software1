import os

# os is the operating system, so the code will speak directly to the os and telling it to delete certain files.
# first we can check if the file exists

# if os.path.exists("Module13/save.txt"):
    # os.remove("Module13/save.txt")
# else:
    # print("File not found.")

# will print "File not found." as we have no file with that name; however, if we use save_new.txt instead
# it will delete the file we created through example.py:

if os.path.exists("Module13/save_new.txt"):
    os.remove("Module13/save_new.txt")
else:
    print("File not found.")
