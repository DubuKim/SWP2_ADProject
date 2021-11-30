from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

class SearchStockPrice:
    def __init__(self, companyNum, parent=None):
        self.url = f"https://finance.naver.com/item/sise.naver?code={companyNum}"
        self.headers = {'User-agent': UserAgent().ie}

    def searchPrice(self):
        response = requests.get(self.url, self.headers)
        soup = BeautifulSoup(response.text, "html.parser")
        no_today = soup.select_one('.no_today')
        blind = no_today.select_one('span.blind')
        self.nowPrice = blind.text


    def getPrice(self):
        return self.nowPrice



if __name__ == '__main__':
    stock = SearchStockPrice("068270") #셀트리온 Company code
    stock.searchPrice()
    price = stock.getPrice()
    print(price)


