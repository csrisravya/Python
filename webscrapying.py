import requests  # A HTTP request is meant to either retrieve data from a specified URI or to push data to a server

from bs4 import BeautifulSoup 
#BeautifulSoup is used extract information from the HTML and XML files. It provides a parse tree and the functions to navigate, search or modify this parse tree.

r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')
# GET method is used to retrieve information from the given server using a given URI.

print(r.status_code)
print(r)  # This statement will print the success code (in this case 200) if the get function performs its operation correctly
print(r.url)
print("\n")
print(r.content) # prints content of request

# Before getting out any information from the HTML of the page, we must understand the structure of the page. 
# This is needed to be done in order to select the desired data from the entire page.
# We can do this by right-clicking on the page we want to scrape and select inspect element and then parse HTML page .
# BeautifulSoup library is built on top of the HTML parsing libraries like html5lib, lxml, html.parser, etc. 
# So BeautifulSoup object and specify the parser library can be created at the same time.

soup = BeautifulSoup(r.content,'html.parser')
print(soup.prettify())

# Getting the title tag
print(soup.title)

s=soup.find('div',class_='entry-content') # here, we are trying to fid all the divisions(div) which have the class'entry-content' in the web page
content=s.find_all('p')  # here we are tryin to find all the content within the paragraph tag(p) 
print(content)
