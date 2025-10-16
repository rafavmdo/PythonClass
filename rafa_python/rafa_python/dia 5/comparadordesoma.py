from os import system 
import random
system("cls")

a = random.randint(1, 10)
b = random.randint(1, 10)
c = random.randint(1, 10)
d = random.randint(1, 10)

print(f"primeira soma: a + b = {a} + {b} = {a + b}")
print(f"segunda soma: c + d = {c} + {d} = {c + d}\n")


A = a + b
B = c + d
if A > B:
    print(f"a soma de a + b é maior que a soma de c + b ({A}, {B})")
    print(A > B)
else:
    print(f"A soma de a + b é menor que a soma de c + b ({A}, {B})")
    print(A < B)