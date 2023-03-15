import requests
x=requests.get("https://www.w3schools.com/python/python_while_loops.asp")
print(x.text)
print(x)