from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent


class BestStock:
    def __init__(self, parent=None):
        self.url = 'https://finance.naver.com/sise/'
        self.headers = {'User-agent': UserAgent().ie}


    def searchBest(self):
        response = requests.get(self.url, headers=self.headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        self.bstStock = soup.select_one('.lst_pop')


    def getBestStock(self):
        return self.bstStock.text


if __name__ == '__main__':
    stock = BestStock()
    stock.searchBest()
    bests = stock.getBestStock()
    print(bests)
