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

## Problems and Solution
* Retrieving social media list was a bit weird since the web devs decided to put the page's default link if the society has no social media page on that website, instead of leaving it empty (e.g. if Anime Society has no facebook group it will leave a default link facebook.com instead of no link). I had to find a list of these defaul links manually (there were only 5 fortunately), and clear them out. 
* Performing simple tasks with Scrapy was quite straightforward, everything can be setup with 1 line and a simple guide can be found on [Scrapy documentation](https://docs.scrapy.org/en/latest/intro/tutorial.html). With a more complicated task, more features of Scrapy should be utilized like `Pipeline` and `ItemLoader`.
* XPath and CSS Selectors were new and interesting, i basically used (this cheatsheet)[https://www.w3schools.com/cssref/css_selectors.asp] for [CSS this one](https://www.w3schools.com/xml/xpath_syntax.asp) for XPath (XPath seems a bit more complicated, but more precise). 
* For testing if the Selector or Xpath works, go to the website inspection mode (`Ctrl` + `Shift` + `I`), use `Ctrl` + `F` on the source code and it will allows you to search for components based on CSS Selectors or Xpaths.
* Another way to test CSS Selector and Xpath is to use `scrapy shell 'http://linktoscrape.com'`

# BeautifulSoup python
## Procedure
* Starts from the main page in ```start_urls```, extract all links to societies info page using CSS selector.
* ```contact_scrape``` is called for each of these links, extract societies info (name, email, social media contacts) and return a dictionary containing these info.
* Results are written into ```soup-contact.json```
## Problems and Solution
* When using `find_all` or `find`, there's a possibility that the element could not be found and return Empty. Always remember to filter this out with a simple `if something is not None:` to avoid the program stopping after a (really) long time of scraping. 


