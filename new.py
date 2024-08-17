import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
df = pd.read_csv("./prices_industryoil.csv")
df.head()

df.columns = ['Month', 'Consumer Price Index (1982-84=1)',
       'Motor Gasoline Price ($/gallon) Nominal',
       ' Motor Gasoline Price ($/gallon) Real']
from matplotlib import pyplot as plt
df.plot(kind='scatter', x='Consumer Price Index (1982-84=1)', y=' Motor Gasoline Price ($/gallon) Real', s=32, alpha=.8)
plt.gca().spines[['top', 'right',]].set_visible(False)

df.columns = ['Month', 'Consumer Price Index (1982-84=1)',
       'Motor Gasoline Price ($/gallon) Nominal',
       ' Motor Gasoline Price ($/gallon) Real']
from matplotlib import pyplot as plt
df['Consumer Price Index (1982-84=1)'].plot(kind='line', figsize=(8, 4), title='Variation of Consumer Price Index')
plt.gca().spines[['top', 'right']].set_visible(False)



df.columns = ['date', 'nominal_price', 'real_price', 'cpi']
df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y')

df.set_index('date', inplace=True)

window_size = 12
df['rolling_avg_real_price'] = df['real_price'].rolling(window=window_size).mean()

plt.figure(figsize=(12, 6))
plt.plot(df.index, df['real_price'], label='Real Gas Price', color='blue', alpha=0.7)
plt.plot(df.index, df['rolling_avg_real_price'], label=f'{window_size}-Month Rolling Average', color='red', linestyle='--')
plt.title('Real Gas Prices with Rolling Average')
plt.xlabel('Date')
plt.ylabel('Real Gas Price in Dollars')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


plt.figure(figsize=(12, 6))
plt.plot(data.i, data['Motor Gasoline Price ($/gallon) Real'], marker='o', linestyle='-', color='b')
plt.title('Motor Gasoline Prices Over 25 Years (Line Plot)')
plt.xlabel('Date')
plt.ylabel('Real Price ($/gallon)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()