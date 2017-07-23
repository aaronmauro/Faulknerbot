import requests
import sys
import re
import webbrowser
from bs4 import BeautifulSoup

	#################
	## Text Search ##
	#################

def search(phrase):
    term = phrase.replace(" ","+")
    query = "https://www.google.com/search?num=001&safe=off&q="+term+"+site:http://faulkner.lib.virginia.edu/"
    #optional open browser
    #webbrowser.open(query)
    htmlText = requests.get(query)
    soup = BeautifulSoup(htmlText.text)
    #print full search results
    #print(soup)
    textSearch = soup.findAll('div',attrs={'id':'search'})
    #pick the text of the top result
    topResult = soup.findAll('span',attrs={"class":"st"})
    return str(topResult)

	#################
	## Link Search ##
	#################

def link(phrase):
    term = phrase.replace(" ","+")
    htmlText = requests.get(query)
    soup = BeautifulSoup(htmlText.text)
    linkSearch = soup.findAll('cite')
    links = str(linkSearch).replace("<cite>","<a href=\"").replace("</cite>","\"></a>")
    return links
