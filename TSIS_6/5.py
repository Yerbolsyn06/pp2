#5Напишите программу на Python со встроенной функцией, которая возвращает True, если все элементы кортежа истинны.
def booltuple(mytuple):
    for i in mytuple:
        if bool(i)==False:
            return False
    return True
    
mytuple=(3,4,4,0,4) 
print(booltuple(mytuple))    
