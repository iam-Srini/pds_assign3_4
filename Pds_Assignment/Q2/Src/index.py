import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("diabetes.csv")

# Set seed for reproducibility
np.random.seed(123)

# a) Random sample of 25 observations and comparison with population statistics for Glucose
sample_indices = np.random.choice(data.index, size=25, replace=False)
sample = data.loc[sample_indices]
sample_mean_glucose = sample['Glucose'].mean()
sample_max_glucose = sample['Glucose'].max()
population_mean_glucose = data['Glucose'].mean()
population_max_glucose = data['Glucose'].max()

# Plot comparison for Glucose
plt.figure(figsize=(10, 5))
plt.bar(['Population Mean', 'Sample Mean'], [population_mean_glucose, sample_mean_glucose], color=['#1f77b4', '#ff7f0e'], edgecolor='black')
plt.xlabel('Statistic')
plt.ylabel('Glucose Level')
plt.title('Comparison of Mean Glucose Levels between Population and Sample', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.savefig('glucose_comparison.png', bbox_inches='tight')
plt.close()

print("Population Max Glucose:", population_max_glucose)
print("Sample Max Glucose:", sample_max_glucose)

# b) 98th percentile of BMI for sample and population comparison
sample_98th_percentile_bmi = np.percentile(sample['BMI'], 98)
population_98th_percentile_bmi = np.percentile(data['BMI'], 98)

# Plot comparison for BMI
plt.figure(figsize=(10, 5))
plt.bar(['Population 98th Percentile', 'Sample 98th Percentile'], [population_98th_percentile_bmi, sample_98th_percentile_bmi], color=['#1f77b4', '#ff7f0e'], edgecolor='black')
plt.xlabel('Statistic')
plt.ylabel('BMI')
plt.title('Comparison of 98th Percentile of BMI between Population and Sample', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.savefig('bmi_comparison.png', bbox_inches='tight')
plt.close()

# c) Bootstrap sampling for BloodPressure statistics comparison
bootstrap_means = []
bootstrap_stds = []
bootstrap_percentiles = []

for _ in range(500):
    bootstrap_sample_indices = np.random.choice(data.index, size=150, replace=True)
    bootstrap_sample = data.loc[bootstrap_sample_indices]
    bootstrap_means.append(bootstrap_sample['BloodPressure'].mean())
    bootstrap_stds.append(bootstrap_sample['BloodPressure'].std())
    bootstrap_percentiles.append(np.percentile(bootstrap_sample['BloodPressure'], 50))

# Calculate population statistics for comparison
population_mean_bp = data['BloodPressure'].mean()
population_std_bp = data['BloodPressure'].std()
population_percentile_bp = np.percentile(data['BloodPressure'], 50)

# Plot comparison for BloodPressure statistics
plt.figure(figsize=(10, 5))
plt.hist(bootstrap_means, bins=30, alpha=0.7, color='#2ca02c', label='Bootstrap Means', edgecolor='black')
plt.axvline(population_mean_bp, color='#1f77b4', linestyle='dashed', linewidth=2, label='Population Mean')
plt.xlabel('Blood Pressure')
plt.ylabel('Frequency')
plt.title('Comparison of Bootstrap Means with Population Mean', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.legend(fontsize=12)
plt.savefig('bp_means_comparison.png', bbox_inches='tight')
plt.close()

plt.figure(figsize=(10, 5))
plt.hist(bootstrap_stds, bins=30, alpha=0.7, color='#2ca02c', label='Bootstrap Standard Deviations', edgecolor='black')
plt.axvline(population_std_bp, color='#1f77b4', linestyle='dashed', linewidth=2, label='Population Standard Deviation')
plt.xlabel('Blood Pressure')
plt.ylabel('Frequency')
plt.title('Comparison of Bootstrap Standard Deviations with Population Standard Deviation', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.legend(fontsize=12)
plt.savefig('bp_stds_comparison.png', bbox_inches='tight')
plt.close()

plt.figure(figsize=(10, 5))
plt.hist(bootstrap_percentiles, bins=30, alpha=0.7, color='#2ca02c', label='Bootstrap Percentiles', edgecolor='black')
plt.axvline(population_percentile_bp, color='#1f77b4', linestyle='dashed', linewidth=2, label='Population 50th Percentile')
plt.xlabel('Blood Pressure')
plt.ylabel('Frequency')
plt.title('Comparison of Bootstrap Percentiles with Population Percentile', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.legend(fontsize=12)
plt.savefig('bp_percentiles_comparison.png', bbox_inches='tight')
plt.close()
