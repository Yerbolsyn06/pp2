#2Напишите программу Python для проверки доступа к указанному пути. Проверить существование, читаемость, возможность записи и исполняемость указанного пути
import os
 
print("Existance:",os.access('os', os.F_OK))

print("readability:",os.access('os', os.R_OK))

print("writibility:",os.access('os',os.W_OK))

print('execuitability:',os.access('os',os.X_OK))