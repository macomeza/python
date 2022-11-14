# Import a scrapy Selector
from scrapy import Selector

# Import requests
import requests

# Create the string html containing the HTML source
html = requests.get( url ).content

# Create the Selector object sel from html
sel = Selector( text = html )

# Print out the number of elements in the HTML document
print( "There are 1020 elements in the HTML document.")
print( "You have found: ", len( sel.xpath('//*') ) )

# Create the XPath string equivalent to the CSS Locator 
xpath = '//div[@id="uid"]/span//h4'

# Create the CSS Locator string equivalent to the XPath
css_locator = 'div#uid > span h4'

# Create a SelectorList of the course titles
crs_title_els = response.css('div.course-block')

# Extract the course titles 
crs_titles = crs_title_els.css('h4::text').extract()

# Print out the course titles 
for el in crs_titles:
  print( ">>", el )