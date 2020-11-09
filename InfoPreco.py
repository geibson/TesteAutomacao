from Localizador import Localizadores
import time


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
    
