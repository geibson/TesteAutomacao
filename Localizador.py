from selenium.webdriver.common.by import By

class Localizadores(object):
    #Botões para proxima pagina
    INSURANCE_DATA = (By.ID, 'nextenterinsurantdata')
    PRODUCT_DATA = (By.ID,'nextenterproductdata')
    SELECT_PRICE= (By.ID, 'nextselectpriceoption')
    SEND_QUOTE= (By.ID, 'nextsendquote')
    SEND_EMAIL = (By.ID, 'sendemail')
    CONFIRM = (By.CSS_SELECTOR,'.confirm')
    
    #Link do tipo de seguro
    CAR = (By.ID,'nav_automobile')
    
    CONTADOR = (By.CSS_SELECTOR,'.zero')
    
    #Campos da primeira página
    MARCA = (By.ID,'make')
    POTENCIA = (By.ID,'engineperformance')
    FABRICADO = (By.ID,'dateofmanufacture')
    ASSENTOS = (By.ID,'numberofseats')
    COMBUSTIVEL = (By.ID,'fuel')
    PRECO = (By.ID,'listprice')
    PLACA = (By.ID,'licenseplatenumber')
    KMANUAL = (By.ID,'annualmileage')
    
        
    #Campos da segunda página
    NOME = (By.ID,'firstname')
    SOBRENOME = (By.ID,'lastname')
    ANIVER = (By.ID,'birthdate')

    ENDERECO = (By.ID,'streetaddress')
    PAIS = (By.ID,'country')
    CEP = (By.ID,'zipcode')
    CIDADE = (By.ID,'city')
    OCUPACAO = (By.ID,'occupation')
    SITE = (By.ID,'website')

    HOBBY1 = (By.ID,'speeding')
    HOBBY2 = (By.ID,'bungeejumping')
    HOBBY3 = (By.ID,'cliffdiving')
    HOBBY4 = (By.ID,'skydiving')
    HOBBY5 = (By.ID,'other')
    FENOTIPOH = (By.ID,'gendermale')
    FENOTIPOM = (By.ID,'genderfemale')
    
    FOTO = (By.ID,'picture')
    
    #Campos da terceira página
    DATAINI = (By.ID,'openstartdatecalender')
    SELECDATA = (By.CSS_SELECTOR,'.ui-datepicker-next')
    DIA = (By.XPATH,"//a[contains(text(),'10')]")
    VALOR = (By.ID,'insurancesum')
    RATING = (By.ID,'meritrating')
    COBERTURA = (By.ID,'damageinsurance')
    CARRORESERVA = (By.ID,'courtesycar')

    OPCAO1 = (By.ID,'EuroProtection')
    OPCAO2= (By.ID,'LegalDefenseInsurance')
    
    #Campos da quarta página
    PLANO1 = (By.ID,'selectsilver')
    PLANO2 = (By.ID,'selectgold')
    PLANO3= (By.ID,'selectplatinum')
    PLANO4 = (By.ID,'selectultimate')
    
    #Campos da quinta página
    EMAIL = (By.ID,'email')
    FONE = (By.ID,'phone')
    USER = (By.ID,'username')
    PASS = (By.ID,'password')
    PASSCON = (By.ID,'confirmpassword')
    MENSAGEM= (By.ID,'Comments')
    
    
    
class resultadoLocalizadores(object):
    """A class for search results locators. All search results locators should come here"""
    pass