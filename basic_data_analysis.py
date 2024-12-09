# Basic Data Analysis

# Generate basic statistics for the numerical columns
statistics = df.describe()

# Display the basic statistics
print("Basic Statistics:")
print(statistics)

# Calculate the mean petal length for each species
mean_petal_length = df.groupby('species')['petal length (cm)'].mean()

# Display the mean petal length for each species
print("\nMean Petal Length for Each Species:")
print(mean_petal_length)
