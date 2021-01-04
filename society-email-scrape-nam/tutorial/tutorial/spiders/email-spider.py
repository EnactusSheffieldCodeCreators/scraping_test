import scrapy


class AuthorSpider(scrapy.Spider):
    name = 'contact'

    # main URL from SU that contains a list of all societies
    start_urls = ['https://su.sheffield.ac.uk/activities/find-a-society']

    def parse(self, response):
        # locate all society links using CSS Selector
        main_page = response.css('div.g__4--m.g__4--t.g__3--d.mgn__b--1 a')

        # access all links, parsing downloaded content to parse_email
        yield from response.follow_all(main_page, self.parse_email)

    def parse_email(self, response):
        # helper method to extract text in elements with CSS selectors
        # Xpath alternative: response.xpath(query)...
        def extract_with_css(query):
            return response.css(query).get(default='').strip()

        # since pages keeps default sites for empty social media links
        # -> we keep track of these sites and clear them out
        default_pages = ['https://www.instagram.com/','https://www.facebook.com/','https://twitter.com/','https://youtube.com/user/']

        # values for contact dictionary
        social =  response.css('div.highlight__social.mgn__t--2 > a::attr(href)').extract()
        # remove empty links  
        social_contact = [x if x not in default_pages else '' for x in social]
 
        # yield a dictionary with societiy names and their contacts
        yield {
                'name': extract_with_css('.t__none.f__b--eb:first-child::text'),
                'email': extract_with_css('.c__b a::text'),
                'twitter': social_contact[0],
                'facebook': social_contact[1],
                'instagram': social_contact[2],
                'youtube': social_contact[3]
            }
        