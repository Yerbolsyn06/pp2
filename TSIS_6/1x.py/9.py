#8Напишите программу Python для удаления файла по указанному пути. Перед удалением проверьте доступ и существует ли указанный путь.

import os


if os.access('os', os.F_OK):
    print("existance:",True)

os.remove('os/almir.py')
