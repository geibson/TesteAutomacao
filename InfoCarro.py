from Elemento import BasePageElement
from Localizador import Localizadores, resultadoLocalizadores
import time


#class SearchTextElement(BasePageElement):

    #The locator for search box where search string is entered
 #   locator = 'q'


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        


class Vehicle_Data(BasePage):
    
    #search_text_element = SearchTextElement()

    #def is_title_matches(self):
    #    return "Vehicle Insurance Application" in self.driver.title

    def insurance_type(self):
        car = self.driver.find_element(*Localizadores.CAR)
        car.click()      
        time.sleep(2)
    
    
    #def valida(self):
    #    try:
    #        field = self.driver.find_element(*Localizadores.CONTADOR)
    #        print(field)
    #    except:
    #        print("Erro ao preencher os campos da tela insurance_type")
    #        self.driver.close()
        
        
        
    def clica_botao(self):
        bt1 = self.driver.find_element(*Localizadores.INSURANCE_DATA) 
        bt1.click()
        time.sleep(10)

    def preenche_campos(self):
        
        field1 = self.driver.find_element(*Localizadores.POTENCIA) 
        field1.send_keys('150')
        field2 = self.driver.find_element(*Localizadores.FABRICADO)
        field2.send_keys('01/01/2008')
        field3 = self.driver.find_element(*Localizadores.ASSENTOS)
        field3.send_keys('5')
        field4 = self.driver.find_element(*Localizadores.PRECO)
        field4.send_keys('15000')
        field5 = self.driver.find_element(*Localizadores.PLACA)
        field5.send_keys('AAA2222')
        field6 = self.driver.find_element(*Localizadores.KMANUAL)
        field6.send_keys('15000')
        
        
    def seleciona_drops(self):
        drop1 = self.driver.find_element(*Localizadores.MARCA)       
        drop1.send_keys('AUDI')      
        drop2 = self.driver.find_element(*Localizadores.COMBUSTIVEL)
        drop2.send_keys('P')
        
#class SearchResultsPage(BasePage):
 #   """Search results page action methods come here"""

#    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
 #       return "No results found." not in self.driver.page_source