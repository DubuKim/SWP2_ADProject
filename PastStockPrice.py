from bs4 import BeautifulSoup
import requests
import pandas as pd
from fake_useragent import UserAgent



class PastStockPrice:
    def __init__(self, companyNum, parent=None):
        self.url = f'https://finance.naver.com/item/sise_day.nhn?code={companyNum}'
        self.headers = {'User-agent': UserAgent().ie}
        #response = requests.get(self.url, self.headers)


    def seachPastPrice(self):
        response = requests.get(self.url, headers=self.headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        lastPage = int(soup.select_one('td.pgRR').a['href'].split('=')[-1])
        if lastPage >= 3:
            lastPage = 3

        self.df = None
        for page in range(1, lastPage + 1):
            response = requests.get(f'{self.url}&page={page}', headers=self.headers)
            self.df = pd.concat([self.df, pd.read_html(response.text)[0]], ignore_index=True)
        self.df.dropna(inplace=True)
        self.df.reset_index(drop=True, inplace=True)


    def getPastPrice(self):
        return self.df


if __name__ == '__main__':
    stock = PastStockPrice("068270") #셀트리온 Company code
    stock.seachPastPrice()
    Prices = stock.getPastPrice()
    print(Prices)
