#!/usr/bin/python

# This script takes a list of Google Reader urls, parses them, and outputs
# them as a bookmarks.html file.

from BeautifulSoup import BeautifulSoup
import urllib2

bookmarks = open("bookmarks.html", "w")
bookmarks.write("""
<!DOCTYPE NETSCAPE-Bookmark-file-1>
<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
<TITLE>Bookmarks</TITLE>
<H1>Bookmarks</H1>
<DL><p>
""")

urls = open("urls.txt", "r")

for url in urls:
    while True:
        try:
            page = urllib2.urlopen(url)
            soup = BeautifulSoup(page)
            allStories = soup.findAll("h2", {"class" : "item-title"})
            allLinks = [tag.div.a for tag in allStories]

            for link in allLinks:
                bookmarks.write('<DT>' + str(link) + '\n')

            url = soup.find("div", {"id" : "more"}).a['href']
        except:
            break

bookmarks.write("""
</DL><p>""")
