from Localizador import Localizadores
import time


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
    
        
