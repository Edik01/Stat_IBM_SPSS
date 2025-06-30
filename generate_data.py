import numpy as np
import pandas as pd
from scipy import stats

np.random.seed(1)
data = np.random.normal(loc=70, scale=15, size=100)

mean = np.mean(data)
median = np.median(data)
std_dev = np.std(data)
t_stat, p_value = stats.ttest_1samp(data, popmean=75)

print('statistics analysis results')
print(f'Mean: {mean:.2f}')
print(f'Median: {median:.2f}')
print(f'Standard Deviation: {std_dev:.2f}')
print(f'T-statistic: {t_stat:.2f}')
print(f'P-value: {p_value:.4f}')