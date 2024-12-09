# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Load and Explore the Dataset
try:
    # Load dataset
    from sklearn.datasets import load_iris
    iris = load_iris(as_frame=True)
    df = iris.frame

    # Display the first few rows
    print("First few rows of the dataset:")
    print(df.head())

    # Explore the structure
    print("\nDataset information:")
    print(df.info())

    # Check for missing values
    print("\nMissing values per column:")
    print(df.isnull().sum())

    # Since the Iris dataset has no missing values, no cleaning is necessary.
    # If needed, use df.fillna() or df.dropna().
except Exception as e:
    print(f"Error loading dataset: {e}")

# Task 2: Basic Data Analysis
try:
    # Compute basic statistics
    print("\nBasic statistics of numerical columns:")
    print(df.describe())

    # Perform groupings: Mean petal length per species
    grouped_data = df.groupby('target')['petal length (cm)'].mean()
    print("\nMean petal length per species:")
    print(grouped_data)

    # Observation
    print("\nObservations: ")
    print("The petal length varies significantly across the species.")
except Exception as e:
    print(f"Error during data analysis: {e}")

# Task 3: Data Visualization
try:
    # Customize seaborn style
    sns.set(style="whitegrid")

    # Line chart
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['sepal length (cm)'], label="Sepal Length", color='blue')
    plt.plot(df.index, df['sepal width (cm)'], label="Sepal Width", color='green')
    plt.title("Sepal Measurements Over Samples")
    plt.xlabel("Sample Index")
    plt.ylabel("Measurement (cm)")
    plt.legend()
    plt.show()

    # Bar chart
    plt.figure(figsize=(10, 6))
    sns.barplot(x=df['target'], y=df['petal length (cm)'], ci=None)
    plt.title("Average Petal Length by Species")
    plt.xlabel("Species")
    plt.ylabel("Petal Length (cm)")
    plt.show()

    # Histogram
    plt.figure(figsize=(10, 6))
    plt.hist(df['sepal length (cm)'], bins=20, color='orange', edgecolor='black')
    plt.title("Distribution of Sepal Length")
    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Frequency")
    plt.show()

    # Scatter plot
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=df['sepal length (cm)'], y=df['petal length (cm)'], hue=df['target'])
    plt.title("Scatter Plot of Sepal Length vs. Petal Length")
    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Petal Length (cm)")
    plt.legend(title="Species")
    plt.show()

except Exception as e:
    print(f"Error during data visualization: {e}")
