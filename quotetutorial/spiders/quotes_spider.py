import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        all_quotes = response.css('div.quote')
        for quote in all_quotes:
            title = quote.css('span.text::text').extract()
            author = quote.css('.author::text').extract()
            tags = quote.css('.tag::text').extract()
            yield {
                    'title': title,
                    'author': author,
                    'tags': tags
                 }
