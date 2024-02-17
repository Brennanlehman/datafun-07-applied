import seaborn as sns
axes = sns.scatterplot(data=nyc, x = 'Date', y = 'temperature', hue = 'Temperature',
palette='winter', legend = False)