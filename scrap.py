# -*- coding: utf-8 -*-


## 1. Todas as inportacoese



from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType

driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())



## 2. Todos os parametros



URL_LINKEDIN_DS ='https://www.linkedin.com/jobs/ci%C3%AAncia-de-dados-vagas/?originalSubdomain=br'



## 3. todas as funcoes e classes



if __name__ == '__main__':
    
    
    
    #Criar uma instancia do Google Chrome pelo Selenium
    
    
    
    driver.implicitly_wait(10)
    
    
    
    #Acessar URL do Linkedin
    
    
    
    driver.get(URL_LINKEDIN_DS)
    
    
    
    #Pegar lista de resultadio de vagas de DS
    
    
   
    resultados = driver.find_elements_by_class_name('result-card')
    lista_descricao = []
    
    
    #Iniciar While Loop em cima de todos os resultados
    
    
while True:   
    
    
    
    #For loop para coletar descrições de dados
    
    
    
            for r in resultados[len(lista_descricao):]:
                     r.click() # Clicar na descrição
                     sleep(1)
try:
    
         #Pegar emlemento com a descricao
         
         
        descricao = driver.find_element_by_class_name('description')
        
        
        
        #Anexar o texto na lista
        
        
        
        lista_descricao.append(descricao.text) 
except:
          print('Erro')
          pass
   
resultados = driver.find_elements_by_class_name('result-card')

 
#Critério de saída do While


while 1:
    if len(lista_descricao) == len(resultados):
       break
    
 
    
#Salvar descrições de vagas



    descricao_salvar = '\n'.join(lista_descricao)
with open('descricoes_vagas.txt', 'w') as f:
    f.write(descricao_salvar)
    
    
    
#Fechar o Google Chrome 

   
     
driver.quit()  


    
    
        
    




