from Company import Company
from NowBestStock import BestStock
from SearchStockPrice import SearchStockPrice
from PastStockPrice import PastStockPrice


def myStock(companyName):
    companyList = Company()
    cpCode = companyList.getCompanyCode(companyName)
    if cpCode == False:
        print(F"{companyName} is not enable Company Name. Please input Correct Name")
        return
    searchStockPrice = SearchStockPrice(cpCode)
    searchStockPrice.searchPrice()
    pastStockPrice = PastStockPrice(cpCode)
    pastStockPrice.seachPastPrice()

    print("-" * 60)
    print(f"Now {companyName}(Companycode: {cpCode}) Price Is {searchStockPrice.getPrice()}")
    print("-" * 60)
    print(f"{companyName}'s Past Price Is \n{pastStockPrice.getPastPrice()}")


def getBestStock():
    nowBestStock = BestStock()
    nowBestStock.searchBest()
    print("-" * 60)
    print(f"Now Best Stock List Is {nowBestStock.getBestStock()}")



if __name__ == '__main__':
    cpName = input("Input Company Name. If You Want Quit, Press 'q'. If You Want To See Best Stock, Press 'b'\n")
    while(cpName != 'q'):
        if cpName != 'b':
            myStock(cpName)
        else:
            getBestStock()
        cpName =  input("Input Company Name. If You Want Quit, Press 'q'. If You Want To See Best Stock, Press 'b'\n")
