#6Напишите программу Python для создания 26 текстовых файлов с именами A.txt, B.txt и т. д. до Z.txt.
import string
import os
for letter in string.ascii_uppercase:
    #print(letter,end=" ")
    with open(letter + '.txt','w') as x:
        pass