import os
import datetime

# Open the file within a with block to make sure it closes when you'r done.
with open("file.txt", "w") as file:
    # "w" opens the file but in write only mode
    # write only mode would write over previous entries in the file if exists.
    # other modes:
    # "r": read only mode. [default]
    # "a": append mode.
    # "r+": read-write mode.

    file.write("Well that's another chunk of text added to the file.\n")
    file.write("Well that's another chunk of text added to the file.\n")
    # The write method returns the number of chars were wrote.

# check if a file exists.
poem = "inspire.txt"
if os.path.exists(poem):
    with open(poem) as file:
        # Iterate over the file contents line by line
        for line in file:
            print(line.strip())

# Get the current working directory
print(f"Current working directory is: {os.getcwd()}")

# Get the absolute path for a file
file_path = os.path.abspath(poem)
print(f"{poem} path is: {file_path}")

# Get a file size
size = os.path.getsize(poem)
print(f"Filesize of {poem}: {size}")

# Get the last time the file was modified
timestamp = os.path.getmtime(poem)
modified = datetime.datetime.fromtimestamp(timestamp)

print("mohee is here..")
print("Kareem is dead...")
print("they are watching movie right now in workshop space")