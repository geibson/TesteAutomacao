import unittest
from selenium import webdriver
import InfoCarro
import InfoSegurado
import InfoProduto
import InfoPreco
import InfoContato
from Localizador import Localizadores



class PythonOrgSearch(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://sampleapp.tricentis.com/101/app.php")
        self.driver.maximize_window()

    def test_search_(self):

        #Carrega a pagina.
        Vehicle_Data = InfoCarro.Vehicle_Data(self.driver)
        Insurant_Data = InfoSegurado.Insurant_Data(self.driver)
        Product_Data = InfoProduto.Product_Data(self.driver)
        Price_Option = InfoPreco.Price_Option(self.driver)
        Send_Quote = InfoContato.Send_Quote(self.driver)


        Vehicle_Data.insurance_type()
        Vehicle_Data.preenche_campos()
        Vehicle_Data.seleciona_drops()
        
        try:
            field = self.driver.find_element(*Localizadores.CONTADOR)
            print(print('Campos da tela Vehicle_Data preenchidos corretamente'))
        except:
            print("Erro ao preencher os campos da tela insurance_type")
           # self.driver.close()
        Vehicle_Data.clica_botao()
        
        Insurant_Data.check_box()
        Insurant_Data.preenche_campos()
        try:
            field = self.driver.find_element(*Localizadores.CONTADOR)
            print('Campos da tela Insurant_Data preenchidos corretamente')
        except:
            print(" Erro ao preencher os campos da tela Insurant_Data")
           # self.driver.close()
        Insurant_Data.clica_botao()
        
        Product_Data.seleciona_drops()
        Product_Data.check_box()
        try:
            self.driver.find_element(*Localizadores.CONTADOR)
            print('Campos da tela Product_Data preenchidos corretamente')
        except:
            print(" Erro ao preencher os campos da tela Product_Data")
           # self.driver.close()
        Product_Data.clica_botao()
        
        Price_Option.check_box()
        try:
            self.driver.find_element(*Localizadores.CONTADOR)
            print('Campos da tela Price_Option preenchidos corretamente')
        except:
            print(" Erro ao preencher os campos da tela Price_Option")
            #self.driver.close()
        Price_Option.clica_botao()
        
        Send_Quote.preenche_campos()
        try:
            self.driver.find_element(*Localizadores.CONTADOR)
            print('Campos da tela Send_Quote preenchidos corretamente')
        except:
            print(" Erro ao preencher os campos da tela Send_Quote")
           # self.driver.close()
               
        Send_Quote.clica_botao()
        

   # def tearDown(self):
    #    self.driver.close()

if __name__ == "__main__":
    unittest.main()