import sys
import re
import webbrowser
from bs4 import BeautifulSoup
import requests

def search(userinput):
    term = userinput.replace(" ","+")
    term2 = term + "+meme"
    query = "https://www.google.com/search?tbm=isch&source=hp&biw=1349&bih=947&ei=bAMnWq70H8uX_Qbf_5bAAQ&q="+term2
    #open browser
    #webbrowser.open(query)
    htmlText = requests.get(query)
    soup = BeautifulSoup(htmlText.text)
    #print full search results
    #print(soup)
    #textSearch = soup.findAll('div',attrs={'id':'search'})
    #pick the text from the top result
    topResult = soup.findAll('img')
    return topResult

def link(userinput):
    term = userinput.replace(" ","+")
    term2 = term + "+meme"
    query = "https://www.google.com/search?tbm=isch&source=hp&biw=1349&bih=947&ei=bAMnWq70H8uX_Qbf_5bAAQ&q="+term2
    #open browser
    #webbrowser.open(query)
    htmlText = requests.get(query)
    soup = BeautifulSoup(htmlText.text)
    imageContainer = soup.findAll(class_="rg_bx")
    #print full search results
    #print(soup)
    #textSearch = soup.findAll('div',attrs={'id':'search'})
    #pick the text from the top result
    linkResult = []
    for image in imageContainer:
        result = image.find("a")
        linkResult.append(result)
    return linkResult
