# Scrapy python
## installation
To install Scrapy: 
```
pip install Scrapy
```

## Procedure:
* The Spider starts from the main page in ```start_urls```, extract all links to societies info page using CSS selector.
* ```parse_email``` is called for each of these links, extract societies info (name, email, social media contacts) and yield a dictionary iterator containing these info.

## Execution:
To run spider + output to JSON file:
```
scrapy crawl contact -O contacts.json
```
or to output to CSV file: 
```
scrapy crawl contact -O contacts.csv -t csv
```

# BeautifulSoup python
## Procedure
* Starts from the main page in ```start_urls```, extract all links to societies info page using CSS selector.
* ```contact_scrape``` is called for each of these links, extract societies info (name, email, social media contacts) and return a dictionary containing these info.
* Results are written into ```soup-contact.json```
