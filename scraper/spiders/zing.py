import scrapy


class ZingSpider(scrapy.Spider):
    name = "zing"
    allowed_domains = ["zingmp3.vn"]
    start_urls = ["https://zingmp3.vn/"]

    def parse(self, response):
        links = response.css("a.thumb-50.mar-right-10::attr(href)").getall()

        # In ra hoặc lưu các liên kết
        for link in links:
            yield {"link": link}
