# Faça um programa que mostre na tela uma
# contagem regressiva para o estouro de
# fogos de artifício. indo de 10 até 0,
# com uma pause de 1s entre eles
from time import sleep

print('Countdown to fireworks:')
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('Fireworks!!!')