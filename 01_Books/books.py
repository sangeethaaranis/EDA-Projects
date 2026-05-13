#%%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

books = pd.read_csv('books.csv')

#%%
books.head()

# %%
books.describe()
# %%
#there is a negative value in publishing year
df = books[books['Publishing Year'] > 0]
print(df.describe())

# %%
#checking for null values
df.isnull().sum()

# %%
#we can ignore language code and delete book name empty empty rows
df = df[df['Book Name'].notna()]
df.isnull().sum()

# %%
