import random
import string

n=int(input("Введите количество сотрудников: "))
s=open('result.txt', 'w')
for i in range(n):
    s.write("Логин №"+str(i+1)+": "+str(''.join(random.choice(string.ascii_letters)for j in range(8)))+"@dmail.com"+" "+"Пароль: "+str(''.join(random.choice(string.ascii_letters)for j in range(8)))+'\n')
s.close()

