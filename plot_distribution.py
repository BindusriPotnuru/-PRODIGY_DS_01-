import matplotlib.pyplot as plt

# Age bins and corresponding populations
age_bins = ['0-10', '11-20', '21-30', '31-40', '41-50', '51-60']
populations = [5, 10, 25, 2, 1, 20]

# Create histogram
plt.bar(age_bins, populations, color='skyblue', edgecolor='black')

# Add title and labels
plt.title('Distribution of Ages in a Population')
plt.xlabel('Age Group')
plt.ylabel('Population')

# Show plot
plt.show()
