from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule

class Articulo(Item):
    titulo = Field()
    precio = Field()
    descripcion = Field()

class MercadoLibreCrawler(CrawlSpider):
    name = 'mercadolibre'
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'
        'CLOSESPIDER_PAGECOUNT': 3
    }
    download_delay = 1
    alowed_domains = ["listado.mercadolibre.cl"]
    start_urls = ["https://listado.mercadolibre.cl/comida-erizo"]