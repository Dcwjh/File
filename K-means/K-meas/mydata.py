# -*- coding:utf-8 -*-

import pandas as pd
import warnings
warnings.filterwarnings("ignore")
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="white", color_codes=True)  
budget = pd.read_csv("user.csv")
print(budget.head())





