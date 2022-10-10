import numpy
import pandas as pd

def listar_inventario(inv):
    '''A função recebe como parâmetro um dicionário e 
    retorna um dataframe com todos os ítens e seus valores


    :param inv : dicionário com itens e valores
    :inv type: dict
    :return: Dataframe
    :rtype: Pandas.Dataframe
    '''
    try:
        chaves = list(inv.keys())
        valores = {'Valores':list(inv.values())}
        
        listagem = pd.DataFrame(data=valores, index=chaves)
        return listagem
    except:
        print('Parâmetro inválido')
        return None
    
def adicionar_item(item, valor, inv):
    '''A função recebe como parâmetro um dicionário e 
    retorna um dataframe com todos os ítens e seus valores


    :param item: Nome do item a ser adicionado como 
    :inv type: str
    :param item: Valor do item a ser adicionado como value
    :inv type: str
    :param inv : dicionário ao qual será adicionado o item
    :inv type: dict
    :return: Dicionário com o item a mais
    :rtype: dict
    '''
    
def remover_item(chave, inv):
    '''A função recebe um dicionário e uma chave e remove um ítem do dicionário a
    partir da chave dada
    
    :param chave: chave do item queserá removido 
    :chave type: str
    :param inv : dicionário ao qual será removido o item
    :inv type: dict
    :return: Dicionário com o item a mais
    :rtype: dict
    '''
    try:
        del inv[chave]
        return inv
    except KeyError:
        print('Chave dada inválida. Use chave válida!')
    except NameError:
        print('O dicionário não existe!')
        
        
        

def busca_item(chave):
    '''
    A função recebe uma chave busca o item referente aquela chave e retorna
    o item e chave dado
    
    :param chave: chave do item que será buscado
    :chave type: str
    :return: Dicionário com a chave e o value do item buscado
    :rtype: dict

    '''
    
