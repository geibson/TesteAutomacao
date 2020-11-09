
from Elemento import BasePageElement
from Localizador import Localizadores, resultadoLocalizadores
import time

#class SearchTextElement(BasePageElement):

    #The locator for search box where search string is entered
 #   locator = 'q'


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class Price_Option(BasePage):


            
     
    def clica_botao(self):
        time.sleep(5)
        bt1 = self.driver.find_element(*Localizadores.SEND_QUOTE) 
        bt1.click()
        time.sleep(5)


    def check_box(self):
    
        check1 = self.driver.find_element(*Localizadores.PLANO1)
        #self.driver.execute_script("arguments[0].click();", check1)
        check2 = self.driver.find_element(*Localizadores.PLANO2)
        #self.driver.execute_script("arguments[0].click();", check2)
        check3 = self.driver.find_element(*Localizadores.PLANO3)
        #self.driver.execute_script("arguments[0].click();", check3) 
        check4 = self.driver.find_element(*Localizadores.PLANO4)
        self.driver.execute_script("arguments[0].click();", check4)
    
    
        
        

        
#class SearchResultsPage(BasePage):
 #   """Search results page action methods come here"""

#    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
 #       return "No results found." not in self.driver.page_source
 