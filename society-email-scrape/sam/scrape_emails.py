# ===== Imports =====
import requests
import time
from bs4 import BeautifulSoup as Bs
from csv_handler import CSVHandler

# ===== Constants =====
SOCIETY_LIST_URL = "https://su.sheffield.ac.uk/activities/find-a-society"
ROOT_PAGE = "https://su.sheffield.ac.uk"
EMAIL_FILE_LOCATION = "data/email-list.csv"

def findSocietyPages():
    """
    Returns:
        A list of all the extensions to the url from the root 
        page to each of the pages about each society.
    """
    # Get and parse page content.
    page = requests.get(SOCIETY_LIST_URL)
    pageSoup = Bs(page.content, 'html.parser')

    # Get the div section for each society.
    societiesSection = pageSoup.find('section', id="socListings")
    societies = societiesSection.findAll(class_="g__4--m g__4--t g__3--d mgn__b--1")

    # Pull all the links from each section.
    links = []
    for society in societies:
        linkTag = society.find('a')
        link = linkTag['href']
        links.append(link)

    return links

def extractSocietyInfo(urlExtensionList):
    """
    Args:
        urlExtensionList: list of extensions from the root of 
        the page to get to each society's page.

    Returns:
        list of sets of information about each society.
    """
    # Get and parse page content.
    url = ROOT_PAGE + urlExtensionList
    page = requests.get(url)
    pageSoup = Bs(page.content, 'html.parser')

    # Get the name of the society.
    nameContainer = pageSoup.find('h2', class_="t__none f__b--eb")
    name = ""
    if nameContainer != None:
        name = nameContainer.text

    # Get the society's email.
    emailContainer = pageSoup.find('div', class_="outlet__header--contact t__def-bl--pri contact__align mgn__t--1 mgn__b--1")
    email = ""
    if emailContainer != None:
        email = emailContainer.find('a').text

    return [name, email]

def getAllInfo(links):
    result = []

    # Setup for the progess meter.
    completion = 0
    step = 100/len(links)

    # Get the page info from each link.
    for link in links:
        currInfo = extractSocietyInfo(link)
        result.append(currInfo)

        # Advance and print out how far through the program is.
        completion += step
        print("{}% done".format(round(completion)))
    return result

# Get society info.
societyUrls = findSocietyPages()
socInfo = getAllInfo(societyUrls)

# Write it all to a CSV.
testFile = CSVHandler(EMAIL_FILE_LOCATION)
testFile.write(socInfo)