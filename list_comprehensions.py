filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.

print("Greetings!")

def remove_hpp(filename: str):
    if filename.endswith(".hpp"):
        filename = filename[:-3] + "h"
    return filename


newfilenames = [remove_hpp(filename) for filename in filenames]

print(newfilenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]
