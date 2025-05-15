import random
import time
import sys

# Aumenta o limite de recursão
sys.setrecursionlimit(20000)

# Variáveis globais para contar trocas e comparações
trocas = 0
comparacoes = 0

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    global trocas, comparacoes
    # Escolhe pivô aleatório
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    trocas += 1

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        comparacoes += 1
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            trocas += 1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    trocas += 1
    return i + 1

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
    quick_sort(lista, 0, len(lista) - 1)
    fim = time.perf_counter()

    tempo_gasto = fim - inicio

    print("\nLista ordenada corretamente.")
    print(f"Tempo gasto: {tempo_gasto:.6f} segundos")
    print(f"Número de comparações: {comparacoes}")
    print(f"Número de trocas: {trocas}")
    

if __name__ == "__main__":
    main()
