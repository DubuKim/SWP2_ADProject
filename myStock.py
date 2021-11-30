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
    pastStockPrice = PastStockPrice(cpCode)
    pastStockPrice.codeToPrice()

    print("-" * 60)
    print(f"Now {companyName}(Companycode: {cpCode}) Price Is {searchStockPrice.getPrice()}")
    print("-" * 60)
    print(f"{companyName}'s Past Price is \n{pastStockPrice.getPastPrice()}")


def getBestStock():
    nowBestStock = BestStock()
    print("-" * 60)
    print(f"Now Best stock list is {nowBestStock.getBestStock()}")



if __name__ == '__main__':
    cpName = input("Input company name. If you want Quit, press 'q'. If you want to see Best Stock, pres 'b'\n")
    while(cpName != 'q'):
        if cpName != 'b':
            myStock(cpName)
        else:
            getBestStock()
        cpName = input("Input company name. If you want Quit, press 'q'\n")

