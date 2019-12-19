import requests
from bs4 import BeautifulSoup


class SimpleScraper:
    """Simple Web Scraper

    I ran out of things to say
    """

    def __init__(self):
        pass
        
    def get_url(self, url):
        try:
            self.url = url
            self.page = requests.get(url)
        except Exception as e:
            print(str(e))
            return 'Error: '+ str(e)
        if self.page.status_code == 200:
            print('page correctly loaded')
            self.parsed_source_code = BeautifulSoup(self.page.text, 'html.parser')
            return 'OK'
        return 'error: '+ str( self.page.status_code)

    def get_elements_by_ID(self, value):
        return self.parsed_source_code.find_all(id=value)

    def get_elements_by_class(self, value):
        return self.parsed_source_code.find_all(class_=value)

    def get_elements(self, value):
        return self.parsed_source_code.find_all(value)
