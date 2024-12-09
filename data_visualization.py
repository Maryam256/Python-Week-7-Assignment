import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming 'df' is your DataFrame loaded with the Iris dataset
# Line Chart: Display trends in sepal measurements across samples
plt.figure(figsize=(10, 6))
plt.plot(df['sepal length (cm)'], label='Sepal Length', color='blue', marker='o', linestyle='-', markersize=5)
plt.title('Trends in Sepal Length Across Samples')
plt.xlabel('Sample Index')
plt.ylabel('Sepal Length (cm)')
plt.legend()
plt.grid(True)
plt.show()

# Bar Chart: Average Petal Length for Each Species
plt.figure(figsize=(10, 6))
species_avg_petal_length = df.groupby('species')['petal length (cm)'].mean()
species_avg_petal_length.plot(kind='bar', color=['green', 'blue', 'red'])
plt.title('Average Petal Length for Each Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length (cm)')
plt.xticks(rotation=45)
plt.show()

# Histogram: Distribution of Sepal Lengths
plt.figure(figsize=(10, 6))
df['sepal length (cm)'].hist(bins=15, color='purple', edgecolor='black')
plt.title('Distribution of Sepal Lengths')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.show()

# Scatter Plot: Relationship between Sepal Length and Petal Length
plt.figure(figsize=(10, 6))
sns.scatterplot(x=df['sepal length (cm)'], y=df['petal length (cm)'], hue=df['species'], palette='Set1')
plt.title('Relationship between Sepal Length and Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.show()
