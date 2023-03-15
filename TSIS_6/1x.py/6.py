#5Напишите программу Python для записи списка в файл.

import os

mylist=["hello","how","are","you"]

with open('input.txt', 'w') as wr:
    for i in mylist:
        wr.write('%s\n'%i)