# Try and except attempts to find the different errors, such as missing files, bad user input, or missing permission.

import os

try:
    with open ("save_new.txt", "r")as my_file:
        file_data = my_file.read()
except FileNotFoundError as e:
    print ("File not found.")
except IOError as e:
    print ("An error has occurred.")
    print(e)

# The "except FileNotFoundError as e:" part means that when the file doesnt exist, this is an error,
# and we can make the response to this specific error unique in comparison to other errors.
# if the systme has an error on its own, it will produce to the user "An error has occurred.".
