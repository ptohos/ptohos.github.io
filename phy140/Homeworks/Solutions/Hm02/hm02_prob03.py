#!/usr/bin/python3

import numpy as np

NtermsMx = int(input("Maximum number of terms in the series "))

SerieSum=0

for iterm in range(1, NtermsMx+1):
    SerieSum += (-1)**iterm * (5*iterm)/(iterm+1)

print('The sum for {:2d} terms is equal to: {:.5f}'.format(NtermsMx,SerieSum))
exit()
