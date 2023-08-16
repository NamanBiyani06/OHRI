import math
import numpy as np

age = 87
eGFR = 12.8
ACR = 32.8 
male = 2
race = 1 
bicarb = 22 
alb = 39 
calc = 2.31 
phos = 0.98 

if(race == 0): coefficient = 0.978
else: coefficient = 0.9827

a = 0
if(male == 1): a = 0.1602 * (1 - 0.5642)
if(male == 2): a = 0.1602 * (-0.5642)
b = -0.1992 * ((age/10) - 7.036)
c = -0.4919 * ((eGFR/5) - 7.222)
d = 0
if(ACR > 0): d = 0.3364 * (math.log(ACR) - 5.137)
e = -0.3441 * ((alb / 10.0) - 3.997)
f = 0.2604 * ((phos * 3.1) - 3.916)
g = -0.07354 * (bicarb - 25.57)
h = -0.2228 * ((calc * 2.5) - 9.355)
kfre = (1.0 - (coefficient ** (math.exp(a + b + c + d + e + f + g + h)))) * 100


print('a:', a)
print('b:', b)
print('c:', c)
print('d:', d)
print('e:', e)
print('f:', f)
print('g:', g)
print('h:', h)

print(kfre, '%', sep='')

# e_cal = -0.2201 * ((age / 10.0) - 7.036)

# g_cal = 0

# if male == 2:
#     g_cal = 0.2467 * (-0.5642)
# elif male == 1:
#     g_cal = 0.2467 * (1 - 0.5642)

# m_cal = -0.5567 * ((eGFR / 5.0) - 7.2222)

# l_cal = 0.451 * (np.log(ACR * 8.84) - 5.137)

# kfre_calc = (1.0 - (0.975 ** (math.exp(e_cal + g_cal + m_cal + l_cal)))) * 100

# print(kfre_calc)