import time
import random

# Função para gerar listas de diferentes tipos
def gerar_lista(tamanho, tipo):
    """
    Gera uma lista com base no tipo especificado:
    - 'ordenada': Lista de elementos em ordem crescente.
    - 'inversa': Lista de elementos em ordem decrescente.
    - 'aleatoria': Lista de elementos aleatórios.

    Parâmetros:
    tamanho (int): Tamanho da lista a ser gerada.
    tipo (str): Tipo de lista a ser gerada ('ordenada', 'inversa', 'aleatoria').

    Retorna:
    list: Lista gerada de acordo com o tipo especificado.
    """
    if tipo == 'ordenada':
        return list(range(tamanho))  # Lista ordenada de 0 a tamanho-1
    elif tipo == 'inversa':
        return list(range(tamanho, 0, -1))  # Lista ordenada de tamanho-1 a 1
    else:  # tipo 'aleatoria'
        return random.sample(range(tamanho * 2), tamanho)  # Lista aleatória com elementos únicos

# Função para testar os algoritmos de ordenação
def testar_algoritmo(nome_algoritmo, funcao, tamanho, tipo_lista):
    """
    Testa um algoritmo de ordenação específico e registra as métricas.

    Parâmetros:
    nome_algoritmo (str): Nome do algoritmo de ordenação.
    funcao (function): Função de ordenação a ser testada.
    tamanho (int): Tamanho da lista a ser ordenada.
    tipo_lista (str): Tipo de lista a ser usada ('ordenada', 'inversa', 'aleatoria').
    """
    lista = gerar_lista(tamanho, tipo_lista)  # Gera a lista com o tipo especificado
    comparacoes = [0]  # Lista para armazenar o número de comparações
    trocas = [0]  # Lista para armazenar o número de trocas

    # Registra o tempo de execução do algoritmo
    inicio = time.time()  # Início da contagem de tempo
    funcao(lista[:], comparacoes, trocas)  # Executa a função de ordenação
    fim = time.time()  # Fim da contagem de tempo

    tempo_execucao = fim - inicio  # Calcula o tempo de execução
    
    # Verificar se o tempo é maior que 60 segundos (1 minuto) para conversão
    if tempo_execucao > 60:
        tempo_execucao = tempo_execucao / 60  # Converte para minutos
        unidade = "minutos"
    else:
        unidade = "segundos"
    
    # Exibe os resultados no formato especificado
    print(f"{nome_algoritmo} | Tipo: {tipo_lista:<9} | Tamanho: {tamanho:>6} | "
          f"Tempo: {tempo_execucao:.6f} {unidade} | "  # Mostra o tempo de execução
          f"Comparações: {comparacoes[0]} | Trocas: {trocas[0]}")

# Algoritmo de ordenação Bubble Sort
def bubble_sort(arr, comparacoes, trocas):
    """
    Implementação do algoritmo Bubble Sort.
    
    Parâmetros:
    arr (list): Lista a ser ordenada.
    comparacoes (list): Lista para armazenar o número de comparações.
    trocas (list): Lista para armazenar o número de trocas.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            comparacoes[0] += 1  # Incrementa o número de comparações
            if arr[j] > arr[j + 1]:  # Verifica se os elementos estão fora de ordem
                trocas[0] += 1  # Incrementa o número de trocas
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Troca os elementos

# Algoritmo de ordenação Selection Sort
def selection_sort(arr, comparacoes, trocas):
    """
    Implementação do algoritmo Selection Sort.

    Parâmetros:
    arr (list): Lista a ser ordenada.
    comparacoes (list): Lista para armazenar o número de comparações.
    trocas (list): Lista para armazenar o número de trocas.
    """
    n = len(arr)
    for i in range(n):
        min_idx = i  # Assume que o menor valor é o primeiro elemento
        for j in range(i + 1, n):
            comparacoes[0] += 1  # Incrementa o número de comparações
            if arr[j] < arr[min_idx]:  # Se encontrar um valor menor
                min_idx = j  # Atualiza o índice do menor valor
        if i != min_idx:
            trocas[0] += 1  # Incrementa o número de trocas
            arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Troca o elemento atual com o menor

# Algoritmo de ordenação Insertion Sort
def insertion_sort(arr, comparacoes, trocas):
    """
    Implementação do algoritmo Insertion Sort.
    
    Parâmetros:
    arr (list): Lista a ser ordenada.
    comparacoes (list): Lista para armazenar o número de comparações.
    trocas (list): Lista para armazenar o número de trocas.
    """
    n = len(arr)
    for i in range(1, n):
        chave = arr[i]  # O elemento a ser inserido na parte ordenada
        j = i - 1
        while j >= 0:
            comparacoes[0] += 1  # Incrementa o número de comparações
            if arr[j] > chave:  # Verifica se o elemento deve ser movido
                trocas[0] += 1  # Incrementa o número de trocas
                arr[j + 1] = arr[j]  # Move o elemento uma posição à frente
                j -= 1
            else:
                break
        arr[j + 1] = chave  # Coloca a chave na posição correta

# Lista de tamanhos para os testes
tamanhos = [1000, 10000, 50000, 100000]

# Tipos de listas a serem testadas
tipos = ['aleatoria', 'ordenada', 'inversa']

# Algoritmos de ordenação a serem testados
algoritmos = [
    ("Bubble Sort", bubble_sort),
    ("Selection Sort", selection_sort),
    ("Insertion Sort", insertion_sort)
]

# Realiza os testes para cada algoritmo e tipo de lista
for nome_algoritmo, func in algoritmos:
    for tipo in tipos:
        for tamanho in tamanhos:
            testar_algoritmo(nome_algoritmo, func, tamanho, tipo)