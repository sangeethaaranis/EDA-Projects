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
books[books['Publishing Year'] < 0]

print(books.describe())
# %%
