# wikicrawler/spiders/WikiPageSpider.py
import scrapy

class WikipagespiderSpider(scrapy.Spider):
    name = "WikiPageSpider"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/List_of_common_misconceptions"]

    def parse(self, response):
        # Extract page title
        title = response.css('h1::text').get()
        
        # Extract paragraphs
        paragraphs = response.css('p::text').getall()
        
        # Yield data
        yield {
            'url': response.url,
            'title': title,
            'content': paragraphs
        }
        
        # Follow links to other wiki pages
        for link in response.css('a[href^="/wiki/"]::attr(href)').getall():
            yield response.follow(link, callback=self.parse)


   
    visited_urls = set()
    
    def parse_item(self, response):
        if response.url in self.visited_urls:
            return
        self.visited_urls.add(response.url)
        
        # Rest of parsing logic
        yield {
            'url': response.url,
            'title': response.css('h1::text').get()
        }
    
    def process_links(self, links):
        # Filter out already visited URLs
        return [link for link in links if link.url not in self.visited_urls]
