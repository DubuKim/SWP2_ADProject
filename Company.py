import csv

class Company:
    def __init__(self, parent=None):
        f = open('companyDate.csv', 'r')
        csvFile = csv.reader(f)
        self.companyDict = {}
        for line in csvFile:
            self.companyDict[line[1]] = line[0]
        f.close()

    def getCompanyCode(self, companyName):
        if not companyName in self.companyDict:
            return False
        return self.companyDict[companyName]

if __name__ == '__main__':
    company = Company()
    print(company.getCompanyCode("흥국"))