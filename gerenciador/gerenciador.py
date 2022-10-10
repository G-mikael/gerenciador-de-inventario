import numpy
import pandas

def listar_inventario(inv):
    '''A função recebe como parâmetro um dicionário e 
    retorna um dataframe com todos os ítens e seus valores


    :param inv : dicionário com itens e valores
    :inv type: dict
    :return: Dataframe
    :rtype: Pandas.Dataframe
    '''
    
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
    inv = inv.copy()
    
    if item not in inv:
        inv[item]=valor
        return inv
    else:
        raise Exception('O item ja está no inventario')
    
    
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

def busca_item(chave, inv):
    '''
    A função recebe uma chave busca o item referente aquela chave e retorna
    o item e chave dado
    
    :param chave: chave do item que será buscado
    :chave type: str
    :param inv : dicionário no qual será buscado o item
    :inv type: dict
    :return: Dicionário com a chave e o value do item buscado
    :rtype: dict

    '''
    if chave in inv:
        return {chave:inv[chave]}
    else:
        raise Exception('O item não está no inventario')
    
dic = {'a':1, 'b':2, 'c':3}
print(dic)
#print(adicionar_item('a', 4, dic))
dic = adicionar_item('d', 4, dic)
print(dic)
print(busca_item('a', dic))
print(busca_item('d', dic))

