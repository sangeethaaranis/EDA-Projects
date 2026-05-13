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
df.hist(bins=50, figsize=(20,15))

# %%
df.Author.value_counts().sort_values(ascending=False)

# %%
plt.hist(df["Publishing Year"])
plt.xlabel("Year")
plt.ylabel("Number of Books")
plt.title("Books Published per Year")

# %%
df.head()
df['genre'].value_counts().plot(kind = 'bar')
plt.xlabel("Genre")
plt.ylabel("Number of books")
plt.title("Number of Books per Genre")
plt.show()

# %%
df.groupby(['Author'])['Book_average_rating'].mean().sort_values(ascending = False)

# %%
sns.boxplot(x='genre',
             y='Book_average_rating',
               data=df)
plt.xlabel("Genre")
plt.ylabel("Average Rating")
plt.title("Average Rating per Genre")
plt.show()

# %%
df.columns
plt.scatter(df['sale price'],df['units sold'])
plt.xlabel("Sale Price")
plt.ylabel("Units Sold")
plt.title("Units Sold vs Sale Price")
plt.show()

# %%
language_counts = df['language_code'].value_counts()

plt.pie(language_counts,
    labels=language_counts.index,
    autopct='%1.1f%%')
plt.show()

# %%
df.groupby("Publisher ")['publisher revenue'].sum().sort_values(ascending= True)

# %%
df.groupby("Author_Rating")["Book_ratings_count"].mean().sort_values(ascending= True)

#%%
df.groupby("language_code").size().sort_values(ascending=False)
