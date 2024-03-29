#
# File to search all text file for a given regex
#
#

# Dependencies
import os
import re
import sys

def search(searchString, path='/'):
    # Check if directory is passed as CLI argument
    if len(sys.argv)>1:
        path = sys.argv[1]

    # Set text file location
    location = os.path.join(os.getcwd(), path)

    # Get regex
    regex = re.compile(searchString)

    for folder, subfolders, files in os.walk(location):

        # Iterate over each file
        for file in files:
            # Opening file
            fileObject = open(os.path.join(folder, file))

            # Reading file
            text = fileObject.read()

            # Closing file
            fileObject.close()

            # Checking for matches
            matches = regex.findall(text)

            # Printing result
            print(os.path.join(folder, file)+" : ", matches)

# Prompt for imput
print("Enter keyword to search for")
# Call search function
search(input())
