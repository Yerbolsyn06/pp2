#2Напишите программу на Python со встроенной функцией, которая принимает строку и вычисляет количество прописных и строчных букв.
def cnt(s):
    upper=0
    lower=0
    for i in s:
        if (i >= 'A'and i<='Z'):
            upper+=1
        else:
            lower+=1
    return upper,lower
s=input()
print(cnt(s))                