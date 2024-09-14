import scrapy


class MlSpider(scrapy.Spider):
    name = "ml"
    start_urls = [
        f"https://1sex.maulon.vip/page/{i}" for i in range(1,31)
    ]

    def parse(self, response):
        links_with_images = response.css("a")

        for link in links_with_images:
            href = link.css("a::attr(href)").get()
            if href and href.endswith('.html'):
                yield response.follow(href, self.parse_link)

    def parse_link(self, response):
        images = response.css("img")
        for img in images:
            img_src = img.attrib.get("src")
            if img_src and "anh-sex" in img_src:
                yield {"src": img_src}
