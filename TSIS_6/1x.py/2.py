import os

with os.scandir('os/') as entries:
    print("Directories:")
    for entry in entries:
        if entry.is_dir():
          print(entry.name)
print()          
with os.scandir('os/') as entries:
    print("Files:")
    for entry in entries:
        if entry.is_file():
          print(entry.name)          
print()
with os.scandir('os') as entries:
    for entry in entries:
        print(entry.name)          