from bs4 import BeautifulSoup
import requests
import pandas as pd
from fake_useragent import UserAgent



class PastStockPrice:
    def __init__(self, companyNum, parent=None):
        self.url = f'https://finance.naver.com/item/sise_day.nhn?code={companyNum}'
        self.headers = {'User-agent': UserAgent().ie}
        #response = requests.get(self.url, self.headers)
        response = requests.get(self.url, headers=self.headers)
        self.soup = BeautifulSoup(response.text, 'html.parser')

    def codeToPrice(self):
        lastPage = int(self.soup.select_one('td.pgRR').a['href'].split('=')[-1])
        if lastPage >= 3:
            lastPage = 3
        self.df = None
        for page in range(1, lastPage + 1):
            response = requests.get(f'{self.url}&page={page}', headers=self.headers)
            self.df = pd.concat([self.df, pd.read_html(response.text, encoding='euc-kr')[0]], ignore_index=True)
        self.df.dropna(inplace=True)
        self.df.reset_index(drop=True, inplace=True)


    def getPastPrice(self):
        return self.df


if __name__ == '__main__':
    stock = PastStockPrice("068270") #셀트리온 Company code
    nowPrice = stock.codeToPrice()
