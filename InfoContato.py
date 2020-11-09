from Elemento import BasePageElement
from Localizador import Localizadores, resultadoLocalizadores
import time
import unittest

#class SearchTextElement(BasePageElement):

    #The locator for search box where search string is entered
 #   locator = 'q'


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class Send_Quote(BasePage):
    

        
    def insurance_type(self):
        car = self.driver.find_element(*Localizadores.CAR)
        car.click()      
        time.sleep(10)
    
        
    def clica_botao(self):
        bt1 = self.driver.find_element(*Localizadores.SEND_EMAIL) 
        bt1.click()
        time.sleep(10)
        bt2 = self.driver.find_element(*Localizadores.CONFIRM) 
        bt2.click()

    def preenche_campos(self):
        
        field1 = self.driver.find_element(*Localizadores.EMAIL) 
        field1.send_keys('teste@teste.com')
        field2 = self.driver.find_element(*Localizadores.FONE)
        field2.send_keys('51933333333')
        field3 = self.driver.find_element(*Localizadores.USER)
        field3.send_keys('teste')
        field4 = self.driver.find_element(*Localizadores.PASS)
        field4.send_keys('T&ste123')
        field5 = self.driver.find_element(*Localizadores.PASSCON)
        field5.send_keys('T&ste123')
        field6 = self.driver.find_element(*Localizadores.MENSAGEM)
        field6.send_keys('Mensagem de teste')
        

        
#class SearchResultsPage(BasePage):
 #   """Search results page action methods come here"""

#    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
 #       return "No results found." not in self.driver.page_source