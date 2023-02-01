# Numeros Aleaotorios
import random
i = 0
numeros = list ()
pp = 0

for i in range(5):
    numeros.insert(i,random.randint(1,50))
    
i=5
while i <= 6:
    numeros.insert(i,random.randint(1,12))
    i += 1
  
t = 0
while t <= 6:
    print (numeros[t])
    t += 1


