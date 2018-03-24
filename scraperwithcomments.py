import urllib2, csv
# imports the urllib2 module, which allows webpage download and the csv
from bs4 import BeautifulSoup
# pulls the BeautifulSoup package from bs4, allowing the parsing of HTML pages
outfile = open('jaildata.csv', 'w')
# creates a file object, which python links to the computer. First thing in parenthesis
# is the file name, the second indicates writing to a file
writer = csv.writer(outfile)
# designates where to output the writing 
url = 'https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s?max_rows=500'
# creates variable which stores the page we're trying to scrape
html = urllib2.urlopen(url).read()
# uses the urlopen to get the HTML from the url
soup = BeautifulSoup(html, "html.parser")
# parses the HTML using BeautifulSoup and stores in variable soup

tbody = soup.find('tbody', {'class': 'stripe'})
# creates a variable containing the data pulled from the HTML with the tbody
# tag, which contain the terms class and stripe
rows = tbody.find_all('tr')
# defining a variable for all the rows, finding all the 'tr' tags in the tbody

for row in rows:
# creates a loop to go through all the rows of data
    cells = row.find_all('td')
# creates cells variable, by going throw the row variable and finding all HTML "td"
# tags
    data = []
# creates a data variable as an empty list?
    for cell in cells:
        data.append(cell.text)
# another loop to which goes through the cells and appends the empty data list with the cell text
    writer.writerow(data)
 # outputs the rows filled with data to the outfile?