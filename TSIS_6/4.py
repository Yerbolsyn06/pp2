#4Напишите программу на Python, которая вызывает функцию извлечения квадратного корня через определенные миллисекунды.
import math
import time
def root(n):
    ans=math.sqrt(n)
    return ans

n=int(input())
t=int(input())
seconds=t/1000
time.sleep(seconds)
print(root(n))        
    
