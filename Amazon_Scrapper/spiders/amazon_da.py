import scrapy
from ..items import AmazonScrapperItem 


class AmazonDaSpider(scrapy.Spider):
    name = 'amazon_da'
    #allowed_domains = ['www.amazon.com']
    #start_urls=['https://www.amazon.com/s?k=headphones'] #now starting the one page scrap

    #use for the multipal page scraping data set the change the page number.
    count = 1 # start the count the number of pages
    start_urls = ['https://www.amazon.com/s?k=headphones&page=1&qid=1669819372&ref=sr_pg_2']
    

    def parse(self, response):
        product = AmazonScrapperItem() # use class name to the items.py pages. 
        name = response.css(".a-size-medium.a-text-normal::text").extract()
        ##name = response.xpath('//span[@class="a-size-medium a-color-base a-text-normal selectorgadget_selected"]/text()').extract()
        reviews = response.css('.s-link-style .s-underline-text::text').extract()
        ##reviews = response.xpath('//span[@class="a-size-mini a-color-base puis-light-weight-text"]/text()').extract()
        price = response.xpath('//span[@class="a-price"]/span/text()').extract()
        img_urls = response.css('.s-image-fixed-height .s-image::attr(src)').extract()
        ##img_urls = response.xpath('//img[@class="s-image selectorgadget_selected"]/@src').extract()

        # list of the scrap datas
        product["p_name"] = name
        product["p_reviews"] = reviews
        product["p_price"] = price
        product["img_url"] = img_urls
        yield product

        AmazonDaSpider.count += 1 # count the pages incrementpage value
        nxt_page = "https://www.amazon.com/s?k=headphones&page="+str(AmazonDaSpider.count)+"&qid=1669819372&ref=sr_pg_2 "  
        if AmazonDaSpider.count < 6: # apply the condition scraping the numbers of pages.
            yield response.follow(nxt_page , callback=self.parse)    #follow the response page and print the result then back to the parser (next page)



# three pages are use  setting, items and spider page