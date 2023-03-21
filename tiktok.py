from selenium import webdriver

class TikTokScraper:

    def __init__(self):
        self.PATH = "/Users/bad/Downloads/chromedriver.exe"
        self.driver = webdriver.Chrome(self.PATH)
        self.text = ""

    def get_comment_count(self, url):
        self.driver.get(url)
        # Parse data out of the page
        self.text = self.driver.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div/div/main/div/div[1]/span[1]/div/div[1]/div[4]/div[2]/div[2]/strong').text


urls = ["https://www.tiktok.com/@gordonramsayofficial/video/6916583398500748550?lang=en",]
TikTokScraper = TikTokScraper()
for url in urls:
    TikTokScraper.get_comment_count(url)
    print(TikTokScraper.text)