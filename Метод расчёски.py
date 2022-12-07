def CombSort(A):
    step = len(A)
    swaps = True
    while step > 1 or swaps:
        step = max(1, int(step / 1.25))
        swaps = False
        for i in range(len(A) - step):
            j = i + step
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]
                swaps = True
    return A


print("Введите элементы массива")
a = []
a = input().split()
print("Отсортированный массив")
print(CombSort(a))
