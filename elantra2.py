# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 22:03:30 2022

@author: luciano marcos paes

Gravando os dados em arquivo
"""
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup

#2101

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}

url = 'https://www.carrosnaserra.com.br/busca/elantra/'

pag_fim = 2

k=0
for i in range(1,pag_fim): # vai varrer páginas 'todas notícias'
    req = requests.get(url+str(i), headers=header)
  #  req = requests.get(url, headers=header)
    soup = BeautifulSoup(req.content, 'html.parser')
    lista_modelo = soup.find_all('div',class_='modelo-estoque-card')
    lista_marca = soup.find_all('div',class_='ano-card')
    lista_ano = soup.find_all('div',class_='ano-cor-km-card')
    lista_preco = soup.find_all('div',class_='preco-estoque-card')
    
    for j in range(0,len(lista_modelo)): # vai coletar a relação das notícias de cada uma das páginas 'todas noticias' 
        print('-------------------------------------------------------------------')    
        texto_modelo = str(lista_modelo[j])
        texto_marca = str(lista_marca[j])
        texto_ano = str(lista_ano[j])
        
        texto_preco = str(lista_preco[j])
        texto_preco = str.strip(texto_preco)
        print(texto_modelo[54:89]+' '+texto_marca[38:50]+' '+str.strip(texto_ano[84:90])+' '+texto_preco[60:75])
       