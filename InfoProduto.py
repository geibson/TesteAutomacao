from Elemento import BasePageElement
from Localizador import Localizadores, resultadoLocalizadores
import time

#class SearchTextElement(BasePageElement):

    #The locator for search box where search string is entered
 #   locator = 'q'


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class Product_Data(BasePage):




     
    def clica_botao(self):
        bt1 = self.driver.find_element(*Localizadores.SELECT_PRICE) 
        bt1.click()
        time.sleep(5)

    def seleciona_drops(self):
        
           
        drop10 = self.driver.find_element(*Localizadores.DATAINI)       
        drop10.click()
        drop11 = self.driver.find_element(*Localizadores.SELECDATA)  
        drop11.click()
        drop12 = self.driver.find_element(*Localizadores.DIA)
        drop12.click()
        drop2 = self.driver.find_element(*Localizadores.VALOR)       
        drop2.send_keys('35')  
        drop3 = self.driver.find_element(*Localizadores.RATING)       
        drop3.send_keys('SUPER')  
        drop4 = self.driver.find_element(*Localizadores.COBERTURA)       
        drop4.send_keys('FULL')  
        drop5 = self.driver.find_element(*Localizadores.CARRORESERVA)       
        drop5.send_keys('YES')  
        
    def check_box(self):
    
        check1 = self.driver.find_element(*Localizadores.OPCAO1)
        self.driver.execute_script("arguments[0].click();", check1)
        check2 = self.driver.find_element(*Localizadores.OPCAO2)
        self.driver.execute_script("arguments[0].click();", check2)
    
        
        

        
#class SearchResultsPage(BasePage):
 #   """Search results page action methods come here"""

#    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
 #       return "No results found." not in self.driver.page_source
 