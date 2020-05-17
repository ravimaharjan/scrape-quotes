import scrapy
from ..items import QuotetutorialItem

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        quote_items = QuotetutorialItem()

        all_quotes = response.css('div.quote')
        for quote in all_quotes:
            title = quote.css('span.text::text').extract()
            author = quote.css('.author::text').extract()
            tags = quote.css('.tag::text').extract()
            quote_items['title'] = title
            quote_items['author'] = author
            quote_items['tags'] = tags
            yield quote_items