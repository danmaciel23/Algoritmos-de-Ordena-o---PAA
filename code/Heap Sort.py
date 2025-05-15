import random
import time

# Variáveis globais para contar trocas e comparações
trocas = 0
comparacoes = 0

def heapify(arr, n, i):
    global trocas, comparacoes
    largest = i
    l = 2 * i + 1  # Filho esquerdo
    r = 2 * i + 2  # Filho direito

    # Verifica filho esquerdo
    if l < n:
        comparacoes += 1
        if arr[l] > arr[largest]:
            largest = l

    # Verifica filho direito
    if r < n:
        comparacoes += 1
        if arr[r] > arr[largest]:
            largest = r

    # Se o maior não for a raiz
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        trocas += 1
        heapify(arr, n, largest)

def heap_sort(arr):
    global trocas  # <---- correção aqui
    n = len(arr)

    # Constrói o heap máximo
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extrai elementos um por um do heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        trocas += 1
        heapify(arr, i, 0)

def gerar_lista(tamanho, tipo):
    if tipo == "ordenada":
        return list(range(1, tamanho + 1))
    elif tipo == "inversa":
        return list(range(tamanho, 0, -1))
    elif tipo == "aleatoria":
        lista = list(range(1, tamanho + 1))
        random.shuffle(lista)
        return lista
    else:
        raise ValueError("Tipo inválido. Escolha 'ordenada', 'inversa' ou 'aleatoria'.")

def main():
    global trocas, comparacoes
    tamanho = int(input("Digite o tamanho da lista: "))
    print("Escolha o tipo da lista:")
    print("1 - Ordenada")
    print("2 - Inversamente ordenada")
    print("3 - Aleatória")
    escolha = input("Digite 1, 2 ou 3: ")

    if escolha == "1":
        tipo = "ordenada"
    elif escolha == "2":
        tipo = "inversa"
    elif escolha == "3":
        tipo = "aleatoria"
    else:
        print("Escolha inválida.")
        return

    lista = gerar_lista(tamanho, tipo)
    print("\nIniciando ordenação...")

    inicio = time.perf_counter()
    heap_sort(lista)
    fim = time.perf_counter()

    tempo_gasto = fim - inicio

    print("\nLista ordenada corretamente.")
    print(f"Tempo gasto: {tempo_gasto:.6f} segundos")
    print(f"Número de comparações: {comparacoes}")
    print(f"Número de trocas: {trocas}")
    

if __name__ == "__main__":
    main()
