from bs4 import BeautifulSoup
import requests
page = requests.get("http://memes.com/img/2795") #sends page into page. eventually auto
soup = BeautifulSoup(page.content,"html.parser") # parses the webpage for the html tags
tags = soup.findAll('img') #finds all image tags in the page
print "\n".join(set(tag['src']for tag in tags)) #prints out the file located in src

