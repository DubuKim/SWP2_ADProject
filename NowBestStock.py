from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent


class BestStock:
    def __init__(self, parent=None):
        url = 'https://finance.naver.com/sise/'
        headers = {'User-agent': UserAgent().ie}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        self.bstStock = soup.select_one('.lst_pop')

    def getBestStock(self):
        return self.bstStock.text

if __name__ == '__main__':
    stock = BestStock()
    stock.getBestStock()
