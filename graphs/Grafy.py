from _Grafy import getBarChart

import pandas as pd
import os
import sys

import seaborn as sns

print("Directory:", os.getcwd())
# /home/funkacer/_venv/_git/Python_2024/graphs
print()

print("Executable:", sys.executable)
print()

df = pd.DataFrame({'Boys': [67, 78],
                         'Girls': [72, 80], },
                        index=['First Year', 'Second Year'])

print(df)


# bez popisku
df.plot(kind='bar', stacked=True)

# s popisky
getBarChart(df)

