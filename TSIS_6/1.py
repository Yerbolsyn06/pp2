#1Напишите программу Python со встроенной функцией для умножения всех чисел в списке.
def multi(n):
    sum=1
    for i in n:
        sum*=i 

    return sum    
l= map(int, input().split())
print(multi(l))

    
    