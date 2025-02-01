import yfinance as yf
import pandas as pd

tickerSymbol = 'GOOGL'
tickerData = yf.Ticker(tickerSymbol)
tickerDF = tickerData.history(period='1d',
                              start='2010-01-01',
                              end='2020-12-31')

tickerDF.reset_index(inplace=True)
tickerDF.head()
tickerDF.info()

split_year = 2015

# Create two DataFrames
df_before = tickerDF[tickerDF["Date"].dt.year < split_year]
df_after = tickerDF[tickerDF["Date"].dt.year >= split_year]

n1 = len(df_before)
n2 = len(df_after)

print(f'{n1} and {n2}')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker  # Import ticker for scientific notation

# Sample DataFrames (assuming 'value' column exists in both)
fig, axes = plt.subplots(1, 2, figsize=(12, 5), sharey=True)  # 1 row, 2 columns

# Histogram for df_before
axes[0].hist(df_before["Volume"], bins=20, color='blue', alpha=0.7)
axes[0].set_title("Volumes Before 2015")
axes[0].set_xlabel("Volume")
axes[0].set_ylabel("Frequency")
axes[0].grid()

# Histogram for df_after
axes[1].hist(df_after["Volume"], bins=20, color='red', alpha=0.7)
axes[1].set_title("Volumes After and Including 2015")
axes[1].set_xlabel("Volume")
axes[1].grid()

# Apply scientific notation formatter
for ax in axes:
    ax.xaxis.set_major_formatter(mticker.ScalarFormatter(useMathText=True))
    ax.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))  # Force scientific notation

# Adjust layout
plt.tight_layout()
plt.show()

import scipy.stats as st


stat, p = st.levene(df_before["Volume"], df_after["Volume"])

print(f'{stat}, {p}')


print(st.ttest_ind(df_before["Volume"], df_after["Volume"], equal_var = False, alternative ='greater'))

