import os

if (os.access('os',os.F_OK)):
    with os.scandir('os') as entries:
        
        for entry in entries:
            print(entry.name)