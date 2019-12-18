#
# Walk dir and locate files with given extension
#
#

# Dependencies
import os
import re
import sys

def locate(path="/"):
    # Set location
    location = os.path.join(os.getcwd(), path)
    # Set regex
    regex = re.compile(r'([a-zA-Z0-9\s_\\.\-\(\):])+(.py|.txt|.sh|.bash)$')
    # Walk over current location
    for directory, subDirectory, files in os.walk(location):
        # Iterate over files
        for file in files:
            # Check file extension
            if regex.match(file):
                # Print file name
                print(directory+" : ", file)

path=sys.argv[1] if len(sys.argv)>1 else "/";

locate(path)
