#
# File to download BNHA manga
#
#

# Dependencies
import requests
import bs4
import os
import sys

# Set base dir location
location = os.path.join(os.getcwd(), "BNHA")

# Make new dir
if not os.path.exists(location):
    os.makedirs(location)

# Set latest chapter
latestChapter = int(sys.argv[1]) if len(sys.argv)>1 else 2

# Iterate over each chapter
for i in range(1, latestChapter):

    res = requests.get("https://myheromanga.com/manga/boku-no-hero-academia-chapter-"+str(i))
    # Getting response HTML
    resHTML = bs4.BeautifulSoup(res.text, features="html.parser")

    # Getting only the links
    links = resHTML.select('img[src]')

    # Set chapter dir location
    chapterDir = os.path.join(location, "Chapter "+str(i))

    # Make new dir for chapter
    if not os.path.exists(chapterDir):
        os.makedirs(chapterDir)

    # Iterate over each image
    for i in range(len(links)):
        # Get image URL
        imageURL = links[i].attrs["src"]

        # Get image from its URL
        image = requests.get(imageURL)

        # Set file name
        filename = "Page "+str(i+1)+".jpeg"

        # Save image to file
        fileObject = open(os.path.join(chapterDir, filename), "wb")
        for chunk in image.iter_content(1024):
            fileObject.write(chunk)
        fileObject.close()
