import requests
import time
from bs4 import BeautifulSoup as Bs
from csv_handler import CSVHandler


SOCIETY_LIST_URL = "https://su.sheffield.ac.uk/activities/find-a-society"
ROOT_PAGE = "https://su.sheffield.ac.uk"

EMAIL_FILE_LOCATION = "data/email-list.csv"

def findSocietyPages():
    page = requests.get(SOCIETY_LIST_URL)
    pageSoup = Bs(page.content, 'html.parser')

    societiesSection = pageSoup.find('section', id="socListings")
    societies = societiesSection.findAll(class_="g__4--m g__4--t g__3--d mgn__b--1")

    links = []
    for society in societies:
        linkTag = society.find('a')
        link = linkTag['href']
        links.append(link)

    return links

def extractSocietyInfo(urlPostfix):
    url = ROOT_PAGE + urlPostfix
    page = requests.get(url)

    pageSoup = Bs(page.content, 'html.parser')
    nameTag = pageSoup.find('h2', class_="t__none f__b--eb")
    name = ""
    if nameTag != None:
        name = nameTag.text

    emailContainer = pageSoup.find('div', class_="outlet__header--contact t__def-bl--pri contact__align mgn__t--1 mgn__b--1")
    email = ""
    if emailContainer != None:
        email = emailContainer.find('a').text

    return [name, email]

def safeExtractInfo(links):
    result = []
    completion = 0
    step = 100/len(links)
    for link in links:
        currInfo = extractSocietyInfo(link)
        result.append(currInfo)
        #time.sleep(0.3)

        completion += step
        print("{}% done".format(round(completion)))
    return result


societyUrls = findSocietyPages()
socInfo = safeExtractInfo(societyUrls)

testFile = CSVHandler(EMAIL_FILE_LOCATION)
testFile.write(socInfo)