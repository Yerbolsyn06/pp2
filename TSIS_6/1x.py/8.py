#7Напишите программу Python для копирования содержимого файла в другой файл.
import os
with open('row.txt','r') as re:
    content=re.read()
with open(input(),'w') as wr:
    wr.write(content)    