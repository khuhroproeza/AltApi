import scrapy
from natsort import natsorted
from AltScraper.items import AltscraperItem


class StarWars(scrapy.Spider):
    name = "starwars"
    allowed_domains = ["cnet.com"]
    start_urls = [
        "https://www.cnet.com/pictures/star-wars-spaceships-ranked-by-power-speed/32/"
    ]

    def process_items(self, item):
        names_of_crafts = [value.replace(u"\u200b", "") for value in item][1:]
        return natsorted(names_of_crafts)

    def parse(self, response):
        for sel in response.xpath("//html"):
            item = AltscraperItem()
            item["names"] = self.process_items(
                sel.xpath("//*[@class='row']//h2//text()").extract()
            )

            yield item
