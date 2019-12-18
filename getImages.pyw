#
# File to open top 5 search results
#
#

# Dependencies
import requests
import bs4
import sys
import os

# Check if CLI argument is provided
if not len(sys.argv)>1:
    print("Search string must be provided as CLI argument")
    sys.exit()

# Set image location
location = os.path.join(os.getcwd(), sys.argv[1])

# Make new dir to store images
if not os.path.exists(location):
    os.makedirs(location)

# Get search string from CLI
searchString = sys.argv[1].replace(' ', '+')

# Send request with search string
res = requests.get("https://www.google.com/search?tbm=isch&q="+searchString)

# Getting response HTML
resHTML = bs4.BeautifulSoup(res.text, features="html.parser")

# Getting only the links
links = resHTML.select('img[src]')

# Setting minimum number of tabs
noOfImages = len(links)

for i in range(noOfImages):
    # Check is href attribute exists in element
    image = requests.get(links[i].attrs["src"])
    # Write image to file
    fileObject = open(os.path.join(location, str(i)+".png"), "wb")
    for chunk in image.iter_content(10000):
        fileObject.write(chunk)
