from _Grafy import getBarChart

import pandas as pd
import os

print("Directory:", os.getcwd())
# /home/funkacer/_venv/_git/Python_2024/graphs
print()

df = pd.DataFrame({'Boys': [67, 78],
                         'Girls': [72, 80], },
                        index=['First Year', 'Second Year'])

print(df)

html = getBarChart(df, html=True)

with open('obrazek.png', 'w') as file:
    file.write(html)

