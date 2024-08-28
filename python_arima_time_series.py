import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller
"""pip install statsmodels"""

np.random.seed(42)

date_range_input = pd.date_range(start="2022-01-01", periods=100,freq="D")
print(date_range_input)

new_data =  np.random.normal(0,1,100).cumsum() + 50
print(new_data)

time_series_data = pd.Series(new_data, index=date_range_input)

plt.figure(figsize=(10,8))
plt.plot(time_series_data, label = "Time Series")
plt.xlabel("date")
plt.ylabel("value")
plt.show()