# -*- coding: utf-8 -*-
"""Пузырьки.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12AqwbuYigsySDdw7axu4zJkXQ-Y-F3E6
"""

print("Введите количество элементов")
N = int(input())
a =[]
print("Перечислете элементы")
a = input().split()
for i in range(N-1):
    for j in range(N-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print("Отсортированный массив")
print(a)