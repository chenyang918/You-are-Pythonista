# -*- coding: utf-8 -*-
"""get_fibonacci_sequence.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xHBv84Uaum-kUatSXuJtgWrxe452H5U3
"""

#Fibonacci sequence
while 1:
    n = input('Input your number:')
    L = [1,1]
    try:
        n = int(n)
        if n <3:
            print('Number should >3')
            break
    except Exception as err:
        print('Please input a number')
        break
    for i in range(2, n):
        t = L[i-1] + L[i-2]
        L.append(t)
    print(L)