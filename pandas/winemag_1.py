import pandas as pd
import matplotlib.pyplot as plt

wine_reviews = pd.read_csv('../data/winemag/winemag-data-130k-v2.csv', index_col=0)

print(wine_reviews.head())

wine_reviews['points'].value_counts().sort_index().plot.bar()

plt.show()