from bs4 import BeautifulSoup
from requests import get
import json

def contact_scrape(link,output):
    key = ['name','email','twitter','facebook','instagram','youtube']
    val = []
    soup = BeautifulSoup(get('https://su.sheffield.ac.uk' + link).text, 'html.parser')
    
    #======================#
    # Extract society name #
    #======================#
    name = soup.find('h2', class_="t__none f__b--eb")
    if name is not None:
        val.append(name.get_text())
    else:
        val.append('')
    
    #=======================#
    # Extract society email #
    #=======================#
    email = soup.find(class_ = 'c__b')
    if email and email.a is not None:
        val.append(email.a.get_text())
    else:
        val.append('')

    #====================================#
    # Extract society social media links #
    #====================================#
    social_media_list = soup.find('div', class_ ='highlight__social mgn__t--2')
    if social_media_list is not None:
        social_media_list = social_media_list.find_all('a')
        for social_media in social_media_list:
            link1 = social_media.get('href')
            if link1 not in default_pages:
                val.append(link1)
            else:
                val.append('')
    
    return dict(zip(key,val))     

#------------------------------------------------------------------------------
# Main Program
#------------------------------------------------------------------------------

# since pages keeps default sites for empty social media links
# -> we keep track of these sites and clear them out        
default_pages = ['https://www.instagram.com/','https://www.facebook.com/','https://twitter.com/','https://youtube.com/user/']

# output to a csv file
output = [['name','email','twitter','facebook','instagram','youtube']]

# Initialise BS object of main page
soup = BeautifulSoup(get("https://su.sheffield.ac.uk/activities/find-a-society").text, 'html.parser')

# retrieve all society links
societies = soup.find_all('div', class_ = 'g__4--m g__4--t g__3--d mgn__b--1')

with open("soup-contact.json", "w", newline="") as f:
    for society in societies:
        link = society.a['href']    # extracting href links 
        line_output = json.dumps(contact_scrape(link,output))
        f.write(line_output + '\n')
