
# 20_miniPython.py
'''
Készítsünk egy ötöslottó sorsoló programot:

- Véletlenszámokat generálunk 1-től 90-ig
- Öt egymástól különböző számra van szükségünk
- A számokat emelkedő sorrendben írassuk ki!
'''


import random as r
import os
os.system('cls')
lotto = []

while True:
    rnd = r.randrange(1,91)
    if rnd not in lotto:
         lotto.append(rnd)
    if len(lotto) == 5:
         break;

lotto.sort()
print(f'\nLóttoszámok: {lotto[0]}, {lotto[1]}, {lotto[2]}, {lotto[3]}, {lotto[4]}\n')