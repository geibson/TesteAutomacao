from Localizador import Localizadores
import time

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class Insurant_Data(BasePage):
    
    def clica_botao(self):
        bt1 = self.driver.find_element(*Localizadores.PRODUCT_DATA) 
        bt1.click()
        time.sleep(5)

    def preenche_campos(self):
        
           
        field1 = self.driver.find_element(*Localizadores.NOME)
        field1.send_keys('JOSE')
        field2 = self.driver.find_element(*Localizadores.SOBRENOME)
        field2.send_keys('SILVA')
        field3 = self.driver.find_element(*Localizadores.ANIVER)
        field3.send_keys('01/01/1990')
        field4 = self.driver.find_element(*Localizadores.ENDERECO)
        field4.send_keys('AV. ANDRADAS, 2000')
        field5 = self.driver.find_element(*Localizadores.PAIS)
        field5.send_keys('BRAZIL')
        field6 = self.driver.find_element(*Localizadores.CEP)
        field6.send_keys('9000000')
        field7 = self.driver.find_element(*Localizadores.CIDADE)
        field7.send_keys('PORTO ALEGRE')
        field8 = self.driver.find_element(*Localizadores.OCUPACAO)
        field8.send_keys('Employee')
        field9 = self.driver.find_element(*Localizadores.SITE)
        field9.send_keys('www.facebook.com')
        
        field10 = self.driver.find_element(*Localizadores.FOTO)
        #field10.send_keys('EU.JPG')
        
        
    def check_box(self):

        check1 = self.driver.find_element(*Localizadores.HOBBY1)
        self.driver.execute_script("arguments[0].click();", check1)
        check2 = self.driver.find_element(*Localizadores.HOBBY2)
        self.driver.execute_script("arguments[0].click();", check2)
        check3 = self.driver.find_element(*Localizadores.HOBBY3)
        self.driver.execute_script("arguments[0].click();", check3)
        check4 = self.driver.find_element(*Localizadores.HOBBY4)
        self.driver.execute_script("arguments[0].click();", check4)
        check5 = self.driver.find_element(*Localizadores.HOBBY5)
        #self.driver.execute_script("arguments[0].click();", check5)
        check6 = self.driver.find_element(*Localizadores.FENOTIPOH)
        self.driver.execute_script("arguments[0].click();", check6)
        check7 = self.driver.find_element(*Localizadores.FENOTIPOM)
        #self.driver.execute_script("arguments[0].click();", check7)
    
