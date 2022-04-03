from random import randint
t = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f"Os valores sorteados foram:", end=" ")
for i in range(len(t)):
    print(t[i], end=" ")
    if i >= len(t)-1:
        print("\n")
print(f"O maior número da tupla é: {max(t)} \nO menor número da tupla é: {min(t)}")
