
import scrapy
from bookscraper.items import BookItem   

class BooksSpider(scrapy.Spider):
    name = 'books'
    custom_settings = {
        'FEEDS': { 'data.csv': { 'format': 'csv',}}
        }

    def start_requests(self):
        url = 'https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        product = response.css("div.product_main")

        book_item = BookItem()
        book_item["title"] =        product.css("h1 ::text").extract_first()
        book_item['category'] =     response.xpath("//ul[@class='breadcrumb']/li[@class='active']/preceding-sibling::li[1]/a/text()").extract_first()
        book_item['description'] =  response.xpath("//div[@id='product_description']/following-sibling::p/text()").extract_first()
        book_item['price'] =        response.css('p.price_color ::text').extract_first()
        
        yield book_item
