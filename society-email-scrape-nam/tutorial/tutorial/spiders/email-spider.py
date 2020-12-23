import scrapy


class AuthorSpider(scrapy.Spider):
    name = 'email'

    # main URL from SU that contains a list of all societies
    start_urls = ['https://su.sheffield.ac.uk/activities/find-a-society']

    def parse(self, response)
        # locate all society links using CSS Selector
        main_page = response.css('div.g__4--m.g__4--t.g__3--d.mgn__b--1 a')

        # access all links, parsing downloaded content to parse_email
        yield from response.follow_all(main_page, self.parse_email)

    def parse_email(self, response):
        # relper method to extract text in elements with CSS selectors
        # Xpath alternative: response.xpath(query)...
        def extract_with_css(query):
            return response.css(query).get(default='').strip()

        # yield a dictionary with societiy names and their emails
        yield {
                'name': extract_with_css('.t__none.f__b--eb:first-child::text'),
                'email': extract_with_css('.c__b a::text')
            }