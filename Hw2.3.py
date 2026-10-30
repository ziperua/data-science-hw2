import kagglehub
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Download latest version
path = kagglehub.dataset_download("sootersaalu/amazon-top-50-bestselling-books-2009-2019")

df = pd.read_csv(os.path.join(path, 'bestsellers with categories.csv'))

print(df.head())

print(df.shape)

#550 книг

df.columns = ['name', 'author', 'user_rating', 'reviews', 'price', 'year', 'genre']


print(df.isna().sum())

#немає пропусків

print(df['genre'].unique())

# non fiction та fiction

#df['price'].plot(kind='hist')
#plt.show()

print(df['price'].max())
print(df['price'].min())
print(df['price'].mean())
print(df['price'].median())


print(df['user_rating'].max())

print(df[df['user_rating'] == df['user_rating'].max()].shape[0])

print(df.loc[df['reviews'].idxmax(), 'name'])

df2015 = df[df['year'] == 2015]
print(df2015.loc[df2015['price'].idxmax(), 'name'])

print(df[(df['year'] == 2010) & (df['genre'] == 'Fiction')].shape[0])

print(df[(df['year'].isin([2010, 2011])) & (df['user_rating'] == 4.9)].shape[0])

print(df2015[df2015['price'] < 8].sort_values(by='price'))

#Old School (Diary of a Wimpy Kid #10)

df_genre_price = df.groupby('genre')['price'].agg(['min', 'max'])

print(df_genre_price)

df_author_by_books = df.groupby('author')[['name']].agg('count')
df_author_by_books.columns = ['count']

print(df_author_by_books.shape)

print(df_author_by_books['count'].idxmax())

print(df_author_by_books['count'].max())

df_by_mean = df.groupby('author')[['user_rating']].agg('mean')

print(df_by_mean['user_rating'].idxmin())

print(df_by_mean['user_rating'].min())

df_concat = pd.concat([df_author_by_books, df_by_mean], axis=1)

df_concat = df_concat.sort_values(by=['count', 'user_rating'])
print(df_concat.head(1))


# sns.countplot(x='year', hue='genre', data=df)
# plt.show()

# sns.scatterplot(x='reviews', y='user_rating', hue='genre', data=df)
# plt.show()

counts = df['genre'].value_counts()
plt.pie(counts, labels=counts.index, autopct='%.1f%%')
plt.show()