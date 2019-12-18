#
# File to open top 5 search results
#
#

# Dependencies
import requests
import bs4
import sys
import re
import webbrowser

# Get search string from CLI
searchString = sys.argv[1].replace(' ', '+')

# Create regex to get url from tag
regex = re.compile(r'url')

# Send request with search string
res = requests.get("https://www.google.com/search?q="+searchString+"&oq="+searchString)

# Getting response HTML
resHTML = bs4.BeautifulSoup(res.text, features="html.parser")

# Getting only the links
links = resHTML.select('a[href]')

# Setting minimum number of tabs
noOfTabs = min(5, len(links))
# noOfTabs = len(links)

for i in range(noOfTabs):
    # Check is href attribute exists in element
    if "href" in links[i].attrs:
        # Check if attribute value is a url
        if regex.search(links[i].attrs["href"]):
            # Open in new tab
            webbrowser.open(links[i].attrs["href"].replace("/url?q=", ""))
