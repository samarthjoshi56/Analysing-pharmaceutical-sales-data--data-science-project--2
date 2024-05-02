import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Load the dataset using pandas
data = pd.read_csv('your_dataset.csv')

# Display the first few rows of the dataset
print(data.head())

# Calculate descriptive statistics for Quantity Sold
quantity_stats = data['Quantity_Sold'].describe()
print("\nDescriptive Statistics for Quantity Sold:")
print(quantity_stats)

# Calculate additional statistics
skewness = data['Quantity_Sold'].skew()
kurtosis = data['Quantity_Sold'].kurtosis()

print("\nAdditional Statistics:")
print("Skewness:", skewness)
print("Kurtosis:", kurtosis)

# Set style for all plots
sns.set(style="whitegrid")

# Plot 1: KDE plot of Quantity Sold
plt.figure(figsize=(10, 6))
sns.kdeplot(data['Quantity_Sold'], fill=True, color='skyblue')
plt.axvline(np.mean(data['Quantity_Sold']), color='r', linestyle='--', label='Mean')
plt.axvline(np.median(data['Quantity_Sold']), color='g', linestyle='-', label='Median')
plt.title('KDE plot of Quantity Sold', fontsize=16)
plt.xlabel('Quantity Sold', fontsize=14)
plt.ylabel('Density', fontsize=14)
plt.legend()
plt.tight_layout()
plt.show()

# Plot 2: Boxplot of Quantity Sold
plt.figure(figsize=(8, 6))
sns.boxplot(y='Quantity_Sold', data=data, color='lightblue')
plt.title('Boxplot of Quantity Sold', fontsize=16)
plt.ylabel('Quantity Sold', fontsize=14)
plt.tight_layout()
plt.show()

# Plot 3: Bar plot of Region wise sales
plt.figure(figsize=(10, 6))
sns.countplot(x='Region', data=data, order=data['Region'].value_counts().index, palette='pastel')
plt.title('Region wise Sales', fontsize=16)
plt.xlabel('Region', fontsize=14)
plt.ylabel('Count', fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot 4: Bar plot of Customer Type
plt.figure(figsize=(8, 6))
sns.countplot(x='Customer_Type', data=data, order=data['Customer_Type'].value_counts().index, palette='pastel')
plt.title('Customer Type Distribution', fontsize=16)
plt.xlabel('Customer Type', fontsize=14)
plt.ylabel('Count', fontsize=14)
plt.tight_layout()
plt.show()

# Plot 5: Bar plot of Country wise sales
plt.figure(figsize=(12, 6))
sns.countplot(x='Country', data=data, order=data['Country'].value_counts().index, palette='pastel')
plt.title('Country wise Sales', fontsize=16)
plt.xlabel('Country', fontsize=14)
plt.ylabel('Count', fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot 6: Scatter plot of Quantity Sold vs Date
plt.figure(figsize=(12, 6))
sns.scatterplot(x='Date', y='Quantity_Sold', data=data, color='skyblue')
plt.title('Quantity Sold over Time', fontsize=16)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Quantity Sold', fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot 7: Scatter plot of Quantity Sold vs City
plt.figure(figsize=(12, 6))
sns.scatterplot(x='City', y='Quantity_Sold', data=data, color='lightgreen')
plt.title('Quantity Sold by City', fontsize=16)
plt.xlabel('City', fontsize=14)
plt.ylabel('Quantity Sold', fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Example of using SciPy
corr_coeff, p_value = stats.pearsonr(data['Quantity_Sold'], data['Quantity_Sold'])
print("\nPearson correlation coefficient between Quantity Sold and itself:", corr_coeff)
print("P-value:", p_value)
