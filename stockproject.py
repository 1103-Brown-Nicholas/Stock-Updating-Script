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

class Apple:
    def appleClose(self,soup):
        prevClose = soup.find('td', {'class': 'Ta(end) Fw(600) Lh(14px)'}).text
        return prevClose

    def appleCurrent(self,soup):
        price = soup.find('fin-streamer', {'class' : 'Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text
        return price

    def deltPrice(self,soup):
        deltPrice = soup.find('fin-streamer', {'class': 'Fw(500) Pstart(8px) Fz(24px)'}).text
        return deltPrice
    
    def yearProj(self,soup):
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
        urlBase = ('https://finance.yahoo.com/quote/'+stock+'?p='+stock+'&.tsrc=fin-srch')
        print(urlBase)
        menuChoice = int(Interface().menu())
        
        if(menuChoice == 1):
            data = ('https://finance.yahoo.com/quote/'+stock+'?p='+stock+'&.tsrc=fin-srch')
            r_1 = requests.get(data)
            soup = BeautifulSoup(r_1.text,'html.parser')
            print(soup.title.text,"\n")

            closingPrice = Apple().appleClose(soup)
            currentPrice = Apple().appleCurrent(soup)
            deltaPrice  = Apple().deltPrice(soup)
            projPrice = Apple().yearProj(soup)
        
            print(stock,"previous closing price: $",closingPrice)
            print(stock,"current price: $",currentPrice,"A change of $",deltaPrice)
            print(stock,"current 1 year projection: $",projPrice)

            #Saving().savingData(closingPrice,currentPrice,deltaPrice,projPrice,today)
            #startfile("apple.txt")
        else:
            print("Error. Invalid Choice.")

Main().mainFunction()
