#1
import os
with os.scandir('os') as entries:
    for entry in entries:
        print(entry.name)