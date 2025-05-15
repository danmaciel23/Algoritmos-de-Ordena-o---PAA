import random
import time

# Variável global para contar as trocas
trocas = 0

def merge_sort(arr):
    global trocas
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        # Merge as duas metades
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            trocas += 1  # Contamos cada escrita no arr
            k += 1

        # Copia o que restou
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            trocas += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            trocas += 1

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
    global trocas
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

    inicio = time.time()
    merge_sort(lista)
    fim = time.time()

    tempo_gasto = fim - inicio

    print("\nLista ordenada corretamente.")
    print(f"Tempo gasto: {tempo_gasto:.6f} segundos")
    print(f"Número de trocas: {trocas}")

if __name__ == "__main__":
    main()
