# Import necessary libraries
from sklearn.datasets import load_iris
import pandas as pd

# Load the Iris dataset
iris = load_iris()

# Convert the data into a Pandas DataFrame
# The Iris dataset contains 'data' for features and 'target' for the target labels
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Add the target labels as a separate column
df['species'] = iris.target

# Map the target labels to species names for readability
df['species'] = df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

# Display the first few rows of the DataFrame
print(df.head())
