import requests
from bs4 import BeautifulSoup
from datetime import date
from os import startfile

class Interface:
    def userStock(self):
        stockChoice = input("Please enter a stock: ")
        return stockChoice
    
    def menu(self):
        menu = input("1.)Daily Stock Data\n2.)Revenue Estimates\n3.)Holder Information\n")
        return menu 

class Stock:
    def stock_close(self,soup):
        prevClose = soup.find('td', {'class': 'Ta(end) Fw(600) Lh(14px)'}).text
        return prevClose

    def stock_current(self,soup):
        price = soup.find('fin-streamer', {'class' : 'Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text
        return price

    def stock_deltprice(self,soup):
        deltPrice = soup.find('fin-streamer', {'class': 'Fw(500) Pstart(8px) Fz(24px)'}).text
        return deltPrice
    
    def stock_yearproj(self,soup):
        yearProj = soup.find('td',{'data-test': 'ONE_YEAR_TARGET_PRICE-value'}).text
        return yearProj

class Saving:
    def savingData(self,closingPrice,currentPrice,appleDelta,appleProj,today):
        
        file = open("apple.txt","w")
        file.write("Apples previous closing price: $" + closingPrice + "\n" + "Apples current price: $" + currentPrice + " with a change of $" + appleDelta + "\n" + "Apples current 1 year projection: $" + appleProj + "\n")
        file.close
    
    def readingData(self):
        with open('apple.txt') as f:
            contents = f.read()
            print(contents)

class Main:
    def mainFunction(self):
        today = date.today()
        
        stock = Interface().userStock()
        url_Base = ('https://finance.yahoo.com/quote/'+stock+'?p='+stock+'&.tsrc=fin-srch')
        print(url_Base)
        menuChoice = int(Interface().menu())
        
        if(menuChoice == 1):
            data = ('https://finance.yahoo.com/quote/'+stock+'?p='+stock+'&.tsrc=fin-srch')
            r_1 = requests.get(data)
            soup = BeautifulSoup(r_1.text,'html.parser')
            print(soup.title.text,"\n")

            closing_price = Stock().stock_close(soup)
            current_price = Stock().stock_current(soup)
            delta_price  = Stock().stock_deltprice(soup)
            proj_price = Stock().stock_yearproj(soup)
        
            print(stock,"previous closing price: $",closing_price)
            print(stock,"current price: $",current_price,"A change of $",delta_price)
            print(stock,"current 1 year projection: $",proj_price)

            #Saving().savingData(closingPrice,currentPrice,deltaPrice,projPrice,today)
            #startfile("apple.txt")
        else:
            print("Error. Invalid Choice.")

Main().mainFunction()
