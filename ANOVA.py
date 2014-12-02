__author__ = 'davide'
# compute one-way ANOVA P value
'''

from scipy import stats

treatment1 = [1,1]
treatment2 = [1,1]
treatment3 = [1,1]
print treatment1
f_val, p_val = stats.f_oneway(treatment1, treatment2, treatment3)

print ("One-way ANOVA P =", p_val)
'''
from scipy import stats

a = ([True, 2, 3])
b = ([True, 2, 3])
c = ([False, 1, 3])

f_val, p_val = stats.f_oneway(a, b, c)
print(p_val)
print(f_val)
print("One-way ANOVA P =", p_val)
