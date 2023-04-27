from .scraper import Scraper


# Default HEADERS
HEADERS = {
    'origin': 'https://www.tokopedia.com',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'accept': 'application/json, text/plain, */*',
    'authority': 'ace.tokopedia.com'
}

class Tokopedia:
    def __init__(self):
        self.scraper = Scraper

    def get(self):
        page = self.scraper.getData(self, "https://www.tokopedia.com/search?st=product&q=pepsodent&srp_component_id=02.01.00.00&srp_page_id=&srp_page_title=&navsource=")
        return page