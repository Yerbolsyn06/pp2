#3Напишите программу на Python со встроенной функцией, которая проверяет, является ли переданная строка палиндромом или нет.
def palin(s):
    t=s[::-1]
    if(s==t):
        return True
    else:
        return False
s=input()
print(palin(s))        
