import matplotlib.pyplot as plt
import pandas as pd

# Read data from CSV file
data = pd.read_csv(r"C:\Sheeba C\Prodigy Infotech\Tasks\sub-division_population_of_pakistan.csv")

# Extracting the columns from the data
categories = data['PROVINCE']
male_urban = data['MALE (URBAN)']
transgender_urban = data['TRANSGENDER (URBAN)']
female_urban = data['FEMALE (URBAN)']

# Plotting the stacked bar chart
plt.figure(figsize=(12, 6))

# Plot each segment of the stacked bar
plt.bar(categories, male_urban, width=0.8, label='MALE (URBAN)', color='skyblue')
plt.bar(categories, transgender_urban, width=0.8, bottom=male_urban, label='TRANSGENDER (URBAN)', color='orange')
plt.bar(categories, female_urban, width=0.8, bottom=male_urban + transgender_urban, label='FEMALE (URBAN)', color='green')

# Create histograms
plt.figure(figsize=(12, 6))

# Histogram for 'MALE (URBAN)'
plt.subplot(1, 3, 1)  # (rows, columns, index)
plt.hist(male_urban, bins=10, color='skyblue', edgecolor='black')
plt.title('Male Urban Population')
plt.xlabel('Population')
plt.ylabel('Frequency')

# Histogram for 'TRANSGENDER (URBAN)'
plt.subplot(1, 3, 2)
plt.hist(transgender_urban, bins=10, color='orange', edgecolor='black')
plt.title('Transgender Urban Population')
plt.xlabel('Population')

# Histogram for 'FEMALE (URBAN)'
plt.subplot(1, 3, 3)
plt.hist(female_urban, bins=10, color='green', edgecolor='black')
plt.title('Female Urban Population')
plt.xlabel('Population')

plt.tight_layout()
plt.show()


# Labeling the chart
plt.xlabel('Province')
plt.ylabel('Population')
plt.title('Urban Population by Gender in Different Provinces of Pakistan')
plt.xticks(rotation=45)
plt.legend()

plt.tight_layout()

# Show the plot
plt.show()


