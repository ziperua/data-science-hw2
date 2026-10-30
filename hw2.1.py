import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://uk.wikipedia.org/wiki/%D0%9D%D0%B0%D1%81%D0%B5%D0%BB%D0%B5%D0%BD%D0%BD%D1%8F_%D0%A3%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D0%B8"

tables = pd.read_html(
    url,
    match="Коефіцієнт народжуваності",
    storage_options={"User-Agent": "Mozilla/5.0"},
)
df = tables[0]

print(df.head())

print(df.shape)

df = df.replace("--", np.nan)
df = df.replace("—", np.nan)

print(df.dtypes)

print(df.isnull().sum() / df.shape[0])

df = df.drop([27])

df['2014'] = pd.to_numeric(df['2014'])
df['2019'] = pd.to_numeric(df['2019'])
df = df.fillna(df.mean(numeric_only=True))

print(df[df['2019'] > df['2019'].mean()]['Регіон'].to_list())

print(df.loc[df['2014'].idxmax(), 'Регіон'])

# plt.barh(df["Регіон"], df['2019'])
# plt.title("народжуваність по регіонах у 2019")
# plt.show()

# sns.boxplot(data=df.drop(['Регіон'], axis=1))
# plt.show()

plt.figure(figsize=(10,10)) 
sns.heatmap(data=df.set_index('Регіон'), yticklabels=True)
plt.show()